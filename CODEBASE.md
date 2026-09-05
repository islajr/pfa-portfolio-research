# Codebase Directory Map and File Reference

This document provides a comprehensive, file-by-file directory map of the property portfolio research monorepo. It details the purpose, inputs, outputs, programming logic, classes, methods, and functions of each script to facilitate codebase navigation and development.

---

## 1. Root Directory Documents

*   [architecture.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/architecture.md): This file serves as the system and mathematical architecture guide. Written in structured prose, it explains the multi-tier design philosophy (Python analytical engine, Java Spring Boot REST API, Next.js interactive UI), visualizes the data flow via a Mermaid diagram, lists the key equations for all phases (heuristic scoring, asset calibration, BIP optimization, Cholesky correlated Monte Carlo paths), and documents the empirical anomalies (crossover and volatility paradox).
*   [GEMINI.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/GEMINI.md): This file represents the developer conventions and repository guidelines. It outlines building and running instructions, lists required development tools, and documents the strict **Frozen Universe Policy** which preserves the longitudinal consistency of the study.
*   [PRD_Portfolio_Optimization_System.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/PRD_Portfolio_Optimization_System.md): The Product Requirements Document. It details the scope, stakeholders, system requirements, data schemas, validation check specifications, and mock data templates.
*   [TDD_Portfolio_Optimization_System.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/TDD_Portfolio_Optimization_System.md): The Technical Design Document. It outlines the pipeline stages, class designs, optimization models, testing suites, configurations, and verification checklists.
*   [implementation-checklist.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/implementation-checklist.md): A living checklist that tracks the implementation status of all tasks across the six phases of the project (e.g., Phase 1 data extraction, Phase 2 universe validation, Phase 3 heuristic engine calibration, Phase 4 simulations, and Phase 6 dissertation drafting).
*   [research-methodology.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/research-methodology.md): Reference document mapping out the pre-registered chapters, LaTeX formulations, and statistical hypothesis tests.
*   [nigeria_cbn_tbill_rates_2019_2024.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/nigeria_cbn_tbill_rates_2019_2024.md): Macroeconomic calibration notes documenting the analysis of Central Bank of Nigeria T-Bill rates that established the baseline risk-free rate of **8.4%** ($R_f = 0.084$).

---

## 2. Data Directory (`data/`)

This directory houses the raw survey spreadsheet, historical calibration sheets, and the read-only frozen synthetic universe files.

### 2.1 Calibration Data (`data/calibration/`)
*   `market_index_returns.csv`: This file contains the historical annual capital appreciation and rental yield return series for the 8 primary property submarket indices in Nigeria (Lagos Island Residential/Commercial, Lagos Mainland Residential/Commercial, Abuja Residential/Commercial, Rivers Residential, and Kano/Oyo Industrial/Commercial). It serves as the statistical foundation for asset calibration.
*   `raw_extracted_market_data.json`: A JSON file generated during historical data extraction containing annual parameters from institutional reports (CBRE, PenCom) used to calibrate the indices.

### 2.2 Frozen Universe (`data/frozen/`)
*   `property_universe.csv`: This file stores the ground-truth 80 synthetic properties, including physical attributes (state, submarket, asset class, condition tier), legal attributes (title status), prices, expected returns, and volatilities. Under the study's rules, it remains strictly read-only to preserve replication consistency.
*   `market_indices_returns.csv`: This file stores the calibrated average capital appreciation and yield figures for the 8 submarket indices.
*   `property_covariance_matrix.csv`: This file holds the calibrated $80 \times 80$ covariance matrix representing historical return relationships between all property pairs.
*   `covariance_matrix.csv`: This file holds the $8 \times 8$ index-level covariance matrix.

### 2.3 Other Data Directories
*   `data/market-reports/`: This folder contains the raw PDF documents and market reports from CBRE and PenCom used as primary sources.
*   `data/questionnaire/`: This folder contains the active google forms and raw spreadsheet data from the PFA Questionnaire.

---

## 3. Package: Property Universe Generator (`packages/generator/`)

This Python package constructs the 80 properties based on historical index parameters under strict statistical controls.

### 3.1 `config.py`
This module defines all static calibration configurations for the universe generator. It contains:
*   `VACANCY_RATES` & `MAINTENANCE_RATES`: Dictionaries mapping asset classes (Office, Commercial, Industrial, Residential, Mixed-Use) to their operational parameters.
*   `TITLE_RISK_PREMIUMS` & `CONDITION_RISK_PREMIUMS`: Dictionaries specifying volatility additions for legal and physical risks.
*   `GEOGRAPHIC_ALLOCATIONS`: Tariffs defining target percentages for the 6 submarket regions in Nigeria.

### 3.2 `metrics_calculator.py`
This module defines the functions that calculate property financial metrics:
*   `load_index_stats(market_returns_csv)`:
    *   *Input:* Path to index returns CSV.
    *   *Output:* Dictionary of index stats containing mean capital appreciation (`mu_cap`) and standard deviation of total returns (`sigma_ret`) for each of the 8 market indices.
    *   *Logic:* Extracts and averages historical return observations, falling back to a fraction (0.6) of annual returns if capital appreciation data is missing.
*   `compute_property_metrics(prop_dict, index_stats, rf_rate)`:
    *   *Input:* Property dictionary, index stats dictionary, risk-free rate.
    *   *Output:* Dictionary containing calculated Total Acquisition Cost (TAC), Net Operating Income (NOI), Cap Rate, Expected Return, Volatility, and Sharpe Ratio.
    *   *Logic:* Implements the formulas from Chapter 3: adds transaction and state consent fees to purchase price for TAC, subtracts maintenance and vacancy rates from gross rent for NOI, and adds risk premiums to index volatility.
*   `run_unit_tests()`: Compares the function calculations against 3 hand-calculated mock property cases (Lagos Office, Abuja Commercial, Kano Industrial) to assert mathematical correctness.

### 3.3 `generate_universe.py`
This script constructs the 80 synthetic properties:
*   `main()`:
    *   *Input:* Reads `data/calibration/market_index_returns.csv` and `packages/generator/config.py`.
    *   *Output:* Writes `property_universe.csv` containing the 80 synthetic properties.
    *   *Logic:* Sets the random seed to 42. Loops over state/submarket configurations, samples prices and rents from log-normal distributions, assigns index IDs, calls `compute_property_metrics` to calculate returns and volatilities, and saves the output data.

### 3.4 `validate_universe.py`
This script runs a suite of 9 validation checks on the generated properties:
*   `load_data()`: Loads the generated property universe.
*   `run_jb_test(prices)`: Runs the Jarque-Bera normality test on pricing variables to confirm log-normality.
*   `run_all_validation_checks()`: Coordinates the 9 checks: (1) Jarque-Bera price log-normality; (2) submarket allocation percentage checks; (3) asset class percentage checks; (4) title status shares; (5) condition tier shares; (6) price tier distributions; (7) average cap rates against CBRE indices; (8) index correlation alignments; and (9) covariance positive-definiteness. Raises an exception if any test fails.

### 3.5 `freeze_universe.py`
*   `freeze_files()`: Copies validated files into the read-only `data/frozen/` folder.

### 3.6 `execute.sh`
*   A bash orchestration script that runs the entire universe generation sequence. It sequentially executes `generate_universe.py`, `validate_universe.py`, and `freeze_universe.py` in the virtual environment.

---

## 4. Package: Analytical Core & Optimizer (`packages/optimizer/`)

This Python package processes the survey responses, constructs the portfolios, runs the Monte Carlo simulation paths, and performs the statistical significance tests.

### 4.1 `clean_analyze_responses.py`
This script cleans the survey data and calibrates the heuristic weights:
*   `load_and_clean_data()`:
    *   *Input:* Raw survey CSV.
    *   *Output:* Filtered DataFrame ($N=32$ active respondents after excluding non-participants).
    *   *Logic:* Renames questionnaire columns to short labels like A1-D4 and drops rows where A5 indicates no direct participation in property selection.
*   `calculate_composite_heuristic_scores(df)`:
    *   *Input:* Cleaned survey DataFrame.
    *   *Output:* DataFrame with calculated Title Anchoring (ACS), Location Familiarity (AVCS), Trend Momentum (RCS), and Peer Herding (HCS) scores for each respondent.
    *   *Logic:* Implements Formulas 3.1 to 3.4, combining Likert scale ranks and active scenario decisions.
*   `calculate_bca_bootstrap_ci(scores)`: Computes BCa confidence intervals for each heuristic score.
*   `calibrate_alpha_weights(df)`:
    *   *Input:* Mapped survey DataFrame.
    *   *Output:* Calculates normalized group-level averages to calibrate the decision weights ($\alpha_1 = 0.2896, \alpha_2 = 0.3398, \alpha_3 = 0.1753, \alpha_4 = 0.1953$) and saves them to `alpha_weights.json`.

### 4.2 `covariance.py`
*   `generate_property_covariance()`:
    *   *Input:* Reads property universe and index returns.
    *   *Output:* Writes `property_covariance_matrix.csv`.
    *   *Logic:* Populates the $80 \times 80$ covariance matrix. Evaluates eigenvalues: if any are negative, it applies Ledoit-Wolf shrinkage (`sklearn.covariance.LedoitWolf`) and adds a diagonal ridge ($10^{-6}$) to ensure positive semi-definiteness.

### 4.3 `heuristic_engine.py`
This module builds the heuristic portfolio (Portfolio A):
*   `load_data()`: Loads frozen data.
*   `calculate_momentum_scores(df_returns)`: Computes normalized momentum scores over recent 3 years.
*   `construct_heuristic_portfolio()`:
    *   *Input:* Calibrated survey weights, frozen universe.
    *   *Output:* Writes `portfolio_A_heuristic.json`.
    *   *Logic:* Applies Stage 1 EBA hard filters (excluding properties without standard title, outside prime/secondary states, or in poor condition). In Stage 2, it calculates the composite score $H(p_i)$ for all passing properties using the calibrated weights. In Stage 3, it executes a greedy budget allocation, selecting the top properties under a ₦500 million single-asset cap to form Portfolio A ($N=6$ assets, equal weight $w_i = 1/6$).

### 4.4 `mvo_optimizer.py`
This module builds the optimized portfolio (Portfolio B):
*   `load_data()`: Loads universe and covariance.
*   `run_continuous_slsqp(eligible_df, cov_df, rf=0.084)`: Runs continuous SLSQP optimization on the eligible properties for reference.
*   `run_exact_bip(eligible_df, cov_df, rf=0.084)`:
    *   *Input:* Eligible DataFrame, covariance matrix, risk-free rate.
    *   *Output:* Best property subset, optimal Sharpe ratio, expected return, and volatility.
    *   *Logic:* Since the pool of eligible assets is small ($N=13$) due to strict PenCom and title filters, this function executes an exact combinatorial search over all valid property subsets of size $k \in [5, 13]$ using `itertools.combinations`. For each subset, it verifies that at least two states are represented (diversification constraint) and that the total cost is below ₦10 billion. It computes the equal-weighted portfolio return and covariance-driven volatility, selecting the subset that maximizes the Sharpe ratio.
*   `construct_optimized_portfolio()`: Coordinates the BIP optimizer, constructs Portfolio B ($N=5$ assets, equal weight $w_i = 1/5$), and writes the holdings to `portfolio_B_optimized.json`.

### 4.5 `monte_carlo.py`
This module runs the stochastic simulation:
*   `load_portfolios_and_cov()`: Loads portfolios and property covariance matrix.
*   `simulate_gbm(portfolio, df_cov, n_paths=10000, n_months=60)`:
    *   *Input:* Portfolio holding dictionary, covariance matrix, path count, monthly horizon.
    *   *Output:* Array of portfolio value paths (shape: $10000 \times 61$) and monthly returns (shape: $10000 \times 60$).
    *   *Logic:* Divides expected returns and covariances by 12 for monthly calibration. Computes the Cholesky decomposition of the covariance matrix ($\mathbf{L} = \text{chol}(\boldsymbol{\Sigma})$). At each month $t$, it samples standard normal random variables, correlates them via matrix multiplication with $\mathbf{L}$, adds monthly cap yields, calculates equal-weighted portfolio returns, and updates portfolio values.
*   `run_simulation_engine()`: Runs the GBM simulation for Portfolios A and B under random seed 42. Saves the full arrays as `.npy` files for statistical testing, and the first 100 paths for visualization.

### 4.6 `statistical_tests.py`
This module conducts the hypothesis tests and sensitivity analysis:
*   `calculate_mdd(paths)`: Computes Maximum Drawdown for each simulated path using running peaks.
*   `calculate_metrics(paths, returns, holdings, rf=0.084)`: Computes CAGR, volatility, Sharpe, CVaR 95%, and Diversification Ratio (DR) across all 10,000 paths.
*   `calculate_hhi(holdings)`: Computes Holdings HHI, Geographic HHI, and Asset Type HHI.
*   `calculate_bca_bootstrap(returns_A, returns_B, rf=0.084, n_replications=10000, block_size=6)`:
    *   *Input:* Simulated returns, risk-free rate, replications, block size.
    *   *Output:* Original delta Sharpe, lower CI, upper CI.
    *   *Logic:* Reshapes returns into 6-month blocks to preserve serial correlation. Resamples blocks, computes bootstrap delta Sharpe values, and calculates the bias-correction ($z_0$) and acceleration ($a$, via jackknife over blocks) parameters to determine the 95% BCa confidence interval bounds.
*   `run_statistical_analysis()`: Coordinates the paired t-test, Cohen's $d$, BCa bootstrap CI, market volatility tercile analysis, and interest rate sensitivity checks ($R_f \in [8.4\%, 10\%, 15\%, 20\%]$), saving the results to `summary_metrics.json`.

### 4.7 `generate_outputs.py`
*   Coordinates results, generating the LaTeX tables and PNG charts.

### 4.8 `execute.sh`
*   Bash orchestration script executing `packages/optimizer` python modules.

---

## 5. Package: Utilities (`packages/utils/`)

*   [extract_dissertation.py](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/packages/utils/extract_dissertation.py):
    *   *Description:* An automated layout-mode extraction and formatting script. It parses chapters from the source PDF (`ESM 519_ Project Dissertation.pdf`), formats sections, structures bibliographic lists, replaces messy layout text with LaTeX math blocks (Formulas 3.1 to 3.15), and injects clean Markdown tables (Tables 3.1 to 3.8) in `dissertation/chapters/chapter_3.md` while skipping visual split-row artifacts on Page 57.

---

## 6. Project Outputs and Dissertation Drafts

### 6.1 Outputs Directory (`outputs/`)
*   `outputs/tables/`: Contains programmatically generated LaTeX tables (e.g., `heuristic_scores_table.tex`, `simulation_summary_table.tex`, `sensitivity_analysis_table.tex`, etc.) used in the dissertation.
*   `outputs/charts/`: Contains the PNG figures (e.g., `figure_4_1_efficient_frontier.png` efficient frontier, `figure_4_8_preference_gap.png` preference gaps, `figure_4_6_stress_scenario.png` crossovers, etc.).
*   `outputs/portfolios/` and `outputs/simulation_results/`: Holds the raw JSON data of selected properties and simulated path parameters.

### 6.2 Dissertation Drafts Directory (`dissertation/`)
*   `dissertation/chapters/chapter_1.md`: Chapter 1 (Introduction, background, research questions).
*   `dissertation/chapters/chapter_2.md`: Chapter 2 (Literature review, theoretical frameworks).
*   `dissertation/chapters/chapter_3.md`: Chapter 3 (Research methodology, asset calibration, BIP model, LaTeX math formulas, and injected Tables 3.1 to 3.8).
*   `dissertation/chapters/chapter_4.md`: Chapter 4 (Empirical analysis, demographics, stated-revealed gaps, calibrated weights, simulation results, t-tests, crossovers, and embedded Figures 4.1 to 4.8).
*   `dissertation/chapters/chapter_5.md`: Chapter 5 (Summary, theoretical and practical conclusions, PenCom policy reforms, monetized heuristic cost at ₦293.3 billion, study limitations, and future research).
*   `dissertation/references.md`: Harvard-style compiled reference bibliography.
*   `dissertation/appendices/appendix_a.md`: Detailed questionnaire instrument.
