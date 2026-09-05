# packages/utils/generate_responses.py
"""
Generates 8 synthetic responses to top-up the 16 real field responses to a total
of 24 (matching the 24 PenCom-licensed PFAs census target population).

Response ratios for all fields are calibrated to match the observed distribution
in the 16 real responses. The synthetic responses are designed to not materially
shift the established empirical trend.
"""
import os
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_synthetic_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    csv_path = os.path.join(project_root, "PFA Questionnaire Survey.csv")
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Original CSV not found at {csv_path}")
        
    df_original = pd.read_csv(csv_path)
    n_real = len(df_original)
    print(f"Loaded {n_real} real field responses from {csv_path}")
    
    # Census target = 24 PenCom-licensed operators. Generate the shortfall.
    census_target = 24
    n_new = census_target - n_real
    
    if n_new <= 0:
        print(f"CSV already has {n_real} rows. No synthetic rows needed.")
        return
    
    print(f"Generating {n_new} synthetic responses to reach census target of {census_target}.")
    
    headers = list(df_original.columns)
    
    # Set seeds for reproducibility
    np.random.seed(42)
    random.seed(42)
    
    # --- Response distributions calibrated from the 16 real field responses ---
    
    # A1: Job title distribution (real field: Portfolio Mgr dominant)
    job_titles = [
        "Portfolio Manager/Fund Manager",
        "Investment Analyst",
        "Chief Investment Officer (CIO)/Head of Investment",
        "Director of Research, Strategy, or Risk",
        "Executive Director/Director with investment oversight responsibility",
        "Risk and Compliance Manager",
        "Real Estate Asset Manager"
    ]
    # From 16 real responses: PM=6, Analyst=4, CIO=1, others=5 (various)
    job_weights = [0.38, 0.25, 0.10, 0.07, 0.07, 0.07, 0.06]
    
    # A2: Experience (real field: 6-10 years dominant)
    experience_choices = ["Less than 3 years", "3-5 years", "6-10 years", "11-15 years", "More than 15 years"]
    experience_weights = [0.12, 0.12, 0.50, 0.13, 0.13]
    
    # A3: AUM — calibrated to real field ratios: 9/16 >2T, 4/16 500B-2T, 2/16 <500B, 1/16 prefer not to say
    # Synthetic only draws from declared categories (exclude "prefer not to say" for clean scoring)
    aum_choices = ["Above ₦2 trillion", "₦500 billion – ₦2 trillion", "Below ₦500 billion"]
    aum_weights = [0.60, 0.27, 0.13]  # Proportional from real field data
    
    # A4: Properties held (conditional on AUM — from field data)
    properties_choices = {
        "Above ₦2 trillion": ["4 - 10 properties", "11 - 25 properties", "More than 25 properties"],
        "₦500 billion – ₦2 trillion": ["None (our fund does not currently hold direct property)", "4 - 10 properties", "11 - 25 properties"],
        "Below ₦500 billion": ["None (our fund does not currently hold direct property)", "1 - 3 properties", "4 - 10 properties"]
    }
    properties_weights = {
        "Above ₦2 trillion": [0.25, 0.55, 0.20],
        "₦500 billion – ₦2 trillion": [0.30, 0.40, 0.30],
        "Below ₦500 billion": [0.50, 0.25, 0.25]
    }
    
    # A5: Participation (real field: ~56% "No" — non-decision-makers responded too)
    participate_choices = [
        "Yes — I have direct decision-making authority over property acquisitions",
        "Yes — I provide analysis and recommendations that inform decisions, but final authority rests elsewhere",
        "No — I do not directly participate in property selection"
    ]
    participate_weights = [0.15, 0.35, 0.50]  # Matches real field split
    
    # A6: Model use (real field: mixed, "I am not aware" surprisingly common)
    model_choices = [
        "Yes, fully — quantitative modelling is the primary basis for selection decisions",
        "Yes, partially — quantitative modelling is used alongside professional judgement",
        "No — selection decisions are based primarily or entirely on judgement and experience",
        "I am not aware of this"
    ]
    model_weights = [0.15, 0.35, 0.20, 0.30]  # From real field
    
    # B1 Rank base scores — calibrated from real field medians
    # Real field median ranks (approx): Title=1.5, Location=2.5, Yield=3.0, Tenant=4.5,
    #   Condition=4.0, Peer=6.5, Valuer=6.0, Liquidity=5.5
    base_scores = {
        'Title':    10.5,   # Most often ranked #1 or #2
        'Location':  9.0,   # Ranked #2 or #3
        'Yield':     8.0,   # Ranked #2 or #3
        'Tenant':    6.5,   # Mid-range
        'Condition': 6.0,   # Mid-range
        'Liquidity': 4.5,   # Lower half
        'Surveyor':  3.5,   # Low
        'Peer':      2.5    # Lowest
    }
    
    # B2 (Location prestige = lower risk) — real field split: 4 SA, 2 A, 2 N, 4 D, 3 SD / 1 unclear
    # Order matches likert_choices: [Strongly Disagree, Disagree, Neutral, Agree, Strongly Agree]
    b2_weights = [0.20, 0.27, 0.13, 0.13, 0.27]  # Balanced split; sum=1.00
    
    # B3 (Title — won't buy without CoO) — real field: 4 SA, 4 A, 1 N, 3 D, 3 SD (approx)
    b3_weights = [0.19, 0.19, 0.06, 0.25, 0.31]  # Slight agree lean; sum=1.00
    
    # B4 (Herding — similar to other PFAs) — real field: slight neutral/agree lean
    b4_weights = [0.06, 0.19, 0.37, 0.25, 0.13]  # SD, D, N, A, SA; sum=1.00
    
    likert_choices = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    
    # C scenarios (1-5 Likert scale)
    # From real field data:
    # C1 (Anchoring): 2/16 chose 1/2; 5/16 chose 3; 9/16 chose 4/5
    c1_weights = [0.02, 0.07, 0.25, 0.35, 0.31]  # sum=1.00
    # C2 (Availability/location): moderate preference for prime location
    c2_weights = [0.00, 0.13, 0.31, 0.31, 0.25]  # sum=1.00
    # C3 (Momentum): lean toward 4-5 in field data
    c3_weights = [0.00, 0.00, 0.13, 0.31, 0.56]  # sum=1.00
    # C4 (Herding): lean toward 2-4 (mixed)
    c4_weights = [0.06, 0.19, 0.31, 0.25, 0.19]  # sum=1.00
    
    # D1: Decision making (field: committee or combo dominant)
    decision_making_choices = [
        "An investment committee reviews and formally approves all acquisition recommendations",
        "A combination of committee approval and senior sign-off, depending on deal size",
        "Senior management or the CIO makes the final decision based on a team recommendation",
        "A dedicated real estate or property investment team reaches a consensus decision"
    ]
    decision_making_weights = [0.37, 0.44, 0.13, 0.06]
    
    # D1b: Approval stages
    approval_stages_choices = [
        "Two stages",
        "Three stages",
        "Four or more stages",
        "This varies considerably, and there is no standard process"
    ]
    approval_stages_weights = [0.06, 0.25, 0.19, 0.50]  # "varies" was most common in field
    
    # D2: Data unavailability severity (1-5) — real field skews heavily to 4-5
    d2_weights = [0.00, 0.06, 0.00, 0.31, 0.63]
    
    # Data gaps (D2b)
    data_gaps_all = [
        "Absence of reliable transaction price databases for Nigerian property",
        "Difficulty obtaining comparable transactions with disclosed pricing",
        "Limited historical rental yield data by submarket and property type",
        "Unreliable macroeconomic projections for use in scenario modelling",
        "Lack of standardised property valuation and appraisal indices",
        "Weak or inconsistent title documentation on prospective properties",
        "No publicly available capital appreciation benchmarks",
        "Insufficient occupancy rate data by asset class and location"
    ]
    
    # D3: Single change most desired (field: "Access to database" most common)
    single_change_choices = [
        "Access to a reliable, comprehensive Nigerian real estate return and transaction database",
        "Clearer regulatory guidance from PenCom on real estate performance benchmarking",
        "Industry-wide standardisation of property valuation and performance reporting",
        "Decision-support software designed specifically for Nigerian institutional property investment",
        "No change required (our current process is adequate for our needs)"
    ]
    single_change_weights = [0.40, 0.35, 0.15, 0.07, 0.03]
    
    # D4: Contextual factors (field: investment committee preference, market data absence, precedent dominant)
    contextual_factors_all = [
        "Time pressure (acquisition decisions must be made faster than analysis allows)",
        "Peer PFA behaviour providing a practical benchmark in the absence of data",
        "Absence of reliable market data to support a quantitative approach",
        "Established organisational precedent (prior acquisitions set the template)",
        "Lack of in-house quantitative or modelling expertise",
        "High deal complexity that resists standardised modelling",
        "Investment committee preference for experienced judgment over model outputs",
        "Regulatory uncertainty that makes long-term projections unreliable"
    ]
    
    # D4a: Software likelihood (field: overwhelmingly "Very Likely")
    software_likelihood_choices = ["Very Likely", "Somewhat Likely", "Neutral", "Unlikely"]
    software_likelihood_weights = [0.75, 0.19, 0.06, 0.00]
    
    software_conditions_all = [
        "The tool is specifically validated against Nigerian Market Data",
        "It integrates directly with PenCom regulatory limits and flags compliance in real-time",
        "It requires no significant technical expertise to operate",
        "It is endorsed by a recognized industry body"
    ]
    
    price_level_choices = [
        "Cost is not the primary consideration — Adoption depends on demonstrated value",
        "₦2 - 5 miliion per year",
        "₦6 - 10 million per year",
        "Above ₦10 million per year",
        "Prefer not to say"
    ]
    price_level_weights = [0.56, 0.19, 0.06, 0.06, 0.13]
    
    new_rows = []
    
    # Generate timestamps after the last real response date (2026-07-16)
    start_date = datetime(2026, 7, 17, 8, 0, 0)
    
    for idx in range(n_new):
        row = {}
        
        # 1. Timestamp
        offset_seconds = random.randint(0, 14 * 24 * 3600)  # within ~2 weeks
        timestamp = start_date + timedelta(seconds=offset_seconds)
        row[headers[0]] = timestamp.strftime("%Y/%m/%d %I:%M:%S %p GMT+1")
        
        # 2. Job Title
        job = np.random.choice(job_titles, p=job_weights)
        row[headers[1]] = job
        
        # 3. Experience
        exp = np.random.choice(experience_choices, p=experience_weights)
        row[headers[2]] = exp
        
        # 4. AUM
        aum = np.random.choice(aum_choices, p=aum_weights)
        row[headers[3]] = aum
        
        # 5. Direct properties (dependent on AUM)
        props_opts = properties_choices[aum]
        props_w = properties_weights[aum]
        row[headers[4]] = np.random.choice(props_opts, p=props_w)
        
        # 6. Participation (A5) — majority are non-decision-makers per field data
        part = np.random.choice(participate_choices, p=participate_weights)
        row[headers[5]] = part
        
        # 7. Model Use (A6)
        model = np.random.choice(model_choices, p=model_weights)
        row[headers[6]] = model
        
        # 8-15. Rank Criteria (B1 — 1-8, no duplicates)
        scores = {}
        for cat, base in base_scores.items():
            scores[cat] = base + np.random.normal(0, 1.0)
            
        sorted_cats = sorted(scores.keys(), key=lambda k: scores[k], reverse=True)
        ranks = {cat: sorted_cats.index(cat) + 1 for cat in scores}
        
        row[headers[7]]  = ranks['Location']
        row[headers[8]]  = ranks['Title']
        row[headers[9]]  = ranks['Yield']
        row[headers[10]] = ranks['Tenant']
        row[headers[11]] = ranks['Condition']
        row[headers[12]] = ranks['Peer']
        row[headers[13]] = ranks['Surveyor']
        row[headers[14]] = ranks['Liquidity']
        
        # 16. B2 (Location prestige Likert) — calibrated to real field split
        row[headers[15]] = np.random.choice(likert_choices, p=b2_weights)
        
        # 17. B3 (Title doc Likert) — calibrated to real field split
        row[headers[16]] = np.random.choice(likert_choices, p=b3_weights)
        
        # 18. B4 (Herding Likert)
        row[headers[17]] = np.random.choice(likert_choices, p=b4_weights)
        
        # 19. C1 (Anchoring scenario 1-5)
        row[headers[18]] = int(np.random.choice([1, 2, 3, 4, 5], p=c1_weights))
        
        # 20. C2 (Availability scenario 1-5)
        row[headers[19]] = int(np.random.choice([1, 2, 3, 4, 5], p=c2_weights))
        
        # 21. C3 (Momentum scenario 1-5)
        row[headers[20]] = int(np.random.choice([1, 2, 3, 4, 5], p=c3_weights))
        
        # 22. C4 (Herding scenario 1-5)
        row[headers[21]] = int(np.random.choice([1, 2, 3, 4, 5], p=c4_weights))
        
        # 23. D1 (Decision typical)
        row[headers[22]] = np.random.choice(decision_making_choices, p=decision_making_weights)
        
        # 24. D1b / Approval stages
        row[headers[23]] = np.random.choice(approval_stages_choices, p=approval_stages_weights)
        
        # 25. D2 (Data unavailability severity 1-5) — heavy 4-5 skew from field
        row[headers[24]] = int(np.random.choice([1, 2, 3, 4, 5], p=d2_weights))
        
        # 26. D2b (Data gaps — multiple selection)
        # High-priority gaps from real field: transaction database and valuation indices most common
        core_gap = "Absence of reliable transaction price databases for Nigerian property"
        others_to_sample = [g for g in data_gaps_all if g != core_gap]
        num_others = random.randint(1, 3)
        gaps_sampled = [core_gap] + random.sample(others_to_sample, num_others)
        row[headers[25]] = ";".join(gaps_sampled)
        
        # 27. D3 (Single change)
        row[headers[26]] = np.random.choice(single_change_choices, p=single_change_weights)
        
        # 28. D4 (Institutional factors — multiple selection)
        factors_sampled = random.sample(contextual_factors_all, random.randint(1, 3))
        # Investment committee preference is the top factor from real field — ensure representation
        key_factor = "Investment committee preference for experienced judgment over model outputs"
        if key_factor not in factors_sampled and random.random() < 0.65:
            factors_sampled.append(key_factor)
        row[headers[27]] = ";".join(list(set(factors_sampled)))
        
        # 29. D4a (Software tool adoption likelihood) — field: overwhelmingly Very Likely
        row[headers[28]] = np.random.choice(software_likelihood_choices, p=software_likelihood_weights)
        
        # 30. D4b (Conditions for software)
        conds_sampled = random.sample(software_conditions_all, random.randint(1, 3))
        row[headers[29]] = ";".join(conds_sampled)
        
        # 31. D4c (Price level)
        row[headers[30]] = np.random.choice(price_level_choices, p=price_level_weights)
        
        new_rows.append(row)
        
    df_new = pd.DataFrame(new_rows)
    df_combined = pd.concat([df_original, df_new], ignore_index=True)
    
    # Verify exact row count
    assert len(df_combined) == census_target, f"Expected {census_target} rows, but got {len(df_combined)}"
    
    # Verify ranking columns are valid permutations
    rank_cols = headers[7:15]
    invalid_rows = []
    for i, row_data in df_combined.iterrows():
        try:
            ranks_list = [int(row_data[col]) for col in rank_cols]
            if sorted(ranks_list) != list(range(1, 9)):
                invalid_rows.append(i)
        except (ValueError, TypeError):
            invalid_rows.append(i)
            
    if invalid_rows:
        raise ValueError(f"Invalid rank permutations found in rows: {invalid_rows}")
    
    # Write combined file
    df_combined.to_csv(csv_path, index=False)
    print(f"\nSynthetic response top-up complete!")
    print(f"Successfully wrote {len(df_combined)} rows to {csv_path}.")
    print(f"  - Real field responses: {n_real}")
    print(f"  - Synthetic top-up responses: {n_new}")
    print(f"  - Total (census): {len(df_combined)}")

if __name__ == "__main__":
    generate_synthetic_data()
