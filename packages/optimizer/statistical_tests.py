# packages/optimizer/statistical_tests.py
"""
Statistical Analysis and Hypothesis Testing Module (Phase 4).
Computes performance metrics M1-M6, paired t-tests, Cohen's d,
BCa block bootstrap, market condition sub-analysis, and sensitivity checks.
"""

import os
import json
import numpy as np
import pandas as pd
import scipy.stats as stats

def load_simulation_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    sim_dir = os.path.join(project_root, "outputs", "simulation_results")
    port_dir = os.path.join(project_root, "outputs", "portfolios")
    
    paths_A = np.load(os.path.join(sim_dir, "portfolio_A_paths_all.npy"))
    paths_B = np.load(os.path.join(sim_dir, "portfolio_B_paths_all.npy"))
    returns_A = np.load(os.path.join(sim_dir, "portfolio_A_returns_all.npy"))
    returns_B = np.load(os.path.join(sim_dir, "portfolio_B_returns_all.npy"))
    
    with open(os.path.join(port_dir, "portfolio_A_heuristic.json"), "r") as f:
        port_A = json.load(f)
    with open(os.path.join(port_dir, "portfolio_B_optimized.json"), "r") as f:
        port_B = json.load(f)
        
    return paths_A, paths_B, returns_A, returns_B, port_A, port_B

def calculate_mdd(paths):
    """
    Computes Maximum Drawdown for each path.
    """
    # paths shape: (n_paths, n_months + 1)
    peaks = np.maximum.accumulate(paths, axis=1)
    drawdowns = (peaks - paths) / peaks
    mdds = np.max(drawdowns, axis=1)
    return mdds

def calculate_metrics(paths, returns, holdings, rf=0.084):
    """
    Computes performance metrics M1-M6 across the 10,000 paths.
    """
    # M1: Cumulative Return (CR)
    v_0 = paths[:, 0]
    v_T = paths[:, -1]
    crs = (v_T - v_0) / v_0
    
    # M2: CAGR
    cagrs = (v_T / v_0) ** (1.0 / 5.0) - 1.0
    
    # M3: Annualized Volatility
    # monthly returns shape: (n_paths, 60)
    vols_ann = np.std(returns, axis=1) * np.sqrt(12.0)
    
    # M4: Sharpe Ratio (using CAGR as return as per checklist M1)
    # Checklist formula: (CAGR - Rf) / Vol
    srs = (cagrs - rf) / vols_ann
    
    # M5: Max Drawdown (MDD)
    mdds = calculate_mdd(paths)
    
    # CVaR 95% of cumulative returns
    var_95 = np.percentile(crs, 5.0)
    cvar_95 = np.mean(crs[crs <= var_95])
    
    # M6: Diversification Ratio (DR)
    # DR = (sum w_i * sigma_i) / sigma_portfolio
    # Individual asset volatilities are in annual terms
    weighted_vols = sum(h["weight"] * h["total_volatility"] for h in holdings)
    drs = weighted_vols / vols_ann
    
    return {
        "crs": crs,
        "cagrs": cagrs,
        "vols_ann": vols_ann,
        "srs": srs,
        "mdds": mdds,
        "cvar_95": cvar_95,
        "drs": drs
    }

def calculate_hhi(holdings):
    """
    Computes Herfindahl-Hirschman Index (HHI) for holdings, states, and asset types.
    """
    # Standard HHI: sum(w_i^2)
    weights = np.array([h["weight"] for h in holdings])
    hhi = float(np.sum(weights ** 2))
    
    # Geographic HHI
    df_holdings = pd.DataFrame(holdings)
    geo_weights = df_holdings.groupby("location_state")["weight"].sum()
    geo_hhi = float(np.sum(geo_weights ** 2))
    
    # Asset-type HHI
    type_weights = df_holdings.groupby("asset_type")["weight"].sum()
    type_hhi = float(np.sum(type_weights ** 2))
    
    return hhi, geo_hhi, type_hhi

def calculate_bca_bootstrap(returns_A, returns_B, rf=0.084, n_replications=10000, block_size=6):
    """
    Computes 95% BCa block bootstrap confidence interval for Delta SR (SR_B - SR_A).
    """
    n_paths, n_months = returns_A.shape
    n_blocks = n_months // block_size # 10 blocks
    
    # Reshape returns into blocks of shape (n_paths, n_blocks, block_size)
    blocks_A = returns_A.reshape(n_paths, n_blocks, block_size)
    blocks_B = returns_B.reshape(n_paths, n_blocks, block_size)
    
    # 1. Compute bootstrap replications of the mean Delta SR
    np.random.seed(42)
    boot_deltas = np.zeros(n_replications)
    
    for b in range(n_replications):
        # Resample block indices
        idxs = np.random.randint(0, n_blocks, size=n_blocks)
        
        res_A = blocks_A[:, idxs, :].reshape(n_paths, n_months)
        res_B = blocks_B[:, idxs, :].reshape(n_paths, n_months)
        
        # Calculate Sharpe for both
        cagr_A = (np.prod(1.0 + res_A, axis=1)) ** (1.0 / 5.0) - 1.0
        vol_A = np.std(res_A, axis=1) * np.sqrt(12.0)
        sr_A = (cagr_A - rf) / vol_A
        
        cagr_B = (np.prod(1.0 + res_B, axis=1)) ** (1.0 / 5.0) - 1.0
        vol_B = np.std(res_B, axis=1) * np.sqrt(12.0)
        sr_B = (cagr_B - rf) / vol_B
        
        boot_deltas[b] = np.mean(sr_B - sr_A)
        
    # 2. Compute original Delta SR
    cagr_orig_A = (np.prod(1.0 + returns_A, axis=1)) ** (1.0 / 5.0) - 1.0
    vol_orig_A = np.std(returns_A, axis=1) * np.sqrt(12.0)
    sr_orig_A = (cagr_orig_A - rf) / vol_orig_A
    
    cagr_orig_B = (np.prod(1.0 + returns_B, axis=1)) ** (1.0 / 5.0) - 1.0
    vol_orig_B = np.std(returns_B, axis=1) * np.sqrt(12.0)
    sr_orig_B = (cagr_orig_B - rf) / vol_orig_B
    
    orig_deltas = sr_orig_B - sr_orig_A
    orig_theta = np.mean(orig_deltas)
    
    # 3. Bias correction parameter (z0)
    p_lower = np.sum(boot_deltas < orig_theta) / n_replications
    p_lower = np.clip(p_lower, 1.0 / n_replications, 1.0 - (1.0 / n_replications))
    z0 = stats.norm.ppf(p_lower)
    
    # 4. Acceleration parameter (a) via jackknife over the 10 blocks
    jack_deltas = np.zeros(n_blocks)
    for i in range(n_blocks):
        # Leave out block i
        jack_idxs = [j for j in range(n_blocks) if j != i]
        jack_A = blocks_A[:, jack_idxs, :].reshape(n_paths, (n_blocks - 1) * block_size)
        jack_B = blocks_B[:, jack_idxs, :].reshape(n_paths, (n_blocks - 1) * block_size)
        
        # Calculate Sharpe over 54 months (4.5 years)
        cagr_j_A = (np.prod(1.0 + jack_A, axis=1)) ** (1.0 / 4.5) - 1.0
        vol_j_A = np.std(jack_A, axis=1) * np.sqrt(12.0)
        sr_j_A = (cagr_j_A - rf) / vol_j_A
        
        cagr_j_B = (np.prod(1.0 + jack_B, axis=1)) ** (1.0 / 4.5) - 1.0
        vol_j_B = np.std(jack_B, axis=1) * np.sqrt(12.0)
        sr_j_B = (cagr_j_B - rf) / vol_j_B
        
        jack_deltas[i] = np.mean(sr_j_B - sr_j_A)
        
    mean_jack = np.mean(jack_deltas)
    num = np.sum((mean_jack - jack_deltas) ** 3)
    den = 6.0 * (np.sum((mean_jack - jack_deltas) ** 2) ** 1.5)
    a = num / den if den != 0 else 0.0
    
    # 5. Compute BCa endpoints
    z_alpha = stats.norm.ppf(0.025)
    z_1_alpha = stats.norm.ppf(0.975)
    
    alpha1 = stats.norm.cdf(z0 + (z0 + z_alpha) / (1.0 - a * (z0 + z_alpha)))
    alpha2 = stats.norm.cdf(z0 + (z0 + z_1_alpha) / (1.0 - a * (z0 + z_1_alpha)))
    
    # Fallback to standard percentile bootstrap if bounds collapse or if p_lower is too close to boundaries
    # (BCa is unstable when p_lower < 0.05 or > 0.95 due to poor overlap)
    if p_lower <= 0.05 or p_lower >= 0.95 or np.isnan(alpha1) or np.isnan(alpha2):
        ci_lower = np.percentile(boot_deltas, 2.5)
        ci_upper = np.percentile(boot_deltas, 97.5)
    else:
        ci_lower = np.percentile(boot_deltas, alpha1 * 100)
        ci_upper = np.percentile(boot_deltas, alpha2 * 100)
        
    return orig_theta, ci_lower, ci_upper

def run_statistical_analysis():
    paths_A, paths_B, returns_A, returns_B, port_A, port_B = load_simulation_data()
    
    rf = 0.084
    
    # 1. Compute path-by-path metrics
    metrics_A = calculate_metrics(paths_A, returns_A, port_A["holdings"], rf)
    metrics_B = calculate_metrics(paths_B, returns_B, port_B["holdings"], rf)
    
    # 2. Run paired t-test on Sharpe Ratio difference (one-tailed: B > A)
    # H0: SR_B <= SR_A vs H1: SR_B > SR_A
    ttest_res = stats.ttest_rel(metrics_B["srs"], metrics_A["srs"])
    p_value_one_tailed = ttest_res.pvalue / 2.0 if ttest_res.statistic > 0 else 1.0 - (ttest_res.pvalue / 2.0)
    
    # Cohen's d
    diff_sr = metrics_B["srs"] - metrics_A["srs"]
    cohen_d = np.mean(diff_sr) / np.std(diff_sr) if np.std(diff_sr) != 0 else 0.0
    
    # 3. Calculate HHI
    hhi_A, geo_hhi_A, type_hhi_A = calculate_hhi(port_A["holdings"])
    hhi_B, geo_hhi_B, type_hhi_B = calculate_hhi(port_B["holdings"])
    
    # 4. Market condition sub-analysis (terciles of market volatility)
    # We define market volatility based on Portfolio A's path volatility
    vols_A = metrics_A["vols_ann"]
    tercile_33 = np.percentile(vols_A, 33.33)
    tercile_66 = np.percentile(vols_A, 66.67)
    
    low_idx = vols_A <= tercile_33
    med_idx = (vols_A > tercile_33) & (vols_A <= tercile_66)
    high_idx = vols_A > tercile_66
    
    diff_srs = metrics_B["srs"] - metrics_A["srs"]
    sub_analysis = {
        "low_volatility": {
            "count": int(np.sum(low_idx)),
            "mean_sr_A": float(np.mean(metrics_A["srs"][low_idx])),
            "mean_sr_B": float(np.mean(metrics_B["srs"][low_idx])),
            "mean_diff": float(np.mean(diff_srs[low_idx]))
        },
        "medium_volatility": {
            "count": int(np.sum(med_idx)),
            "mean_sr_A": float(np.mean(metrics_A["srs"][med_idx])),
            "mean_sr_B": float(np.mean(metrics_B["srs"][med_idx])),
            "mean_diff": float(np.mean(diff_srs[med_idx]))
        },
        "high_volatility": {
            "count": int(np.sum(high_idx)),
            "mean_sr_A": float(np.mean(metrics_A["srs"][high_idx])),
            "mean_sr_B": float(np.mean(metrics_B["srs"][high_idx])),
            "mean_diff": float(np.mean(diff_srs[high_idx]))
        }
    }
    
    # 5. BCa block bootstrap for Delta SR
    delta_mean, ci_lower, ci_upper = calculate_bca_bootstrap(returns_A, returns_B, rf)
    
    # Significance flags
    stat_sig = bool(ci_lower > 0.0 or ci_upper < 0.0)
    prac_sig = bool(delta_mean >= 0.05)
    
    # 6. Sensitivity Analysis
    sensitivity_results = {}
    for rf_test in [0.10, 0.15, 0.20]:
        test_A = calculate_metrics(paths_A, returns_A, port_A["holdings"], rf_test)
        test_B = calculate_metrics(paths_B, returns_B, port_B["holdings"], rf_test)
        sensitivity_results[f"rf_{int(rf_test*100)}"] = {
            "mean_sr_A": float(np.mean(test_A["srs"])),
            "mean_sr_B": float(np.mean(test_B["srs"])),
            "mean_diff": float(np.mean(test_B["srs"] - test_A["srs"]))
        }
        
    # Summary of metrics for saving
    summary = {
        "benchmark_rf": rf,
        "portfolio_A": {
            "name": port_A["portfolio_name"],
            "mean_cumulative_return": float(np.mean(metrics_A["crs"])),
            "mean_cagr": float(np.mean(metrics_A["cagrs"])),
            "mean_volatility": float(np.mean(metrics_A["vols_ann"])),
            "mean_sharpe": float(np.mean(metrics_A["srs"])),
            "mean_mdd": float(np.mean(metrics_A["mdds"])),
            "cvar_95": float(metrics_A["cvar_95"]),
            "mean_diversification_ratio": float(np.mean(metrics_A["drs"])),
            "hhi": hhi_A,
            "geo_hhi": geo_hhi_A,
            "type_hhi": type_hhi_A
        },
        "portfolio_B": {
            "name": port_B["portfolio_name"],
            "mean_cumulative_return": float(np.mean(metrics_B["crs"])),
            "mean_cagr": float(np.mean(metrics_B["cagrs"])),
            "mean_volatility": float(np.mean(metrics_B["vols_ann"])),
            "mean_sharpe": float(np.mean(metrics_B["srs"])),
            "mean_mdd": float(np.mean(metrics_B["mdds"])),
            "cvar_95": float(metrics_B["cvar_95"]),
            "mean_diversification_ratio": float(np.mean(metrics_B["drs"])),
            "hhi": hhi_B,
            "geo_hhi": geo_hhi_B,
            "type_hhi": type_hhi_B
        },
        "hypothesis_testing": {
            "paired_t_test": {
                "t_statistic": float(ttest_res.statistic),
                "p_value_one_tailed": float(p_value_one_tailed),
                "cohen_d": float(cohen_d)
            },
            "bca_bootstrap": {
                "mean_delta_sr": float(delta_mean),
                "ci_lower": float(ci_lower),
                "ci_upper": float(ci_upper),
                "statistically_significant": stat_sig,
                "practically_significant": prac_sig
            },
            "market_conditions_sub_analysis": sub_analysis
        },
        "sensitivity_analysis": sensitivity_results
    }
    
    # Save results to json
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    out_path = os.path.join(project_root, "outputs", "simulation_results", "summary_metrics.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
        
    print(f"Summary metrics and hypothesis test results saved to {out_path}")
    
    # Print high-level results to console
    print("\n--- HIGH-LEVEL RESULTS ---")
    print(f"Portfolio A Mean Sharpe: {summary['portfolio_A']['mean_sharpe']:.4f}")
    print(f"Portfolio B Mean Sharpe: {summary['portfolio_B']['mean_sharpe']:.4f}")
    print(f"Delta Sharpe (B - A): {summary['hypothesis_testing']['bca_bootstrap']['mean_delta_sr']:.4f}")
    print(f"BCa 95% Confidence Interval: [{summary['hypothesis_testing']['bca_bootstrap']['ci_lower']:.4f}, {summary['hypothesis_testing']['bca_bootstrap']['ci_upper']:.4f}]")
    print(f"Statistically Significant (excludes 0): {summary['hypothesis_testing']['bca_bootstrap']['statistically_significant']}")
    print(f"Practically Significant (>= 0.05): {summary['hypothesis_testing']['bca_bootstrap']['practically_significant']}")
    print(f"Paired t-statistic: {summary['hypothesis_testing']['paired_t_test']['t_statistic']:.4f}, p-value: {summary['hypothesis_testing']['paired_t_test']['p_value_one_tailed']:.4e}")
    print(f"Cohen's d: {summary['hypothesis_testing']['paired_t_test']['cohen_d']:.4f}")

if __name__ == "__main__":
    run_statistical_analysis()
