# Master Implementation Checklist — Version 2.0
## *Heuristics in Property Portfolio Selection Decisions of Nigerian Pension Funds*
### Obafemi Awolowo University · Department of Estate Management · 2024/2025

**Issued:** April 26, 2026  
**Status at Issue:** Project defense cleared. Approved to proceed.  
**Estimated completion:** Mid-July 2026 (11 working weeks)

> **How to use this document.** Print it. Keep it on your desk. Every checkbox represents a concrete, completable unit of work. Work through it in sequence — phases are ordered by dependency. Nothing in Phase 3 can start until Phase 2 is done. Mark each item with the date it was completed. When this document is fully checked, your dissertation is ready to submit.

---

## ◈ WHAT IS ALREADY DONE

The following are completed and locked. Do not revisit or revise without a compelling reason.

| Deliverable | Status | Notes |
|---|---|---|
| Chapter 1 — Introduction | ✅ Complete | Supervisor-corrected draft |
| Chapter 2 — Literature Review | ✅ Complete | Restructured per revision guidelines; all citations verified |
| Chapter 3 — Methodology | ✅ Complete | Body draft ~10,200 words; Formulas 3.1–3.6 finalized |
| Questionnaire Instrument | ✅ Complete | v2 final; Sections A–D fully close-ended; CPFA census design confirmed |
| Companion Guide | ✅ Complete | v3; operationalizes Formulas 3.1–3.6; covers Chapters 4 and 5 |
| PRD + TDD | ✅ Complete | System architecture fully designed |
| Generator Specification | ✅ Complete | Generator v1 document; all calibration parameters defined |
| Project Defense | ✅ Passed | Approved to proceed |

---

## ◈ FROZEN STUDY PARAMETERS

These values are pre-registered. They must not change for any reason after the universe is generated. Changing them after analysis has started invalidates the study's epistemological consistency.

| Parameter | Frozen Value | Source |
|---|---|---|
| Synthetic property universe size | **80 properties** | Generator v1, PRD |
| Random seed | **42** | Generator v1 |
| Fund size (₦) | **₦10,000,000,000 (₦10B)** | Chapter 3 |
| Risk-free rate | **15% (0.15)** | CBN T-bill average 2019–2024 |
| Monte Carlo paths | **10,000** | Chapter 3, Section 3.5.4 |
| Simulation horizon | **60 months (5 years)** | Chapter 3 |
| Covariance shocks | **Cholesky-correlated** | Chapter 3 |
| Bootstrap method | **BCa (bias-corrected accelerated)** | Chapter 3 |
| Bootstrap block length | **6 months** | Chapter 3 |
| Bootstrap replications | **10,000** | Chapter 3 |
| Max single property weight | **5% of fund** | PenCom regulation |
| Practical significance threshold | **ΔSharpe = 0.05** | Pre-registered |
| AUM brackets | **<₦500B / ₦500B–₦2T / >₦2T** | Chapter 3 |

---

## ◈ MONOREPO STRUCTURE

All code for this dissertation lives in a single repository. This guarantees that the property universe used in the academic analysis is identical to the universe powering the PFA-Simulator demo. There is one source of truth.

```
pfa-portfolio-research/                 ← Root monorepo
├── packages/
│   ├── generator/                      ← Python: property universe generator
│   │   ├── generate_universe.py
│   │   ├── validate_universe.py
│   │   ├── config.py                   ← All calibration parameters
│   │   └── metrics_calculator.py
│   ├── optimizer/                      ← Python/FastAPI: optimizer + heuristic engine + MC
│   │   ├── main.py
│   │   ├── heuristic_engine.py
│   │   ├── mvo_optimizer.py
│   │   ├── monte_carlo.py
│   │   └── statistical_tests.py
│   ├── research-backend/               ← Java 17 / Spring Boot 3.2
│   │   └── src/main/java/...
│   └── simulator/                      ← Next.js 14 / TypeScript / Tailwind
│       └── src/...
├── data/
│   ├── frozen/                         ← WRITE ONCE, READ ONLY after generation
│   │   ├── property_universe.csv
│   │   ├── market_indices_returns.csv
│   │   └── covariance_matrix.csv
│   ├── calibration/                    ← Your collected secondary market data
│   │   ├── knight_frank_2024.csv
│   │   ├── cbre_2023.csv
│   │   └── nbs_real_estate_2018_2024.csv
│   └── questionnaire/                  ← Raw responses, cleaned data
│       ├── raw_responses.csv
│       └── composite_scores.csv
├── outputs/                            ← All generated results
│   ├── portfolios/
│   ├── simulation_results/
│   ├── charts/
│   └── tables/
└── dissertation/                       ← Chapter drafts, LaTeX tables
    ├── chapters/
    └── appendices/
```

**First action:** Create this repository on GitHub today. Tag an empty initial commit as `v0.0-structure`.

---

## ◈ THE EIGHT MARKET INDICES

Every property in the universe maps to one of these eight indices. Their return series drive the covariance matrix. Collecting the real return data for these is your primary research task in Week 1.

| Index Code | Name | Region | Asset Class | Primary Source |
|---|---|---|---|---|
| `LG_OFF_ISL` | Lagos Island Office | VI, Ikoyi, Marina | Office | Knight Frank Nigeria |
| `LG_RET_ISL` | Lagos Island Retail | VI, Lekki Phase 1 | Commercial/Retail | Knight Frank Nigeria |
| `LG_IND_MLN` | Lagos Mainland Industrial | Apapa, Oshodi, Ikeja Ind. | Industrial | CBN; Broll Nigeria |
| `LG_RES_PRM` | Lagos Premium Residential | Ikoyi, VI, Lekki Phase 1 | Residential | Knight Frank; CBRE |
| `AB_OFF_CEN` | Abuja Central Office | Maitama, Asokoro, Wuse II | Office | CBRE Abuja |
| `AB_RET_CEN` | Abuja Central Retail | Wuse II, Garki, Jabi | Commercial/Retail | NIESV Abuja |
| `PH_COM_OIL` | Port Harcourt Commercial | GRA, Rumuola, Trans Amadi | Mixed | CBRE Rivers |
| `KN_IND_NTH` | Kano Industrial North | Bompai, Sharada | Industrial | CBN Northern; NIESV Kano |

**For each index, you need:** annual total return (capital appreciation + rental yield) for each year 2018–2024, decomposed into components where available. Years not found in published sources: flag `is_simulated = TRUE` and backfill using GBM with documented μ and σ. Minimum coverage: 2021–2024 from documented sources for at least 6 of 8 indices.

---

---

# PHASE 1 — IMMEDIATE ACTIONS
## Questionnaire Distribution + Secondary Market Data Research
### Weeks 1–2 · Target completion: May 10, 2026

---

### TASK 1.1 — Create the Google Form

**Dependency:** None. Start today.  
**Time estimate:** 3 hours  
**Acceptance:** Form live and tested on mobile; all branching logic works; cover page displays correctly

- [ ] Open Google Forms. Create a new blank form.
- [ ] Set title: *Heuristics in Property Portfolio Selection — Pension Fund Administrators Survey*
- [ ] Set form description to the cover page text from the questionnaire instrument (the "Dear Investment Professional" paragraph, the confidentiality notice, and the contact email)
- [ ] Add Section A — Respondent Profile (6 questions: A1–A6). Use "Multiple choice" for all; ensure A5 has the correct advisory/authority distinction.
- [ ] Add Section B — Property Selection Criteria (4 questions). B1 must use "Grid" format (rows = criteria, column = rank 1–8). B2–B4 use "Linear scale" (1–5).
- [ ] Add Section C — Investment Scenarios (4 questions: C1–C4). Each scenario text appears as the question description; the response is a "Linear scale" (1–5) with labelled endpoints.
- [ ] Add Section D — Decision Process (6 questions). D1, D1b, D3 use "Multiple choice". D2 uses "Linear scale" (1–5). D2b, D4 use "Checkboxes" (select all that apply).
- [ ] Add Section D Supplementary — Technology (3 questions: D4a–D4c). Add a section header stating these are not part of the dissertation analysis.
- [ ] Add an "Add section" divider between all lettered sections so they display cleanly.
- [ ] Set the response deadline notice in the form description: **Friday, 30 April 2026** → UPDATE to actual deadline.
- [ ] Insert your actual email address wherever `[researcher.email@oauife.edu.ng]` appears.
- [ ] Turn on "Collect email addresses" → NO (for anonymity).
- [ ] Turn on "Limit to 1 response" → NO (one Google account may be shared on a device).
- [ ] Preview the form on mobile. Confirm all questions render correctly on a small screen.
- [ ] Test-complete the form yourself to confirm all questions are captured in the response spreadsheet.
- [ ] Copy the shareable link.

---

### TASK 1.2 — Prepare Distribution Materials

**Dependency:** 1.1 complete  
**Time estimate:** 2 hours  
**Acceptance:** All seven CPFAs identified and mapped; outreach materials prepared per institution; father briefed; tracking spreadsheet ready

**Design note:** Only Closed Pension Fund Administrators (CPFAs) are licensed by PenCom to invest directly in real estate. There are seven active CPFAs as at Q1 2025. This study therefore adopts a **census design** — all seven institutions are targeted, not a sample. This is methodologically superior to sampling: it eliminates sampling error entirely. Within each CPFA, multiple senior investment staff are targeted (CIO, Head of Investments, Portfolio Manager, Senior Analysts), expanding the accessible respondent pool to an estimated 14–28 individuals. A supplementary tier of property investment advisors with documented CPFA mandates may also be included, weighted at 0.5 in composite score calculations.

- [ ] Identify all seven PenCom-licensed CPFAs from PenCom's public register. Confirm the complete list and record each institution's name, AUM tier (from public PenCom data), and headquarter city.
- [ ] For each CPFA, identify senior investment staff by name and role using LinkedIn and public annual report disclosures. Record in the tracking spreadsheet: Institution, Respondent name, Role, Contact channel, Outreach date, Response received (Y/N), A5 classification.
- [ ] Determine which CPFAs have active direct real estate portfolios from PenCom quarterly asset allocation disclosures. Flag those without active real estate exposure — their responses are still valid (they reveal stated heuristics and institutional constraints) but will be noted as "stated-preference" respondents in Chapter 4.
- [ ] Brief your father on the CPFA-specific outreach. Give him this exact forwarding text verbatim:

> *"My son is completing his dissertation at OAU on how pension fund managers make real estate investment decisions. He's specifically looking for input from Closed Pension Fund Administrators — only CPFAs can invest directly in property under PenCom rules, so their perspective is uniquely important. He needs 12 minutes from senior investment staff. Completely confidential, no commercial purpose. I'd appreciate any help you can give him with introductions."*

- [ ] Draft personalised LinkedIn outreach messages for each identified investment staff member. Personalise per institution — reference the fund by name, not generically. Keep under 100 words per message.
- [ ] Draft an email to PenOp secretariat explaining the CPFA-specific focus and requesting facilitation with their member institutions.
- [ ] Identify 3–5 property investment advisors (estate surveyors, real estate fund managers) who have worked on documented CPFA mandates. These form the supplementary tier. Note: they must have direct professional experience advising CPFAs on property acquisition decisions, not just general institutional investment knowledge.
- [ ] Set up response tracking spreadsheet with columns: Respondent ID, Institution (anonymised as CPFA-1 through CPFA-7), Respondent tier (Primary / Supplementary), Date received, A5 classification (A/B/C), Composite weight (1.0 / 0.7 / 0.5), Usable (Y/N), Notes.

---

### TASK 1.3 — Distribute Questionnaire

**Dependency:** 1.1 and 1.2 complete  
**Time estimate:** 1 hour (distribution) + ongoing monitoring  
**Acceptance:** Form link sent to all identified investment staff across all seven CPFAs; supplementary tier contacted; father's outreach initiated; every contact logged

- [ ] Send form link to all investment staff identified across the seven CPFAs via LinkedIn direct message (personalised per person, not bulk).
- [ ] Send form link to supplementary tier (property advisors with CPFA mandates).
- [ ] Activate father's PFC network outreach for warm introductions to CPFA investment teams.
- [ ] Send PenOp secretariat email.
- [ ] Log every outreach contact in the tracking spreadsheet with date sent.
- [ ] Set response collection deadline at **3 weeks from distribution date**.
- [ ] Set a calendar reminder for Day 10: send one warm follow-up to all non-respondents who received warm introductions (WhatsApp or LinkedIn message — not another form link email).
- [ ] On deadline day: record final response count by tier (primary CPFA staff / supplementary advisors) and by A5 classification. This count determines which analysis path is followed in Phase 3.

**Response outcome handling:**

| Outcome | Path |
|---|---|
| ≥ 10 usable primary responses (A5 = A or B) | Standard analysis — Formulas 3.1–3.6 as designed |
| 5–9 usable primary responses | Census partial coverage — compute α weights with explicit coverage caveat; supplement with literature-derived baseline weights for comparison |
| < 5 usable primary responses | Literature-derived α weights as primary; questionnaire findings reported descriptively only; Objective I reframed as expert validation rather than empirical measurement |
| 0 usable responses | Equal-weighted α = [0.25, 0.25, 0.25, 0.25]; full disclosure in Chapter 3 and Chapter 4 |

---

### TASK 1.4 — Secondary Market Data Research

**Dependency:** None. Run parallel with 1.1–1.3.  
**Time estimate:** 10–12 hours over two weeks  
**Acceptance:** Calibration spreadsheet populated with ≥ 6 years of documented returns for each of the 8 indices; every data point has a citation; `is_simulated` flag assigned to GBM-backfilled years

This is your primary data collection task. For each of the 8 market indices, collect annual total return data (capital appreciation % + rental yield %) for each year 2018–2024. Work through the sources in this priority order:

**Source 1 — Knight Frank Nigeria** (knightfrank.com.ng)
- [ ] Download: Knight Frank Nigeria Prime Office Report (latest available, 2023–2024)
- [ ] Download: Knight Frank Nigeria Residential Report (2022–2024)
- [ ] Extract: rental growth %, capital value change %, yield ranges by submarket
- [ ] Target indices: `LG_OFF_ISL`, `LG_RET_ISL`, `LG_RES_PRM`, `AB_OFF_CEN`

**Source 2 — CBRE Nigeria** (cbre.com.ng)
- [ ] Download: CBRE Nigeria Office Market Report (2022–2023)
- [ ] Download: CBRE Nigeria Market Outlook (most recent available)
- [ ] Target indices: `AB_OFF_CEN`, `AB_RET_CEN`, `PH_COM_OIL`

**Source 3 — NBS Real Estate Sector Reports** (nigerianstat.gov.ng)
- [ ] Download: NBS Real Estate Sector GDP contribution reports (2018–2024)
- [ ] Extract: sectoral growth rates as proxy for capital appreciation
- [ ] Covers: all indices (broad market context)

**Source 4 — CBN Statistical Bulletins** (cbn.gov.ng)
- [ ] Download: CBN Statistical Bulletin, most recent edition
- [ ] Extract: Real estate credit growth, MPR history, inflation series 2018–2024
- [ ] Target indices: `LG_IND_MLN`, `KN_IND_NTH` (less covered by commercial reports)

**Source 5 — PenCom Annual Reports** (pencom.gov.ng)
- [ ] Download: PenCom Annual Reports 2020–2024
- [ ] Extract: Real estate allocation data, any return benchmarks cited
- [ ] Use as contextual validation

**Source 6 — Estate Intel** (estateintell.co)
- [ ] Check for any freely available quarterly market reports
- [ ] If available, extract submarket rental rates and occupancy data
- [ ] Target indices: `LG_OFF_ISL`, `LG_RET_ISL`

**Source 7 — NIESV publications**
- [ ] Contact OAU Department of Estate Management for any NIESV Kano or Abuja chapter data
- [ ] Target indices: `AB_RET_CEN`, `KN_IND_NTH`

**After collection — data organisation:**
- [ ] Create `data/calibration/market_index_returns.csv` with columns: `index_code`, `year`, `annual_return`, `capital_apprc`, `rental_yield`, `data_source`, `is_simulated`
- [ ] For each year where no primary source data was found: calculate GBM backfill using `annual_return = μ + σ * ε` where μ and σ are derived from the available years; set `is_simulated = TRUE`
- [ ] Document every calibration assumption in `data/calibration/calibration_notes.md`
- [ ] Produce the "Starter Calibration Values" table from the Generator v1 document, updated with your actual collected figures

---

---

# PHASE 2 — PROPERTY UNIVERSE GENERATOR
## Build, Calibrate, Validate, and Freeze the Universe
### Weeks 2–3 · Target completion: May 18, 2026

---

### TASK 2.1 — Repository Initialisation

**Dependency:** None  
**Time estimate:** 1 hour  
**Acceptance:** Monorepo exists on GitHub; directory structure is in place; `README.md` explains the project

- [ ] Create GitHub repository: `pfa-portfolio-research`
- [ ] Clone locally
- [ ] Create the full directory structure shown in the Monorepo Structure section above
- [ ] Create `README.md` at the root with: project title, research context, tech stack, how to run each package
- [ ] Create `.gitignore` (exclude: `__pycache__/`, `*.pyc`, `.env`, `node_modules/`, `target/`, `*.class`)
- [ ] Initial commit: `git commit -m "chore: initialise monorepo structure"`
- [ ] Tag: `git tag v0.0-structure`

---

### TASK 2.2 — `config.py` — Calibration Parameters

**Dependency:** 1.4 (market data collection) at minimum partially complete  
**Time estimate:** 3 hours  
**Acceptance:** `config.py` contains all calibration parameters; every parameter has an inline comment citing its source; SEED = 42 is set and commented as immutable

- [ ] Create `packages/generator/config.py`
- [ ] Define `SEED = 42` at the top, with comment: `# DO NOT CHANGE — frozen after first generation`
- [ ] Define `PENCOM_CONSTRAINTS` dict (max 5% single property, max 30% total real estate, min 2 states, min 7-year commercial leases)
- [ ] Define `TRANSACTION_COSTS` dict (agency 5%, legal 5%, Gov Consent: Lagos 10%, others 5%)
- [ ] Define `RISK_FREE_RATE = 0.15` with source citation in comment
- [ ] Define `TITLE_RISK_PREMIUMS` dict per specification (C of O = 0.000, Gov Consent = 0.005, Gazette = 0.030, Excision = 0.050, Deed only = 0.020)
- [ ] Define `CONDITION_RISK_PREMIUMS` dict (New = 0.000, Good = 0.005, Fair = 0.015, Needs Renovation = 0.030)
- [ ] Define `VACANCY_RATES` nested dict (asset type → condition → vacancy %)
- [ ] Define `MAINTENANCE_RATES` dict (by asset type)
- [ ] Define `GROSS_YIELD_PARAMS` nested dict (asset type → location tier → {mean, std})
- [ ] Define `PRICE_DISTRIBUTIONS` nested dict (state → tier → asset type → {log_mean, log_sigma, floor_ngn, ceiling_ngn})
- [ ] Populate all values from your collected market data (Task 1.4); use the Generator v1 starter values where primary data was not collected
- [ ] Define `CALIBRATION_SOURCES` multi-line string at the top listing every source used, with dates

---

### TASK 2.3 — `generate_universe.py` — Core Generator

**Dependency:** 2.2 complete  
**Time estimate:** 8 hours  
**Acceptance:** Script runs without errors; produces a DataFrame of 80 properties; all required columns present; all values within expected ranges; `generation_config` record saved

- [ ] Create `packages/generator/generate_universe.py`
- [ ] Import: `numpy`, `pandas`, `uuid`, `config`
- [ ] Set `numpy.random.seed(SEED)` at script initialization
- [ ] Implement `_sample_geography_allocation(n=80)` → returns list of (state, lga, micro, tier) tuples matching the geographic distribution from Generator v1 spec (Lagos Island 25%, Lagos Mainland 15%, Abuja 20%, Rivers 18%, Kano 12%, Oyo 10%)
- [ ] Implement `_sample_asset_type(state, tier)` → samples from the asset type distribution (Office 28%, Commercial 22%, Industrial 18%, Residential 20%, Mixed-Use 12%) with state-appropriate biases
- [ ] Implement `_sample_price(state, tier, asset_type, floor_area)` → log-normal with resample (NOT clamp) until within floor/ceiling bounds
- [ ] Implement `_sample_gross_yield(asset_type, tier, condition)` → normal distribution clipped to [0.04, 0.14]
- [ ] Implement `_sample_title_status()` → categorical: C of O 45%, Gov Consent 25%, Gazette 15%, Excision 10%, Deed 5%
- [ ] Implement `_sample_condition()` → New 20%, Good 50%, Fair 20%, Needs Renovation 10%
- [ ] Implement `_sample_occupancy(asset_type, condition)` → from vacancy rate tables
- [ ] Implement `_assign_market_index(state, lga, asset_type, tier)` → maps to one of the 8 index codes
- [ ] Compute heuristic trigger flags: `is_prime_location`, `is_preferred_asset_type`, `triggers_anchoring_rule` (price > ₦800M), `is_heuristic_eligible` (C of O or Gov Consent AND Good or New AND not anchoring trigger)
- [ ] Compute `pencom_lease_compliant` flag (for commercial: lease_term_years ≥ 7; for non-commercial: always TRUE)
- [ ] Assemble each property record as a dict; collect all 80 records into a DataFrame
- [ ] Write `generation_config` to a JSON file: `{seed: 42, n: 80, timestamp: now, calibration_hash: md5(config)}`

---

### TASK 2.4 — `metrics_calculator.py` — Financial Metrics

**Dependency:** 2.3 complete  
**Time estimate:** 4 hours  
**Acceptance:** All six financial metrics computed correctly for every property; unit tests pass for each formula

Implements Formulas from Chapter 3. For each property:

- [ ] `total_acquisition_cost` = asking price + agency fee (5%) + legal fee (5%) + gov consent fee (10% Lagos / 5% others)
- [ ] `effective_rent` = estimated annual rent × (1 − vacancy_rate)
- [ ] `maintenance_cost` = estimated annual rent × maintenance_rate
- [ ] `noi` = effective_rent − maintenance_cost
- [ ] `cap_rate` = noi / total_acquisition_cost
- [ ] `expected_return` = cap_rate + mean capital appreciation of assigned market index
- [ ] `total_volatility` = index_volatility + title_risk_premium + condition_risk_premium
- [ ] `sharpe_ratio` = (expected_return − RISK_FREE_RATE) / total_volatility

- [ ] Write `compute_property_metrics(prop_dict, index_returns_dict, config)` function
- [ ] Write unit tests: 3 hand-calculated properties; verify all 8 outputs match manual calculations
- [ ] Run on full 80-property DataFrame; append all metrics columns

---

### TASK 2.5 — `validate_universe.py` — Statistical Validation

**Dependency:** 2.4 complete  
**Time estimate:** 4 hours  
**Acceptance:** All 9 validation tests pass; validation report and all 4 figures saved; report is dissertation-appendix quality

- [ ] **Test 1:** Log-normality of prices — KS test on log(asking_price). Pass condition: p > 0.05
- [ ] **Test 2:** Price skewness — mean > median (right-tailed distribution). Pass: TRUE
- [ ] **Test 3:** Gross yield range — all values within [4%, 14%]. Pass: TRUE
- [ ] **Test 4:** State count ≥ 5. Pass: TRUE
- [ ] **Test 5:** Lagos share < 70%. Pass: TRUE
- [ ] **Test 6:** Sub-optimal title % ∈ [20%, 40%]. Pass: TRUE
- [ ] **Test 7:** Covariance matrix PSD — minimum eigenvalue ≥ −1e-10. Pass: TRUE
- [ ] **Test 8:** Heuristic-eligible count ≥ 25. Pass: TRUE
- [ ] **Test 9:** All properties have valid market_index_id (no nulls). Pass: TRUE

- [ ] Generate Q-Q plot of log-transformed prices (save as `outputs/validation/qqplot_prices.png`, 300 DPI)
- [ ] Generate geographic distribution pie chart (`geo_distribution.png`)
- [ ] Generate asset type distribution bar chart (`asset_type_distribution.png`)
- [ ] Generate covariance matrix heatmap — sample 30 properties (`covariance_heatmap.png`)
- [ ] Print validation report to `outputs/validation/validation_report.txt` in the table format shown in Generator v1 document (pass/fail per test; summary statistics)
- [ ] This report becomes Appendix [X] Table in the dissertation

---

### TASK 2.6 — CSV Export and Universe Freeze

**Dependency:** 2.5 — ALL tests must pass before freeze  
**Time estimate:** 1 hour  
**Acceptance:** Three frozen CSV files in `data/frozen/`; git tag applied; data directory is read-only from this point

- [ ] Export `data/frozen/property_universe.csv` — all 80 properties, all columns, in the column order specified by Generator v1 Section 5.8
- [ ] Export `data/frozen/market_indices_returns.csv` — wide format (year as row index, index codes as columns), annual returns as decimals
- [ ] Export `data/frozen/covariance_matrix.csv` — 8×8 matrix with index codes as row/column headers
- [ ] Commit all three files: `git commit -m "data: freeze property universe v1.0 (seed=42, n=80)"`
- [ ] Tag: `git tag v1.0-frozen-universe`
- [ ] **UNIVERSE IS NOW FROZEN.** No changes to these files permitted for any reason. All subsequent pipeline steps read from these files.

---

---

# PHASE 3 — QUESTIONNAIRE ANALYSIS
## Process Survey Responses and Derive α Weights
### Week 4 · Target completion: May 25, 2026

*This phase runs when questionnaire responses have closed (approximately 3 weeks after distribution). If responses are still coming in, begin Phase 4 in parallel.*

---

### TASK 3.1 — Data Export and Cleaning

**Dependency:** Questionnaire response window closed  
**Time estimate:** 3 hours  
**Acceptance:** Clean CSV in `data/questionnaire/cleaned_responses.csv`; exclusion log documented; A5 weights and tier weights assigned; analysis path selected based on final response count

- [ ] Export Google Forms responses to Google Sheets, then to `data/questionnaire/raw_responses.csv`
- [ ] Rename all columns to short codes: A1, A2, A3, A4, A5, A6, B1_loc, B1_title, B1_yield, B1_tenant, B1_cond, B1_peer, B1_valuer, B1_liq, B2, B3, B4, C1, C2, C3, C4, D1, D1b, D2, D2b_1...D2b_9, D3, D4_1...D4_9, D4a, D4b_1...D4b_8, D4c
- [ ] Apply exclusion criteria in order: (1) A5 = C → exclude entirely; (2) Any C1–C4 blank → exclude from composite score calculations; (3) Invalid B1 (duplicate ranks) → exclude B1 from that respondent; (4) Completion time < 5 minutes AND > 25% items missing → exclude
- [ ] Document each exclusion with reason in `data/questionnaire/exclusion_log.csv`
- [ ] Assign composite weights per respondent:
  - Primary CPFA staff, A5 = A → weight = 1.0
  - Primary CPFA staff, A5 = B → weight = 0.7
  - Supplementary advisors, A5 = A → weight = 0.5
  - Supplementary advisors, A5 = B → weight = 0.35
  - A5 = C → excluded
- [ ] Normalise all B and C inputs to [0, 1] scale: B2–B4 and C1–C4 → `(raw − 1) / 4`; B1 rank inversions → `(8 − rank) / 7`
- [ ] Count final usable responses by tier. Select analysis path from the table in Task 1.3 and record the selected path in `data/questionnaire/analysis_path.txt`
- [ ] Save cleaned, normalised data as `data/questionnaire/cleaned_responses.csv`

---

### TASK 3.2 — Compute Heuristic Composite Scores (Formulas 3.1–3.4)

**Dependency:** 3.1 complete  
**Time estimate:** 3 hours  
**Acceptance:** Four composite scores computed per respondent; mean H̄_j and BCa 95% CIs computed for each heuristic; α weights derived and saved; literature-derived baseline weights documented for comparison regardless of response count

**Note on small n:** Because the CPFA population is small by structural necessity, α weights are reported alongside literature-derived baseline weights drawn from Babawale (2013), Ogunba (2013), and the herding literature. These baselines serve two purposes: (1) they give the examiner a reference point for whether survey-derived weights are plausible; (2) if the response count is very low, they serve as the primary calibration source with survey responses treated as validation. Document both sets of weights in `data/questionnaire/alpha_weights.json` under keys `survey_derived` and `literature_baseline`.

Per Companion Guide Sections 7 and 8:

- [ ] **Formula 3.1 — ACS_k:** `0.4 × B3_k + 0.6 × C1_k`
- [ ] **Formula 3.2 — AVCS_k:** `0.3 × B1_loc_k + 0.3 × B2_k + 0.4 × C2_k`
- [ ] **Formula 3.3 — RCS_k:** `0.4 × B1_sector_k + 0.6 × C3_k` (B1_sector_k = inverted valuer recommendation rank)
- [ ] **Formula 3.4 — HCS_k:** `0.25 × B1_peer_k + 0.35 × B4_k + 0.40 × C4_k`
- [ ] Apply A5 weighting: weighted mean `H̄_j = Σ(w_k × H_jk) / Σ(w_k)` — **Formula 3.5**
- [ ] Compute BCa bootstrap 95% CIs around each H̄_j (10,000 replications of weighted mean)
- [ ] Classify each H̄_j: < 0.30 (not prevalent) / 0.30–0.49 (low) / 0.50–0.69 (moderate) / ≥ 0.70 (prevalent)
- [ ] **Formula 3.6 — α weights:** `α_j = H̄_j / (H̄_1 + H̄_2 + H̄_3 + H̄_4)`
- [ ] **Record α_1, α_2, α_3, α_4** — these are the calibration weights for Portfolio A. Write them to `data/questionnaire/alpha_weights.json`

---

### TASK 3.3 — Section D Analysis (Objective IV)

**Dependency:** 3.1 complete  
**Time estimate:** 2 hours  
**Acceptance:** Frequency tables for D1/D1b, D2/D2b, D3, D4 computed; COG/INF/INS/REG category totals computed; ecological rationality test comparison ready

- [ ] **D1/D1b:** Frequency table (governance structure). Cross-tabulate against HCS.
- [ ] **D2:** Mean severity score; proportion scoring ≥ 4.
- [ ] **D2b:** Item-level frequency table; identify top-3 most-selected data gaps.
- [ ] **D3:** Modal response — record which single change was most frequently selected. This drives Chapter 5 recommendations.
- [ ] **D4:** Item-level frequency table; aggregate into COG/INF/INS/REG category counts.
- [ ] **Ecological rationality test:** Classify respondents as INF-citing (selected D4 options B or H) vs. INF-non-citing. Compare mean AVCS and RCS between groups. Record the direction and magnitude of the difference.
- [ ] **Cross-tabulations:** Experience group vs. composite scores; fund size group vs. A6; role type vs. HCS.

---

### TASK 3.4 — Stated vs. Revealed Preference Gap

**Dependency:** 3.2 complete  
**Time estimate:** 1 hour  
**Acceptance:** Gap scores computed for all three paired heuristics; direction and magnitude recorded

- [ ] Anchoring gap: `C1_k − B3_k` per respondent → mean gap
- [ ] Availability gap: `C2_k − B2_k` per respondent → mean gap
- [ ] Herding gap: `C4_k − B4_k` per respondent → mean gap
- [ ] Interpret: positive gap = scenario reveals more heuristic-consistency than stated belief (expected per behavioural finance literature)

---

---

# PHASE 4 — COMPUTATIONAL PIPELINE
## Heuristic Engine + MVO Optimizer + Monte Carlo Simulation
### Weeks 3–5 (run parallel with Phase 3) · Target completion: June 1, 2026

*This phase can begin as soon as the frozen universe is in place (Phase 2 complete). The α weights from Phase 3 are injected once available, before the final portfolio generation run.*

---

### TASK 4.1 — Heuristic Engine (`heuristic_engine.py`)

**Dependency:** Frozen universe (2.6 complete)  
**Time estimate:** 6 hours  
**Acceptance:** Engine produces a valid heuristic portfolio; all PENCOM constraints respected; property selection and scores logged

- [ ] Create `packages/optimizer/heuristic_engine.py`
- [ ] Implement **Stage 1 — Hard Filters** (boolean exclusions, applied in this order):
  - F1: `pencom_lease_compliant == TRUE` (commercial properties with lease < 7 years excluded)
  - F2: Title Quality — `title_status ∈ {C_OF_O, GOVERNORS_CONSENT}` (calibrated from B3 survey result; adjust to scoring if B3 mean < 0.5)
  - F3: Location Prestige — prime and secondary tiers only (calibrated from AVCS result)
  - F4: Condition — `property_condition ∈ {NEW, GOOD}` (unless survey shows weak condition filter)
- [ ] Implement **Stage 2 — Composite Scoring** (Formula 3.15):
  - `H(p_i) = α_1 × TS(p_i) + α_2 × LS(p_i) + α_3 × MS(p_i) + α_4 × PS(p_i)`
  - `TS(p_i)` (Title Score): C of O = 1.0, Gov Consent = 0.7
  - `LS(p_i)` (Location Score): Prime = 1.0, Secondary = 0.6, Emerging = 0.2
  - `MS(p_i)` (Momentum Score): normalised market index mean return over prior 3 years, relative to all indices
  - `PS(p_i)` (Peer Score): 1.0 if index is one of the top-2 most-invested indices in PenCom aggregate data; 0 otherwise
  - α weights come from `alpha_weights.json` (Phase 3 output); use placeholder values `[0.25, 0.25, 0.25, 0.25]` until survey data is available
- [ ] Implement **Stage 3 — Greedy Allocation**:
  - Sort surviving properties by `H(p_i)` descending
  - Allocate greedily: for each property in order, if `total_acquisition_cost ≤ remaining_budget` AND `allocation_weight ≤ 5% of fund`: add to portfolio
  - Repeat until budget exhausted or no eligible properties remain
- [ ] Validate PENCOM constraints post-selection: ≥ 2 states, all commercial leases ≥ 7 years
- [ ] Log each stage: properties remaining after F1, F2, F3, F4; final composite scores; final selection and weights
- [ ] Output Portfolio A to `outputs/portfolios/portfolio_A_heuristic.json`

---

### TASK 4.2 — Covariance Matrix Module (`covariance.py`)

**Dependency:** Frozen universe (2.6 complete)  
**Time estimate:** 3 hours  
**Acceptance:** 80×80 property-level covariance matrix produced; positive semi-definite check passes; Ledoit-Wolf applied if needed

- [ ] Create `packages/optimizer/covariance.py`
- [ ] Load `data/frozen/market_indices_returns.csv`
- [ ] Pivot to wide format (year × index) and compute 8×8 index covariance matrix using `pandas.DataFrame.cov()`
- [ ] For each property pair (i, j):
  - Diagonal (i = j): `index_variance + title_premium² + condition_premium²`
  - Off-diagonal (i ≠ j): `index_covariance[index_i, index_j]` (inherited from market index pair)
- [ ] Check PSD: `min(np.linalg.eigvals(cov_matrix)) ≥ -1e-10`
- [ ] If not PSD: apply Ledoit-Wolf shrinkage via `sklearn.covariance.LedoitWolf`; re-check; log warning
- [ ] Export `data/frozen/property_covariance_matrix.csv` (80×80, property codes as row/column headers)

---

### TASK 4.3 — MVO Optimizer (`mvo_optimizer.py`)

**Dependency:** 4.2 complete; frozen universe in place  
**Time estimate:** 8 hours  
**Acceptance:** Produces Portfolio B with higher Sharpe ratio than Portfolio A; all PENCOM constraints satisfied; optimization log saved

- [ ] Create `packages/optimizer/mvo_optimizer.py`
- [ ] Load property universe, financial metrics, and covariance matrix from frozen data
- [ ] Build expected return vector (μ) from `expected_return` field of each property
- [ ] Implement Sharpe-maximizing objective using **Binary Integer Programming** via `PuLP` with CBC solver:
  - Decision variables: `x_i ∈ {0, 1}` for each of 80 properties
  - Objective: maximize `(μ'w − Rf) / sqrt(w'Σw)` — approximate linearization via target return constraint
  - Constraint 1: Budget — `Σ(x_i × TAC_i) ≤ ₦10,000,000,000`
  - Constraint 2: Max single property — `x_i × TAC_i ≤ 0.05 × fund_size`
  - Constraint 3: Min states — `Σ_states (any x_i in state ≥ 1) ≥ 2`
  - Constraint 4: Commercial lease — all selected commercial properties must have `lease_term_years ≥ 7`
  - Constraint 5: Non-negativity — `x_i ≥ 0`
- [ ] Set solver time limit: 300 seconds. Accept best feasible solution found within limit.
- [ ] If solver returns infeasible: relax cardinality by ±2 and re-run; document in methodology
- [ ] Equal-weight selected properties: `w_i = 1 / n_selected` for each selected property `i`
- [ ] Calculate portfolio metrics: expected return, volatility, Sharpe ratio
- [ ] Output Portfolio B to `outputs/portfolios/portfolio_B_optimized.json`
- [ ] Log: number of properties considered, selected, objective value, solver status

---

### TASK 4.4 — Monte Carlo Simulation Engine (`monte_carlo.py`)

**Dependency:** 4.1 and 4.3 complete (both portfolios constructed)  
**Time estimate:** 6 hours  
**Acceptance:** 10,000 × 60-month simulation paths generated for both portfolios; final value distributions saved; all six performance metrics computed

- [ ] Create `packages/optimizer/monte_carlo.py`
- [ ] Set `numpy.random.seed(42)` at initialization
- [ ] For each portfolio (A and B), implement the GBM simulation:
  - Initialize: `V_0 = ₦10,000,000,000`
  - At each month `t` (60 months total):
    - Generate standard normal shocks `z ~ N(0, I_n)`
    - Apply Cholesky decomposition: `ε = L @ z` where `L = cholesky(Σ_monthly)`
    - Monthly return: `R_monthly = μ_monthly + ε` where `μ_monthly = expected_return / 12`
    - Portfolio return: `R_p = w' @ R_monthly`
    - Update value: `V_t = V_{t-1} × (1 + R_p)`
  - Record `V_t` for all 60 months (for path visualization)
  - Record final value `V_60`
- [ ] Run 10,000 simulations for each portfolio. Store final values as arrays.
- [ ] Save first 100 paths per portfolio for visualization (don't store all 10,000 full paths — memory)
- [ ] Export: `outputs/simulation_results/portfolio_A_paths.npy` and `portfolio_B_paths.npy`

---

### TASK 4.5 — Performance Metrics and Statistical Tests (`statistical_tests.py`)

**Dependency:** 4.4 complete  
**Time estimate:** 4 hours  
**Acceptance:** All six metrics (M1–M6) computed for both portfolios; hypothesis test results recorded; all outputs in `outputs/simulation_results/`

Compute for each portfolio across the 10,000 simulation paths:

- [ ] **M1 — Sharpe Ratio (SR):** `(CAGR − 0.15) / σ_annual`
- [ ] **M2 — CAGR:** `(V_60 / V_0)^(1/5) − 1`
- [ ] **M3 — Annualised Volatility:** `std(monthly_returns) × sqrt(12)`
- [ ] **M4 — Maximum Drawdown (MDD):** `max[(V_peak − V_trough) / V_peak]` across each path; take mean MDD across paths
- [ ] **M5 — CVaR 95%:** mean of the worst 5% of final values (expressed as return)
- [ ] **M6 — Diversification Ratio:** `(Σ w_i × σ_i) / σ_portfolio`

**Hypothesis tests:**
- [ ] **H₁ (Sharpe):** Paired t-test on distribution of SR differences across 10,000 paths. Report: t-statistic, p-value (one-tailed), Cohen's d.
- [ ] **H₂ (Diversification):** Compare Herfindahl Index (Σ w_i²) geographic HHI and asset-type HHI between portfolios.
- [ ] **H₃ (Market conditions):** Partition 10,000 paths into terciles by simulated market volatility. Compare ΔSR across low/medium/high volatility groups.

**BCa Bootstrap:**
- [ ] For ΔSR = SR_B − SR_A: compute BCa 95% CI using block bootstrap (block length = 6 months, 10,000 replications)
- [ ] Record whether ΔSR CI excludes zero (statistical significance) AND whether ΔSR ≥ 0.05 (practical significance)

**Sensitivity analysis:**
- [ ] Re-run metrics with Rf = 0.10, 0.15, 0.20 (the frozen value is 0.15; others are sensitivity checks)

- [ ] Save all results to `outputs/simulation_results/summary_metrics.json`

---

### TASK 4.6 — Generate All Charts and Tables

**Dependency:** 4.5 complete  
**Time estimate:** 5 hours  
**Acceptance:** All figures saved as high-resolution PNG/PDF; all LaTeX tables generated in `outputs/tables/`; all figures are dissertation-quality (300 DPI, serif font, clear labels)

**Figures:**
- [ ] **Figure 4.1:** Efficient frontier scatter with Portfolio A and B positions marked
- [ ] **Figure 4.2:** Distribution of Sharpe ratios — overlapping histograms (Portfolio A in blue, B in green)
- [ ] **Figure 4.3:** Monte Carlo paths — 100 representative paths per portfolio, facet-plotted
- [ ] **Figure 4.4:** Geographic allocation pie charts — side by side (Portfolio A vs. B)
- [ ] **Figure 4.5:** Asset type allocation bar charts — side by side
- [ ] **Figure 4.6:** Stress scenario performance bar chart (market condition sub-analysis)
- [ ] **Figure 4.7:** Heuristic composite scores radar chart (H̄_1 through H̄_4 with CIs)
- [ ] **Figure 4.8:** Stated vs. revealed preference gap — paired bar chart

**Tables (LaTeX format for direct dissertation inclusion):**
- [ ] **Table 4.1:** Respondent profile summary (Section A frequencies)
- [ ] **Table 4.2:** Heuristic composite scores, 95% CIs, classification, α weights
- [ ] **Table 4.3:** B1 median ranks — all 8 criteria, including proportion ranking top-3
- [ ] **Table 4.4:** D4 factor frequencies by item and by COG/INF/INS/REG category
- [ ] **Table 4.5:** Portfolio composition comparison (n properties, states, asset types, Herfindahl)
- [ ] **Table 4.6:** Performance metrics M1–M6 — side by side with difference column and p-values
- [ ] **Table 4.7:** Stress scenario results (low/medium/high volatility ΔSR)
- [ ] **Table 4.8:** Sensitivity analysis (Rf = 0.10 / 0.15 / 0.20)

Set these matplotlib parameters for all figures:
```python
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
```
Save all figures to `outputs/charts/` at 300 DPI.  
Save all LaTeX tables to `outputs/tables/` as `.tex` files.

---

---

# PHASE 5 — JAVA RESEARCH BACKEND
## Spring Boot API Layer for Data Persistence and Query
### Week 5–6 · Target completion: June 8, 2026

*This phase builds the Java backend described in the TDD. It is required by the PFA-Simulator frontend (Phase 7) and by the dissertation's demonstration of a complete system. It is NOT required for the core academic analysis (Phases 2–4 are sufficient for Chapters 4 and 5).*

---

### TASK 5.1 — Spring Boot Project Initialisation

**Dependency:** None (can begin any time after monorepo is set up)  
**Time estimate:** 2 hours

- [ ] Navigate to `packages/research-backend/`
- [ ] Use Spring Initializr (start.spring.io): Java 17, Maven, Spring Boot 3.2, Dependencies: Spring Web, Spring Data JPA, PostgreSQL Driver, Lombok, Validation, SpringDoc OpenAPI
- [ ] Unzip into `packages/research-backend/`
- [ ] Configure `application.yml`: datasource URL, JPA settings, Flyway migrations, optimization service URL
- [ ] Create `V1__initial_schema.sql` in `src/main/resources/db/migration/` (schema from TDD Section 2.2)
- [ ] Confirm application starts: `mvn spring-boot:run`

---

### TASK 5.2 — Entity Classes and Repository Layer

**Dependency:** 5.1 complete  
**Time estimate:** 4 hours

- [ ] Create entity classes: `Property.java`, `Portfolio.java`, `PortfolioHolding.java`, `MarketIndex.java`, `HistoricalReturn.java`
- [ ] Annotate with `@Entity`, `@Table`, `@Id`, `@GeneratedValue`, `@Column`, `@ManyToOne`, `@OneToMany`
- [ ] Create repository interfaces extending `JpaRepository`
- [ ] Write data loader class that imports `property_universe.csv` from the frozen data directory on application startup (if database is empty)

---

### TASK 5.3 — REST Controllers and Service Layer

**Dependency:** 5.2 complete  
**Time estimate:** 6 hours

- [ ] `PropertyController` — GET /api/properties (with pagination and filtering by asset type, state, title), GET /api/properties/{id}
- [ ] `PortfolioController` — POST /api/portfolios/heuristic, POST /api/portfolios/algorithmic, GET /api/portfolios/{id}, GET /api/portfolios/compare
- [ ] `MarketDataController` — GET /api/indices, GET /api/indices/{code}/returns
- [ ] `AnalysisController` — POST /api/portfolios/{id}/simulate (calls Python FastAPI service)
- [ ] `HeuristicEngineService` — implements greedy allocation logic in Java (mirrors Python engine; results must be identical for the same α weights)
- [ ] `OptimizationClientService` — REST client calling the Python FastAPI optimizer

---

### TASK 5.4 — Docker Compose Setup

**Dependency:** 5.1 complete  
**Time estimate:** 1 hour

- [ ] Create `docker-compose.yml` at monorepo root with: `postgres` service, `research-backend` service, `optimizer` service
- [ ] Confirm `docker-compose up` starts all three services without errors
- [ ] Confirm Java backend can reach PostgreSQL; confirm Java backend can reach Python optimizer at port 8000

---

---

# PHASE 6 — DISSERTATION WRITING
## Chapters 4 and 5 + Final Chapter Polish
### Weeks 7–9 · Target completion: June 29, 2026

---

### TASK 6.1 — Chapter 4: Results and Analysis

**Dependency:** All Phase 4 outputs (charts, tables, simulation results) complete  
**Time estimate:** 14–16 hours  
**Target length:** 18–22 pages  
**Acceptance:** All four research objectives addressed with quantitative findings; every table and figure referenced in text; all metrics defined before use; written in past tense

Work through the Chapter 4 structure from the Companion Guide Section 12.1 in order:

- [x] **4.1 Introduction** — restate aim and four objectives; briefly explain the analytical sequence (survey → universe → portfolios → simulation)
- [x] **4.2 Respondent Profile** — Table 4.1 (sample descriptive statistics); A5 weight distribution; A6 (quantitative model use) as the anchor statistic for Objective IV
- [x] **4.3 Stated Selection Criteria** — Table 4.3 (B1 median ranks); B2–B4 mean scores and agreement frequencies; discuss the priority ordering: which heuristic-associated criteria outrank financial criteria in stated preferences
- [x] **4.4 Revealed Heuristic Tendencies** — Table 4.5 (C1–C4 descriptive stats); scenario-by-scenario interpretation; the stated-revealed preference gap for each heuristic (Figure 4.8)
- [x] **4.5 Heuristic Composite Scores and α Weights** — Table 4.2 (H̄_j, CIs, classification, α weights); the critical transitional paragraph linking α weights to Portfolio A construction: *"These empirically calibrated weights — α_1 = X.XX, α_2 = X.XX, α_3 = X.XX, α_4 = X.XX — were substituted into the heuristic scoring function (Formula 3.15) as the pre-registered parameters for Portfolio A's construction."*
- [x] **4.6 Factors Driving Heuristic Use (Objective IV)** — Table 4.7 (D1/D1b governance); Table 4.8 (D2 severity, D2b specific gaps); Table 4.9 (D3 modal preferred change); Table 4.10 (D4 by item and by COG/INF/INS/REG); ecological rationality test results; cross-tabulation findings
- [x] **4.7 Portfolio Construction Outcomes** — Properties selected into each portfolio; composition comparison (Table 4.5); geographic allocation (Figure 4.4); asset type allocation (Figure 4.5); Herfindahl indices
- [x] **4.8 Monte Carlo Simulation Results** — Table 4.6 (M1–M6 side by side); Figure 4.2 (Sharpe distribution); Figure 4.3 (representative paths); percentile comparison
- [x] **4.9 Statistical Tests** — State H₁, H₂, H₃ formally; report t-statistics, p-values, Cohen's d; BCa CI for ΔSR; state plainly whether each hypothesis is supported; market condition sub-analysis (Table 4.7); sensitivity analysis under three Rf values (Table 4.8)
- [x] **4.10 Chapter Summary** — Four-paragraph summary, one per objective

**Writing conventions for Chapter 4:**
- Every metric is defined before it is reported (e.g., "Sharpe ratio, defined as (CAGR − Rf) / σ...")
- Report means with SDs: "M = X.XX (SD = X.XX)"
- Distinguish percentage points (pp) from percentage changes (%)
- All tables generated programmatically from actual results — no hand-typed numbers
- Report the practical significance threshold explicitly: *"The mean Sharpe ratio difference was ΔSR = X.XX (95% CI [X.XX, X.XX]), which [exceeds / falls below] the pre-registered practical significance threshold of ΔSR = 0.05 Sharpe units."*

---

### TASK 6.2 — Chapter 5: Summary, Conclusions, and Recommendations

**Dependency:** 6.1 complete  
**Time estimate:** 8–10 hours  
**Target length:** 10–14 pages  
**Acceptance:** Every finding from Chapter 4 is interpreted and linked back to a theoretical framework from Chapter 2; recommendations are grounded in specific D3/D4 findings; limitations are honest and specific

Work through the Chapter 5 structure from Companion Guide Section 13.1 in order:

- [x] **5.1 Introduction** — Restate aim and objectives; confirm research questions are answered
- [x] **5.2 Summary of Key Findings** — One paragraph per objective, factual and direct: what was found, at what significance level
- [x] **5.3 Discussion — Interpretive Conclusions:**
  - 5.3.1: The heuristics employed — which dominated, in what rank order by α weight; compare to the theoretical predictions from Chapter 2
  - 5.3.2: Deviation from efficient frontier — where Portfolio A sits relative to Portfolio B on the frontier; what the Sharpe gap means in ₦ terms on a ₦10B fund
  - 5.3.3: Comparative performance — interpret ΔSR relative to both statistical and practical thresholds; what the market condition sub-analysis implies; what the negative-Sharpe environment (if Rf = 15% exceeds most property expected returns) means for PFA property investment rationale
  - 5.3.4: Factors driving heuristic use — which constraint category (COG/INF/INS/REG) dominated in D4; interpret the ecological rationality test result (does INF-citing correlate with higher AVCS/RCS?); position the finding within the Gigerenzer vs. Kahneman-Tversky debate
- [x] **5.4 Theoretical Implications:**
  - 5.4.1: The adaptive vs. costly heuristic question — which interpretation does the evidence support, and under what conditions might it be reversed?
  - 5.4.2: Contribution to ecological rationality debate — does the Nigerian PFA data support heuristics as adaptive responses to data scarcity, or as habitual patterns persisting beyond rational justification?
- [x] **5.5 Practical Recommendations** — grounded in D3 modal response and D4 category findings:
  - For PFA investment managers (short, medium, and long-term actions)
  - For PenCom (regulatory and benchmark guidance recommendations)
  - Include monetisation of the heuristic cost: *"The ΔSR of X.XX, sustained over five years on the ₦18 trillion industry aggregate real estate allocation of approximately ₦630 billion [PenCom 2024], implies foregone risk-adjusted value of approximately ₦X billion."*
- [x] **5.6 Limitations Revisited** — four specific limitations: (1) synthetic universe; (2) purposive small sample; (3) simplified MVO framework (normal distributions, static correlations); (4) risk-free rate selection. Each limitation must be paired with a mitigation already taken.
- [x] **5.7 Directions for Future Research** — minimum four recommendations: longitudinal study with larger survey sample; ML-enhanced return prediction; cross-country comparison (Ghana, Kenya, South South Africa); live PenCom data integration
- [x] **5.8 Conclusion** — Two to three paragraphs; no new information; synthesizes the study's contribution to knowledge

---

### TASK 6.3 — Chapter 3 Final Review

**Dependency:** Phase 3 complete (α weights known)  
**Time estimate:** 3 hours

- [ ] Update Section 3.5.1 description: change "content analysis of open-text responses" to "frequency analysis of pre-coded constraint options" — this accurately reflects what Section D now collects
- [ ] Confirm the heuristic scoring function (Formula 3.15) α weight placeholders are updated to state that final weights are empirically derived from questionnaire results and presented in Chapter 4 Table 4.2
- [ ] Confirm the risk-free rate sensitivity analysis section states all three values (0.10, 0.15, 0.20) are tested, with 0.15 as the pre-registered primary value
- [ ] Read the full Chapter 3 body draft once more; confirm every section heading is followed by at least one justificatory paragraph

---

### TASK 6.4 — Front Matter and Appendices

**Dependency:** Chapters 4 and 5 complete  
**Time estimate:** 4 hours

- [ ] **Abstract** (300 words): aim, method in one sentence, key finding (ΔSR), practical implication
- [ ] **Table of Contents** — generate from final document
- [ ] **List of Figures** — auto-generate; all 8 figures listed with captions and page numbers
- [ ] **List of Tables** — auto-generate; all 8 tables listed
- [ ] **Appendix A — Questionnaire Instrument** (the full finalized v2 instrument)
- [ ] **Appendix B — Synthetic Universe Validation Report** (the 9-test validation output from Task 2.5)
- [ ] **Appendix C — Heuristic Scoring Algorithm** (the full Formula 3.15 specification and Stage 1 filter definitions)
- [ ] **Appendix D — Statistical Test Details** (full t-test and bootstrap output tables)
- [ ] **Appendix E — Market Index Calibration Table** (all 8 indices, μ and σ, sources for each year, is_simulated flags)
- [ ] **Appendix F — Code Repository** (GitHub URL + brief description of each package)
- [ ] **References** — compile full reference list in Harvard style; verify every entry against the reference log from Task 1.5

---

### TASK 6.5 — Final Dissertation Review

**Dependency:** All chapters complete  
**Time estimate:** 4 hours

- [ ] Read the full dissertation from start to finish. This is the one read where you are the examiner, not the author.
- [ ] Check: every claim has a citation or derivation
- [ ] Check: all in-text figure and table numbers match the actual figures and tables
- [ ] Check: no formula contains an undefined variable
- [ ] Check: no "however" opens a paragraph
- [ ] Check: tense is consistent within each chapter (Ch 1–3: future; Ch 4–5: past/present)
- [ ] Check: no paragraph is shorter than 4 sentences in the substantive sections; at least one paragraph in each chapter is noticeably shorter than the others (introduces variance)
- [ ] Run institutional plagiarism check (Turnitin or equivalent) — target: < 15% similarity
- [ ] Format according to OAU dissertation guidelines (margins, font, binding format)
- [ ] Page count target: 65–85 pages excluding appendices

---

---

# PHASE 7 — PFA-SIMULATOR FRONTEND
## Public-Facing Next.js Web Application
### Weeks 8–10 (parallel with writing) · Target completion: July 6, 2026

*This is the PFA-Simulator: the public-facing interactive tool that mirrors the questionnaire and demonstrates the heuristic vs. optimized comparison. It is the technical contribution of the dissertation beyond the academic document itself. It can be developed in parallel with Phases 5 and 6.*

---

### TASK 7.1 — Next.js Project Setup

**Dependency:** Monorepo structure (1.1 complete)  
**Time estimate:** 2 hours

- [ ] Navigate to `packages/simulator/`
- [ ] Run: `npx create-next-app@14 . --typescript --tailwind --app`
- [ ] Install: `npx shadcn-ui@latest init`
- [ ] Install: `npm install zustand recharts lucide-react`
- [ ] Confirm dev server runs: `npm run dev`

---

### TASK 7.2 — Core Application Screens

**Dependency:** 7.1 complete; Java backend operational (5.3 complete)  
**Time estimate:** 12–16 hours

Build the following screens in sequence:

- [ ] **Landing page** — title, brief research context, "Try the Simulator" CTA, disclaimer that data is synthetic
- [ ] **Heuristic Simulator** — walks the user through the 4 heuristic filters (title, location, condition, peer activity) with toggleable controls; shows how many of the 80 properties survive each filter; displays the resulting portfolio composition
- [ ] **MVO Comparison** — shows the algorithmically optimized portfolio alongside the heuristic portfolio; side-by-side metrics table (SR, CAGR, MDD, diversification ratio)
- [ ] **Efficient Frontier Chart** — interactive scatter plot showing the frontier, Portfolio A, and Portfolio B positions; powered by Recharts
- [ ] **Monte Carlo Viewer** — animated paths for both portfolios; percentile bands; final distribution histogram
- [ ] **Research Page** — summary of the dissertation's research questions, methodology, and findings; links to the full dissertation PDF (when available)

**State management:** Use Zustand for global application state (selected heuristic filters, portfolio results, simulation outcomes). All portfolio data is fetched from the Java backend API on demand.

---

### TASK 7.3 — Deployment

**Dependency:** 7.2 complete  
**Time estimate:** 1 hour

- [ ] Create Vercel account; connect to GitHub repository
- [ ] Set `packages/simulator` as the root directory
- [ ] Set environment variables: `NEXT_PUBLIC_API_URL` pointing to Railway-deployed backend
- [ ] Deploy backend to Railway: connect GitHub, set `packages/research-backend` as service root
- [ ] Confirm both services are live; test all simulator screens on production URL

---

---

# PHASE 8 — FINAL DELIVERABLES AND SUBMISSION
## Weeks 10–11 · Target completion: Mid-July 2026

---

### TASK 8.1 — Code Repository Final State

- [ ] Clean up all packages: remove debug print statements, commented-out blocks, unused imports
- [ ] Ensure all three packages have a `README.md` explaining how to run them
- [ ] Write the root `README.md`: project title, research context, directory structure, "how to reproduce" instructions (step by step from cloning the repo to producing the final results)
- [ ] Tag the final code state: `git tag v1.0-dissertation-submission`
- [ ] Make the repository public on GitHub

---

### TASK 8.2 — Data Files Final State

- [ ] Confirm `data/frozen/` contains the three frozen files (property_universe.csv, market_indices_returns.csv, covariance_matrix.csv) and has not been modified since the freeze tag
- [ ] Confirm `outputs/` contains all charts (PNG, 300 DPI) and all LaTeX tables (.tex files)
- [ ] Confirm `data/questionnaire/` contains raw responses (anonymized — no names or identifying details) and computed composite scores
- [ ] Confirm `data/calibration/` contains market data collection files with source citations

---

### TASK 8.3 — Dissertation Document Final State

- [ ] All five chapters complete and reviewed
- [ ] All appendices compiled
- [ ] Abstract written (300 words)
- [ ] References complete (Harvard style; all verified against reference log)
- [ ] Table of contents, list of figures, list of tables generated
- [ ] Page count check: 65–85 pages excluding appendices
- [ ] Format check: OAU guidelines (margins, font size, line spacing, binding format)
- [ ] PDF generated from final document

---

### TASK 8.4 — Submission

- [ ] Submit PDF to department by the official deadline
- [ ] Submit a copy to supervisor for records
- [ ] Archive the GitHub repository URL in the dissertation footer (Appendix F)

---

---

## ◈ CONTINGENCY PLANS

### If the CPFA census yields very few usable responses

This is managed through the four-path analysis framework established in Task 1.3. The key principle is that the analysis design adapts to what the census returns — it does not fail. Even a single CPFA's investment staff providing responses constitutes evidence about how that institution approaches property selection, and it is presented honestly as such.

If the response count is low enough that Formulas 3.1–3.4 cannot be meaningfully computed (fewer than 5 usable respondents), the heuristic portfolio (Portfolio A) is constructed using **literature-derived α weights** derived from the documented patterns in Babawale (2013), Ogunba (2013), and Bikhchandani, Hirshleifer & Welch (1992). These weights are defensible because they are grounded in the same literature that motivated the study's theoretical framework. The baseline weights are approximately: α₁ (anchoring/title) = 0.35, α₂ (availability/location) = 0.35, α₃ (representativeness/momentum) = 0.15, α₄ (herding/peer) = 0.15 — reflecting the documented primacy of title quality and location prestige in Nigerian institutional property practice. Acknowledge explicitly in Chapter 3 (revised sampling section), Chapter 4 Section 4.5, and Chapter 5 Section 5.6. Objectives II, III, and IV are entirely unaffected by this path.

### If the optimizer fails to converge within 300 seconds

Reduce the property universe from 80 to 60 for the optimization step (select the 60 properties with the highest individual Sharpe ratios). Document in methodology. The frozen 80-property universe remains unchanged; the optimizer simply works on a pre-filtered subset.

### If ΔSharpe < 0.05 (null finding)

This is a valid and publishable result. It supports the ecological rationality interpretation (Gigerenzer). Do not suppress or reframe it. Present it as the finding: *"The study failed to detect a practically significant performance cost associated with heuristic-driven portfolio selection in the Nigerian PFA context, consistent with the ecological rationality hypothesis that simple heuristics may perform comparably to complex algorithms in data-scarce environments."* Chapter 5 recommendations shift from "adopt optimization" to "invest in data infrastructure first, as data sufficiency is a prerequisite for optimization to outperform heuristics."

### If the CBN T-bill rate (15%) produces mostly negative Sharpe ratios

This is itself a finding worth reporting. Note it explicitly in Chapter 4 and discuss it in Chapter 5: at the study's pre-registered risk-free rate, the expected returns on most institutional real estate investments do not clear the risk-adjusted hurdle, suggesting PFAs investing in property are betting on capital appreciation and inflation hedging rather than excess return in the Sharpe sense. Run the sensitivity analysis at 10% to show what Sharpe ratios look like at a lower rate.

### If the Java backend is not complete in time

The Java backend is NOT required for the academic analysis. Phases 2–4 (Python pipeline) produce all the data needed for Chapters 4 and 5. The Java backend is required only for the PFA-Simulator frontend. If pressed for time, complete the dissertation submission first, then finish the Java backend and deploy the simulator.

---

## ◈ TIME BUDGET SUMMARY

| Phase | Weeks | Est. Hours | Dependency Chain |
|---|---|---|---|
| Phase 1 — Questionnaire + Data Research | 1–2 | 16 hrs | Start immediately |
| Phase 2 — Generator | 2–3 | 21 hrs | After 1.4 begins |
| Phase 3 — Questionnaire Analysis | 4 | 9 hrs | After responses close |
| Phase 4 — Computational Pipeline | 3–6 | 29 hrs | After Phase 2 freeze |
| Phase 5 — Java Backend | 5–6 | 13 hrs | After Phase 2 |
| Phase 6 — Dissertation Writing | 7–9 | 43 hrs | After Phase 4 |
| Phase 7 — Simulator Frontend | 8–10 | 20 hrs | After Phase 5 |
| Phase 8 — Submission Prep | 10–11 | 6 hrs | After Phase 6 |
| **Total** | **11 weeks** | **~155 hours** | |

**Average:** ~15 hours/week. Achievable for a dedicated final-year student.

---

## ◈ SUCCESS MILESTONES

| Milestone | Target Date | Criteria |
|---|---|---|
| **M0 — Launch** | April 28, 2026 | Google Form live; GitHub repo created; all 7 CPFAs identified; father briefed |
| **M1 — Market Data** | May 10, 2026 | ≥ 6 of 8 indices populated; calibration spreadsheet documented |
| **M2 — Universe Frozen** | May 18, 2026 | All validation tests pass; frozen CSVs committed; `v1.0-frozen-universe` tag applied |
| **M3 — Questionnaire Closed** | May 21, 2026 | Response window closed; final count recorded by tier; analysis path selected; α weights computed or literature baseline confirmed |
| **M4 — Both Portfolios Built** | May 28, 2026 | Portfolio A and B constructed; PENCOM constraints verified |
| **M5 — Simulation Complete** | June 3, 2026 | 10,000 Monte Carlo paths run; all metrics computed; all charts saved |
| **M6 — Chapter 4 Draft** | June 22, 2026 | All results reported; supervisor review requested |
| **M7 — Chapter 5 Draft** | June 29, 2026 | Conclusions, recommendations, limitations written |
| **M8 — Full Draft** | July 5, 2026 | All chapters complete; front matter done; references verified |
| **M9 — Submission** | Mid-July 2026 | PDF submitted to department |

---

## ◈ MINIMUM VIABLE DISSERTATION

If everything goes wrong and you must cut scope, this is the floor below which you cannot go and still defend:

- 80-property frozen universe *(non-negotiable — already designed)*
- α weights from questionnaire OR equal-weighted placeholder *(either works)*
- Portfolio A (heuristic) and Portfolio B (MVO) constructed in Python *(no Java backend required)*
- Monte Carlo simulation: 1,000 paths is acceptable if 10,000 is too slow
- One primary performance metric reported (Sharpe ratio) with statistical test
- Chapter 4 and Chapter 5 written from the above results
- Java backend and PFA-Simulator deferred to post-submission

This still constitutes a complete, defensible, novel dissertation.

---

*Document version: 2.1 — April 26, 2026*  
*Prepared for: Isla · OAU, Department of Estate Management · 2024/2025 Academic Session*  
*Status at issue: Project defense passed. Approved to proceed.*  
*Companion documents: PRD v1.0 · TDD v1.0 · Generator v1.0 · Chapter 3 Body Draft · Questionnaire v2 Final · Companion Guide v3*
