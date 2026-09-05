# packages/optimizer/clean_analyze_responses.py
"""
Phase 3: Questionnaire response data cleaning, composite score calculations,
bootstrap confidence intervals, descriptive Section D analysis, and alpha weights export.
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

def load_and_clean_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    src_csv = os.path.join(project_root, "PFA Questionnaire Survey.csv")
    dest_dir = os.path.join(project_root, "data", "questionnaire")
    os.makedirs(dest_dir, exist_ok=True)
    
    dest_raw_csv = os.path.join(dest_dir, "raw_responses.csv")
    shutil.copy(src_csv, dest_raw_csv)
    print(f"Copied raw survey responses to {dest_raw_csv}")
    
    df = pd.read_csv(dest_raw_csv)
    
    # Rename columns using mapped codes
    df = df.rename(columns=COLUMN_MAPPING)
    
    # Clean up column spaces and strings
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].str.strip()
            
    # Apply exclusion criteria
    # 1. A5 == C -> Exclude
    # Check A5 string representation
    a5_c_mask = df['A5'].str.contains("No — I do not directly participate", na=False)
    exclusion_log = []
    
    for idx in df[a5_c_mask].index:
        exclusion_log.append({"row_idx": idx, "reason": "Excluded: Respondent has no decision authority (A5 = C)"})
        
    # Check if there are any blank scenario columns (C1-C4)
    for scenario_col in ["C1", "C2", "C3", "C4"]:
        blank_mask = df[scenario_col].isna()
        for idx in df[blank_mask].index:
            exclusion_log.append({"row_idx": idx, "reason": f"Excluded: Blank response in scenario {scenario_col}"})
            
    # Check if B1 ranks are unique permutations of 1-8
    rank_cols = ["B1_loc", "B1_title", "B1_yield", "B1_tenant", "B1_cond", "B1_peer", "B1_valuer", "B1_liq"]
    for idx, row in df.iterrows():
        try:
            row_ranks = [int(row[col]) for col in rank_cols]
            if sorted(row_ranks) != list(range(1, 9)):
                exclusion_log.append({"row_idx": idx, "reason": "Excluded: Invalid rank permutation (duplicates or missing ranks)"})
        except ValueError:
            exclusion_log.append({"row_idx": idx, "reason": "Excluded: Non-integer rank values"})
            
    # Save exclusion log to CSV
    df_exclusions = pd.DataFrame(exclusion_log)
    df_exclusions.to_csv(os.path.join(dest_dir, "exclusion_log.csv"), index=False)
    print(f"Exclusion checks completed. Excluded {len(df_exclusions['row_idx'].unique())} respondents.")
    
    # Filter dataset (keep only clean rows)
    excluded_indices = df_exclusions["row_idx"].unique()
    df_clean = df.drop(index=excluded_indices).reset_index(drop=True)
    
    # Assign composite weights per respondent
    weights = []
    primary_titles = [
        "Portfolio Manager/Fund Manager",
        "Investment Analyst",
        "Chief Investment Officer (CIO)/Head of Investment",
        "Director of Research, Strategy, or Risk",
        "Executive Director/Director with investment oversight responsibility",
        "Risk and Compliance Manager",
        "Real Estate Asset Manager"
    ]
    
    for idx, row in df_clean.iterrows():
        job = str(row['A1']).strip()
        is_primary = any(t in job for t in primary_titles) or (job == "Real Estate Asset Manager")
        
        part = str(row['A5']).strip()
        if "direct decision-making authority" in part or "veto power" in part:
            a5_class = "A"
        else:
            a5_class = "B"
            
        if is_primary:
            weight = 1.0 if a5_class == "A" else 0.7
        else:
            weight = 0.5 if a5_class == "A" else 0.35
            
        weights.append(weight)
        
    df_clean['weight'] = weights
    df_clean.to_csv(os.path.join(dest_dir, "cleaned_responses.csv"), index=False)
    print(f"Cleaned dataset saved with {len(df_clean)} rows.")
    return df_clean

def bca_bootstrap_ci(scores, weights, n_replications=10000, confidence_level=0.95):
    """
    Computes standard BCa (Bias-Corrected and Accelerated) Bootstrap Confidence Intervals.
    """
    n = len(scores)
    theta_hat = np.sum(scores * weights) / np.sum(weights)
    
    # Generate bootstrap replicates
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
    
    # Jackknife estimates for acceleration parameter a
    jack_estimates = []
    for i in range(n):
        sub_indices = [idx for idx in range(n) if idx != i]
        sub_scores = scores[sub_indices]
        sub_weights = weights[sub_indices]
        jack_estimates.append(np.sum(sub_scores * sub_weights) / np.sum(sub_weights))
        
    jack_estimates = np.array(jack_estimates)
    mean_jack = np.mean(jack_estimates)
    
    # Acceleration parameter (a)
    num = np.sum((mean_jack - jack_estimates) ** 3)
    den = 6 * (np.sum((mean_jack - jack_estimates) ** 2) ** 1.5)
    a = num / den if den != 0 else 0.0
    
    # Bias-correction parameter (z0)
    p = np.sum(boot_estimates < theta_hat) / n_replications
    p = np.clip(p, 1e-6, 1 - 1e-6)
    z0 = norm.ppf(p)
    
    # Percentile limits
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

def analyze_questionnaire():
    df_clean = load_and_clean_data()
    n_usable = len(df_clean)
    
    # Mapping for Likert columns B2, B3, B4
    likert_mapping = {
        "Strongly Agree": 5,
        "Agree": 4,
        "Neutral": 3,
        "Disagree": 2,
        "Strongly Disagree": 1
    }
    
    # Normalize Likert scores to [0, 1] using: (val - 1) / 4
    b2_norm = df_clean['B2'].map(likert_mapping).fillna(3).values
    b3_norm = df_clean['B3'].map(likert_mapping).fillna(3).values
    b4_norm = df_clean['B4'].map(likert_mapping).fillna(3).values
    
    b2_norm = (b2_norm - 1.0) / 4.0
    b3_norm = (b3_norm - 1.0) / 4.0
    b4_norm = (b4_norm - 1.0) / 4.0
    
    # Normalize Scenario scores to [0, 1]
    c1_norm = (df_clean['C1'].astype(float).values - 1.0) / 4.0
    c2_norm = (df_clean['C2'].astype(float).values - 1.0) / 4.0
    c3_norm = (df_clean['C3'].astype(float).values - 1.0) / 4.0
    c4_norm = (df_clean['C4'].astype(float).values - 1.0) / 4.0
    
    # Normalize Rank variables to [0, 1] using: (8 - rank) / 7
    b1_loc_norm = (8.0 - df_clean['B1_loc'].astype(float).values) / 7.0
    b1_title_norm = (8.0 - df_clean['B1_title'].astype(float).values) / 7.0
    b1_yield_norm = (8.0 - df_clean['B1_yield'].astype(float).values) / 7.0
    b1_tenant_norm = (8.0 - df_clean['B1_tenant'].astype(float).values) / 7.0
    b1_cond_norm = (8.0 - df_clean['B1_cond'].astype(float).values) / 7.0
    b1_peer_norm = (8.0 - df_clean['B1_peer'].astype(float).values) / 7.0
    b1_valuer_norm = (8.0 - df_clean['B1_valuer'].astype(float).values) / 7.0
    b1_liq_norm = (8.0 - df_clean['B1_liq'].astype(float).values) / 7.0
    
    # Composite Scores
    # H1: Title Heuristic (ACS)
    acs_scores = 0.4 * b3_norm + 0.6 * c1_norm
    # H2: Location Heuristic (AVCS)
    avcs_scores = 0.3 * b1_loc_norm + 0.3 * b2_norm + 0.4 * c2_norm
    # H3: Momentum/Valuer Heuristic (RCS)
    rcs_scores = 0.4 * b1_valuer_norm + 0.6 * c3_norm
    # H4: Peer/Herding Heuristic (HCS)
    hcs_scores = 0.25 * b1_peer_norm + 0.35 * b4_norm + 0.40 * c4_norm
    
    # Append to dataframe and export composite scores CSV
    df_scores = df_clean[['Timestamp', 'A1', 'A2', 'A3', 'weight']].copy()
    df_scores['H1_ACS'] = acs_scores
    df_scores['H2_AVCS'] = avcs_scores
    df_scores['H3_RCS'] = rcs_scores
    df_scores['H4_HCS'] = hcs_scores
    
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    df_scores.to_csv(os.path.join(project_root, "data", "questionnaire", "composite_scores.csv"), index=False)
    
    # Weights vector
    w = df_clean['weight'].values
    
    # Weighted Means & BCa CIs
    h1_ci_l, h1_ci_u, h1_mean = bca_bootstrap_ci(acs_scores, w)
    h2_ci_l, h2_ci_u, h2_mean = bca_bootstrap_ci(avcs_scores, w)
    h3_ci_l, h3_ci_u, h3_mean = bca_bootstrap_ci(rcs_scores, w)
    h4_ci_l, h4_ci_u, h4_mean = bca_bootstrap_ci(hcs_scores, w)
    
    # Sum of weighted means for normalization
    sum_means = h1_mean + h2_mean + h3_mean + h4_mean
    alpha_1 = h1_mean / sum_means
    alpha_2 = h2_mean / sum_means
    alpha_3 = h3_mean / sum_means
    alpha_4 = h4_mean / sum_means
    
    print("\nHeuristic Composite Score Summary:")
    print(f"H1 Title (ACS): Mean = {h1_mean:.4f}, CI = [{h1_ci_l:.4f}, {h1_ci_u:.4f}]")
    print(f"H2 Location (AVCS): Mean = {h2_mean:.4f}, CI = [{h2_ci_l:.4f}, {h2_ci_u:.4f}]")
    print(f"H3 Momentum (RCS): Mean = {h3_mean:.4f}, CI = [{h3_ci_l:.4f}, {h3_ci_u:.4f}]")
    print(f"H4 Peer (HCS): Mean = {h4_mean:.4f}, CI = [{h4_ci_l:.4f}, {h4_ci_u:.4f}]")
    
    print("\nEmpirical Alpha Weights:")
    print(f"alpha_1 (Title): {alpha_1:.4f}")
    print(f"alpha_2 (Location): {alpha_2:.4f}")
    print(f"alpha_3 (Momentum): {alpha_3:.4f}")
    print(f"alpha_4 (Peer): {alpha_4:.4f}")
    
    # Export Alpha Weights JSON
    alpha_weights = {
        "survey_derived": [
            round(alpha_1, 6),
            round(alpha_2, 6),
            round(alpha_3, 6),
            round(alpha_4, 6)
        ],
        "literature_baseline": [0.35, 0.35, 0.15, 0.15]
    }
    
    weights_path = os.path.join(project_root, "data", "questionnaire", "alpha_weights.json")
    with open(weights_path, "w") as f:
        json.dump(alpha_weights, f, indent=2)
    print(f"\nEmpirical alpha weights saved to {weights_path}")
    
    # Descriptive classifications
    def classify_prevalence(mean_score):
        if mean_score < 0.30: return "Not Prevalent"
        elif mean_score < 0.50: return "Low Prevalence"
        elif mean_score < 0.70: return "Moderate Prevalence"
        else: return "Highly Prevalent"
        
    # generate LaTeX Tables for Thesis Report
    tables_dir = os.path.join(project_root, "outputs", "tables")
    os.makedirs(tables_dir, exist_ok=True)
    
    # 1. Heuristic Table (Table 4.2)
    heuristic_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Empirically Elicited Heuristic Scores, Prevalence, and Weight Calibration}}
\\label{{tab:heuristic_scores}}
\\begin{{tabular}}{{lcccc}}
\\hline
\\textbf{{Heuristic Dimension (Index Code)}} & \\textbf{{Weighted Mean}} & \\textbf{{BCa 95\\% CI}} & \\textbf{{Prevalence Level}} & \\textbf{{Calibrated Weight ($\\alpha_j$)}} \\\\
\\hline
Title Anchoring ($H_1$: ACS) & {h1_mean:.4f} & [{h1_ci_l:.4f}, {h1_ci_u:.4f}] & {classify_prevalence(h1_mean)} & {alpha_1:.4f} \\\\
Location Familiarity ($H_2$: AVCS) & {h2_mean:.4f} & [{h2_ci_l:.4f}, {h2_ci_u:.4f}] & {classify_prevalence(h2_mean)} & {alpha_2:.4f} \\\\
Trend Momentum ($H_3$: RCS) & {h3_mean:.4f} & [{h3_ci_l:.4f}, {h3_ci_u:.4f}] & {classify_prevalence(h3_mean)} & {alpha_3:.4f} \\\\
Peer Herding ($H_4$: HCS) & {h4_mean:.4f} & [{h4_ci_l:.4f}, {h4_ci_u:.4f}] & {classify_prevalence(h4_mean)} & {alpha_4:.4f} \\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    with open(os.path.join(tables_dir, "heuristic_scores_table.tex"), "w") as f:
        f.write(heuristic_latex)
        
    # 2. Median Criteria Ranks (Table 4.3)
    rank_cols = ["B1_loc", "B1_title", "B1_yield", "B1_tenant", "B1_cond", "B1_peer", "B1_valuer", "B1_liq"]
    ranks_df = df_clean[rank_cols].astype(float)
    median_ranks = ranks_df.median()
    top_3_pct = (ranks_df <= 3.0).sum() / len(ranks_df)
    
    criteria_labels = {
        "B1_loc": "Location Prestige",
        "B1_title": "Title Status",
        "B1_yield": "Rental Yield",
        "B1_tenant": "Tenant Profile/Lease",
        "B1_cond": "Physical Condition",
        "B1_peer": "Peer Activity",
        "B1_valuer": "Valuer Recommendation",
        "B1_liq": "Market Liquidity"
    }
    
    criteria_latex_rows = []
    for col in rank_cols:
        label = criteria_labels[col]
        criteria_latex_rows.append(f"{label} & {median_ranks[col]:.1f} & {top_3_pct[col]*100:.1f}\\% \\\\")
        
    criteria_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Criteria Ranks Summary: Medians and Top-3 Rankings (N={n_usable})}}
\\label{{tab:criteria_ranks}}
\\begin{{tabular}}{{lcc}}
\\hline
\\textbf{{Property Evaluation Criterion}} & \\textbf{{Median Rank (1-8)}} & \\textbf{{Proportion Ranking Top-3 (\\%)}} \\\\
\\hline
{"\n".join(criteria_latex_rows)}
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    with open(os.path.join(tables_dir, "criteria_ranks_table.tex"), "w") as f:
        f.write(criteria_latex)
        
    # 3. Section D Contextual Factors (Table 4.4)
    # Aggregate D4 factors into counts
    d4_counts = {cat: 0 for cat in D4_CATEGORIES.values()}
    d4_option_counts = {}
    
    # Process multiple selections separated by semicolon
    for factors_str in df_clean['D4'].dropna():
        options = [o.strip() for o in factors_str.split(";")]
        for opt in options:
            if opt in D4_CATEGORIES:
                cat = D4_CATEGORIES[opt]
                d4_counts[cat] += 1
                d4_option_counts[opt] = d4_option_counts.get(opt, 0) + 1
                
    d4_latex_rows = []
    for opt, count in sorted(d4_option_counts.items(), key=lambda x: x[1], reverse=True):
        cat = D4_CATEGORIES[opt]
        pct = (count / n_usable) * 100
        d4_latex_rows.append(f"{opt[:50]}... & {cat} & {count} & {pct:.1f}\\% \\\\")
        
    d4_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Institutional Contextual Constraints Driving Heuristic Use}}
\\label{{tab:institutional_context_factors}}
\\begin{{tabular}}{{lccc}}
\\hline
\\textbf{{Factor / Context Description}} & \\textbf{{Category}} & \\textbf{{Frequency}} & \\textbf{{Proportion (\\%)}} \\\\
\\hline
{"\n".join(d4_latex_rows)}
\\hline
\\textbf{{Category Aggregate Selections:}} \\\\
Cognitive (COG) & -- & {d4_counts['COG']} & -- \\\\
Informational (INF) & -- & {d4_counts['INF']} & -- \\\\
Institutional (INS) & -- & {d4_counts['INS']} & -- \\\\
Regulatory (REG) & -- & {d4_counts['REG']} & -- \\\\
\\hline
\\end{{tabular}}
\\end{{table}}
"""
    with open(os.path.join(tables_dir, "d4_factors_table.tex"), "w") as f:
        f.write(d4_latex)
        
    # 4. Respondent Profile Frequencies (Table 4.1)
    title_freq = df_clean['A1'].value_counts()
    exp_freq = df_clean['A2'].value_counts()
    aum_freq = df_clean['A3'].value_counts()
    
    profile_latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Respondent Demographic Profile Summary (N={n_usable})}}
\\label{{tab:respondent_profile}}
\\begin{{tabular}}{{lcc}}
\\hline
\\textbf{{Profile Attribute}} & \\textbf{{Frequency}} & \\textbf{{Proportion (\\%)}} \\\\
\\hline
\\multicolumn{{3}}{{l}}{{\\textbf{{Current Job Title}}}} \\\\
"""
    for title, val in title_freq.items():
        profile_latex += f"{title} & {val} & {(val/n_usable)*100:.1f}\\% \\\\\n"
    profile_latex += "\\hline\n\\multicolumn{3}{l}{\\textbf{Years of Experience}} \\\\\n"
    for exp, val in exp_freq.items():
        profile_latex += f"{exp} & {val} & {(val/n_usable)*100:.1f}\\% \\\\\n"
    profile_latex += "\\hline\n\\multicolumn{3}{l}{\\textbf{Assets Under Management (AUM)}} \\\\\n"
    for aum, val in aum_freq.items():
        profile_latex += f"{aum} & {val} & {(val/n_usable)*100:.1f}\\% \\\\\n"
    profile_latex += """\\hline
\\end{{tabular}}
\\end{{table}}
"""
    with open(os.path.join(tables_dir, "respondent_profile_table.tex"), "w") as f:
        f.write(profile_latex)
        
    # 5. Ecological Rationality Test
    # INF-citing defined as selecting Option B (peer behavior) or Option H (regulatory uncertainty)
    inf_cite_mask = df_clean['D4'].astype(str).apply(
        lambda s: "Peer PFA behaviour" in s or "Regulatory uncertainty" in s
    )
    
    df_inf = df_clean[inf_cite_mask]
    df_non_inf = df_clean[~inf_cite_mask]
    
    print("\nEcological Rationality Test Comparison:")
    print(f"INF-citing count: {len(df_inf)}, INF-non-citing count: {len(df_non_inf)}")
    
    # Calculate means for AVCS and RCS
    w_inf = df_inf['weight'].values
    w_non_inf = df_non_inf['weight'].values
    
    mean_avcs_inf = np.sum(avcs_scores[inf_cite_mask] * w_inf) / np.sum(w_inf) if len(df_inf) > 0 else 0.0
    mean_avcs_non_inf = np.sum(avcs_scores[~inf_cite_mask] * w_non_inf) / np.sum(w_non_inf) if len(df_non_inf) > 0 else 0.0
    
    mean_rcs_inf = np.sum(rcs_scores[inf_cite_mask] * w_inf) / np.sum(w_inf) if len(df_inf) > 0 else 0.0
    mean_rcs_non_inf = np.sum(rcs_scores[~inf_cite_mask] * w_non_inf) / np.sum(w_non_inf) if len(df_non_inf) > 0 else 0.0
    
    print(f"Mean AVCS (Location) - INF-citing: {mean_avcs_inf:.4f} vs Non-citing: {mean_avcs_non_inf:.4f} (Diff: {mean_avcs_inf - mean_avcs_non_inf:.4f})")
    print(f"Mean RCS (Momentum) - INF-citing: {mean_rcs_inf:.4f} vs Non-citing: {mean_rcs_non_inf:.4f} (Diff: {mean_rcs_inf - mean_rcs_non_inf:.4f})")
    
    # Write test output to data folder
    test_results = {
        "inf_citing_count": int(len(df_inf)),
        "inf_non_citing_count": int(len(df_non_inf)),
        "mean_avcs_inf": float(mean_avcs_inf),
        "mean_avcs_non_inf": float(mean_avcs_non_inf),
        "mean_rcs_inf": float(mean_rcs_inf),
        "mean_rcs_non_inf": float(mean_rcs_non_inf),
        "avcs_difference": float(mean_avcs_inf - mean_avcs_non_inf),
        "rcs_difference": float(mean_rcs_inf - mean_rcs_non_inf)
    }
    
    with open(os.path.join(project_root, "data", "questionnaire", "ecological_rationality_results.json"), "w") as f:
        json.dump(test_results, f, indent=2)
        
    # 6. Preference Gaps
    gap_anchoring = (c1_norm - b3_norm).mean()
    gap_availability = (c2_norm - b2_norm).mean()
    gap_herding = (c4_norm - b4_norm).mean()
    
    print("\nStated vs. Revealed Preference Gaps (Positive = Revealed > Stated):")
    print(f"Anchoring gap (C1 - B3): {gap_anchoring:.4f}")
    print(f"Availability gap (C2 - B2): {gap_availability:.4f}")
    print(f"Herding gap (C4 - B4): {gap_herding:.4f}")
    
    with open(os.path.join(project_root, "data", "questionnaire", "preference_gaps.json"), "w") as f:
        json.dump({
            "anchoring_gap": float(gap_anchoring),
            "availability_gap": float(gap_availability),
            "herding_gap": float(gap_herding)
        }, f, indent=2)

if __name__ == "__main__":
    analyze_questionnaire()
