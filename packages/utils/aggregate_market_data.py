import os
import json
import pandas as pd
import numpy as np

# Configuration based on GEMINI.md and implementation-checklist.md
INDEX_CODES = [
    "LG_OFF_ISL", "LG_RET_ISL", "LG_IND_MLN", "LG_RES_PRM", 
    "AB_OFF_CEN", "AB_RET_CEN", "PH_COM_OIL", "KN_IND_NTH"
]
YEAR_RANGE = range(2018, 2025)  # 2018 to 2024
SEED = 42

def aggregate_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    input_file = os.path.join(project_root, "data", "calibration", "raw_extracted_market_data.json")
    output_file = os.path.join(project_root, "data", "calibration", "market_index_returns.csv")
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Run extract_reports.py first.")
        return

    with open(input_file, "r") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # 1. Cleaning
    # Drop records without an index_code or year
    df = df.dropna(subset=['index_code', 'year'])
    # Ensure year is integer
    df['year'] = df['year'].astype(int)
    # Filter for target years only
    df = df[df['year'].isin(YEAR_RANGE)]

    # 2. Component Reconciliation
    # If annual_return is null, try to calculate it from components
    # If components are null, we still keep the record to see if other records for the same group have them
    df['annual_return'] = df['annual_return'].fillna(df['capital_apprc'].fillna(0) + df['rental_yield'].fillna(0))
    # If annual_return was 0 because components were null, turn back to NaN for proper averaging
    df.loc[(df['annual_return'] == 0) & (df['capital_apprc'].isna()) & (df['rental_yield'].isna()), 'annual_return'] = np.nan

    # 3. Aggregation (Averaging multiple reports for the same index/year)
    grouped = df.groupby(['index_code', 'year']).agg({
        'capital_apprc': 'mean',
        'rental_yield': 'mean',
        'annual_return': 'mean'
    }).reset_index()

    grouped['is_simulated'] = False
    grouped['data_source'] = "Aggregated Reports"

    # 4. Identifying Gaps and GBM Backfill
    all_combinations = []
    for code in INDEX_CODES:
        for year in YEAR_RANGE:
            all_combinations.append({'index_code': code, 'year': year})
    
    full_df = pd.DataFrame(all_combinations)
    final_df = pd.merge(full_df, grouped, on=['index_code', 'year'], how='left')

    # Seed for reproducibility in GBM
    np.random.seed(SEED)

    # Calculate global μ and σ for backfilling where index-specific data is too sparse
    # As per methodology: annual_return = μ + σ * ε
    global_mu = final_df['annual_return'].mean() if not final_df['annual_return'].isna().all() else 0.12
    global_sigma = final_df['annual_return'].std() if final_df['annual_return'].count() > 1 else 0.05

    for index, row in final_df.iterrows():
        if pd.isna(row['annual_return']):
            # For this dissertation, if we don't have index-specific stats yet, we use global proxies
            # derived from the observed Nigerian market data context
            mu = global_mu
            sigma = global_sigma
            
            # Simple GBM step
            epsilon = np.random.normal(0, 1)
            simulated_return = mu + sigma * epsilon
            
            final_df.at[index, 'annual_return'] = simulated_return
            final_df.at[index, 'is_simulated'] = True
            final_df.at[index, 'data_source'] = "GBM Backfill"
            # Split simulated return into components using a 60/40 rule of thumb if missing
            final_df.at[index, 'capital_apprc'] = simulated_return * 0.6
            final_df.at[index, 'rental_yield'] = simulated_return * 0.4

    # 5. Export
    final_df.to_csv(output_file, index=False)
    print(f"Aggregation complete. Processed {len(grouped)} observed points.")
    print(f"Filled {final_df['is_simulated'].sum()} points via GBM.")
    print(f"Saved to {output_file}")

if __name__ == "__main__":
    aggregate_data()
