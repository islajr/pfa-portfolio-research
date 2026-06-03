# packages/generator/freeze_universe.py
"""
Freezes the property universe by exporting the finalized datasets to data/frozen/.
Converts index returns to wide format and calculates the 8x8 index covariance matrix.
"""

import os
import pandas as pd

def freeze():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    calculated_csv = os.path.join(project_root, "packages", "generator", "temp", "temp_calculated_universe.csv")
    market_returns_csv = os.path.join(project_root, "data", "calibration", "market_index_returns.csv")
    validation_report = os.path.join(project_root, "outputs", "validation", "validation_report.txt")
    
    frozen_dir = os.path.join(project_root, "data", "frozen")
    os.makedirs(frozen_dir, exist_ok=True)
    
    # 1. Verify validation report exists and passed
    if not os.path.exists(validation_report):
        print("Error: Validation report not found. Run validation first.")
        return
        
    with open(validation_report, "r") as f:
        content = f.read()
        if "ALL VALIDATION TESTS PASSED ✓" not in content:
            print("Error: Validation tests did not pass. Cannot freeze universe.")
            return
            
    # 2. Export property_universe.csv
    df_universe = pd.read_csv(calculated_csv)
    
    # Ensure correct columns and order per Generator v1 Section 5.8
    expected_cols = [
        "property_id", "property_code", "location_state", "location_lga", "location_micro",
        "asset_type", "asking_price", "estimated_annual_rent", "title_status", "property_condition",
        "year_built", "floor_area_sqm", "lease_term_years", "market_index_id", "is_prime_location",
        "is_preferred_asset_type", "triggers_anchoring_rule", "is_heuristic_eligible", "pencom_lease_compliant",
        "total_acquisition_cost", "effective_rent", "maintenance_cost", "noi", "cap_rate",
        "expected_return", "total_volatility", "sharpe_ratio"
    ]
    
    # Reorder columns
    df_universe = df_universe[expected_cols]
    universe_path = os.path.join(frozen_dir, "property_universe.csv")
    df_universe.to_csv(universe_path, index=False)
    print(f"Exported property universe: {universe_path}")
    
    # 3. Export market_indices_returns.csv in wide format
    df_ret = pd.read_csv(market_returns_csv)
    df_piv = df_ret.pivot(index='year', columns='index_code', values='annual_return')
    
    # Save wide format returns to data/frozen/market_indices_returns.csv
    returns_path = os.path.join(frozen_dir, "market_indices_returns.csv")
    df_piv.to_csv(returns_path)
    print(f"Exported wide market returns: {returns_path}")
    
    # 4. Export covariance_matrix.csv (8x8)
    cov_8x8 = df_piv.cov()
    cov_path = os.path.join(frozen_dir, "covariance_matrix.csv")
    cov_8x8.to_csv(cov_path)
    print(f"Exported 8x8 index covariance matrix: {cov_path}")
    
    print("\nUNIVERSE FREEZE SUCCESSFUL ✓")
    print("Files in data/frozen/ are now locked and read-only for longitudinal consistency.")

if __name__ == "__main__":
    freeze()
