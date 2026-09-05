# packages/optimizer/mvo_optimizer.py
"""
MVO Optimizer (Portfolio B).

RECALIBRATION (v2):
- Fund AUM updated to ₦2 trillion (median from Q1 2026 field survey).
- Real estate budget set to 10% = ₦200 billion (PenCom regulatory ceiling).
- Per-property cap set to ₦3 billion (universe ceiling), replacing the former
  ₦500M cap which was based on 5% of a ₦10B fund.
- BIP subset range updated to 10–20 properties to target the modal bracket
  observed in survey data (11–25 properties).
- Budget constraint updated to enforce sum(TAC) <= ₦200B (the real estate budget),
  ensuring the optimized portfolio is PenCom-compliant.

Selects a subset of properties from the synthetic universe to maximize the Sharpe ratio
subject to PenCom regulatory and cardinality constraints (Formulas 3.7–3.9).
"""

import os
import json
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Representative fund AUM from survey median (Q1 2026 field data)
FUND_SIZE = 2_000_000_000_000.0             # ₦2 trillion

# PenCom 10% direct real estate cap
REAL_ESTATE_BUDGET = FUND_SIZE * 0.10       # ₦200 billion

# Per-property cap: universe ceiling (Trophy tier max = ₦3B)
MAX_SINGLE_PROPERTY = 3_000_000_000.0       # ₦3 billion


def load_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    universe_path = os.path.join(project_root, "data", "frozen", "property_universe.csv")
    cov_path = os.path.join(project_root, "data", "frozen", "property_covariance_matrix.csv")
    
    if not os.path.exists(universe_path) or not os.path.exists(cov_path):
        raise FileNotFoundError("Frozen universe or covariance matrix not found. Run previous phases first.")
        
    df_universe = pd.read_csv(universe_path)
    df_cov = pd.read_csv(cov_path, index_col=0)
    return df_universe, df_cov


def run_continuous_slsqp(eligible_df, cov_df, rf=0.084):
    """
    Runs a continuous SLSQP optimization on the eligible property set.
    Used for reference (as a benchmark lower bound) and logging.
    """
    m = len(eligible_df)
    mu = eligible_df['expected_return'].values
    property_ids = eligible_df['property_id'].tolist()
    sigma = cov_df.loc[property_ids, property_ids].values
    
    def neg_sharpe(w):
        port_ret = np.sum(w * mu)
        port_vol = np.sqrt(w.T @ sigma @ w)
        if port_vol == 0:
            return 0.0
        return -(port_ret - rf) / port_vol

    cons = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0})
    bounds = [(0, 1) for _ in range(m)]
    
    res = minimize(neg_sharpe, [1.0/m]*m, bounds=bounds, constraints=cons, method='SLSQP')
    return res


def run_bip_local_search(eligible_df, cov_df, rf=0.084, target_k=15, n_restarts=2000):
    """
    Cardinality-constrained portfolio optimisation via greedy initialisation
    followed by random-restart local search (swap moves).

    Replaces exact BIP enumeration, which is computationally intractable for
    large eligible sets (C(60,15) > 10^12 combinations). This approach produces
    near-optimal solutions and is standard in the real estate portfolio literature
    for discrete, indivisible asset selection problems.

    Constraints:
      - target_k properties selected (default 15, to match surveyed modal bracket)
      - >= 2 states represented (PenCom geographic diversification)
      - sum(TAC) <= REAL_ESTATE_BUDGET (PenCom 10% cap)
      - Each TAC <= MAX_SINGLE_PROPERTY (universe ceiling)

    Objective: maximise equal-weighted Sharpe ratio.
    """
    m = len(eligible_df)
    ids = eligible_df['property_id'].tolist()
    mu = eligible_df['expected_return'].values
    tac = eligible_df['total_acquisition_cost'].values
    states = eligible_df['location_state'].values
    sigma = cov_df.loc[ids, ids].values
    
    def sharpe(indices):
        k = len(indices)
        w = np.ones(k) / k
        sub_mu = mu[list(indices)]
        sub_sig = sigma[np.ix_(list(indices), list(indices))]
        p_ret = np.dot(w, sub_mu)
        p_vol = np.sqrt(w.T @ sub_sig @ w)
        if p_vol < 1e-12:
            return -np.inf
        return (p_ret - rf) / p_vol
    
    def is_feasible(indices):
        idx_list = list(indices)
        if tac[idx_list].sum() > REAL_ESTATE_BUDGET:
            return False
        if len(set(states[i] for i in idx_list)) < 2:
            return False
        return True
    
    # --- Greedy initialisation: pick top-target_k by expected return ---
    sorted_by_ret = np.argsort(-mu)  # descending
    seed = []
    for i in sorted_by_ret:
        if len(seed) >= target_k:
            break
        candidate = seed + [i]
        if tac[candidate].sum() <= REAL_ESTATE_BUDGET:
            seed.append(i)
    
    # Ensure seed is feasible by budget and at least 1 property
    if len(seed) == 0:
        raise ValueError("Greedy seed empty — all properties violate budget constraint.")
    
    best_indices = set(seed)
    best_sr = sharpe(best_indices) if is_feasible(best_indices) else -np.inf
    
    print(f"Greedy seed: {len(seed)} properties, Sharpe = {best_sr:.4f}")
    print(f"Running {n_restarts} random-restart swap moves...")
    
    np.random.seed(42)
    all_idx = set(range(m))
    
    for restart in range(n_restarts):
        # Start from best or a random perturbation every 100 restarts
        if restart % 100 == 0 and restart > 0:
            # Random restart: shuffle and re-seed
            rand_subset = list(np.random.choice(m, target_k, replace=False))
            current = set(rand_subset)
        else:
            current = set(best_indices)
        
        # Perform a random swap: remove one property, add one not in set
        if len(current) == 0:
            continue
        out_idx = int(np.random.choice(list(current)))
        candidate_in = list(all_idx - current)
        if not candidate_in:
            continue
        in_idx = int(np.random.choice(candidate_in))
        
        new_subset = (current - {out_idx}) | {in_idx}
        
        # Enforce target_k cardinality (allow ±1 for exploration)
        if len(new_subset) < 10 or len(new_subset) > 20:
            continue
        
        if not is_feasible(new_subset):
            continue
        
        sr = sharpe(new_subset)
        if sr > best_sr:
            best_sr = sr
            best_indices = new_subset
    
    best_idx_list = sorted(list(best_indices))
    best_subset = eligible_df.iloc[best_idx_list]
    k = len(best_idx_list)
    w = np.ones(k) / k
    port_ret = np.dot(w, mu[best_idx_list])
    port_vol = np.sqrt(w.T @ sigma[np.ix_(best_idx_list, best_idx_list)] @ w)
    
    print(f"Local search complete. Final Sharpe = {best_sr:.6f}, N = {k} properties.")
    return best_subset, best_sr, port_ret, port_vol


def construct_optimized_portfolio():
    df_universe, df_cov = load_data()
    
    # ─────────────────────────────────────────────────────────
    # Apply MVO Eligibility Filters
    # The MVO optimizer observes all PenCom regulatory constraints
    # but does NOT apply heuristic-driven filters.
    # ─────────────────────────────────────────────────────────
    
    # F1: PenCom lease compliance (commercial >= 7 years)
    eligible_df = df_universe[df_universe['pencom_lease_compliant'] == True].copy()
    
    # F2: Per-property size cap (universe ceiling ₦3B; practical PenCom single-asset limit)
    eligible_df = eligible_df[eligible_df['total_acquisition_cost'] <= MAX_SINGLE_PROPERTY]
    eligible_df = eligible_df.reset_index(drop=True)
    
    print(f"\n--- Portfolio B (MVO) Construction ---")
    print(f"Properties passing MVO eligibility filters: {len(eligible_df)} / {len(df_universe)}")
    print(f"Real estate budget: ₦{REAL_ESTATE_BUDGET/1e9:,.1f} billion (10% of ₦{FUND_SIZE/1e12:.0f}T AUM)")
    
    # Run continuous SLSQP for reference
    slsqp_res = run_continuous_slsqp(eligible_df, df_cov)
    print(f"Continuous SLSQP successful: {slsqp_res.success} | Obj (neg Sharpe): {slsqp_res.fun:.4f}")
    
    # Solve cardinality-constrained portfolio problem via greedy + local search
    best_subset_df, best_sharpe, port_ret, port_vol = run_bip_local_search(eligible_df, df_cov)
    
    if best_subset_df is None:
        raise ValueError("No feasible portfolio found satisfying PenCom and cardinality constraints.")
        
    n_selected = len(best_subset_df)
    total_allocated = best_subset_df['total_acquisition_cost'].sum()
    
    print(f"Local search selected {n_selected} properties.")
    print(f"Optimal Sharpe ratio: {best_sharpe:.6f}")
    print(f"Total allocated: ₦{total_allocated/1e9:,.2f} billion")
    
    # Form holdings list with equal weighting
    w_i = 1.0 / n_selected
    portfolio_holdings = []
    
    for idx, row in best_subset_df.iterrows():
        portfolio_holdings.append({
            "property_id": row["property_id"],
            "property_code": row["property_code"],
            "location_state": row["location_state"],
            "location_micro": row["location_micro"],
            "asset_type": row["asset_type"],
            "total_acquisition_cost": row["total_acquisition_cost"],
            "expected_return": row["expected_return"],
            "total_volatility": row["total_volatility"],
            "weight": w_i
        })
        
    # Output Portfolio B
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    out_dir = os.path.join(project_root, "outputs", "portfolios")
    os.makedirs(out_dir, exist_ok=True)
    
    portfolio_B = {
        "portfolio_name": "Portfolio B — MVO-Optimized",
        "strategy_type": "MVO",
        "total_fund_value": FUND_SIZE,
        "real_estate_budget": REAL_ESTATE_BUDGET,
        "n_properties": n_selected,
        "expected_return": round(port_ret, 6),
        "total_allocated": round(float(total_allocated), 2),
        "holdings": portfolio_holdings
    }
    
    out_path = os.path.join(out_dir, "portfolio_B_optimized.json")
    with open(out_path, "w") as f:
        json.dump(portfolio_B, f, indent=2)
        
    print(f"Portfolio B saved to {out_path}")
    return portfolio_B

if __name__ == "__main__":
    construct_optimized_portfolio()
