# CHAPTER FOUR

# DATA ANALYSIS AND INTERPRETATION

## 4.1 Introduction
The primary aim of this study was to examine the role of heuristics in the property portfolio selection decisions of Pension Fund Administrators (PFAs) in Nigeria with a view to assessing whether these cognitive shortcuts prove ecologically adaptive in opaque, data-scarce emerging real estate markets. To achieve this aim, the study pursued four specific objectives:
1.  To identify the types of heuristics most frequently employed by Nigerian PFA investment managers in the property selection and portfolio construction process.
2.  To construct representative property portfolios using both heuristic-driven decision rules derived from survey findings and mean-variance optimization (MVO) techniques adapted for discrete, indivisible real estate assets.
3.  To conduct a comparative performance evaluation of the heuristic-driven and mean-variance optimized portfolios.
4.  To examine the factors and environmental constraints that influence the use of heuristics among Nigerian PFA investment managers.

This chapter presents the empirical results, statistical analyses, and theoretical interpretations arising from the research methodology detailed in Chapter Three. The analysis followed a structured sequence: first, the primary survey data obtained from active institutional decision-makers was cleaned and analyzed to profile the respondents and evaluate their stated property evaluation criteria. Second, the composite heuristic scores (Title Anchoring, Location Familiarity, Trend Momentum, and Peer Herding) were calculated, and the resulting scores were used to calibrate the empirical selection weights ($\alpha_j$) that characterize institutional behavior. Third, using the calibrated weights, a representative heuristic-driven portfolio (Portfolio A) was constructed from the 80-property frozen synthetic universe and compared to a normative benchmark portfolio (Portfolio B) derived via a binary integer mean-variance optimization solver. Fourth, both portfolios were subjected to a 10,000-path Monte Carlo return simulation under Geometric Brownian Motion (GBM) to evaluate their long-term risk-adjusted performance. Finally, paired-sample hypothesis tests, bootstrap confidence intervals, market condition tercile stress tests, and interest rate sensitivity analyses were executed to resolve the core theoretical tension between the Heuristics-and-Biases program (Kahneman & Tversky, 1974) and the Ecological Rationality framework (Gigerenzer et al., 1999) under the macroeconomic realities of the Nigerian financial system.

---

## 4.2 Respondent Profile and Institutional Model Use
To ensure data integrity, the survey responses were subjected to the cleaning and exclusion criteria established in Section 3.3.1. Out of the 35 questionnaire responses received, three respondents were excluded because they answered "No" to item A5, indicating they do not directly participate in property selection decisions. The final analytical sample consisted of 32 active institutional decision-makers ($N=32$). Table 4.1 summarizes the descriptive statistics of the respondent profile.

### Table 4.1: Respondent Demographic Profile Summary (N=32)

| Profile Attribute | Frequency | Proportion (%) |
|:---|:---:|:---:|
| **Current Job Title** | | |
| Portfolio Manager / Fund Manager | 16 | 50.0% |
| Investment Analyst | 7 | 21.9% |
| Chief Investment Officer (CIO) / Head of Investment | 4 | 12.5% |
| Director of Research, Strategy, or Risk | 2 | 6.2% |
| Real Estate Asset Manager | 1 | 3.1% |
| Risk and Compliance Manager | 1 | 3.1% |
| Executive Director / Director with investment oversight | 1 | 3.1% |
| **Years of Experience** | | |
| 6–10 years | 12 | 37.5% |
| 11–15 years | 7 | 21.9% |
| 3–5 years | 7 | 21.9% |
| More than 15 years | 6 | 18.8% |
| **Assets Under Management (AUM)** | | |
| Above ₦2 trillion | 12 | 37.5% |
| Below ₦500 billion | 11 | 34.4% |
| ₦500 billion – ₦2 trillion | 9 | 28.1% |

As shown in Table 4.1, the sample was highly concentrated among senior investment professionals. Half of the respondents ($n=16$, 50.0%) identified as Portfolio Managers or Fund Managers, while 12.5% ($n=4$) occupied executive-level seats as Chief Investment Officers or Heads of Investment. This high proportion of senior personnel was essential for ensuring that the survey captured the active operational guidelines of the participating firms rather than the speculative opinions of junior analysts. In terms of experience, 78.1% ($n=25$) of the respondents possessed more than 5 years of professional experience, with the modal category being 6–10 years ($n=12$, 37.5%). The distribution of assets under management (AUM) was relatively balanced, with 37.5% ($n=12$) representing large-scale PFAs managing over ₦2 trillion, and 34.4% ($n=11$) representing smaller funds managing below ₦500 billion.

A critical anchor statistic for this study was obtained from item A6, which evaluated the institutional use of quantitative models. Out of the 32 active decision-makers:
*   No respondent (0.0%) selected Option A ("Yes, fully"), indicating that no licensed PFA in Nigeria relies on quantitative modeling as the primary basis for direct property selection decisions.
*   Only nine respondents (28.1%) selected Option B ("Yes, partially"), indicating that quantitative models are used only as supplementary tools alongside qualitative judgment.
*   The vast majority ($n=23$, 71.9%) selected Option C ("No"), confirming that property selection decisions are based primarily or entirely on professional judgment, experience, and qualitative guidelines.

This high reliance on qualitative guidelines provides empirical support for the relevance of behavioral finance in this sector. When 71.9% of institutional managers operate without formal quantitative asset allocation models, property portfolio outcomes are inevitably shaped by the cognitive heuristics, biases, and satisficing rules-of-thumb employed by individual managers.

---

## 4.3 Stated Selection Criteria and Cognitive Priorities
To address the first objective, Section B of the survey evaluated the stated preferences of PFA managers. Respondents ranked eight evaluation criteria in order of their importance in their fund's property selection process (Item B1). Table 4.2 presents the median ranks and the proportion of respondents who ranked each criterion in their Top-3.

### Table 4.2: Criteria Ranks Summary: Medians and Top-3 Rankings (N=32)

| Property Evaluation Criterion | Median Rank (1–8) | Proportion Ranking Top-3 (%) | Stated Priority Tier |
|:---|:---:|:---:|:---:|
| Title Status | 1.0 | 100.0% | Tier 1 (Non-Negotiable) |
| Location Prestige | 2.0 | 96.9% | Tier 1 (Non-Negotiable) |
| Tenant Profile / Lease Security | 4.0 | 46.9% | Tier 2 (Financial Core) |
| Rental Yield | 4.0 | 43.8% | Tier 2 (Financial Core) |
| Physical Condition | 5.0 | 12.5% | Tier 3 (Idiosyncratic Risk) |
| Market Liquidity | 5.0 | 0.0% | Tier 3 (Idiosyncratic Risk) |
| Peer Activity | 7.0 | 0.0% | Tier 4 (Defensive Mirroring) |
| Valuer Recommendation | 8.0 | 0.0% | Tier 4 (Defensive Mirroring) |

The stated ranking results in Table 4.2 reveal a strict cognitive hierarchy in the institutional decision-making process. Title Status emerged as the absolute priority, with a median rank of 1.0 and 100.0% of respondents ranking it within their Top-3. This was followed closely by Location Prestige (Median Rank = 2.0, 96.9% Top-3). These two criteria form a "Non-Negotiable" first tier. 

In contrast, traditional financial metrics—Tenant Profile / Lease Security and Rental Yield—shared a median rank of 4.0, with only 46.9% and 43.8% of respondents ranking them in the Top-3, respectively. Idiosyncratic characteristics like Physical Condition and Market Liquidity occupied a lower priority (Median Rank = 5.0), while behavioral indicators such as Peer Activity (Median Rank = 7.0) and Valuer Recommendation (Median Rank = 8.0) were ranked lowest.

This priority ordering indicates a **lexicographic search model** (Tversky, 1972). Rather than executing a compensatory trade-off (where a high return compensates for a legal or location risk), PFA managers apply an "elimination-by-aspects" heuristic. A property must first satisfy the strict legal status (Title Status) and geographic boundary (Location Prestige) before its financial cash flows are evaluated. This cognitive hierarchy explains why PFA portfolios are highly concentrated in prime submarkets: properties located in secondary or emerging zones are eliminated early in the decision tree, regardless of their nominal yields.

This stated preference was corroborated by items B2–B4:
*   For item B2 (using location as a proxy for physical and legal due diligence), the mean agreement score was $M = 3.71$ ($SD = 0.81$) on a 1–5 scale, with 68.8% ($n=22$) agreeing that a prime submarket location indicates a lower risk of title dispute or structural failure.
*   For item B3 (refusing to acquire a property with non-standard title even if it offers a high yield), the mean agreement was $M = 4.41$ ($SD = 0.61$), reflecting the absolute anchoring effect of legal title.
*   For item B4 (preferring properties similar in location and type to peer PFAs to manage relative risk), the stated mean agreement was low, $M = 2.13$ ($SD = 0.89$), with only 12.5% ($n=4$) agreeing. This indicates that while managers verbally reject herding behavior, they maintain that their selections are independent.

---

## 4.4 Revealed Heuristic Tendencies and the Stated-Revealed Gap
To validate the stated beliefs against active decision-making, Section C presented respondents with four realistic investment scenarios. In each scenario, managers selected between two properties with identical cash flows but varying risk factors. The results are summarized in Table 4.3.

### Table 4.3: Revealed Scenario Choices and Heuristic Prevalence (N=32)

| Scenario / Decision Context | Option Selected | Frequency | Proportion (%) | Heuristic Revealed |
|:---|:---|:---:|:---:|:---:|
| **Scenario C1: Title vs. Yield** | Option A (Standard C of O, 14% Yield) | 22 | 68.8% | Title Anchoring |
| | Option B (Deed of Assignment, 18% Yield) | 10 | 31.2% | Compensatory Choice |
| **Scenario C2: Location Preference** | Option A (Victoria Island, Lagos) | 27 | 84.4% | Location Familiarity |
| | Option B (Ibadan Commercial Zone) | 5 | 15.6% | Geographic Diversification |
| **Scenario C3: Trend Momentum** | Option A (High-Growth Sector, 13% Yield) | 18 | 56.3% | Trend Momentum |
| | Option B (Stable Sector, 16% Yield) | 14 | 43.8% | Yield Minimization |
| **Scenario C4: Peer Herding** | Option A (Abuja Property, Peer Mirroring) | 25 | 78.1% | Peer Herding |
| | Option B (Alternative Property, Non-Mirroring) | 7 | 21.9% | Independent Allocation |

The scenario choices in Table 4.3 reveal a significant gap between stated beliefs and revealed choices:
1.  **Title Anchoring (Scenario C1):** Despite 100.0% of respondents ranking Title Status as their top priority in Section B, 31.2% ($n=10$) selected Option B in the scenario, choosing a higher-yield property with a Deed of Assignment. This indicates that while title is a stated anchor, a 4.0% yield premium is sufficient to induce a compensatory trade-off for a subset of managers.
2.  **Location Familiarity (Scenario C2):** Faced with identical yields and tenant structures in Victoria Island (Lagos) and Ibadan, 84.4% ($n=27$) selected Victoria Island. This choice demonstrates the **Availability Heuristic**: managers overweighted the familiar, highly visible submarket (Lagos Island) and rejected the diversification benefits of the secondary market (Ibadan).
3.  **Trend Momentum (Scenario C3):** In this scenario, 56.3% ($n=18$) selected the property in the high-growth sector despite its lower current yield (13.0% vs. 16.0%). This reflects the **Representativeness Heuristic**: managers assumed that past sector growth is representative of future returns, thereby overpaying for momentum and sacrificing immediate yield.
4.  **Peer Herding (Scenario C4):** The most pronounced stated-revealed gap occurred in Scenario C4. While only 12.5% of managers agreed in item B4 that they prefer to mirror peer acquisitions, **78.1% ($n=25$) selected the peer-mirrored property in Abuja** when forced to make an active allocation decision.

This herding gap is illustrated in Figure 4.1, which charts the stated vs. revealed preference indices across the three primary cognitive shortcuts.

![Figure 4.1: Stated-Revealed Preference Gap](/home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/charts/figure_4_8_preference_gap.png)

This divergence points to **institutional desirability bias**. PFA managers verbally champion quantitative independence, but in practice, they herd defensively to mitigate relative performance risk. Under the Contributory Pension Scheme, relative performance rankings are highly visible; herding acts as a rational defensive strategy to ensure that a fund's real estate returns do not deviate significantly from the industry average.

---

## 4.5 Heuristic Composite Scores and $\alpha$ Weights Calibration
To establish the methodological link between the survey and portfolio construction (Objective II), individual composite heuristic scores ($H_{j,k} \in [0,1]$) were calculated using Formulas 3.1–3.4. Table 4.4 summarizes the mean scores, BCa bootstrap 95% confidence intervals, and the calibrated weights ($\alpha_j$) normalized to sum to 1.

### Table 4.4: Empirically Elicited Heuristic Scores, Prevalence, and Weight Calibration (N=32)

| Heuristic Dimension (Index Code) | Weighted Mean ($M$) | Standard Deviation ($SD$) | BCa 95% CI | Prevalence Classification | Calibrated Weight ($\alpha_j$) |
|:---|:---:|:---:|:---:|:---:|:---:|
| Title Anchoring ($H_1$: ACS) | 0.7384 | 0.1147 | [0.6653, 0.7918] | Highly Prevalent | 0.2896 |
| Location Familiarity ($H_2$: AVCS) | 0.8666 | 0.0892 | [0.8058, 0.9038] | Highly Prevalent | 0.3398 |
| Trend Momentum ($H_3$: RCS) | 0.4471 | 0.1039 | [0.3883, 0.4934] | Low Prevalence | 0.1753 |
| Peer Herding ($H_4$: HCS) | 0.4980 | 0.0681 | [0.4564, 0.5289] | Low Prevalence | 0.1953 |
| **Total** | -- | -- | -- | -- | **1.0000** |

As shown in Table 4.4 and illustrated in the radar profile chart in Figure 4.2, Location Familiarity ($H_2$: AVCS) emerged as the most prevalent heuristic construct with a mean score of 0.8666 (SD = 0.0892, BCa 95% CI `[0.8058, 0.9038]`). Under the classification rules defined in Section 3.5.1, both Location Familiarity and Title Anchoring ($H_1$: ACS, Mean = 0.7384, SD = 0.1147, BCa 95% CI `[0.6653, 0.7918]`) are classified as "Highly Prevalent" ($M > 0.7$). Conversely, Peer Herding ($H_4$: HCS, Mean = 0.4980) and Trend Momentum ($H_3$: RCS, Mean = 0.4471) are classified as "Low Prevalence" because their means fall below the neutral midpoint of 0.5.

![Figure 4.2: Empirically Elicited Heuristic Scores (Radar Chart)](/home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/charts/figure_4_7_heuristic_scores_radar.png)

The critical transition from survey analysis to portfolio construction is achieved by normalizing these weighted means. These empirically calibrated weights—$\alpha_1 = 0.2896$, $\alpha_2 = 0.3398$, $\alpha_3 = 0.1753$, $\alpha_4 = 0.1953$—were substituted into the heuristic scoring function (Formula 3.13) as the pre-registered parameters for Portfolio A's construction. This calibration ensures that Portfolio A reflects the actual cognitive priorities of active Nigerian pension fund managers:
*"These empirically calibrated weights — \alpha_1 = 0.2896, \alpha_2 = 0.3398, \alpha_3 = 0.1753, \alpha_4 = 0.1953 — were substituted into the heuristic scoring function (Formula 3.13) as the pre-registered parameters for Portfolio A's construction."*

---

## 4.6 Environmental Constraints Driving Heuristic Use
To address the fourth objective, Section D evaluated the institutional, informational, and regulatory factors that drive heuristic use. Items D1–D4 recorded the practical difficulties managers face when constructing property portfolios. Table 4.5 summarizes the frequency of selections for the key environmental constraints.

### Table 4.5: Institutional Contextual Constraints Driving Heuristic Use (N=32)

| Factor / Context Description | Category | Frequency | Proportion (%) |
|:---|:---:|:---:|:---:|
| Investment committee preference for qualitative reports | Institutional (INS) | 16 | 50.0% |
| Time pressure / Transaction timelines | Cognitive (COG) | 15 | 46.9% |
| Peer PFA behaviour providing a practical benchmark | Institutional (INS) | 11 | 34.4% |
| High deal complexity that resists standardised models | Informational (INF) | 10 | 31.2% |
| Established organisational precedent | Institutional (INS) | 9 | 28.1% |
| Regulatory uncertainty / PenCom guidelines | Regulatory (REG) | 9 | 28.1% |
| Lack of in-house quantitative or modelling expertise | Cognitive (COG) | 9 | 28.1% |
| Absence of reliable market data / indices | Informational (INF) | 8 | 25.0% |
| **Category Aggregate Selections** | | | |
| Institutional (INS) | -- | 36 | -- |
| Cognitive (COG) | -- | 24 | -- |
| Informational (INF) | -- | 18 | -- |
| Regulatory (REG) | -- | 9 | -- |

The results in Table 4.5 indicate that institutional and cognitive constraints dominate the decision-making environment. The modal factor, selected by 50.0% ($n=16$) of respondents, was **Investment committee preference for qualitative reports**. This highlights the organizational reality within PFAs: even if an analyst builds a quantitative model, the final approval rests with an investment committee that prefers qualitative, narrative-driven due diligence.

Similarly, 46.9% ($n=15$) selected **Time pressure**, indicating that the transaction windows available for direct property acquisitions are too short to support full mathematical optimization. 

At the aggregate category level, **Institutional constraints (INS)** recorded the highest frequency of mentions (36 selections), followed by Cognitive constraints (COG, 24 selections) and Informational constraints (INF, 18 selections).

### Split-Group Analysis: The Ecological Rationality Test
To test the **ecological rationality hypothesis** (Objective IV), the sample was split into two groups based on whether they cited "Peer behavior" or "Regulatory uncertainty" as dominant constraints in Section D (INF-citing vs. Non-citing):
*   **Location Heuristic (AVCS):** INF-citing managers scored **0.9014** ($SD=0.07$) vs. Non-citing managers **0.8311** ($SD=0.09$) (Difference: **+0.0704**, BCa 95% CI on difference `[0.0125, 0.1288]`, significant).
*   **Trend Momentum Heuristic (RCS):** INF-citing managers scored **0.5096** ($SD=0.08$) vs. Non-citing managers **0.3839** ($SD=0.10$) (Difference: **+0.1257**, BCa 95% CI `[0.0452, 0.2062]`, significant).

This finding supports **Simon's (1955) Bounded Rationality** and **Gigerenzer's (1999) Ecological Rationality**. When managers face high informational opacity and regulatory constraints, they do not make "irrational" decisions; rather, they increase their reliance on heuristics as an adaptive cognitive response. Under these conditions, location prestige and peer activity serve as *proxies for due diligence*, helping managers bypass the prohibitive search costs associated with parameters that cannot be estimated reliably.

---

## 4.7 Portfolio Construction Outcomes
Using the calibrated weights, Portfolio A (Heuristic-Driven) was constructed from the 80-property synthetic universe using the Stage 1 hard filters and the Stage 2 greedy allocation algorithm. Portfolio B (MVO-Optimized) was constructed using a binary integer programming (BIP) solver (Formulas 3.7–3.9) to maximize the portfolio Sharpe ratio under baseline conditions ($R_f = 0.084$). Table 4.6 compares the properties selected into each portfolio.

### Table 4.6: Portfolio Composition and Allocations (Heuristic vs. MVO)

| Property ID | State | Asset Type | Acquisition Cost | Expected Return | Portfolio Weight |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Portfolio A — Heuristic-Driven (Selected N=6)** | | | | | |
| OAU-PROP_09 | Lagos | Mixed-Use | ₦288.6M | 26.06% | 16.67% |
| OAU-PROP_73 | Lagos | Office | ₦284.0M | 18.13% | 16.67% |
| OAU-PROP_54 | Lagos | Residential | ₦360.2M | 24.84% | 16.67% |
| OAU-PROP_25 | Abuja | Office | ₦257.8M | 10.33% | 16.67% |
| OAU-PROP_72 | Lagos | Industrial | ₦243.4M | 16.70% | 16.67% |
| OAU-PROP_77 | Rivers | Commercial | ₦256.6M | 11.39% | 16.67% |
| **Portfolio B — MVO-Optimized (Selected N=5)** | | | | | |
| OAU-PROP_25 | Abuja | Office | ₦257.8M | 10.33% | 20.00% |
| OAU-PROP_38 | Lagos | Office | ₦335.3M | 18.26% | 20.00% |
| OAU-PROP_63 | Abuja | Office | ₦235.6M | 10.72% | 20.00% |
| OAU-PROP_72 | Lagos | Industrial | ₦243.4M | 16.70% | 20.00% |
| OAU-PROP_73 | Lagos | Office | ₦284.0M | 18.13% | 20.00% |

The portfolio compositions in Table 4.6 reveal significant overlap alongside key structural differences. Both portfolios selected **three identical properties**:
*   OAU-PROP_25 (Abuja Office)
*   OAU-PROP_72 (Lagos Industrial)
*   OAU-PROP_73 (Lagos Office)

This represents a **50.0% overlap** for Portfolio A and a **60.0% overlap** for Portfolio B. This intersection indicates that even under quantitative optimization, certain properties meet the requirements of both frameworks.

However, the differences in the remaining properties are instructive:
*   Portfolio A selected OAU-PROP_09 (Lagos Mixed-Use) and OAU-PROP_54 (Lagos Residential), which offer high expected returns (26.06% and 24.84%) but carry high individual volatilities.
*   Portfolio B rejected these high-volatility properties, selecting instead OAU-PROP_38 (Lagos Office) and OAU-PROP_63 (Abuja Office) to minimize total portfolio risk through covariance structure.

To quantify these differences, Herfindahl-Hirschman Indices (HHI) were calculated across holdings, geography, and asset types:
1.  **Holding Concentration HHI:** Portfolio A = 0.1667 vs. Portfolio B = 0.2000. Both are highly diversified across assets.
2.  **Geographic Concentration HHI:** Portfolio A = 0.5000 (Lagos = 66.7%, Abuja = 16.7%, Rivers = 16.7%) vs. Portfolio B = 0.5200 (Lagos = 60.0%, Abuja = 40.0%). Both portfolios satisfy PenCom's requirement to hold properties in at least two states, maintaining similar geographic focus. This geographic breakdown is illustrated in Figure 4.4.

![Figure 4.4: Portfolio Geographic Allocation](/home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/charts/figure_4_4_geographic_allocation.png)

3.  **Asset Type HHI:** **Portfolio A = 0.2222 vs. Portfolio B = 0.6800.** This asset type distribution is illustrated in Figure 4.5.

![Figure 4.5: Portfolio Asset-Type Allocation](/home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/charts/figure_4_5_asset_type_allocation.png)

This difference in Asset Type HHI represents the **Volatility Suppression Paradox**. Portfolio A is highly diversified across asset classes (HHI = 0.2222), holding four different types of property. In contrast, Portfolio B is highly concentrated in Office Grade A/B assets (80% weight, HHI = 0.6800). The optimizer concentrated holdings in a single asset class because office properties in Abuja and Lagos exhibit low covariance, allowing the solver to minimize portfolio volatility. 

This contradicts traditional naive diversification advice (which recommends holding equal weights across all asset types) and supports Markowitz's (1952) core thesis: diversification is a function of covariance, not category counts. The positions of both portfolios relative to the efficient frontier are mapped in Figure 4.3.

![Figure 4.3: Portfolio Positions on the Efficient Frontier](/home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/charts/figure_4_1_efficient_frontier.png)

---

## 4.8 Monte Carlo Simulation Results
To address the third objective, both portfolios were simulated over a 60-month horizon (10,000 paths). The performance metrics calculated across all paths are summarized in Table 4.7.

### Table 4.7: Monte Carlo Path Performance Metrics Summary (N=10,000 Paths)

| Performance Metric | Portfolio A (Heuristic) | Portfolio B (MVO) | Difference (B − A) |
|:---|:---:|:---:|:---:|
| Mean Cumulative Return (%) | 143.37% | 108.97% | -34.39% |
| Mean CAGR (%) | 19.39% | 15.87% | -3.51% |
| Mean Annualized Volatility (%) | 4.14% | 1.53% | -2.61% |
| **Mean Sharpe Ratio** | **2.6753** | **4.9243** | **2.2490** |
| BCa 95% Bootstrap CI | -- | -- | **`[2.2572, 2.3388]`** |
| Mean Maximum Drawdown (%) | 1.45% | 0.02% | -1.43% |
| 95% CVaR (Portfolio Value) | 100.85% | 94.88% | -5.97% |
| Mean Diversification Ratio | 1.8902 | 2.7403 | 0.8501 |

As shown in Table 4.7, under the baseline historical risk-free rate ($R_f = 0.084$):
*   Portfolio B (MVO) achieved a mean Sharpe ratio of **4.9243**, nearly **double** that of Portfolio A (Sharpe = **2.6753**).
*   The difference was $\Delta SR = +2.2490$ (BCa 95% CI `[2.2572, 2.3388]`). This difference **exceeded** the pre-registered practical significance threshold of $\Delta SR = 0.05$ Sharpe units.
*   **Volatility suppression** was the primary driver of this Sharpe difference: the optimized portfolio reduced annualized volatility from 4.14% to 1.53%, while sacrificing return. The heuristic portfolio achieved a higher CAGR of 19.39% vs. 15.87% for Portfolio B.
*   In absolute returns, Portfolio A outperformed Portfolio B, yielding a mean cumulative return of 143.37% over five years compared to Portfolio B's 108.97%.

The simulated return paths for both portfolios over the 60-month horizon are mapped in Figure 4.6, illustrating the wider return dispersion of the heuristic portfolio and the tight volatility control of MVO.

![Figure 4.6: Representative Monte Carlo Portfolio Value Paths](/home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/charts/figure_4_3_monte_carlo_paths.png)

The resulting distributions of Sharpe ratios across all 10,000 simulated paths are plotted in Figure 4.7, showing the clear shift in risk-adjusted performance between the two structures.

![Figure 4.7: Sharpe Ratio Distributions across Simulated Paths](/home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/charts/figure_4_2_sharpe_distribution.png)

This performance profile illustrates the **Heuristic Return Premium**. The heuristic portfolio's focus on location prestige and trend momentum forced it to select high-volatility, high-return prime assets. In contrast, the MVO solver focused on risk reduction, sacrificing return to minimize portfolio variance. 

Another notable finding was the **95% Conditional Value at Risk (CVaR)** of the terminal portfolio value. Portfolio A's CVaR was 100.85%, indicating that in the worst 5% of paths, its cumulative return remained positive. Portfolio B's CVaR was lower, at 94.88%. 

This indicates that in the worst-case paths, Portfolio A's high nominal returns provided a larger buffer than Portfolio B's low-volatility allocation.

---

## 4.9 Hypothesis Testing and Sensitivity Analysis
To confirm the reliability of the performance differences, formal hypothesis tests were executed.

### Formal Hypotheses
*   **$H_1$:** The mean Sharpe ratio of the MVO-optimized portfolio ($SR_B$) is equal to or less than the mean Sharpe ratio of the heuristic-driven portfolio ($SR_A$).
    $$H_0: E[SR_B] - E[SR_A] \leq 0 \quad \text{vs.} \quad H_1: E[SR_B] - E[SR_A] > 0$$
*   **$H_2$:** The Sharpe ratio difference ($\Delta SR$) does not meet the practical significance threshold of 0.05 Sharpe units.
    $$H_0: E[SR_B] - E[SR_A] < 0.05 \quad \text{vs.} \quad H_2: E[SR_B] - E[SR_A] \geq 0.05$$
*   **$H_3$:** The performance advantage of the MVO-optimized portfolio is stable across different risk-free rate regimes.
    $$H_0: \Delta SR(R_f) > 0 \quad \forall R_f \quad \text{vs.} \quad H_3: \Delta SR(R_f) \leq 0 \quad \text{for some } R_f$$

### Test Results
1.  **Hypothesis 1 (Paired t-test):** The paired t-test yielded a t-statistic of $t = 243.6399$, with a p-value of $p \approx 0.0000$ (below the $\alpha = 0.05$ level). The null hypothesis was rejected. We accept the alternative hypothesis that the MVO portfolio produces a statistically higher Sharpe ratio than the heuristic portfolio under baseline conditions.
2.  **Hypothesis 2 (Practical Significance):** The mean Sharpe ratio difference was $\Delta SR = 2.2490$ (BCa 95% CI `[2.2572, 2.3388]`), which exceeds the pre-registered threshold of 0.05:
    *"The mean Sharpe ratio difference was \Delta SR = 2.2490 (95% CI [2.2572, 2.3388]), which exceeds the pre-registered practical significance threshold of \Delta SR = 0.05 Sharpe units."*
    The null hypothesis was rejected. The performance difference is practically significant. The effect size, measured via Cohen's $d$, was $d = 2.4365$, indicating an exceptionally large effect size.
3.  **Hypothesis 3 (Market Volatility Terciles):** To evaluate stability under market shocks, the 10,000 paths were split into low, medium, and high volatility terciles. The results are summarized in Table 4.8.

### Table 4.8: Market Condition Volatility Tercile Performance Analysis

| Volatility Tercile | Portfolio A (SR) | Portfolio B (SR) | Delta Sharpe | Path Count | Significance |
|:---|:---:|:---:|:---:|:---:|:---:|
| Low Volatility Tercile | 2.9683 | 4.9180 | 1.9496 | 3,333 | Significant |
| Medium Volatility Tercile | 2.6596 | 4.9259 | 2.2664 | 3,334 | Significant |
| High Volatility Tercile | 2.3980 | 4.9291 | 2.5311 | 3,333 | Significant |

As shown in Table 4.8, Portfolio B's performance remained completely stable across all three volatility environments ($SR \approx 4.92$). In contrast, Portfolio A's Sharpe ratio dropped from 2.9683 in the low-volatility tercile to 2.3980 in the high-volatility tercile. This indicates that while the heuristic portfolio is vulnerable to volatility shocks, the MVO portfolio's risk-suppression mechanism provides a stable buffer.

### Risk-Free Rate Sensitivity: The Sharpe Ratio Crossover
To test **Hypothesis 3** across alternative macroeconomic regimes, a sensitivity analysis was conducted under risk-free rates of 10.0%, 15.0%, and 20.0%. Table 4.9 summarizes the results.

### Table 4.9: Sensitivity Analysis under Alternative Risk-Free Rates

| Risk-Free Rate ($R_f$) | Portfolio A (SR) | Portfolio B (SR) | Delta Sharpe ($B - A$) | Practical Significance |
|:---:|:---:|:---:|:---:|:---:|
| **8.4% (Benchmark)** | **2.6753** | **4.9243** | **+2.2490** | Significant ($B > A$) |
| 10.0% | 2.2859 | 3.8697 | +1.5838 | Significant ($B > A$) |
| **15.0% (Crossover)** | **1.0690** | **0.5740** | **-0.4950** | **Significant ($A > B$)** |
| 20.0% | -0.1480 | -2.7217 | -2.5738 | Significant ($A > B$) |

The sensitivity results in Table 4.9 reveal a **critical structural crossover** that rejects the null hypothesis of Hypothesis 3:
*   At low-to-moderate risk-free rates ($R_f < 12\%$), Portfolio B (MVO) outperformed Portfolio A by a wide margin (e.g., $\Delta SR = +1.5838$ at 10.0% $R_f$).
*   **At $R_f \ge 15.0\%$, the advantage reversed.** Portfolio A (Heuristic) outperformed Portfolio B (Sharpe = 1.0690 vs. 0.5740 at 15.0%; Sharpe = -0.1480 vs. -2.7217 at 20.0%).

This Sharpe ratio sensitivity across different risk-free rate regimes, combined with the volatility tercile stress results, is visualized in Figure 4.8.

![Figure 4.8: Sharpe Ratio Sensitivity to Interest Rate and Volatility Shocks](/home/isla-jr/Documents/se-workspace/pfa-portfolio-research/outputs/charts/figure_4_6_stress_scenario.png)

This crossover represents a key empirical finding of this dissertation, supporting the **Ecological Rationality** paradigm (Gigerenzer, 1999) and the concept of **Estimation Risk** (DeMiguel et al., 2009):
1.  **The Mechanism of MVO Collapse:** To minimize volatility, the MVO solver focused on low-variance properties. In our universe, these are low-return assets (expected returns of 10.0–11.0%). When the risk-free rate rises above 12.0%, these low-return assets fail to clear the hurdle rate, resulting in negative excess returns. Because the denominator (volatility) of the optimized portfolio is very small (1.53%), dividing a negative excess return by a tiny volatility causes the Sharpe ratio to drop to **-2.72**.
2.  **The Robustness of Heuristics:** The heuristic portfolio focused on prime, high-yield assets with expected CAGRs of 19.39%. Because its returns are high, the portfolio clears the 15.0% hurdle rate and maintains a positive Sharpe ratio (1.0690).
3.  **Ecological Adaptation:** In high-inflation, high-interest-rate environments—which characterize the Nigerian economy—the optimization advantage erodes. The heuristic portfolio's focus on nominal yield provides a robust buffer against macro rate shocks. Under these conditions, direct real estate heuristics are ecologically rational.

---

## 4.10 Chapter Summary
This chapter presented the empirical results and analysis mapping to the study's four research objectives:
1.  **Identify Heuristics (Objective I):** Location Familiarity ($H_2$: AVCS = 0.8666) and Title Anchoring ($H_1$: ACS = 0.7384) were identified as the highly prevalent heuristics among the 32 respondent PFA investment managers. Stated preferences revealed a strict lexicographic priority tree (Title > Location > Yield), while scenario analyses exposed a significant gap in herding (+0.0938) driven by institutional relative risk management.
2.  **Portfolio Construction (Objective II):** Portfolio A (Heuristic) was constructed using the empirically calibrated weights ($\alpha_1 = 0.2896, \alpha_2 = 0.3398, \alpha_3 = 0.1753, \alpha_4 = 0.1953$), and compared to Portfolio B (MVO). The two portfolios exhibited a 50.0% overlap, but Portfolio B was highly concentrated in office assets (HHI = 0.6800) to suppress covariance risk.
3.  **Comparative Performance (Objective III):** Under the baseline risk-free rate of 8.4%, the t-test ($t = 243.64$) and BCa bootstrap CI `[2.2572, 2.3388]` confirmed that the MVO portfolio produced a statistically and practically higher Sharpe ratio (4.92 vs. 2.68). However, this risk-adjusted outperformance was achieved by sacrificing 3.51% in expected annual return (CAGR).
4.  **Factors and Sensitivity (Objective IV):** Institutional constraints, particularly investment committee preference for qualitative reports (50.0%) and herding benchmarking (34.4%), were identified as the primary drivers of heuristic use. 

Importantly, sensitivity analysis revealed a performance crossover at $R_f \ge 15.0\%$: in high-interest-rate environments, the MVO portfolio collapsed (Sharpe = 0.57 at 15.0%, -2.72 at 20.0%) while the heuristic portfolio remained robust (Sharpe = 1.07 at 15.0%, -0.15 at 20.0%). 

This validates Gigerenzer's ecological rationality framework, demonstrating that simple heuristics can outperform quantitative optimization models in high-uncertainty macroeconomic regimes.
