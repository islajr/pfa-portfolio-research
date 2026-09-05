# packages/optimizer/covariance.py
"""
Generates the 80x80 property-level covariance matrix from index returns and property attributes.
"""

import os
import pandas as pd
import numpy as np
from sklearn.covariance import LedoitWolf

# Pre-registered premium constants
TITLE_RISK_PREMIUMS = {
    "C of O": 0.000,
    "Gov Consent": 0.005,
    "Gazette": 0.030,
    "Excision": 0.050,
    "Deed of Assignment": 0.020
}

CONDITION_RISK_PREMIUMS = {
    "New": 0.000,
    "Good": 0.005,
    "Fair": 0.015,
    "Needs Renovation": 0.030
}

def generate_property_covariance():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    universe_path = os.path.join(project_root, "data", "frozen", "property_universe.csv")
    returns_path = os.path.join(project_root, "data", "frozen", "market_indices_returns.csv")
    out_path = os.path.join(project_root, "data", "frozen", "property_covariance_matrix.csv")
    
    if not os.path.exists(universe_path) or not os.path.exists(returns_path):
        raise FileNotFoundError("Frozen universe or market returns file not found. Ensure Phase 2 is complete.")
        
    df_universe = pd.read_csv(universe_path)
    df_returns = pd.read_csv(returns_path)
    
    # 1. Compute 8x8 index covariance matrix
    # Drop 'year' column to only compute index return covariances
    index_returns = df_returns.drop(columns=["year"])
    index_cov = index_returns.cov()
    
    # 2. Construct 80x80 property covariance matrix
    n = len(df_universe)
    cov_matrix = np.zeros((n, n))
    
    for i in range(n):
        idx_i = df_universe.loc[i, "market_index_id"]
        title_i = df_universe.loc[i, "title_status"]
        cond_i = df_universe.loc[i, "property_condition"]
        
        # Premiums
        title_prem_i = TITLE_RISK_PREMIUMS.get(title_i, 0.0)
        cond_prem_i = CONDITION_RISK_PREMIUMS.get(cond_i, 0.0)
        
        for j in range(n):
            idx_j = df_universe.loc[j, "market_index_id"]
            
            if i == j:
                # Diagonal (i = j): index_variance + title_premium^2 + condition_premium^2
                index_variance = index_cov.loc[idx_i, idx_i]
                cov_matrix[i, j] = index_variance + (title_prem_i ** 2) + (cond_prem_i ** 2)
            else:
                # Off-diagonal (i != j): index_covariance[index_i, index_j]
                cov_matrix[i, j] = index_cov.loc[idx_i, idx_j]
                
    # 3. Check positive semi-definiteness (PSD)
    eigenvals = np.linalg.eigvals(cov_matrix)
    min_eig = np.min(np.real(eigenvals))
    print(f"Minimum eigenvalue of raw property covariance matrix: {min_eig:.6e}")
    
    if min_eig < -1e-10:
        print("Warning: Property covariance matrix is not PSD. Applying Ledoit-Wolf shrinkage...")
        # To apply Ledoit-Wolf shrinkage to a covariance matrix structure, we can generate a large sample
        # from the multivariate normal distribution with the raw covariance and apply the Ledoit-Wolf estimator.
        np.random.seed(SEED := 42)
        mean = np.zeros(n)
        # Generate 1000 samples
        samples = np.random.multivariate_normal(mean, cov_matrix, size=1000)
        lw = LedoitWolf().fit(samples)
        cov_matrix = lw.covariance_
        
        # Re-check eigenvalues
        new_eigenvals = np.linalg.eigvals(cov_matrix)
        new_min_eig = np.min(np.real(new_eigenvals))
        print(f"Minimum eigenvalue after Ledoit-Wolf shrinkage: {new_min_eig:.6e}")
        if new_min_eig < -1e-10:
            print("Warning: Shrunk matrix is still not PSD. Adding small diagonal ridge (1e-6)...")
            cov_matrix += 1e-6 * np.eye(n)
            
    # 4. Save to CSV with property IDs as row/column headers
    property_ids = df_universe["property_id"].tolist()
    df_cov = pd.DataFrame(cov_matrix, index=property_ids, columns=property_ids)
    df_cov.to_csv(out_path)
    print(f"Property covariance matrix saved to {out_path}")
    return df_cov

if __name__ == "__main__":
    generate_property_covariance()
