# packages/generator/validate_universe.py
"""
Statistical validation script for the generated property universe.
Verifies all 9 pre-registered validation tests and generates dissertation-quality charts.
"""

import os
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
import config

# Set matplotlib parameters for dissertation-quality figures
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'

def build_property_covariance(df, index_corr):
    """
    Builds the 80x80 property-level covariance matrix from index correlations and property volatilities.
    """
    n = len(df)
    cov_matrix = np.zeros((n, n))
    
    for i in range(n):
        idx_i = df.loc[i, 'market_index_id']
        vol_i = df.loc[i, 'total_volatility']
        
        for j in range(n):
            idx_j = df.loc[j, 'market_index_id']
            vol_j = df.loc[j, 'total_volatility']
            
            if i == j:
                cov_matrix[i, j] = vol_i ** 2
            else:
                corr = index_corr.loc[idx_i, idx_j]
                cov_matrix[i, j] = corr * vol_i * vol_j
                
    return cov_matrix

def run_validation():
    print("Starting statistical validation...")
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    calculated_csv = os.path.join(project_root, "packages", "generator", "temp", "temp_calculated_universe.csv")
    market_returns_csv = os.path.join(project_root, "data", "calibration", "market_index_returns.csv")
    
    # Target output directories
    chart_dir = os.path.join(project_root, "outputs", "charts")
    val_dir = os.path.join(project_root, "outputs", "validation")
    os.makedirs(chart_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    
    if not os.path.exists(calculated_csv):
        print(f"Error: {calculated_csv} not found. Run metrics_calculator.py first.")
        return
        
    df = pd.read_csv(calculated_csv)
    df_ret = pd.read_csv(market_returns_csv)
    
    # Calculate index correlations from returns CSV
    df_piv = df_ret.pivot(index='year', columns='index_code', values='annual_return')
    index_corr = df_piv.corr()
    
    results = {}
    
    # Test 1: Log-normality of prices (KS test on standardized log(asking_price))
    log_prices = np.log(df['asking_price'])
    z_prices = (log_prices - log_prices.mean()) / log_prices.std()
    ks_stat, ks_p = stats.kstest(z_prices, 'norm')
    results["Test 1: Price Log-normality"] = {
        "status": "PASS" if ks_p > 0.05 else "FAIL",
        "value": f"KS stat = {ks_stat:.4f}, p-value = {ks_p:.4f} (expected p > 0.05)"
    }
    
    # Test 2: Price skewness
    skew = df['asking_price'].skew()
    results["Test 2: Price Skewness"] = {
        "status": "PASS" if skew > 0 else "FAIL",
        "value": f"Skewness = {skew:.4f} (expected > 0)"
    }
    
    # Test 3: Price mean > median
    mean_val = df['asking_price'].mean()
    median_val = df['asking_price'].median()
    results["Test 3: Price Mean > Median"] = {
        "status": "PASS" if mean_val > median_val else "FAIL",
        "value": f"Mean = ₦{mean_val/1e6:.1f}M, Median = ₦{median_val/1e6:.1f}M (expected mean > median)"
    }
    
    # Test 4: Gross yield range
    gross_yields = df['estimated_annual_rent'] / df['asking_price']
    yield_min = gross_yields.min()
    yield_max = gross_yields.max()
    yields_ok = all(0.04 - 1e-4 <= y <= 0.14 + 1e-4 for y in gross_yields)
    results["Test 4: Gross Yield Range"] = {
        "status": "PASS" if yields_ok else "FAIL",
        "value": f"Yield range = [{yield_min:.2%}, {yield_max:.2%}] (expected [4.0%, 14.0%])"
    }
    
    # Test 5: State count >= 5
    state_count = df['location_state'].nunique()
    results["Test 5: State Count"] = {
        "status": "PASS" if state_count >= 5 else "FAIL",
        "value": f"States represented = {state_count} (expected >= 5)"
    }
    
    # Test 6: Lagos share < 70%
    lagos_count = (df['location_state'] == 'Lagos').sum()
    lagos_share = lagos_count / len(df)
    results["Test 6: Lagos Share Limit"] = {
        "status": "PASS" if lagos_share < 0.70 else "FAIL",
        "value": f"Lagos share = {lagos_share:.2%} ({lagos_count}/80) (expected < 70%)"
    }
    
    # Test 7: Sub-optimal title share [20%, 40%]
    suboptimal_titles = ["Gazette", "Excision", "Deed of Assignment"]
    suboptimal_count = df['title_status'].isin(suboptimal_titles).sum()
    suboptimal_share = suboptimal_count / len(df)
    results["Test 7: Sub-optimal Title Share"] = {
        "status": "PASS" if 0.20 <= suboptimal_share <= 0.40 else "FAIL",
        "value": f"Sub-optimal title share = {suboptimal_share:.2%} ({suboptimal_count}/80) (expected [20%, 40%])"
    }
    
    # Test 8: Covariance Matrix PSD Check
    cov_matrix = build_property_covariance(df, index_corr)
    eigenvalues = np.linalg.eigvals(cov_matrix)
    min_eig = eigenvalues.min()
    results["Test 8: Covariance PSD"] = {
        "status": "PASS" if min_eig >= -1e-10 else "FAIL",
        "value": f"Min eigenvalue = {min_eig:.4e} (expected >= -1.0e-10)"
    }
    
    # Test 9: Heuristic Eligible Pool Size >= 25
    eligible_count = df['is_heuristic_eligible'].sum()
    results["Test 9: Heuristic Eligible Pool"] = {
        "status": "PASS" if eligible_count >= 25 else "FAIL",
        "value": f"Heuristic eligible properties = {eligible_count}/80 (expected >= 25)"
    }
    
    # Save the 80x80 covariance matrix to outputs for Phase 4
    cov_df = pd.DataFrame(cov_matrix, index=df['property_id'], columns=df['property_id'])
    cov_df.to_csv(os.path.join(project_root, "packages", "generator", "temp", "temp_covariance_matrix.csv"))
    
    # Generate report file
    report_file = os.path.join(val_dir, "validation_report.txt")
    with open(report_file, "w") as f:
        f.write("="*70 + "\n")
        f.write("PROPERTY UNIVERSE VALIDATION REPORT\n")
        f.write("="*70 + "\n\n")
        f.write(f"Generated at: {pd.Timestamp.now().isoformat()}\n")
        f.write(f"Total Properties Sourced: {len(df)}\n\n")
        
        all_passed = True
        for test_name, test_res in results.items():
            f.write(f"{test_name}:\n")
            f.write(f"  Status: {test_res['status']}\n")
            f.write(f"  Details: {test_res['value']}\n\n")
            if test_res["status"] == "FAIL":
                all_passed = False
                
        f.write("="*70 + "\n")
        if all_passed:
            f.write("OVERALL STATUS: ALL VALIDATION TESTS PASSED ✓\n")
        else:
            f.write("OVERALL STATUS: VALIDATION FAILED ❌\n")
        f.write("="*70 + "\n")
        
    print(f"Validation report saved to {report_file}")
    
    # ==================== CHART GENERATION ====================
    print("Generating validation figures...")
    
    # 1. Figure 2.1: Q-Q Plot of Log Prices
    plt.figure()
    stats.probplot(log_prices, dist="norm", plot=plt)
    plt.title("Q-Q Plot of Log-Transformed Asking Prices")
    plt.xlabel("Theoretical Quantiles")
    plt.ylabel("Ordered Log Prices")
    plt.grid(True, alpha=0.3)
    plt.savefig(os.path.join(chart_dir, "qqplot_prices.png"), dpi=300, bbox_inches='tight')
    plt.close()
    
    # 2. Figure 2.2: Geographic Distribution Pie Chart
    plt.figure()
    geo_counts = df['location_state'].value_counts()
    # Handle 'Abuja' as state for chart
    labels = geo_counts.index
    plt.pie(geo_counts, labels=labels, autopct='%1.1f%%', startangle=140, 
            colors=sns.color_palette("viridis", len(labels)))
    plt.title("Geographic Distribution of Synthetic Property Universe")
    plt.savefig(os.path.join(chart_dir, "geo_distribution.png"), dpi=300, bbox_inches='tight')
    plt.close()
    
    # 3. Figure 2.3: Asset Type Distribution Bar Chart
    plt.figure()
    asset_counts = df['asset_type'].value_counts()
    sns.barplot(x=asset_counts.index, y=asset_counts.values, palette="magma")
    plt.title("Asset Type Distribution of Synthetic Property Universe")
    plt.xlabel("Asset Class")
    plt.ylabel("Property Count")
    plt.grid(True, axis='y', alpha=0.3)
    plt.savefig(os.path.join(chart_dir, "asset_type_distribution.png"), dpi=300, bbox_inches='tight')
    plt.close()
    
    # 4. Figure 2.4: Covariance Matrix Heatmap (Sample 30 properties)
    plt.figure(figsize=(10, 8))
    sample_indices = np.linspace(0, len(df)-1, 30, dtype=int)
    sample_cov = cov_matrix[np.ix_(sample_indices, sample_indices)]
    sample_ids = df.loc[sample_indices, 'property_id']
    sns.heatmap(sample_cov, xticklabels=sample_ids, yticklabels=sample_ids, cmap="plasma")
    plt.title("Covariance Matrix Heatmap (Sample of 30 Properties)")
    plt.savefig(os.path.join(chart_dir, "covariance_heatmap.png"), dpi=300, bbox_inches='tight')
    plt.close()
    
    print("All charts generated and saved successfully.")
    return all_passed

if __name__ == "__main__":
    run_validation()
