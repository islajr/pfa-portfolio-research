# packages/optimizer/heuristic_engine.py
"""
Heuristic selection engine (Portfolio A).

REDESIGN (v2 — field-data recalibration):
- Removes the previous hard exclusion filters for title status, geographic location,
  and property condition. These filters were contradicted by the 16 real field responses:
  B3 and B2 both showed substantially split opinions (not the near-unanimous agreement
  that would justify hard exclusion). The field data shows heuristics as strongly
  influential SCORING biases, not as absolute gatekeepers.

- Replaces hard filters with graded scoring penalties calibrated from real field data.
- Updates fund_size to ₦2 trillion (median survey AUM) with a 10% PenCom-compliant
  real estate budget of ₦200 billion.
- Targets a portfolio of ~15 properties to match the surveyed institutional norm
  (11–25 properties, modal bracket).

Only F1 (PenCom commercial lease compliance) is retained as a hard filter — it is a
regulatory requirement, not a heuristic.
"""

import os
import json
import numpy as np
import pandas as pd

# Representative fund AUM from survey median (Q1 2026 field data)
# 9 of 16 real respondents reported AUM "Above ₦2 trillion"
FUND_SIZE = 2_000_000_000_000.0             # ₦2 trillion (representative median fund)

# PenCom 10% direct real estate cap (PenCom Regulation on Investment of Pension Fund Assets, 2024)
REAL_ESTATE_BUDGET = FUND_SIZE * 0.10       # ₦200 billion maximum deployment

# Practical per-property cap: the property universe ceiling is ₦3 billion (Trophy tier).
# PenCom's 5% single-property rule on ₦2T = ₦100B (far above any individual property cost).
# We cap at the universe ceiling: ₦3 billion.
MAX_SINGLE_PROPERTY = 3_000_000_000.0       # ₦3 billion (universe upper bound)

# Target property count: modal bracket from survey = 11–25; representative target = 15
TARGET_N_PROPERTIES = 15


def load_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    universe_path = os.path.join(project_root, "data", "frozen", "property_universe.csv")
    returns_path = os.path.join(project_root, "data", "frozen", "market_indices_returns.csv")
    
    if not os.path.exists(universe_path) or not os.path.exists(returns_path):
        raise FileNotFoundError("Frozen universe or return data not found. Run Phase 2 pipeline first.")
        
    df_universe = pd.read_csv(universe_path)
    df_returns = pd.read_csv(returns_path)
    return df_universe, df_returns


def calculate_momentum_scores(df_returns):
    """
    Computes normalized momentum scores (MS) over the last 3 years (2022–2024).
    Recent return momentum is used as a representativeness heuristic proxy.
    """
    recent_returns = df_returns[df_returns['year'].isin([2022, 2023, 2024])]
    avg_returns = recent_returns.mean().drop('year')
    
    min_ret = avg_returns.min()
    max_ret = avg_returns.max()
    
    if max_ret == min_ret:
        normalized_returns = {code: 1.0 for code in avg_returns.index}
    else:
        normalized_returns = ((avg_returns - min_ret) / (max_ret - min_ret)).to_dict()
        
    return normalized_returns


def title_score(title_status):
    """
    Graded title score (TS) — replaces the previous binary hard filter.

    Calibration note: B3 responses from 16 real respondents showed substantial
    disagreement (8 agree vs 6 disagree). This supports a graded penalty rather
    than absolute exclusion. C of O remains the gold standard; non-CoO properties
    are penalized but not categorically excluded by the heuristic.
    """
    scores = {
        "C of O":          1.00,
        "Gov Consent":     0.65,
        "Gazette":         0.30,
        "Deed of Assignment": 0.15,
        "Excision":        0.00,
    }
    return scores.get(title_status, 0.20)


def location_score(location_state, is_prime):
    """
    Graded location score (LS) — replaces the previous hard geographic exclusion.

    Calibration note: B2 responses from 16 real respondents showed a near-equal
    split (6 agree vs 7 disagree). C2 scenario also showed moderate (not extreme)
    location preference. This supports a penalty — not exclusion — for non-prime
    locations. Kano and Oyo are penalised but accessible to the heuristic portfolio,
    reflecting real investment practice.
    """
    if is_prime:
        return 1.00   # Lagos Island, Maitama/Asokoro (Abuja prime)
    elif location_state in ["Lagos", "Abuja"]:
        return 0.70   # Lagos Mainland, secondary Abuja (e.g. Garki, Jabi)
    elif location_state == "Rivers":
        return 0.55   # Port Harcourt — established but not prime
    elif location_state == "Oyo":
        return 0.35   # Ibadan — emerging; penalised but reachable
    else:
        return 0.25   # Kano — most emerging; heavy penalty


def condition_score(property_condition):
    """
    Graded condition score (CS) — new sub-component.

    Properties in Fair or Needs Renovation condition carry lower NOI and higher
    holding costs. This is a genuine heuristic-consistent preference (investors
    prefer move-in-ready assets) but need not be an absolute exclusion.
    """
    scores = {
        "New":              1.00,
        "Good":             0.80,
        "Fair":             0.45,
        "Needs Renovation": 0.15,
    }
    return scores.get(property_condition, 0.50)


def construct_heuristic_portfolio():
    df_universe, df_returns = load_data()
    
    # ─────────────────────────────────────────────────────────
    # Stage 1 — Regulatory Hard Filter (ONLY)
    # F1: PenCom commercial lease term compliance (>= 7 years)
    # This is a statutory requirement, not a heuristic — retained.
    # ─────────────────────────────────────────────────────────
    filtered_df = df_universe[df_universe['pencom_lease_compliant'] == True].copy()
    
    print(f"Properties passing regulatory lease filter (F1): {len(filtered_df)} / {len(df_universe)}")
    
    # ─────────────────────────────────────────────────────────
    # Stage 2 — Composite Heuristic Scoring
    # Applies graded scores for title, location, momentum, condition, and peer.
    # Hard filters for title, location, and condition have been removed
    # and replaced with scoring penalties reflecting real field data.
    # ─────────────────────────────────────────────────────────
    momentum_scores = calculate_momentum_scores(df_returns)
    
    # Load empirically-derived alpha weights from clean_analyze_responses output
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    weights_path = os.path.join(project_root, "data", "questionnaire", "alpha_weights.json")
    if os.path.exists(weights_path):
        with open(weights_path, "r") as f:
            weights_data = json.load(f)
            alpha = weights_data.get("survey_derived", [0.30, 0.30, 0.20, 0.20])
        print(f"Loaded survey-derived alpha weights: {alpha}")
    else:
        # Fallback placeholder (will be overwritten after analyze_questionnaire runs)
        alpha = [0.30, 0.30, 0.20, 0.20]
        print(f"Alpha weights JSON not found. Using interim fallback: {alpha}")
    
    scores_list = []
    for idx, row in filtered_df.iterrows():
        ts = title_score(row['title_status'])
        ls = location_score(row['location_state'], row.get('is_prime_location', False))
        ms = momentum_scores.get(row['market_index_id'], 0.5)
        cs = condition_score(row['property_condition'])

        # Peer Score (PS): prime submarkets where peer PFAs cluster
        ps = 1.0 if row['market_index_id'] in ["LG_OFF_ISL", "LG_RES_PRM"] else 0.0
        
        # Composite Heuristic Score:
        # alpha[0] = Title (H1/ACS), alpha[1] = Location (H2/AVCS),
        # alpha[2] = Momentum (H3/RCS), alpha[3] = Peer (H4/HCS)
        # Condition score is blended into the title dimension as a quality signal.
        composite = (
            alpha[0] * (0.65 * ts + 0.35 * cs) +   # Title + Condition blend
            alpha[1] * ls +                           # Location
            alpha[2] * ms +                           # Momentum
            alpha[3] * ps                             # Peer
        )
        scores_list.append(composite)
        
    filtered_df = filtered_df.copy()
    filtered_df['heuristic_score'] = scores_list
    filtered_df = filtered_df.sort_values(by='heuristic_score', ascending=False).reset_index(drop=True)
    
    # ─────────────────────────────────────────────────────────
    # Stage 3 — Greedy Budget Allocation
    # Budget = ₦200 billion (10% of ₦2T median fund AUM, per PenCom cap).
    # Per-property cap = ₦3 billion (universe ceiling).
    # Target: ~15 properties (modal bracket from survey: 11–25).
    # ─────────────────────────────────────────────────────────
    remaining_budget = REAL_ESTATE_BUDGET
    selected_properties = []
    
    for idx, row in filtered_df.iterrows():
        tac = row['total_acquisition_cost']
        if tac <= remaining_budget and tac <= MAX_SINGLE_PROPERTY:
            selected_properties.append(row.to_dict())
            remaining_budget -= tac
            if len(selected_properties) >= TARGET_N_PROPERTIES:
                # Once we hit the target count, stop greedy allocation
                break
            
    n_selected = len(selected_properties)
    total_allocated = REAL_ESTATE_BUDGET - remaining_budget
    
    print(f"\n--- Portfolio A Construction ---")
    print(f"Properties selected: {n_selected} (target: {TARGET_N_PROPERTIES})")
    print(f"Total real estate budget: ₦{REAL_ESTATE_BUDGET/1e9:,.1f} billion (10% of ₦{FUND_SIZE/1e12:.0f}T AUM)")
    print(f"Total allocated: ₦{total_allocated/1e9:,.2f} billion")
    print(f"Remaining undeployed budget: ₦{remaining_budget/1e9:,.2f} billion")
    
    w_i = 1.0 / n_selected if n_selected > 0 else 0.0
    
    portfolio_holdings = []
    for prop in selected_properties:
        portfolio_holdings.append({
            "property_id": prop["property_id"],
            "property_code": prop["property_code"],
            "location_state": prop["location_state"],
            "location_micro": prop["location_micro"],
            "asset_type": prop["asset_type"],
            "total_acquisition_cost": prop["total_acquisition_cost"],
            "expected_return": prop["expected_return"],
            "total_volatility": prop["total_volatility"],
            "heuristic_score": round(prop["heuristic_score"], 6),
            "weight": w_i
        })
        
    portfolio_return = sum(h["expected_return"] * h["weight"] for h in portfolio_holdings)
    
    # Save output
    out_dir = os.path.join(project_root, "outputs", "portfolios")
    os.makedirs(out_dir, exist_ok=True)
    
    portfolio_A = {
        "portfolio_name": "Portfolio A — Heuristic-Driven",
        "strategy_type": "HEURISTIC",
        "total_fund_value": FUND_SIZE,
        "real_estate_budget": REAL_ESTATE_BUDGET,
        "n_properties": n_selected,
        "expected_return": round(portfolio_return, 6),
        "total_allocated": round(total_allocated, 2),
        "holdings": portfolio_holdings
    }
    
    out_path = os.path.join(out_dir, "portfolio_A_heuristic.json")
    with open(out_path, "w") as f:
        json.dump(portfolio_A, f, indent=2)
        
    print(f"Portfolio A saved to {out_path}")
    return portfolio_A

if __name__ == "__main__":
    construct_heuristic_portfolio()
