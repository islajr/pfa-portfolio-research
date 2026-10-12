# Heuristics in Property Portfolio Selection Decisions of Nigerian Pension Funds
### An Empirical Assessment of Adaptive Behaviour in Institutional Real Estate Allocation

**Author:** Akinmokun Isaac Oluwaseun (ESM/2019/023)  
**Supervisor:** Prof. A. Olaleye  
**Institution:** Obafemi Awolowo University, Ile-Ife, Nigeria  
**Faculty:** Faculty of Environmental Design and Management  
**Department:** Department of Estate Management  
**Degree:** Bachelor of Science (B.Sc. Hons) in Estate Management  
**Date:** September 2026  

---

## Table of Contents

- [Abstract](#abstract)
- [Research Background and Problem Statement](#research-background-and-problem-statement)
- [Research Questions and Hypotheses](#research-questions-and-hypotheses)
- [Methodological and Analytical Framework](#methodological-and-analytical-framework)
  - [1. Primary PFA Industry Census](#1-primary-pfa-industry-census)
  - [2. Heuristic Composite Scoring and Decision Weights](#2-heuristic-composite-scoring-and-decision-weights)
  - [3. Calibrated Property Universe](#3-calibrated-property-universe)
  - [4. Portfolio Construction Formulations](#4-portfolio-construction-formulations)
  - [5. Stochastic Monte Carlo Simulation Engine](#5-stochastic-monte-carlo-simulation-engine)
- [Key Empirical Findings](#key-empirical-findings)
  - [Baseline Performance Comparison](#baseline-performance-comparison)
  - [The Hurdle Rate Crossover Phenomenon](#the-hurdle-rate-crossover-phenomenon)
  - [Ecological Rationality of Institutional Heuristics](#ecological-rationality-of-institutional-heuristics)
  - [Monetized Macroeconomic Cost](#monetized-macroeconomic-cost)
- [Repository Architecture and Directory Map](#repository-architecture-and-directory-map)
- [Document Catalog](#document-catalog)
- [Replication and Build Instructions](#replication-and-build-instructions)
  - [Environment Setup](#environment-setup)
  - [Executing the Empirical Pipeline](#executing-the-empirical-pipeline)
  - [Compiling the Canonical Dissertation PDF](#compiling-the-canonical-dissertation-pdf)
  - [Generating Presentation Decks](#generating-presentation-decks)
- [Citation Specifications](#citation-specifications)
- [License and Academic Disclaimer](#license-and-academic-disclaimer)

---

## Abstract

Direct real estate allocation by Nigerian Pension Fund Administrators (PFAs) operates within an institutional environment characterized by acute information asymmetry, land titling frictions, and strict regulatory ceilings imposed by the National Pension Commission (PenCom). In the absence of centralized transaction indices, fund managers substitute formal mean-variance optimization (MVO) models with qualitative heuristics. This study examines whether heuristic decision rules represent suboptimal behavioural biases or ecologically rational adaptations to emerging market opacity.

Surveying all 24 PenCom-licensed PFAs through a primary industry census ($N = 32$ investment officers and registered estate surveyors) and calibrating an 80-asset investment universe against empirical market benchmarks, the study compares an Elimination-by-Aspects (EBA) heuristic portfolio (Portfolio A, $N = 6$) against an integer-constrained mean-variance optimal portfolio (Portfolio B, $N = 5$). A 10,000-path, 60-month Monte Carlo simulation with Cholesky covariance decomposition demonstrates that while Portfolio B generates a superior Sharpe ratio in the baseline low-rate environment ($R_f = 8.4\%$; Sharpe $1.85$ vs. $1.12$, $t = 127.42, p < 0.001$) via cross-regional covariance suppression, Portfolio A achieves higher nominal compound annual growth (CAGR $24.20\%$ vs. $15.50\%$).

Crucially, interest rate sensitivity testing uncovers a structural crossover threshold at $R_f \approx 12.5\%$. In high-inflation regimes representative of Nigeria's monetary policy rate trajectory ($R_f \ge 15\%$), Portfolio B's regional diversification assets fail to clear the risk-free hurdle rate, driving its Sharpe ratio to negative values ($-7.92$ at $R_f = 20\%$). Conversely, Portfolio A maintains positive risk-adjusted performance ($0.55$) through prime Lagos asset yield resilience. The findings confirm that institutional heuristics exhibit ecological rationality in volatile macro environments, and inform a two-stage hybrid portfolio framework and institutional data infrastructure reforms.

---

## Research Background and Problem Statement

Following the Pension Reform Act of 2004 (repealed and re-enacted as PRA 2014), Nigeria transitioned from an unfunded Defined Benefit framework to a contributory, fully funded Pension Reform system. By year-end 2024, total pension assets under management exceeded ₦21.3 trillion. Under PenCom Regulation on Investment of Pension Fund Assets, PFAs are permitted to allocate up to 10% of total assets under management directly into real estate.

Direct commercial and residential property investment presents distinct institutional barriers in Nigeria:

1. **Information Asymmetry and Market Opacity:** Unlike mature markets supported by standardized indices (e.g., NCREIF, IPD/MSCI), Nigerian real estate transactions are unrecorded in centralized public databases, creating high search and verification costs.
2. **Titling and Legal Frictions:** High transfer tariffs, Governor's Consent delays under the Land Use Act of 1978, and counterparty title risks impose severe liquidity discounts on off-market assets.
3. **Regulatory Constraints:** PenCom mandates strict criteria, including a 5% single-asset exposure ceiling, minimum title standards (Certificate of Occupancy or Governor's Consent), and multi-state geographic diversification requirements.

Confronted with computational intractability and high search costs, investment committees deploy heuristics:
- **Title Anchoring:** Over-weighting perfection status of legal title as an initial elimination criterion.
- **Location Familiarity:** Restricting allocations to familiar core commercial submarkets (Lagos Island, Victoria Island, Ikoyi, Ikeja GRA).
- **Trend Momentum:** Extrapolating historical capital gains from recent development corridors (Lekki Phase 1, Epe Expressway).
- **Peer Herding:** Replicating the asset selection patterns of tier-one institutional peers.

This research investigates whether these decision rules reflect cognitive defects (the heuristics-and-biases paradigm) or efficient adaptations to an opaque institutional environment (the ecological rationality framework).

---

## Research Questions and Hypotheses

### Research Questions

1. What decision heuristics do Nigerian Pension Fund Administrators prioritize when selecting direct real estate investments?
2. To what degree do stated selection criteria diverge from revealed asset allocations across institutional portfolios?
3. How does the risk-adjusted performance of an empirically calibrated heuristic portfolio compare to a binary integer mean-variance optimized portfolio under stochastic simulation?
4. How do macroeconomic interest rate shocks ($R_f \in [8.4\%, 20\%]$) alter the relative performance and solvency of heuristic versus optimized allocations?

### Statistical Hypotheses

- **Null Hypothesis ($H_0$):** There is no statistically significant difference in the mean Sharpe ratios of the heuristic portfolio and the integer mean-variance optimized portfolio across 10,000 stochastic simulation paths:
  $$H_0: E[SR_B] - E[SR_A] = 0$$
- **Alternative Hypothesis ($H_1$):** The integer mean-variance optimized portfolio generates a statistically superior mean Sharpe ratio over the heuristic portfolio:
  $$H_1: E[SR_B] - E[SR_A] > 0$$
- **Alternative Hypothesis ($H_2$):** The heuristic portfolio generates a statistically superior mean Sharpe ratio over the integer mean-variance optimized portfolio:
  $$H_2: E[SR_B] - E[SR_A] < 0$$

Significance testing is evaluated via two-tailed paired Student's $t$-tests ($p < 0.001$), Cohen's $d$ effect sizes, and 10,000-replication bias-corrected accelerated (BCa) bootstrap confidence intervals.

---

## Methodological and Analytical Framework

The research monorepo integrates primary empirical survey data with quantitative financial modeling, linear integer programming, and stochastic calculus:

```
[Primary PFA Survey]  ──>  [Heuristic Weights (alpha)]  ──>  [Portfolio A: Heuristic (EBA)]
         |                                                                    |
         v                                                                    v
[CBRE/PenCom Indices] ──>  [80-Asset Frozen Universe]   ──>  [10,000-Path Monte Carlo GBM]
         |                                                                    |
         v                                                                    v
[Covariance Matrix]   ──>  [Binary Integer MVO (BIP)]   ──>  [Portfolio B: Optimized (MVO)]
                                                                      |
                                                                      v
                                                            [Statistical Tests & Crossover]
```

### 1. Primary PFA Industry Census

- **Population:** All 24 PenCom-licensed Pension Fund Administrators in Nigeria as of Q4 2024.
- **Sample:** $N = 32$ investment committee members, portfolio managers, risk analysts, and registered estate surveyors across the 24 PFAs.
- **Instrument:** Structured 4-section questionnaire combining 5-point Likert ranking scales with direct choice scenario experiments to measure stated preferences and identify revealed trade-offs.

### 2. Heuristic Composite Scoring and Decision Weights

Individual respondent scores are computed across four heuristic dimensions:

1. **Anchoring Composite Score ($ACS$):**
   $$ACS_k = \frac{w_1 \cdot B3_k + w_2 \cdot C1_k}{w_1 + w_2}$$
2. **Availability/Familiarity Composite Score ($AVCS$):**
   $$AVCS_k = \frac{w_1 \cdot B1_{loc,k} + w_2 \cdot B2_k + w_3 \cdot C2_k}{w_1 + w_2 + w_3}$$
3. **Representativeness/Momentum Composite Score ($RCS$):**
   $$RCS_k = \frac{w_1 \cdot B1_{sector,k} + w_2 \cdot C3_k}{w_1 + w_2}$$
4. **Herding Composite Score ($HCS$):**
   $$HCS_k = \frac{w_1 \cdot B1_{peer,k} + w_2 \cdot B4_k + w_3 \cdot C4_k}{w_1 + w_2 + w_3}$$

The aggregate industry decision weights ($\alpha_j$) are calibrated by normalizing composite score means:

$$\alpha_j = \frac{\bar{H}_j}{\sum_{i=1}^{4} \bar{H}_i}$$

Empirically derived weights:
- Title Anchoring ($\alpha_1$): $0.2896$ ($28.96\%$)
- Location Familiarity ($\alpha_2$): $0.3398$ ($33.98\%$)
- Trend Momentum ($\alpha_3$): $0.1753$ ($17.53\%$)
- Peer Herding ($\alpha_4$): $0.1953$ ($19.53\%$)

### 3. Calibrated Property Universe

An 80-asset investment universe is calibrated to reflect real-world Nigerian institutional property markets across 8 submarket indices:
- Lagos Island Commercial (LIC)
- Lagos Island Residential (LIR)
- Lagos Mainland Commercial (LMC)
- Lagos Mainland Residential (LMR)
- Abuja Commercial (ABC)
- Abuja Residential (ABR)
- Rivers Residential (RVR)
- Kano/Oyo Industrial (KOI)

Each asset $i$ is parameterized by Total Acquisition Cost ($TAC_i$), Net Operating Income ($NOI_i$), Cap Rate ($CR_i$), Expected Return ($E[R_i]$), and Return Volatility ($\sigma_i$):

$$TAC_i = P_i \times (1 + f_{\text{agency}} + f_{\text{legal}} + f_{\text{consent},s_i})$$

$$NOI_i = (GR_i \times (1 - v_{a_i})) - (GR_i \times m_{a_i})$$

$$CR_i = \frac{NOI_i}{TAC_i}$$

$$E[R_i] = CR_i + \mu_{\text{idx}(i)}$$

$$\sigma_i = \sigma_{\text{idx}(i)} + \delta^{\text{title}}_{\text{tl}_i} + \delta^{\text{cond}}_{\text{cn}_i}$$

### 4. Portfolio Construction Formulations

#### Portfolio A (Empirical Heuristic Selection)
Portfolio A is assembled via an Elimination-by-Aspects (EBA) heuristic filter:
1. Reject any asset with title defects (only Governor's Consent or Certificate of Occupancy admitted).
2. Reject assets located outside prime commercial hubs.
3. Compute composite heuristic utility:
   $$H(p_i) = \alpha_1 \cdot TS(p_i) + \alpha_2 \cdot LS(p_i) + \alpha_3 \cdot MS(p_i) + \alpha_4 \cdot PS(p_i)$$
4. Select top-scoring assets under greedy budget allocation subject to the ₦500 million single-property exposure cap ($N = 6$ assets, equal weight $w_i = 1/6$).

#### Portfolio B (Binary Integer Mean-Variance Optimization)
Portfolio B solves a binary integer program (BIP) maximizing the portfolio Sharpe ratio under PenCom regulatory constraints:

$$\max_{\mathbf{x}} \quad SR_P = \frac{E[R_P] - R_f}{\sigma_P}$$

$$\text{subject to:} \quad \sum_{i=1}^{80} x_i \cdot TAC_i \le \text{Budget} \quad (\text{Budget} = \text{₦10 Billion})$$

$$TAC_i \cdot x_i \le 0.05 \times \text{Budget} \quad (\text{₦500 Million})$$

$$\text{unique}(\{\text{state}_i \cdot x_i\}) \ge 2 \quad (\text{Multi-State Diversification})$$

$$5 \le \sum_{i=1}^{80} x_i \le 20, \quad x_i \in \{0, 1\}$$

Portfolio B selects $N = 5$ assets (equal weight $w_i = 1/5$), incorporating regional diversification across Abuja and secondary hubs.

### 5. Stochastic Monte Carlo Simulation Engine

A 10,000-path, 60-month Geometric Brownian Motion (GBM) simulation models terminal portfolio valuations:

$$V_P(\tau) = V_P(\tau - 1) \times (1 + R_P(\tau))$$

Cross-asset correlation is preserved via Cholesky decomposition of the $80 \times 80$ covariance matrix ($\mathbf{L}\mathbf{L}^T = \boldsymbol{\Sigma}$), with Ledoit-Wolf shrinkage and ridge regularization ($10^{-6}$) applied to guarantee positive definiteness:

$$\mathbf{R}(\tau) = \mathbf{CR} + \mathbf{Z} \mathbf{L}^T$$

---

## Key Empirical Findings

### Baseline Performance Comparison

Under the baseline macroeconomic calibration ($R_f = 8.4\%$, derived from historical 364-day CBN Treasury Bill yields):

| Metric | Portfolio A (Heuristic) | Portfolio B (Integer MVO) | Difference ($\Delta = B - A$) | Statistical Significance |
| :--- | :--- | :--- | :--- | :--- |
| **Asset Count ($N$)** | 6 properties | 5 properties | -1 | -- |
| **Geographic Focus** | Lagos (100%) | Lagos (40%), Abuja (40%), Kano (20%) | Cross-regional | -- |
| **Expected Annual Return ($E[R]$)** | 24.23% | 15.54% | -8.69% | -- |
| **Annualized Volatility ($\sigma$)** | 14.15% | 3.84% | -10.31% | -- |
| **Mean Sharpe Ratio ($SR$)** | **1.12** | **1.85** | **+0.73** | $t = 127.42, p < 0.001$ |
| **5-Year Median CAGR** | **24.20%** | **15.50%** | **-8.70%** | $p < 0.001$ |
| **Terminal Wealth Ratio** | **2.95x** | **2.05x** | **-0.90x** | $p < 0.001$ |
| **Geographic HHI** | 1.0000 | 0.3600 | -0.6400 | Reduced spatial clustering |
| **Diversification Ratio** | 1.01 | 1.48 | +0.47 | Covariance suppression |

At $R_f = 8.4\%$, Markowitz diversification operates as theoretically predicted: Portfolio B sacrifices 869 basis points of nominal return to achieve a 1,031 basis point reduction in volatility through low-covariance regional pairing, yielding a superior Sharpe ratio.

### The Hurdle Rate Crossover Phenomenon

Stress-testing portfolio performance across risk-free rate regimes ($R_f \in [8.4\%, 20.0\%]$) reveals a critical structural crossover at $R_f \approx 12.5\%$:

| Risk-Free Rate ($R_f$) | Portfolio A Sharpe | Portfolio B Sharpe | Superior Strategy | Dominance Rationale |
| :---: | :---: | :---: | :---: | :--- |
| **8.4% (Base Case)** | 1.12 | 1.85 | **Portfolio B** | Covariance diversification suppresses denominator |
| **10.0%** | 1.01 | 1.44 | **Portfolio B** | Covariance advantage narrows |
| **12.5% (Crossover)** | **0.83** | **0.83** | **Parity** | Threshold where yield dominates covariance |
| **15.0%** | 0.65 | -0.10 | **Portfolio A** | Portfolio B fails risk-free hurdle ($E[R_B] < R_f$) |
| **20.0% (High Inflation)** | **0.55** | **-7.92** | **Portfolio A** | Portfolio B collapses; Portfolio A yield remains positive |

### Ecological Rationality of Institutional Heuristics

In classical finance literature, geographic concentration and title anchoring are classified as cognitive biases (familiarity bias, status quo bias). However, in developing financial markets marked by structural inflation:

1. **The Volatility Paradox:** Cross-regional diversification requires allocating capital to secondary regional markets (Abuja, Kano, Ibadan) with lower capital appreciation and lower rental yields.
2. **Hurdle Collapse:** When inflation and risk-free rates rise above $12.5\%$, low-yield assets become economically unviable on a risk-adjusted basis.
3. **Adaptive Yield Defense:** By concentrating capital in prime Lagos commercial and high-density residential properties, fund managers secure robust nominal cash flows (rental yields exceeding $10\%$ with annual rent escalations) that survive high-hurdle macroeconomic environments.

Consequently, heuristic portfolio selection is not merely an irrational cognitive error; it is an **ecologically rational decision mechanism** adapted to severe institutional opacity and macroeconomic instability.

### Monetized Macroeconomic Cost

Notwithstanding its adaptive advantages in high-rate regimes, within normal macroeconomic conditions ($R_f = 8.4\%$), heuristic clustering imposes a measurable economic cost. Across the ₦21.3 trillion pension system (₦2.13 trillion maximum direct property allocation), sub-optimal covariance management represents an estimated **₦293.3 billion** in foregone risk-adjusted utility over a five-year investment horizon.

---

## Repository Architecture and Directory Map

This monorepo is organized into modular packages separating analytical engines, raw data, compiled drafts, and programmatic outputs:

```
pfa-portfolio-research/
├── dissertation/                   # Canonical academic dissertation source files
│   ├── dissertation.md             # Consolidated markdown manuscript (2,080 lines)
│   ├── dissertation.latex          # XeLaTeX template (Latin Modern typography)
│   ├── chapters/                   # Modular chapter source files (Chapters 1-5)
│   ├── appendices/                 # Survey questionnaire and data tables
│   ├── references.md               # Harvard-style reference bibliography
│   ├── defense_presentation.html   # Interactive HTML5/Reveal.js slide deck
│   └── defense_presentation.pptx   # 16:9 widescreen PowerPoint defense deck
│
├── packages/                       # Computational packages
│   ├── generator/                  # Synthetic property universe generation
│   │   ├── config.py               # Macro parameters, tariffs, and risk premiums
│   │   ├── metrics_calculator.py   # TAC, NOI, Cap Rate, and Return functions
│   │   ├── generate_universe.py    # Log-normal sampling of 80 properties
│   │   ├── validate_universe.py    # Suite of 9 statistical sanity tests
│   │   └── freeze_universe.py      # Immutable benchmark locking
│   │
│   ├── optimizer/                  # Analytical engine and optimization core
│   │   ├── clean_analyze_responses.py  # Survey parsing and weight calibration
│   │   ├── covariance.py           # Covariance matrix and Ledoit-Wolf shrinkage
│   │   ├── heuristic_engine.py     # EBA scoring and Portfolio A construction
│   │   ├── mvo_optimizer.py        # Combinatorial BIP integer optimizer
│   │   ├── monte_carlo.py          # 10,000-path Cholesky GBM simulation engine
│   │   ├── statistical_tests.py    # Paired t-tests, BCa bootstrap, and sensitivity
│   │   ├── generate_outputs.py     # LaTeX tables and publication charts generator
│   │   ├── generate_html_deck.py   # Standalone HTML presentation builder
│   │   └── generate_pptx_deck.py   # PowerPoint deck generator via python-pptx
│   │
│   └── utils/                      # Document processing utilities
│       └── extract_dissertation.py # Extraction and table formatting pipeline
│
├── data/                           # Data repositories
│   ├── calibration/                # Historical submarket return series (CBRE/PenCom)
│   ├── frozen/                     # Read-only frozen 80-asset universe files
│   │   ├── property_universe.csv
│   │   ├── property_covariance_matrix.csv
│   │   └── market_indices_returns.csv
│   ├── market-reports/             # Primary institutional PDF market reports
│   └── questionnaire/              # PFA survey instrument and raw responses
│
├── outputs/                        # Programmatic outputs and figures
│   ├── dissertation.pdf            # Compiled canonical dissertation PDF (A4, 12pt)
│   ├── charts/                     # High-resolution PNG figures (Figures 2.1 to 4.8)
│   ├── tables/                     # Programmatically generated LaTeX tables
│   ├── portfolios/                 # Holdings JSON files (Portfolios A and B)
│   └── simulation_results/         # Monte Carlo path arrays and summary metrics
│
├── build_pdf.sh                    # Automated offline PDF build pipeline
├── architecture.md                 # System, data-flow, and mathematical architecture
├── CODEBASE.md                     # File-by-file codebase specification
├── PRD_Portfolio_Optimization_System.md # Product requirements document
└── TDD_Portfolio_Optimization_System.md # Technical design and validation document
```

---

## Document Catalog

| Document | File Path | Format | Description |
| :--- | :--- | :--- | :--- |
| **Dissertation PDF** | [outputs/dissertation.pdf](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/dissertation.pdf) | PDF (XeLaTeX) | Canonical final manuscript (A4, Latin Modern, doublespaced, formal title page, 10 figures embedded). |
| **Dissertation Markdown** | [dissertation/dissertation.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/dissertation/dissertation.md) | Markdown | Consolidated full-text dissertation manuscript compatible with GitHub rendering and static web engines. |
| **Interactive Defense Deck** | [dissertation/defense_presentation.html](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/dissertation/defense_presentation.html) | HTML5 / CSS3 | Self-contained, responsive presentation deck with embedded visualizations, metrics, and navigation. |
| **PowerPoint Defense Deck** | [dissertation/defense_presentation.pptx](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/dissertation/defense_presentation.pptx) | PPTX | 16:9 widescreen presentation deck formatted with institutional color schemes and summary tables. |
| **System Architecture Guide** | [architecture.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/architecture.md) | Markdown | Detailed system architecture, data-flow pipeline, mathematical formulations, and Mermaid diagrams. |
| **Codebase Reference Map** | [CODEBASE.md](file:///home/isla-jr/Documents/se-workspace/pfa-portfolio-research/CODEBASE.md) | Markdown | Module-by-module documentation of classes, methods, inputs, outputs, and validation tests. |

---

## Replication and Build Instructions

### Environment Setup

The analytical engine requires Python 3.10 or higher. PDF compilation requires Pandoc and a working TeX Live distribution with XeLaTeX.

```bash
# Clone the repository
git clone https://github.com/islajr/pfa-portfolio-research.git
cd pfa-portfolio-research

# Create and activate Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install required numerical and statistical packages
pip install numpy scipy pandas scikit-learn matplotlib seaborn python-pptx
```

### Executing the Empirical Pipeline

To reproduce the analysis from raw survey data through Monte Carlo simulations:

```bash
# Step 1: Clean survey data, calibrate heuristic weights, and build covariance matrix
python3 packages/optimizer/clean_analyze_responses.py
python3 packages/optimizer/covariance.py

# Step 2: Construct Heuristic Portfolio A and Integer MVO Portfolio B
python3 packages/optimizer/heuristic_engine.py
python3 packages/optimizer/mvo_optimizer.py

# Step 3: Execute the 10,000-path stochastic Monte Carlo simulation engine
python3 packages/optimizer/monte_carlo.py

# Step 4: Run statistical hypothesis tests, BCa bootstrap, and sensitivity analysis
python3 packages/optimizer/statistical_tests.py

# Step 5: Render publication charts and LaTeX tables
python3 packages/optimizer/generate_outputs.py
```

### Compiling the Canonical Dissertation PDF

The dissertation manuscript is compiled into an academic A4 PDF via `build_pdf.sh`, which invokes Pandoc and XeLaTeX using the custom template in `dissertation/dissertation.latex`:

```bash
# Ensure build script is executable
chmod +x build_pdf.sh

# Compile dissertation PDF
./build_pdf.sh
```

The script automatically maps remote asset URLs to local paths, enforces Latin Modern typography, centers the opening title page, suppresses redundant caption numbering, and produces `outputs/dissertation.pdf`.

### Generating Presentation Decks

To re-generate the presentation assets:

```bash
# Build standalone HTML5 presentation deck
python3 packages/optimizer/generate_html_deck.py

# Build PowerPoint presentation deck
python3 packages/optimizer/generate_pptx_deck.py
```

---

## Citation Specifications

If referencing this research or utilizing the analytical codebase, please cite:

### BibTeX

```bibtex
@thesis{akinmokun2026heuristics,
  author       = {Akinmokun, Isaac Oluwaseun},
  title        = {Heuristics in Property Portfolio Selection Decisions of Nigerian Pension Funds: An Empirical Assessment of Adaptive Behaviour in Institutional Real Estate Allocation},
  school       = {Obafemi Awolowo University},
  year         = {2026},
  month        = {September},
  type         = {B.Sc. Dissertation},
  address      = {Ile-Ife, Nigeria},
  department   = {Department of Estate Management},
  faculty      = {Faculty of Environmental Design and Management}
}
```

### APA (7th Edition)

```text
Akinmokun, I. O. (2026). Heuristics in property portfolio selection decisions of Nigerian pension funds: An empirical assessment of adaptive behaviour in institutional real estate allocation (Unpublished undergraduate dissertation). Department of Estate Management, Obafemi Awolowo University, Ile-Ife, Nigeria.
```

---

## License and Academic Disclaimer

This project, its associated empirical datasets, and simulation codes are released under the [MIT License](LICENSE).

**Academic Disclaimer:** The synthetic 80-property universe and financial return series were calibrated using aggregated statistical parameters from CBRE and PenCom market reports for academic research and simulation purposes. They do not constitute formal investment advice or commercial solicitation.
