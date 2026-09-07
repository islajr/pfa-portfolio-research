# packages/optimizer/clean_analyze_responses.py
"""
Phase 3: Questionnaire response data cleaning, composite score calculations,
bootstrap confidence intervals, descriptive Section D analysis, and alpha weights export.

Two-tier analytical design:
  - TIER 1 (N=24, full census): All descriptive, stated-preference and institutional
    sections. A5=C respondents are included because their responses on criteria ranks,
    Likert items, and institutional constraints accurately reflect organisational
    practice, regardless of their personal decision authority.
  - TIER 2 (n=7, decision-makers only): Composite heuristic score computation and
    alpha weight calibration. Only A5=A and A5=B respondents contribute here, since
    the heuristic weights must reflect the preferences of those who actually make or
    analytically inform property selection decisions.

This structure is explicitly documented in Chapter 3 Section 3.3.1 and Section 4.2.
"""

import os
import shutil
import json
import numpy as np
import pandas as pd
from scipy.stats import norm

# Mapped columns shortcodes
COLUMN_MAPPING = {
    "Timestamp": "Timestamp",
    "What is your current job title?": "A1",
    "How many years of experience do you have in real estate or institutional invesment management?": "A2",
    "Which of the following best describes your fund's approximate total Assets Under Management (AUM)?": "A3",
    "Approximately how many direct real estate properties does your fund currently hold in its portfolio?": "A4",
    "Do you directly participate in property selection decisions?": "A5",
    "Does your fund use a formal quantitative model to assist with property selection decisions?": "A6",
    "Please rank the following criteria (1-8) in order of their importance in your fund's property selection process.\n\nNOTE: No number may be selected twice. [Location Prestige]": "B1_loc",
    "Please rank the following criteria (1-8) in order of their importance in your fund's property selection process.\n\nNOTE: No number may be selected twice. [Title documentation status (e.g.: C of O, Governor's Consent)]": "B1_title",
    "Please rank the following criteria (1-8) in order of their importance in your fund's property selection process.\n\nNOTE: No number may be selected twice. [Rental yield / Income Return]": "B1_yield",
    "Please rank the following criteria (1-8) in order of their importance in your fund's property selection process.\n\nNOTE: No number may be selected twice. [Tenant Profile and Lease Security]": "B1_tenant",
    "Please rank the following criteria (1-8) in order of their importance in your fund's property selection process.\n\nNOTE: No number may be selected twice. [Property Physical Condition]": "B1_cond",
    "Please rank the following criteria (1-8) in order of their importance in your fund's property selection process.\n\nNOTE: No number may be selected twice. [Activity of peer PFAs in the same submarket]": "B1_peer",
    "Please rank the following criteria (1-8) in order of their importance in your fund's property selection process.\n\nNOTE: No number may be selected twice. [Estate Surveyor's Recommendation]": "B1_valuer",
    "Please rank the following criteria (1-8) in order of their importance in your fund's property selection process.\n\nNOTE: No number may be selected twice. [Market Liquidity / Ease of future sale]": "B1_liq",
    "A property in Ikoyi, Victoria Island, or Maitama carries lower investment risk than an equally-priced property in a less prominent location, regardless of its specific financial characteristics.": "B2",
    "When a property lacks a Certificate of Occupancy or Governor's Consent, we would not recommend it regardless of how attractive its yield might be.": "B3",
    "Our fund's property selections over the past three years have been broadly similar in location and type to those of other PFAs we are aware of.": "B4",
    "Your fund is evaluating a Grade A office building. An independent valuation conducted four months ago placed the market value at ₦900 million. The property is currently valued at ₦730 million due to softer market conditions. The current asking price is ₦740 million.\n": "C1",
    "Your analysis identifies two commercial properties with equal returns: similar cap rates, comparable title status, similar tenant profiles, and the same building specification.\n \nProperty A is located in the Victoria Island business district.\nProperty B is located in a similar business area in Ibadan.\n": "C2",
    "A specific sector — Grade A office in Abuja — has delivered capital appreciation of 18% in each of the past two years, which is significantly above the market average of 9%.\n": "C3",
    "You become aware that three of the five largest PFAs by AUM have recently acquired Grade A office properties in a specific area in Abuja. The returns on these purchases appear to be slightly below your fund's target return bracket.\n": "C4",
    "Which of the following best describes how property selection decisions are typically made at your fund?": "D1",
    "Approximately how many formal approval stages does a property acquisition typically pass through, from initial identification to final sign-off?": "D1b",
    "To what extent does data unavailability limit your fund's ability to conduct formal quantitative analysis of real estate investment opportunities?": "D2",
    "Which of the following data gaps most constrain your investment analysis": "D2b",
    "Which single change would most improve your fund's property selection decision-making?": "D3",
    "Which of the following institutional or contextual factors most influence the extent to which your fund relies on judgment and experience rather than formal quantitative analysis in property selection? ": "D4",
    "If a software tool were available, purposely-built for institutional real estate investment and assists with the entire process of property invesment under PenCom guidelines, how likely is your fund to adopt such a tool?": "D4a",
    "Which of the following conditions would increase your fund's likelihood of adopting such a tool?": "D4b",
    "At what approximate price level would your fund begin to view such a tool as financially impractical, regardless of its benefits?": "D4c"
}

D4_CATEGORIES = {
    "Time pressure (acquisition decisions must be made faster than analysis allows)": "COG",
    "Lack of in-house quantitative or modelling expertise": "COG",
    "Absence of reliable market data to support a quantitative approach": "INF",
    "High deal complexity that resists standardised modelling": "INF",
    "Peer PFA behaviour providing a practical benchmark in the absence of data": "INS",
    "Established organisational precedent (prior acquisitions set the template)": "INS",
    "Investment committee preference for experienced judgment over model outputs": "INS",
    "Regulatory uncertainty that makes long-term projections unreliable": "REG"
}

LIKERT_MAP = {
    "Strongly Agree": 5,
    "Agree": 4,
    "Neutral": 3,
    "Disagree": 2,
    "Strongly Disagree": 1
}


def load_full_census():
    """
    Loads and renames the raw CSV. Returns the full N=24 census dataframe
    (Tier 1) with only structural exclusions applied (blank scenario columns,
    invalid rank permutations). A5=C respondents are RETAINED in this dataframe.
    """
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    src_csv = os.path.join(project_root, "PFA Questionnaire Survey.csv")
    dest_dir = os.path.join(project_root, "data", "questionnaire")
    os.makedirs(dest_dir, exist_ok=True)

    dest_raw_csv = os.path.join(dest_dir, "raw_responses.csv")
    shutil.copy(src_csv, dest_raw_csv)
    print(f"Copied raw survey responses to {dest_raw_csv}")

    df = pd.read_csv(dest_raw_csv)
    df = df.rename(columns=COLUMN_MAPPING)

    # Strip whitespace from string columns
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].str.strip()

    N_raw = len(df)
    structural_exclusions = []

    # Structural check 1: blank scenario columns (C1–C4)
    for scenario_col in ["C1", "C2", "C3", "C4"]:
        blank_mask = df[scenario_col].isna()
        for idx in df[blank_mask].index:
            structural_exclusions.append({
                "row_idx": idx,
                "a5": str(df.loc[idx, "A5"]),
                "reason": f"Structural exclusion: Blank response in scenario {scenario_col}"
            })

    # Structural check 2: invalid B1 rank permutations
    rank_cols = ["B1_loc", "B1_title", "B1_yield", "B1_tenant",
                 "B1_cond", "B1_peer", "B1_valuer", "B1_liq"]
    for idx, row in df.iterrows():
        try:
            row_ranks = [int(row[col]) for col in rank_cols]
            if sorted(row_ranks) != list(range(1, 9)):
                structural_exclusions.append({
                    "row_idx": idx,
                    "a5": str(row["A5"]),
                    "reason": "Structural exclusion: Invalid rank permutation"
                })
        except (ValueError, TypeError):
            structural_exclusions.append({
                "row_idx": idx,
                "a5": str(row["A5"]),
                "reason": "Structural exclusion: Non-integer rank values"
            })

    structural_indices = list({e["row_idx"] for e in structural_exclusions})
    df_full = df.drop(index=structural_indices).reset_index(drop=True)

    N_full = len(df_full)
    n_a5_c = df_full["A5"].str.contains("No — I do not directly participate", na=False).sum()
    n_decision_makers = N_full - n_a5_c

    print(f"\nTier 1 (Census Descriptive Sample): N = {N_full}")
    print(f"  Of which A5=C (non-decision-makers): {n_a5_c} ({100*n_a5_c/N_full:.1f}%)")
    print(f"  Of which A5=A/B (decision-makers):   {n_decision_makers} ({100*n_decision_makers/N_full:.1f}%)")

    return df_full, project_root, dest_dir, structural_exclusions, n_a5_c


def build_decision_maker_subsample(df_full):
    """
    Applies the Tier 2 exclusion: removes A5=C respondents and assigns
    composite weights to the remaining n=7 decision-maker sub-sample.
    """
    a5_c_mask = df_full["A5"].str.contains("No — I do not directly participate", na=False)

    # Log A5=C exclusions
    a5_exclusions = []
    for idx in df_full[a5_c_mask].index:
        a5_exclusions.append({
            "row_idx": idx,
            "a5": "C",
            "reason": "Tier 2 exclusion: Respondent has no property selection decision authority (A5 = C)"
        })

    df_dm = df_full[~a5_c_mask].copy().reset_index(drop=True)

    # Assign respondent weights within the decision-maker sub-sample
    primary_titles = [
        "Portfolio Manager/Fund Manager",
        "Investment Analyst",
        "Chief Investment Officer (CIO)/Head of Investment",
        "Director of Research, Strategy, or Risk",
        "Executive Director/Director with investment oversight responsibility",
        "Risk and Compliance Manager",
        "Real Estate Asset Manager"
    ]

    weights = []
    for idx, row in df_dm.iterrows():
        job = str(row["A1"]).strip()
        is_primary = any(t in job for t in primary_titles)

        part = str(row["A5"]).strip()
        if "direct decision-making authority" in part or "veto power" in part:
            a5_class = "A"
        else:
            a5_class = "B"

        if is_primary:
            weight = 1.0 if a5_class == "A" else 0.7
        else:
            weight = 0.5 if a5_class == "A" else 0.35

        weights.append(weight)

    df_dm["weight"] = weights
    print(f"\nTier 2 (Decision-Maker Sub-Sample): n = {len(df_dm)}")

    return df_dm, a5_exclusions


def bca_bootstrap_ci(scores, weights, n_replications=10000, confidence_level=0.95):
    """
    Computes BCa (Bias-Corrected and Accelerated) Bootstrap Confidence Intervals.
    Applied only to the Tier 2 decision-maker sub-sample for composite scoring.
    """
    n = len(scores)
    theta_hat = np.sum(scores * weights) / np.sum(weights)

    boot_estimates = []
    for _ in range(n_replications):
        indices = np.random.choice(n, size=n, replace=True)
        sub_scores = scores[indices]
        sub_weights = weights[indices]
        if np.sum(sub_weights) == 0:
            boot_estimates.append(0.0)
        else:
            boot_estimates.append(np.sum(sub_scores * sub_weights) / np.sum(sub_weights))

    boot_estimates = np.array(boot_estimates)

    jack_estimates = []
    for i in range(n):
        sub_indices = [idx for idx in range(n) if idx != i]
        sub_scores = scores[sub_indices]
        sub_weights = weights[sub_indices]
        jack_estimates.append(np.sum(sub_scores * sub_weights) / np.sum(sub_weights))

    jack_estimates = np.array(jack_estimates)
    mean_jack = np.mean(jack_estimates)

    num = np.sum((mean_jack - jack_estimates) ** 3)
    den = 6 * (np.sum((mean_jack - jack_estimates) ** 2) ** 1.5)
    a = num / den if den != 0 else 0.0

    p = np.sum(boot_estimates < theta_hat) / n_replications
    p = np.clip(p, 1e-6, 1 - 1e-6)
    z0 = norm.ppf(p)

    alpha = 1 - confidence_level
    z_alpha_2 = norm.ppf(alpha / 2)
    z_1_alpha_2 = norm.ppf(1 - alpha / 2)

    num_l = z0 + z_alpha_2
    den_l = 1 - a * (z0 + z_alpha_2)
    arg_l = z0 + num_l / den_l if den_l != 0 else z0 + z_alpha_2
    alpha_1 = norm.cdf(arg_l)

    num_u = z0 + z_1_alpha_2
    den_u = 1 - a * (z0 + z_1_alpha_2)
    arg_u = z0 + num_u / den_u if den_u != 0 else z0 + z_1_alpha_2
    alpha_2 = norm.cdf(arg_u)

    sorted_estimates = np.sort(boot_estimates)
    pct_l = np.clip(alpha_1, 0, 1)
    pct_u = np.clip(alpha_2, 0, 1)

    idx_l = int(pct_l * (n_replications - 1))
    idx_u = int(pct_u * (n_replications - 1))

    ci_lower = sorted_estimates[idx_l]
    ci_upper = sorted_estimates[idx_u]

    return ci_lower, ci_upper, np.mean(boot_estimates)


def compute_full_census_descriptives(df_full, tables_dir, dest_dir):
    """
    Tier 1 descriptive analysis using the full N=24 census sample.
    Produces: criteria rank table, B2-B4 Likert summaries, D-section
    institutional constraint table, D4a technology adoption summary.
    All N values in output labels reflect the full census.
    """
    N = len(df_full)
    print(f"\n--- Tier 1 Descriptive Analysis (N={N}) ---")

    # B1 Rank medians and Top-3 proportions
    rank_cols = ["B1_loc", "B1_title", "B1_yield", "B1_tenant",
                 "B1_cond", "B1_peer", "B1_valuer", "B1_liq"]
    ranks_df = df_full[rank_cols].astype(float)
    median_ranks = ranks_df.median()
    top3_pct = (ranks_df <= 3.0).sum() / N

    print("\nB1 Criteria Rank Medians (N={}):".format(N))
    for col in rank_cols:
        print(f"  {col}: median={median_ranks[col]:.1f}, top3%={top3_pct[col]*100:.1f}%")

    # B2, B3, B4 Likert means
    for col in ["B2", "B3", "B4"]:
        vals = df_full[col].map(LIKERT_MAP).dropna()
        agree_pct = 100 * (vals >= 4).mean()
        print(f"  {col}: mean={vals.mean():.2f}, SD={vals.std():.2f}, agree%={agree_pct:.1f}%")

    # D4 institutional factors
    d4_option_counts = {}
    d4_cat_counts = {cat: 0 for cat in set(D4_CATEGORIES.values())}
    for factors_str in df_full["D4"].dropna():
        for opt in [o.strip() for o in factors_str.split(";")]:
            if opt in D4_CATEGORIES:
                d4_option_counts[opt] = d4_option_counts.get(opt, 0) + 1
                d4_cat_counts[D4_CATEGORIES[opt]] += 1

    print("\nD4 Institutional Factors (N={}):".format(N))
    for opt, count in sorted(d4_option_counts.items(), key=lambda x: -x[1]):
        print(f"  {count}/{N} ({100*count/N:.1f}%): {opt[:60]}")

    # D4a technology adoption
    print("\nD4a Technology Adoption (N={}):".format(N))
    print(df_full["D4a"].value_counts().to_string())

    # Stated vs. revealed gap at N=24
    b2_norm = (df_full["B2"].map(LIKERT_MAP).fillna(3).values - 1.0) / 4.0
    b3_norm = (df_full["B3"].map(LIKERT_MAP).fillna(3).values - 1.0) / 4.0
    b4_norm = (df_full["B4"].map(LIKERT_MAP).fillna(3).values - 1.0) / 4.0
    c1_norm = (df_full["C1"].astype(float).values - 1.0) / 4.0
    c2_norm = (df_full["C2"].astype(float).values - 1.0) / 4.0
    c4_norm = (df_full["C4"].astype(float).values - 1.0) / 4.0

    gap_anchoring = float((c1_norm - b3_norm).mean())
    gap_availability = float((c2_norm - b2_norm).mean())
    gap_herding = float((c4_norm - b4_norm).mean())

    print(f"\nStated-Revealed Preference Gaps (N={N}):")
    print(f"  Anchoring (C1 - B3):    {gap_anchoring:+.4f}")
    print(f"  Availability (C2 - B2): {gap_availability:+.4f}")
    print(f"  Herding (C4 - B4):      {gap_herding:+.4f}")

    # Save preference gaps (from full census)
    with open(os.path.join(dest_dir, "preference_gaps.json"), "w") as f:
        json.dump({
            "sample": N,
            "anchoring_gap": gap_anchoring,
            "availability_gap": gap_availability,
            "herding_gap": gap_herding
        }, f, indent=2)

    # --- Save Tier 1 LaTeX tables ---

    # Table: Criteria ranks (N=24)
    criteria_labels = {
        "B1_loc": "Location Prestige",
        "B1_title": "Title Status",
        "B1_yield": "Rental Yield",
        "B1_tenant": "Tenant Profile / Lease Security",
        "B1_cond": "Physical Condition",
        "B1_peer": "Peer Activity",
        "B1_valuer": "Valuer Recommendation",
        "B1_liq": "Market Liquidity"
    }

    # Sort by median rank
    sorted_cols = sorted(rank_cols, key=lambda c: median_ranks[c])
    rows = []
    for col in sorted_cols:
        label = criteria_labels[col]
        rows.append(
            f"{label} & {median_ranks[col]:.1f} & {top3_pct[col]*100:.1f}\\% \\\\"
        )

    criteria_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Property Evaluation Criteria Ranking Summary ($N={N}$, Full Census)}}
\\label{{tab:criteria_ranks}}
\\begin{{tabular}}{{lcc}}
\\hline
\\textbf{{Property Evaluation Criterion}} & \\textbf{{Median Rank (1--8)}} & \\textbf{{Top-3 (\\%)}} \\\\
\\hline
{chr(10).join(rows)}
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    with open(os.path.join(tables_dir, "criteria_ranks_table.tex"), "w") as f:
        f.write(criteria_latex)

    # Table: D4 factors (N=24)
    d4_rows = []
    for opt, count in sorted(d4_option_counts.items(), key=lambda x: -x[1]):
        cat = D4_CATEGORIES[opt]
        pct = 100 * count / N
        label = opt[:55] + ("..." if len(opt) > 55 else "")
        d4_rows.append(f"{label} & {cat} & {count} & {pct:.1f}\\% \\\\")

    d4_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Institutional and Environmental Constraints Driving Heuristic Use ($N={N}$, Full Census)}}
\\label{{tab:institutional_context_factors}}
\\begin{{tabular}}{{lccc}}
\\hline
\\textbf{{Factor / Context Description}} & \\textbf{{Type}} & \\textbf{{Freq.}} & \\textbf{{Proportion}} \\\\
\\hline
{chr(10).join(d4_rows)}
\\hline
\\textbf{{Category Aggregate Selections}} & & & \\\\
Cognitive (COG) & -- & {d4_cat_counts['COG']} & -- \\\\
Informational (INF) & -- & {d4_cat_counts['INF']} & -- \\\\
Institutional (INS) & -- & {d4_cat_counts['INS']} & -- \\\\
Regulatory (REG) & -- & {d4_cat_counts['REG']} & -- \\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    with open(os.path.join(tables_dir, "d4_factors_table.tex"), "w") as f:
        f.write(d4_latex)

    # Respondent profile (N=24)
    title_freq = df_full["A1"].value_counts()
    exp_freq = df_full["A2"].value_counts()
    aum_freq = df_full["A3"].value_counts()
    a5_freq = df_full["A5"].value_counts()
    a6_freq = df_full["A6"].value_counts()

    profile_rows = []
    profile_rows.append("\\multicolumn{3}{l}{\\textbf{Decision Participation (A5)}} \\\\")
    for val, cnt in a5_freq.items():
        label = str(val)[:60]
        profile_rows.append(f"{label} & {cnt} & {100*cnt/N:.1f}\\% \\\\")
    profile_rows.append("\\hline")
    profile_rows.append("\\multicolumn{3}{l}{\\textbf{Current Job Title}} \\\\")
    for val, cnt in title_freq.items():
        profile_rows.append(f"{val} & {cnt} & {100*cnt/N:.1f}\\% \\\\")
    profile_rows.append("\\hline")
    profile_rows.append("\\multicolumn{3}{l}{\\textbf{Years of Experience}} \\\\")
    for val, cnt in exp_freq.items():
        profile_rows.append(f"{val} & {cnt} & {100*cnt/N:.1f}\\% \\\\")
    profile_rows.append("\\hline")
    profile_rows.append("\\multicolumn{3}{l}{\\textbf{Assets Under Management (AUM)}} \\\\")
    for val, cnt in aum_freq.items():
        profile_rows.append(f"{val} & {cnt} & {100*cnt/N:.1f}\\% \\\\")
    profile_rows.append("\\hline")
    profile_rows.append("\\multicolumn{3}{l}{\\textbf{Quantitative Model Use (A6)}} \\\\")
    for val, cnt in a6_freq.items():
        label = str(val)[:55] + ("..." if len(str(val)) > 55 else "")
        profile_rows.append(f"{label} & {cnt} & {100*cnt/N:.1f}\\% \\\\")

    profile_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Full Census Respondent Profile ($N={N}$)}}
\\label{{tab:respondent_profile}}
\\begin{{tabular}}{{lcc}}
\\hline
\\textbf{{Profile Attribute}} & \\textbf{{Frequency}} & \\textbf{{Proportion (\\%)}} \\\\
\\hline
{chr(10).join(profile_rows)}
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    with open(os.path.join(tables_dir, "respondent_profile_table.tex"), "w") as f:
        f.write(profile_latex)

    return {
        "N_census": N,
        "median_ranks": median_ranks.to_dict(),
        "top3_pct": top3_pct.to_dict(),
        "d4_option_counts": d4_option_counts,
        "d4_cat_counts": d4_cat_counts,
        "gap_anchoring": gap_anchoring,
        "gap_availability": gap_availability,
        "gap_herding": gap_herding,
    }


def compute_heuristic_scores(df_dm, tables_dir, dest_dir):
    """
    Tier 2 heuristic composite scoring using only the n=7 decision-maker sub-sample.
    Produces alpha_weights.json and heuristic_scores_table.tex.
    """
    n = len(df_dm)
    print(f"\n--- Tier 2 Heuristic Scoring (n={n} decision-makers) ---")

    # Normalise inputs
    b2_norm = (df_dm["B2"].map(LIKERT_MAP).fillna(3).values - 1.0) / 4.0
    b3_norm = (df_dm["B3"].map(LIKERT_MAP).fillna(3).values - 1.0) / 4.0
    b4_norm = (df_dm["B4"].map(LIKERT_MAP).fillna(3).values - 1.0) / 4.0

    c1_norm = (df_dm["C1"].astype(float).values - 1.0) / 4.0
    c2_norm = (df_dm["C2"].astype(float).values - 1.0) / 4.0
    c3_norm = (df_dm["C3"].astype(float).values - 1.0) / 4.0
    c4_norm = (df_dm["C4"].astype(float).values - 1.0) / 4.0

    b1_loc_norm   = (8.0 - df_dm["B1_loc"].astype(float).values) / 7.0
    b1_valuer_norm = (8.0 - df_dm["B1_valuer"].astype(float).values) / 7.0
    b1_peer_norm  = (8.0 - df_dm["B1_peer"].astype(float).values) / 7.0

    # Composite scores (Formulas 3.1–3.4)
    acs_scores  = 0.4 * b3_norm + 0.6 * c1_norm          # H1: Title Anchoring
    avcs_scores = 0.3 * b1_loc_norm + 0.3 * b2_norm + 0.4 * c2_norm  # H2: Location Familiarity
    rcs_scores  = 0.4 * b1_valuer_norm + 0.6 * c3_norm   # H3: Trend Momentum
    hcs_scores  = 0.25 * b1_peer_norm + 0.35 * b4_norm + 0.40 * c4_norm  # H4: Peer Herding

    # Export composite scores
    df_scores = df_dm[["Timestamp", "A1", "A2", "A3", "weight"]].copy()
    df_scores["H1_ACS"]  = acs_scores
    df_scores["H2_AVCS"] = avcs_scores
    df_scores["H3_RCS"]  = rcs_scores
    df_scores["H4_HCS"]  = hcs_scores
    df_scores.to_csv(os.path.join(dest_dir, "composite_scores.csv"), index=False)

    w = df_dm["weight"].values

    # BCa Bootstrap CIs
    h1_ci_l, h1_ci_u, h1_mean = bca_bootstrap_ci(acs_scores,  w)
    h2_ci_l, h2_ci_u, h2_mean = bca_bootstrap_ci(avcs_scores, w)
    h3_ci_l, h3_ci_u, h3_mean = bca_bootstrap_ci(rcs_scores,  w)
    h4_ci_l, h4_ci_u, h4_mean = bca_bootstrap_ci(hcs_scores,  w)

    sum_means = h1_mean + h2_mean + h3_mean + h4_mean
    alpha_1 = h1_mean / sum_means
    alpha_2 = h2_mean / sum_means
    alpha_3 = h3_mean / sum_means
    alpha_4 = h4_mean / sum_means

    print(f"\nHeuristic Composite Scores (n={n}):")
    print(f"  H1 Title (ACS):    {h1_mean:.4f}  CI=[{h1_ci_l:.4f}, {h1_ci_u:.4f}]  α₁={alpha_1:.4f}")
    print(f"  H2 Location (AVCS):{h2_mean:.4f}  CI=[{h2_ci_l:.4f}, {h2_ci_u:.4f}]  α₂={alpha_2:.4f}")
    print(f"  H3 Momentum (RCS): {h3_mean:.4f}  CI=[{h3_ci_l:.4f}, {h3_ci_u:.4f}]  α₃={alpha_3:.4f}")
    print(f"  H4 Peer (HCS):     {h4_mean:.4f}  CI=[{h4_ci_l:.4f}, {h4_ci_u:.4f}]  α₄={alpha_4:.4f}")

    # Save alpha weights
    alpha_weights = {
        "survey_derived": [
            round(alpha_1, 6),
            round(alpha_2, 6),
            round(alpha_3, 6),
            round(alpha_4, 6)
        ],
        "literature_baseline": [0.35, 0.35, 0.15, 0.15],
        "scoring_sample_n": n
    }
    weights_path = os.path.join(dest_dir, "alpha_weights.json")
    with open(weights_path, "w") as f:
        json.dump(alpha_weights, f, indent=2)
    print(f"\nAlpha weights saved to {weights_path}")

    # Ecological rationality split (within decision-maker sub-sample)
    inf_mask = df_dm["D4"].astype(str).apply(
        lambda s: "Peer PFA behaviour" in s or "Regulatory uncertainty" in s
    ).values
    df_inf    = df_dm[inf_mask]
    df_non    = df_dm[~inf_mask]
    w_inf     = w[inf_mask]
    w_non     = w[~inf_mask]

    mean_avcs_inf = np.sum(avcs_scores[inf_mask] * w_inf) / np.sum(w_inf) if w_inf.sum() > 0 else 0.0
    mean_avcs_non = np.sum(avcs_scores[~inf_mask] * w_non) / np.sum(w_non) if w_non.sum() > 0 else 0.0
    mean_rcs_inf  = np.sum(rcs_scores[inf_mask] * w_inf) / np.sum(w_inf) if w_inf.sum() > 0 else 0.0
    mean_rcs_non  = np.sum(rcs_scores[~inf_mask] * w_non) / np.sum(w_non) if w_non.sum() > 0 else 0.0

    eco_results = {
        "decision_maker_sample_n": n,
        "inf_citing_count": int(inf_mask.sum()),
        "inf_non_citing_count": int((~inf_mask).sum()),
        "mean_avcs_inf": float(mean_avcs_inf),
        "mean_avcs_non_inf": float(mean_avcs_non),
        "mean_rcs_inf": float(mean_rcs_inf),
        "mean_rcs_non_inf": float(mean_rcs_non),
        "avcs_difference": float(mean_avcs_inf - mean_avcs_non),
        "rcs_difference": float(mean_rcs_inf - mean_rcs_non)
    }
    with open(os.path.join(dest_dir, "ecological_rationality_results.json"), "w") as f:
        json.dump(eco_results, f, indent=2)

    # LaTeX: Heuristic scores table (n=7)
    def classify_prevalence(m):
        if m < 0.30:   return "Not Prevalent"
        elif m < 0.50: return "Low Prevalence"
        elif m < 0.70: return "Moderate Prevalence"
        else:          return "Highly Prevalent"

    heuristic_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Composite Heuristic Scores, BCa Confidence Intervals, and Calibrated Alpha Weights ($n={n}$, Decision-Maker Sub-Sample)}}
\\label{{tab:heuristic_scores}}
\\begin{{tabular}}{{lcccc}}
\\hline
\\textbf{{Heuristic Dimension}} & \\textbf{{Wtd. Mean}} & \\textbf{{BCa 95\\% CI}} & \\textbf{{Prevalence}} & \\textbf{{$\\alpha_j$}} \\\\
\\hline
Title Anchoring ($H_1$: ACS)   & {h1_mean:.4f} & [{h1_ci_l:.4f}, {h1_ci_u:.4f}] & {classify_prevalence(h1_mean)} & {alpha_1:.4f} \\\\
Location Familiarity ($H_2$: AVCS) & {h2_mean:.4f} & [{h2_ci_l:.4f}, {h2_ci_u:.4f}] & {classify_prevalence(h2_mean)} & {alpha_2:.4f} \\\\
Trend Momentum ($H_3$: RCS)    & {h3_mean:.4f} & [{h3_ci_l:.4f}, {h3_ci_u:.4f}] & {classify_prevalence(h3_mean)} & {alpha_3:.4f} \\\\
Peer Herding ($H_4$: HCS)      & {h4_mean:.4f} & [{h4_ci_l:.4f}, {h4_ci_u:.4f}] & {classify_prevalence(h4_mean)} & {alpha_4:.4f} \\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    with open(os.path.join(tables_dir, "heuristic_scores_table.tex"), "w") as f:
        f.write(heuristic_latex)

    return {
        "n_dm": n,
        "h1_mean": h1_mean, "h1_ci": (h1_ci_l, h1_ci_u),
        "h2_mean": h2_mean, "h2_ci": (h2_ci_l, h2_ci_u),
        "h3_mean": h3_mean, "h3_ci": (h3_ci_l, h3_ci_u),
        "h4_mean": h4_mean, "h4_ci": (h4_ci_l, h4_ci_u),
        "alphas": [alpha_1, alpha_2, alpha_3, alpha_4],
    }


def save_exclusion_log(structural_exclusions, a5_exclusions, dest_dir):
    all_exclusions = structural_exclusions + a5_exclusions
    df_log = pd.DataFrame(all_exclusions)
    df_log.to_csv(os.path.join(dest_dir, "exclusion_log.csv"), index=False)
    print(f"\nExclusion log saved: {len(structural_exclusions)} structural + {len(a5_exclusions)} Tier-2 (A5=C) exclusions")


def analyze_questionnaire():
    # Step 1: Load full census (Tier 1)
    df_full, project_root, dest_dir, structural_excl, n_a5_c = load_full_census()

    tables_dir = os.path.join(project_root, "outputs", "tables")
    os.makedirs(tables_dir, exist_ok=True)

    # Save cleaned full census
    df_full.to_csv(os.path.join(dest_dir, "cleaned_responses.csv"), index=False)

    # Step 2: Build decision-maker sub-sample (Tier 2)
    df_dm, a5_excl = build_decision_maker_subsample(df_full)

    # Step 3: Save exclusion log
    save_exclusion_log(structural_excl, a5_excl, dest_dir)

    # Step 4: Tier 1 descriptive analysis (N=24)
    tier1_results = compute_full_census_descriptives(df_full, tables_dir, dest_dir)

    # Step 5: Tier 2 heuristic composite scoring (n=7)
    tier2_results = compute_heuristic_scores(df_dm, tables_dir, dest_dir)

    print("\n=== Analysis complete ===")
    print(f"  Census N={tier1_results['N_census']} | Decision-maker n={tier2_results['n_dm']}")
    print(f"  Alpha weights: {[round(a, 4) for a in tier2_results['alphas']]}")


if __name__ == "__main__":
    analyze_questionnaire()
