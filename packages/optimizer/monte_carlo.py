# packages/optimizer/monte_carlo.py
"""
Monte Carlo Simulation Engine (GBM).
Simulates monthly property value paths over a 5-year (60-month) horizon
using Geometric Brownian Motion (Formula 3.10) for Portfolio A and Portfolio B.
"""

import os
import json
import numpy as np
import pandas as pd

def load_portfolios_and_cov():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    port_A_path = os.path.join(project_root, "outputs", "portfolios", "portfolio_A_heuristic.json")
    port_B_path = os.path.join(project_root, "outputs", "portfolios", "portfolio_B_optimized.json")
    cov_path = os.path.join(project_root, "data", "frozen", "property_covariance_matrix.csv")
    
    if not os.path.exists(port_A_path) or not os.path.exists(port_B_path) or not os.path.exists(cov_path):
        raise FileNotFoundError("Portfolios or covariance matrix not found. Run previous stages first.")
        
    with open(port_A_path, "r") as f:
        port_A = json.load(f)
    with open(port_B_path, "r") as f:
        port_B = json.load(f)
        
    df_cov = pd.read_csv(cov_path, index_col=0)
    return port_A, port_B, df_cov

def simulate_gbm(portfolio, df_cov, n_paths=10000, n_months=60):
    """
    Simulates monthly value paths using Geometric Brownian Motion (GBM).
    Returns:
      paths: np.ndarray of shape (n_paths, n_months + 1) containing portfolio values.
      returns: np.ndarray of shape (n_paths, n_months) containing monthly portfolio returns.
    """
    holdings = portfolio["holdings"]
    n_assets = len(holdings)
    
    # Extract asset properties
    property_ids = [h["property_id"] for h in holdings]
    expected_returns = np.array([h["expected_return"] for h in holdings])
    weights = np.array([h["weight"] for h in holdings])
    
    # Extract sub-covariance matrix
    sub_cov = df_cov.loc[property_ids, property_ids].values
    
    # Monthly calibration
    mu_monthly = expected_returns / 12.0
    cov_monthly = sub_cov / 12.0
    
    # Cholesky decomposition of monthly covariance matrix
    # Add minor ridge if Cholesky fails due to precision
    try:
        L = np.linalg.cholesky(cov_monthly)
    except np.linalg.LinAlgError:
        print("Warning: Cholesky failed. Adding small diagonal ridge (1e-12)...")
        cov_monthly += 1e-12 * np.eye(n_assets)
        L = np.linalg.cholesky(cov_monthly)
        
    # Simulation parameters
    fund_size = portfolio["total_fund_value"]
    
    # Initialize arrays
    # paths shape: (n_paths, n_months + 1)
    paths = np.zeros((n_paths, n_months + 1))
    paths[:, 0] = fund_size
    
    # returns shape: (n_paths, n_months)
    returns = np.zeros((n_paths, n_months))
    
    # Run simulation month-by-month
    for t in range(1, n_months + 1):
        # Generate independent standard normal shocks: shape (n_assets, n_paths)
        z = np.random.normal(0.0, 1.0, size=(n_assets, n_paths))
        # Correlate shocks: shape (n_assets, n_paths)
        shocks = L @ z
        
        # Monthly returns for each asset on each path: shape (n_assets, n_paths)
        asset_returns = mu_monthly[:, np.newaxis] + shocks
        
        # Portfolio return for each path: shape (n_paths,)
        port_returns = weights @ asset_returns
        
        # Record monthly portfolio returns
        returns[:, t - 1] = port_returns
        
        # Update portfolio value
        paths[:, t] = paths[:, t - 1] * (1.0 + port_returns)
        
    return paths, returns

def run_simulation_engine():
    np.random.seed(42)  # Set seed for reproducibility
    
    port_A, port_B, df_cov = load_portfolios_and_cov()
    
    print("Running Monte Carlo simulation for Portfolio A (Heuristic-Driven)...")
    paths_A, returns_A = simulate_gbm(port_A, df_cov)
    
    print("Running Monte Carlo simulation for Portfolio B (MVO-Optimized)...")
    paths_B, returns_B = simulate_gbm(port_B, df_cov)
    
    # Export paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    out_dir = os.path.join(project_root, "outputs", "simulation_results")
    os.makedirs(out_dir, exist_ok=True)
    
    # Save first 100 paths for visualization
    paths_A_100 = paths_A[:100, :]
    paths_B_100 = paths_B[:100, :]
    
    out_path_A = os.path.join(out_dir, "portfolio_A_paths.npy")
    out_path_B = os.path.join(out_dir, "portfolio_B_paths.npy")
    np.save(out_path_A, paths_A_100)
    np.save(out_path_B, paths_B_100)
    print(f"Saved first 100 paths to {out_path_A} and {out_path_B}")
    
    # Save full 10,000 paths and returns for statistical analysis
    np.save(os.path.join(out_dir, "portfolio_A_paths_all.npy"), paths_A)
    np.save(os.path.join(out_dir, "portfolio_B_paths_all.npy"), paths_B)
    np.save(os.path.join(out_dir, "portfolio_A_returns_all.npy"), returns_A)
    np.save(os.path.join(out_dir, "portfolio_B_returns_all.npy"), returns_B)
    print("Saved all 10,000 paths and returns for analysis.")

if __name__ == "__main__":
    run_simulation_engine()
