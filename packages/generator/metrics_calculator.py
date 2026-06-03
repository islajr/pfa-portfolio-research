# packages/generator/metrics_calculator.py
"""
Calculates financial metrics for each property in the universe.
Includes unit tests with hand-calculated examples to verify mathematical correctness.
"""

import os
import pandas as pd
import numpy as np
import config

def load_index_stats(market_returns_csv):
    """
    Computes mean capital appreciation (mu) and standard deviation of returns (sigma)
    for each of the 8 market indices from the frozen/calibration returns CSV.
    """
    df_ret = pd.read_csv(market_returns_csv)
    index_stats = {}
    
    for code in df_ret['index_code'].unique():
        subset = df_ret[df_ret['index_code'] == code]
        
        # Mean capital appreciation (capital_apprc)
        # Sourced from data; if NaN, fallback to annual_return * 0.6
        mu_cap = subset['capital_apprc'].dropna().mean()
        if pd.isna(mu_cap):
            mu_cap = subset['annual_return'].mean() * 0.6
            
        # Standard deviation of total annual returns
        sigma_ret = subset['annual_return'].std()
        if pd.isna(sigma_ret) or sigma_ret == 0:
            sigma_ret = 0.05  # Reasonable default fallback
            
        index_stats[code] = {
            "mu_cap": mu_cap,
            "sigma_ret": sigma_ret
        }
    return index_stats

def compute_property_metrics(prop_dict, index_stats, rf_rate):
    """
    Computes all 8 financial metrics for a single property dictionary.
    """
    price = prop_dict["asking_price"]
    rent = prop_dict["estimated_annual_rent"]
    state = prop_dict["location_state"]
    asset_type = prop_dict["asset_type"]
    title = prop_dict["title_status"]
    condition = prop_dict["property_condition"]
    index_code = prop_dict["market_index_id"]
    
    # 1. Total Acquisition Cost (TAC)
    f_agency = config.TRANSACTION_COSTS["agency_fee_pct"]
    f_legal = config.TRANSACTION_COSTS["legal_fee_pct"]
    f_consent = (
        config.TRANSACTION_COSTS["consent_fee_lagos_pct"]
        if state == "Lagos"
        else config.TRANSACTION_COSTS["consent_fee_other_pct"]
    )
    total_acquisition_cost = price * (1.0 + f_agency + f_legal + f_consent)
    
    # 2. Net Operating Income (NOI)
    v_rate = config.VACANCY_RATES[asset_type]
    m_rate = config.MAINTENANCE_RATES[asset_type]
    
    effective_rent = rent * (1.0 - v_rate)
    maintenance_cost = rent * m_rate
    noi = effective_rent - maintenance_cost
    
    # 3. Capitalization Rate (Cap Rate)
    cap_rate = noi / total_acquisition_cost
    
    # 4. Expected Return
    # expected_return = cap_rate + index_capital_appreciation_mean
    stats = index_stats.get(index_code, {"mu_cap": 0.05, "sigma_ret": 0.06})
    mu_idx = stats["mu_cap"]
    expected_return = cap_rate + mu_idx
    
    # 5. Volatility
    sigma_idx = stats["sigma_ret"]
    title_premium = config.TITLE_RISK_PREMIUMS[title]
    cond_premium = config.CONDITION_RISK_PREMIUMS[condition]
    total_volatility = sigma_idx + title_premium + cond_premium
    
    # 6. Sharpe Ratio
    sharpe_ratio = (expected_return - rf_rate) / total_volatility
    
    return {
        "total_acquisition_cost": round(total_acquisition_cost, 2),
        "effective_rent": round(effective_rent, 2),
        "maintenance_cost": round(maintenance_cost, 2),
        "noi": round(noi, 2),
        "cap_rate": round(cap_rate, 6),
        "expected_return": round(expected_return, 6),
        "total_volatility": round(total_volatility, 6),
        "sharpe_ratio": round(sharpe_ratio, 6)
    }

def run_unit_tests():
    """
    Runs metrics calculator tests against 3 hand-calculated test cases.
    """
    print("Running metrics calculator unit tests...")
    
    # Mock index statistics
    mock_stats = {
        "LG_OFF_ISL": {"mu_cap": 0.080000, "sigma_ret": 0.060000},
        "AB_RET_CEN": {"mu_cap": 0.060000, "sigma_ret": 0.080000},
        "KN_IND_NTH": {"mu_cap": 0.040000, "sigma_ret": 0.050000}
    }
    rf = 0.15
    
    # Case 1: Lagos Office, C of O, New, 500M price, 40M rent
    case1 = {
        "asking_price": 500_000_000.0,
        "estimated_annual_rent": 40_000_000.0,
        "location_state": "Lagos",
        "asset_type": "Office",
        "title_status": "C of O",
        "property_condition": "New",
        "market_index_id": "LG_OFF_ISL"
    }
    
    res1 = compute_property_metrics(case1, mock_stats, rf)
    
    # Hand Calculations:
    # TAC = 500M * (1 + 0.05 + 0.05 + 0.10) = 600M
    # Effective Rent = 40M * (1 - 0.05) = 38M
    # Maintenance = 40M * 0.10 = 4M
    # NOI = 38M - 4M = 34M
    # Cap Rate = 34M / 600M = 0.056667
    # Expected Return = 0.056667 + 0.08 = 0.136667
    # Volatility = 0.06 + 0.0 + 0.0 = 0.06
    # Sharpe = (0.136667 - 0.15) / 0.06 = -0.22222
    
    assert abs(res1["total_acquisition_cost"] - 600_000_000.0) < 1e-2, f"Failed Case 1 TAC: {res1['total_acquisition_cost']}"
    assert abs(res1["noi"] - 34_000_000.0) < 1e-2, f"Failed Case 1 NOI: {res1['noi']}"
    assert abs(res1["cap_rate"] - 0.056667) < 1e-4, f"Failed Case 1 Cap Rate: {res1['cap_rate']}"
    assert abs(res1["expected_return"] - 0.136667) < 1e-4, f"Failed Case 1 Exp Return: {res1['expected_return']}"
    assert abs(res1["total_volatility"] - 0.06) < 1e-4, f"Failed Case 1 Volatility: {res1['total_volatility']}"
    assert abs(res1["sharpe_ratio"] - -0.222222) < 1e-4, f"Failed Case 1 Sharpe: {res1['sharpe_ratio']}"
    print("✓ Case 1 passed.")

    # Case 2: Abuja Commercial (Asset Type: Commercial), Gov Consent, Good, 200M price, 20M rent
    case2 = {
        "asking_price": 200_000_000.0,
        "estimated_annual_rent": 20_000_000.0,
        "location_state": "Abuja",
        "asset_type": "Commercial",
        "title_status": "Gov Consent",
        "property_condition": "Good",
        "market_index_id": "AB_RET_CEN"
    }
    res2 = compute_property_metrics(case2, mock_stats, rf)
    
    # Hand Calculations:
    # TAC = 200M * (1 + 0.05 + 0.05 + 0.05) = 230M
    # Effective Rent = 20M * (1 - 0.04) = 19.2M
    # Maintenance = 20M * 0.10 = 2.0M
    # NOI = 19.2M - 2.0M = 17.2M
    # Cap Rate = 17.2M / 230M = 0.074783
    # Expected Return = 0.074783 + 0.06 = 0.134783
    # Volatility = 0.08 (index) + 0.005 (consent) + 0.005 (good) = 0.090000
    # Sharpe = (0.134783 - 0.15) / 0.09 = -0.16908
    
    assert abs(res2["total_acquisition_cost"] - 230_000_000.0) < 1e-2, f"Failed Case 2 TAC: {res2['total_acquisition_cost']}"
    assert abs(res2["noi"] - 17_200_000.0) < 1e-2, f"Failed Case 2 NOI: {res2['noi']}"
    assert abs(res2["cap_rate"] - 0.074783) < 1e-4, f"Failed Case 2 Cap Rate: {res2['cap_rate']}"
    assert abs(res2["expected_return"] - 0.134783) < 1e-4, f"Failed Case 2 Exp Return: {res2['expected_return']}"
    assert abs(res2["total_volatility"] - 0.09) < 1e-4, f"Failed Case 2 Volatility: {res2['total_volatility']}"
    assert abs(res2["sharpe_ratio"] - -0.16908) < 1e-4, f"Failed Case 2 Sharpe: {res2['sharpe_ratio']}"
    print("✓ Case 2 passed.")

    # Case 3: Kano Industrial, Gazette, Needs Renovation, 100M price, 12M rent
    case3 = {
        "asking_price": 100_000_000.0,
        "estimated_annual_rent": 12_000_000.0,
        "location_state": "Kano",
        "asset_type": "Industrial",
        "title_status": "Gazette",
        "property_condition": "Needs Renovation",
        "market_index_id": "KN_IND_NTH"
    }
    res3 = compute_property_metrics(case3, mock_stats, rf)
    
    # Hand Calculations:
    # TAC = 100M * (1 + 0.05 + 0.05 + 0.05) = 115M
    # Effective Rent = 12M * (1 - 0.05) = 11.4M
    # Maintenance = 12M * 0.08 = 0.96M
    # NOI = 11.4M - 0.96M = 10.44M
    # Cap Rate = 10.44M / 115M = 0.090783
    # Expected Return = 0.090783 + 0.04 = 0.130783
    # Volatility = 0.05 (index) + 0.030 (gazette) + 0.030 (needs renovation) = 0.110000
    # Sharpe = (0.130783 - 0.15) / 0.11 = -0.17470
    
    assert abs(res3["total_acquisition_cost"] - 115_000_000.0) < 1e-2, f"Failed Case 3 TAC: {res3['total_acquisition_cost']}"
    assert abs(res3["noi"] - 10_440_000.0) < 1e-2, f"Failed Case 3 NOI: {res3['noi']}"
    assert abs(res3["cap_rate"] - 0.090783) < 1e-4, f"Failed Case 3 Cap Rate: {res3['cap_rate']}"
    assert abs(res3["expected_return"] - 0.130783) < 1e-4, f"Failed Case 3 Exp Return: {res3['expected_return']}"
    assert abs(res3["total_volatility"] - 0.11) < 1e-4, f"Failed Case 3 Volatility: {res3['total_volatility']}"
    assert abs(res3["sharpe_ratio"] - -0.17470) < 1e-4, f"Failed Case 3 Sharpe: {res3['sharpe_ratio']}"
    print("✓ Case 3 passed.")
    print("All unit tests passed successfully!")

def calculate_metrics_for_universe():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    raw_csv = os.path.join(project_root, "packages", "generator", "temp", "temp_raw_universe.csv")
    market_returns_csv = os.path.join(project_root, "data", "calibration", "market_index_returns.csv")
    output_csv = os.path.join(project_root, "packages", "generator", "temp", "temp_calculated_universe.csv")
    
    if not os.path.exists(raw_csv):
        print(f"Error: {raw_csv} not found. Run generate_universe.py first.")
        return
        
    df = pd.read_csv(raw_csv)
    index_stats = load_index_stats(market_returns_csv)
    
    metrics = []
    for _, row in df.iterrows():
        prop_metrics = compute_property_metrics(row.to_dict(), index_stats, config.RISK_FREE_RATE)
        metrics.append(prop_metrics)
        
    df_metrics = pd.DataFrame(metrics)
    
    # Merge metrics back
    df_final = pd.concat([df, df_metrics], axis=1)
    
    df_final.to_csv(output_csv, index=False)
    print(f"Metrics calculation complete. Saved to {output_csv}")

if __name__ == "__main__":
    run_unit_tests()
    calculate_metrics_for_universe()
