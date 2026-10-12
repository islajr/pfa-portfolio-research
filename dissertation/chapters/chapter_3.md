# CHAPTER THREE

## RESEARCH METHODOLOGY

## 3.1 Preamble

This chapter clearly outlines the research techniques used to examine the role of heuristics in the process of property portfolio selection of the decision-making of Nigerian pension funds. Resulting from the lack of available, granular data on the investment portfolios of Nigerian PFAs, and the need for a controlled environment to rigorously isolate and test the heuristics, a methodological choice was made. The paper employs a calibrated simulation model in which a simulated universe of 80 institutional-level properties are created based on statistical parameters derived from reported real market publications.

The remainder of this chapter describes the research design, data requirements, study population, sampling methods, data collection and data analysis methods all aimed at fulfilling the purpose of the research.

## 3.2 Research Design

This study uses a purely quantitative research method, in line with its aim and objectives. The design, however, is sequential, as it involves two components: the survey component, and the computational component. The survey component involves the distribution of questionnaires to the headquarters of licensed PFAs with active real estate portfolios. The findings from this component inform the parameters of the computational component, where they are calibrated and used to construct a portfolio. Both components are discussed further in subsequent sections of this chapter.

## 3.3 Data Requirements and Study Population

This section details the specifics of required data for this study and information about the study population, including sampling frame, sample size, and sampling techniques.

### 3.3.1 Data Requirements

The data requirement for this study varies by objective, as a single data source would fail to satisfy all the research objectives. Table 3.1 below maps each objective to its specific data requirement, type, and source.

**Table 3.1: Objectives Data Requirement**

| **Objective** | **Data Required** | **Data Type** | **Data Source** |
| :--- | :--- | :--- | :--- |
| Identify heuristics | Selection criteria rankings, Likert responses, scenario responses, institutional process descriptions | Primary | Questionnaire administered to PFA investment staff |
| Construct portfolios | Property-level expected returns, individual volatilities, covariance matrix, optimal portfolio weights | Synthetic / Secondary | Calibrated 80-property universe; market index return series |
| Comparative performance | Simulated return paths for both portfolios over 60-month horizon; six performance metrics | Synthetic / Computational | Monte Carlo simulation using GBM calibrated from market index data |
| Factors driving heuristics | Selection criteria rankings, Likert responses | Primary | Questionnaire administered to PFA investment staff |

*Source: Author's Research (2026)*

### 3.3.2 Study Population

The study population is all Pension Fund Administrators licensed by the National Pension Commission as of Q1, 2026. According to the PenCom Directory, there are 24 licensed PFAs (closed and otherwise) as at Q1, 2026.

### 3.3.3 Sampling Frame and Sampling Technique

Because the target population of licensed pension fund operators in Nigeria is small ($N = 24$) and strictly defined in terms of regulations, this study does not use sampling. Rather, this study uses a census approach, which focuses on the total population of all 24 PFAs and CPFAs across the country that are licensed by PenCom. Table 3.2 below details a complete directory of the study population:

**Table 3.2: Complete Directory of PenCom-Licensed PFAs in Nigeria (Q1, 2026)**

| **#** | **Operator Name** | **Headquarters Address** |
| :---: | :--- | :--- |
| 1 | Access Pensions Limited | Plot 339, Tarkwa Crescent, Off Adetokunbo Crescent, Wuse II, Abuja |
| 2 | CardinalStone Pensions Limited | 12A, Adeola Hopewell Street, Victoria Island, Lagos |
| 3 | Citizens Pensions Limited | 3rd Floor, The Beacon Plot 15, Admiralty Way, Lekki Phase 1, Lagos |
| 4 | Crusader Sterling Pensions Limited | 14B, Keffi Street, Off Awolowo Road, Ikoyi, Lagos |
| 5 | FCMB Pensions Limited | 207, Zakaria Maimalari Street, Central Business District, Abuja |
| 6 | Fidelity Pension Managers Limited | Plot 668, Ahmodu Tijjani Close, Victoria Island, Lagos |
| 7 | Guaranty Trust Pension Managers Limited | 172B, Moshood Olugbani Street, Victoria Island, Lagos |
| 8 | Leadway Pensure PFA Limited | 121/123 Funsho Williams Street, Surulere, Lagos |
| 9 | NLPC Pension Fund Administrators Limited | 312A, Ikorodu Road, Anthony, Lagos |
| 10 | Norrenberger Pensions Limited | 22, Otukpo Street, Area 11, Garki, Abuja |
| 11 | NUPEMCO (Nigeria Universities Pension Management Co. Ltd) | 772, Dahiru Mustapher Boulevard, Abuja |
| 12 | OAK Pensions Limited | 266, Murtala Muhammed Way, Alagomeji, Yaba, Lagos |
| 13 | Parthian Pensions Limited | 1st Floor, Nij House, Plot 20, Adeyemo Alakija Street, Victoria Island, Lagos |
| 14 | Premium Pension Limited | 4, Agwu Close, Off Faskari Crescent, Area 3, Garki, Abuja |
| 15 | Radix Pension Managers Limited | 20, Isaac John Street, GRA, Ikeja, Lagos |
| 16 | Stanbic IBTC Pension Managers Limited | 6F, Walter Carrington Crescent, Victoria Island, Lagos |
| 17 | Tangerine APT Pensions Limited | Plot 266, Cadastral AO, Garki, Abuja |
| 18 | Trustfund Pensions Plc | Plot 1363, Samuel Ademulegun Avenue, Central Business District, Abuja |
| 19 | Veritas Glanvills Pensions Limited | 1698, Oyin Jolayemi Street, Victoria Island, Lagos |
| 20 | Chevron CPFA Limited | 2, Chevron Drive, Off Lekki-Epe Expressway, Lekki, Lagos |
| 21 | Nestle Nigeria Trust CPFA Limited | 22/24, Industrial Avenue, Ilupeju, Lagos |
| 22 | Progress Trust CPFA Limited | No. 1, Abebe Village Road, Iganmu, Lagos |
| 23 | Shell Nigeria CPFA Limited | 21, Lugard Avenue, Ikoyi, Lagos |
| 24 | TotalEnergies EP Nigeria CPFA Limited | Plot 30, Kofo Abayomi Street, Victoria Island, Lagos |

*Source: PenCom CPFA Directory (2026)*

### 3.3.4 Secondary Data for Market Data Calibration

The function of collecting secondary data for this study is to calibrate the parameters of the synthetic properties. These parameters include: the expected return, volatility, and correlation parameters that define each of the market indices to which synthetic properties are assigned. This distinction is important, because while the properties are synthetic, the risk structure connecting them to documented market dynamics provides empirical grounding.

The market indices are defined along two dimensions: geography (Lagos Island; Lagos Mainland; Abuja FCT; Rivers State; Kano State; Oyo State) and asset type (Office; Commercial/Retail; Industrial; Residential). The index structure reflects a realistic segmentation of the Nigerian institutional property market.

### 3.3.5 Synthetic Property Universe Design

There are 80 institutional-grade synthetic properties in the property universe. This size is large enough to allow the optimizer to make non-trivial decisions and to have the heuristic engine reject a significant percentage of the candidates and still have a large enough eligible pool. The size is also in line with similar simulation studies in the portfolio optimization literature (DeMiguel et al., 2009).

The universe is designed in such a way that the heuristic scoring algorithm and the optimizer can reasonably pick various portfolios. To obtain valid results in the performance comparison, the universe design must include properties that will be systematically eliminated or down-weighted by each heuristic, but which the optimizer can pick on the basis of risk-adjusted return. This is what renders the research question testable. It is recorded openly herein such that the reader appreciates that the composition of the universe is based on the research design, rather than on convenience.

#### 3.3.5.1 Geographic Distribution

The universe contains properties across five states in Nigeria, distributed as follows:

**Table 3.3: Property Universe Geographic Distribution**

| **State** | **Submarket** | **Target Share** |
| :--- | :--- | :---: |
| Lagos | Island (Ikoyi, VI, Lekki) | 25% |
| Lagos | Mainland (Ikeja GRA) | 15% |
| FCT, Abuja | Central (Maitama, Asokoro, Wuse II) | 20% |
| Rivers | Port Harcourt (GRA, Rumuola) | 18% |
| Kano | Bompai/Sharada Industrial | 12% |
| Oyo | Ibadan (Ring Road, Bodija Commercial) | 10% |

*Source: Author's Research (2026)*

The inclusion of non-Lagos/Abuja properties at 40% of the universe is a methodological requirement: without them, geographic availability bias cannot manifest as a measurable differentiator between the two portfolios.

#### 3.3.5.2 Asset-type Distribution

Properties are distributed across five institutional asset classes as follows:

**Table 3.4: Property Universe Asset-type Distribution**

| **Asset Type** | **Target Share** |
| :--- | :---: |
| Office Grade A/B | 28% |
| Commercial/Retail | 22% |
| Industrial/Logistics | 20% |
| Institutional Residential | 20% |
| Mixed-Use | 10% |

*Source: Author's Research (2026)*

The deliberate inclusion of multiple asset types is consistent with real-world choice scenarios. More significantly, however, this is aimed at testing whether asset preference heuristics impose a cost by excluding certain classes from consideration.

#### 3.3.5.3 Title Status Distribution

The universe includes properties across the full spectrum of Nigerian title quality:

**Table 3.5: Property Universe Title Status Distribution**

| **Title Status** | **Target Share** | **Risk Premium** |
| :--- | :---: | :---: |
| Certificate of Occupancy | 45% | 0.0% |
| Governor's Consent | 25% | 0.5% |
| Gazette | 15% | 3.0% |
| Excision | 10% | 5.0% |
| Deed of Assignment | 5% | 2.0% |

*Source: Author's Research (2026)*

#### 3.3.5.4 Price Range Distribution

Prices span the full institutional range, from ₦150M to ₦3B, and are distributed to activate multiple price-related heuristics. This is detailed in Table 3.6 below:

**Table 3.6: Property Universe Price Range Distribution**

| **Tiers** | **Price Range (₦)** | **Target Share** |
| :--- | :--- | :---: |
| Accessible | 150M – 350M | 20% |
| Core | 350M – 800M | 45% |
| Premium | 800M – 1.5B | 25% |
| Trophy | 1.5B – 3B | 10% |

*Source: Author's Research (2026)*

The presence of 'premium' and 'trophy' tiers specifically test the anchoring hypothesis that PFAs resist large single commitments above a psychological comfort ceiling.

#### 3.3.5.5 Property Condition Distribution

Conditions are distributed as detailed in Table 3.7 below:

**Table 3.7: Property Universe Condition Distribution**

| **Condition** | **Target Share** |
| :--- | :---: |
| New | 20% |
| Good | 50% |
| Fair | 20% |
| Needs Renovation | 10% |

*Source: Author's Research (2026)*

The distribution of properties across multiple conditions is a measured choice to trigger certain heuristics or tendencies. Properties in 'Fair' and 'Needs Renovation' conditions possess lower NOI and cap rates, but some may still offer competitive total returns when located in high-appreciation market segments. The condition preference heuristic is tested against this distribution.

## 3.4 Data Collection Methods

This part discusses data collection procedures in this study. As noted earlier, a sequenced quantitative approach is used in research design. To enable this, the section discusses the primary data collection tool: the questionnaire. The questionnaire was selected as the main instrument of data collection since it is the best instrument to give the bridge between cognitive behaviour observation and computational analysis needed by the study. Equally, PFA investment managers have limited time and thus a questionnaire would be more feasible to the study population as opposed to other tools.

### 3.4.1 Questionnaire Instrument Design

The main data gathering tool is a structured questionnaire that was given to PFA investment personnel. The questionnaire is designed in such a way that the study needs answers that can be easily compared among the respondents and easily translated into the composite heuristic scores that input the portfolio construction algorithm. The questionnaire is divided into four sections that have different objectives and types of questions.

Section A gathers information on the profile of the respondents and their fund information. This plays a role in determining the quality of responses. Section B defines the property selection criteria, which aims at determining the existence of heuristics by using ordinal scales. Section C relies on investment scenarios to identify the existence or absence of certain heuristics and Section D is aimed at eliciting information on factors that motivate the use of heuristics.

## 3.5 Data Analysis Methods

This section specifies the analytical methods that were applied to address each research objective. All formulae are numbered sequentially for reference in Chapter Four.

### 3.5.1 Heuristic Identification and Scoring (Objective I)

This part deals with the identification and quantification of the particular heuristics used by investment managers at Nigerian PFAs. The heuristic prevalence was measured using composite scores made up of questionnaire Sections B and C, with one composite score per heuristic per respondent. This is a priori index model based on the concept of Simple Additive Weighting (SAW) that has been extensively developed in the literature of property investment to combine divergent decision variables (Hargitay & Yu, 1993).

The composite score formulae combine Likert-scale responses (Section B) and scenario responses (Section C) with their theoretical weight on the underlying heuristic construct. The weight of scenario responses ($w_2 = 0.6$ or $w_3 = 0.4$) is greater than Likert items where feasible because the literature favors revealed over stated measures of cognitive bias (Tversky & Kahneman, 1974).

**Formula 3.1: Anchoring Composite Score (ACS)**

$$ACS_k = \frac{w_1 \cdot B3_k + w_2 \cdot C1_k}{w_1 + w_2} \tag{3.1}$$

Where for respondent $k$: $B3_k$ = normalized response to Likert item B3 (title exclusion regardless of yield); $C1_k$ = normalized response to scenario C1 (anchoring scenario).

**Formula 3.2: Availability Composite Score (AVCS)**

$$AVCS_k = \frac{w_1 \cdot B1_{loc,k} + w_2 \cdot B2_k + w_3 \cdot C2_k}{w_1 + w_2 + w_3} \tag{3.2}$$

Where: $B1_{loc,k}$ = inverted, normalized rank assigned to "location prestige" in item B1 (rank 1 = score 1.0; rank 8 = score 0.0); $B2_k$ = normalized response to Likert item B2 (location as risk proxy); $C2_k$ = normalized response to scenario C2 (geographic preference scenario).

**Formula 3.3: Representativeness Composite Score (RCS)**

$$RCS_k = \frac{w_1 \cdot B1_{sector,k} + w_2 \cdot C3_k}{w_1 + w_2} \tag{3.3}$$

Where: $B1_{sector,k}$ = inverted, normalized rank assigned to a momentum-relevant criterion in B1; $C3_k$ = normalized response to scenario C3 (momentum scenario).

**Formula 3.4: Herding Composite Score (HCS)**

$$HCS_k = \frac{w_1 \cdot B1_{peer,k} + w_2 \cdot B4_k + w_3 \cdot C4_k}{w_1 + w_2 + w_3} \tag{3.4}$$

Where: $B1_{peer,k}$ = inverted, normalized rank assigned to "activity of peer PFAs" in B1; $B4_k$ = normalized response to Likert item B4 (portfolio similarity to peers); $C4_k$ = normalized response to scenario C4 (herding scenario).

**Formula 3.5: Population Prevalence Formula**

$$\bar{H}_j = \frac{1}{N} \sum_{k=1}^{N} H_{j,k} \tag{3.5}$$

Where: $\bar{H}_j$ = mean composite score for heuristic $j$ across all $N$ respondents; $H_{j,k}$ = individual composite score for respondent $k$ on heuristic $j$. A score of 0.5 represents a neutral midpoint. Scores above 0.5 indicate net heuristic-consistent responses; scores above 0.7 are classified as prevalent.

**Formula 3.6: Calibration of Portfolio Construction Weights**

$$\alpha_j = \frac{\bar{H}_j}{\sum_{i=1}^{4} \bar{H}_i} \tag{3.6}$$

Where: $\alpha_j$ = portfolio scoring weight for heuristic $j$ ($j = 1$: anchoring; $j = 2$: availability; $j = 3$: representativeness; $j = 4$: herding), normalized so that $\alpha_1 + \alpha_2 + \alpha_3 + \alpha_4 = 1$. These weights are the direct methodological link between Phase 1 (survey) and Phase 2 (portfolio construction): the empirically observed heuristic weights from the questionnaire calibrate the scoring function used to construct the heuristic portfolio.

### 3.5.2 Financial Metrics Calculation

To build either of the portfolios, one needs to compute individual financial metrics of all 80 properties in the universe. These measures are the inputs to both the heuristic scoring function and MVO optimizer. All the formulae are in accordance with the standard practice of real estate investment analysis as reported in Geltner et al. (2014). This part fulfills all three purposes: the metrics are applied in the construction of a portfolio (Objectives I and II), in optimization (Objective II) and in simulation (Objective III).

**Formula 3.7: Total Acquisition Cost (TAC)**

$$TAC_i = P_i \times (1 + f_{agency} + f_{legal} + f_{consent,s_i}) \tag{3.7}$$

Where: $P_i$ = asking price of property $i$ (₦); $f_{agency}$ = 0.05 (agency fee, 5%); $f_{legal}$ = 0.05 (legal fee, 5%); $f_{consent,s_i}$ = Governor's Consent fee applicable to the state of property $i$ (0.10 for Lagos; 0.05 for all other states). All three cost rates are calibrated from standard Nigerian institutional practice.

**Formula 3.8: Net Operating Income (NOI)**

$$NOI_i = (GR_i \times (1 - v_{a_i})) - (GR_i \times m_{a_i}) \tag{3.8}$$

Where: $GR_i$ = estimated annual gross rent of property $i$ (₦); $v_{a_i}$ = vacancy rate applicable to asset type $a_i$ (0.05 for office; 0.04 for commercial; 0.05 for industrial; 0.06 for residential and mixed-use); $m_{a_i}$ = maintenance rate applicable to asset type $a_i$ (0.10 for office and commercial; 0.08 for industrial; 0.15 for residential; 0.12 for mixed-use). Rates are calibrated from CBRE Nigeria (2023) and PenCom annual report data.

**Formula 3.9: Capitalization Rate**

$$CR_i = \frac{NOI_i}{TAC_i} \tag{3.9}$$

The cap rate measures the income yield on total investment cost and is the fundamental measure of current income return for a buy-and-hold investment.

**Formula 3.10: Expected Annual Return**

$$E[R_i] = CR_i + \mu_{idx(i)} \tag{3.10}$$

Where: $\mu_{idx(i)}$ = mean annual capital appreciation for the market index to which property $i$ is assigned, estimated as the arithmetic mean of the index's historical capital appreciation observations. This decomposes expected return into its two components: income return (cap rate) and capital return (index mean appreciation).

**Formula 3.11: Total Volatility**

$$\sigma_i = \sigma_{idx(i)} + \delta^{title}_{tl_i} + \delta^{cond}_{cn_i} \tag{3.11}$$

Where: $\sigma_{idx(i)}$ = standard deviation of annual total returns for property $i$'s market index, computed from the historical index return series; $\delta^{title}_{tl_i}$ = title risk premium (0.000 for C of O; 0.005 for Governor's Consent; 0.030 for Gazette; 0.050 for Excision; 0.020 for Deed of Assignment); $\delta^{cond}_{cn_i}$ = condition risk premium (0.000 for New; 0.005 for Good; 0.015 for Fair; 0.030 for Needs Renovation). These property-specific premiums are added to the general market volatility to capture the extra risk introduced by the building's physical condition and legal title.

**Formula 3.12: Individual Sharpe Ratio**

$$SR_i = \frac{E[R_i] - R_f}{\sigma_i} \tag{3.12}$$

Where: $R_f$ = the approximate average Nigerian T-Bill rate over the study period. The study employs the average rate over the backtest period rather than the current spot rate (~27.5% as at Q1 2026) because the performance comparison is set against the backtest market environment.

### 3.5.3 Portfolio Construction (Objective II)

Two portfolios were constructed from the 80-property universe. Portfolio A uses the heuristic scoring algorithm calibrated from questionnaire findings (Phase 1 output). Portfolio B uses mean-variance optimization (the normative benchmark). Both portfolios observe PenCom's regulatory constraints and both are subject to the same ₦10 billion fund budget.

**Formula 3.13: Composite Heuristic Scoring Function**

$$H(p_i) = \alpha_1 \cdot TS(p_i) + \alpha_2 \cdot LS(p_i) + \alpha_3 \cdot MS(p_i) + \alpha_4 \cdot PS(p_i) \tag{3.13}$$

Where: $H(p_i) \in [0, 1]$ is the composite heuristic score for property $i$; $TS(p_i)$ = Title Score (1.0 if C of O; 0.5 if Governor's Consent; 0.0 otherwise); $LS(p_i)$ = Location Score (1.0 if prime tier; 0.6 if secondary; 0.2 if emerging); $MS(p_i)$ = Momentum Score, normalized recent return of property $i$'s market index: $MS(p_i) = (R_{idx(i),recent} - R_{min}) / (R_{max} - R_{min})$; $PS(p_i)$ = Peer Score (1.0 if property $i$ is in a submarket where $\geq 2$ peer PFAs have reported holdings in the most recent PenCom quarterly data; 0.0 otherwise); $\alpha_1 – \alpha_4$ = calibration weights from Formula 3.6.

**Formula 3.14: Portfolio Expected Return**

$$E[R_P] = \sum_{i=1}^{80} w_i x_i E[R_i] \quad \text{where} \quad w_i = \frac{1}{\sum_{j=1}^{80} x_j} \tag{3.14}$$

### 3.5.4 Performance Metrics Calculation

Each of the two portfolios has six performance measures calculated based on each simulation path. All the metrics are shown in Table 3.8 below with their formulae and variable definitions.

**Table 3.8: Performance Metric Calculation**

| **#** | **Metric** | **Formula** | **Variables** |
| :---: | :--- | :--- | :--- |
| M1 | Cumulative Return | $CR_P = V_P(60) / V_P(0) - 1$ | $V_P(0) = 1.0$; $V_P(60)$ = terminal value |
| M2 | Annualized Return | $AR_P = (1 + CR_P)^{1/T} - 1$ | $T = 5$ years |
| M3 | Annualized Volatility | $\sigma_P = \text{std}(r_{P,t}) \times \sqrt{12}$ | Monthly returns annualized by $\sqrt{12}$ |
| M4 | Sharpe Ratio | $SR_P = (AR_P - R_f) / \sigma_P$ | $R_f = 0.15$; sensitivity at 0.10 and 0.20 |
| M5 | Maximum Drawdown | $MDD_P = \max_t [(V_{peak}(t) - V_P(t)) / V_{peak}(t)]$ | $V_{peak}(t)$ = running maximum to month $t$ |
| M6 | Diversification Ratio | $DR_P = \sum_i w_i \sigma_i / \sigma_P$ | Weighted average vol / portfolio vol |

*Source: Author's Research (2026)*

### 3.5.5 Statistical Significance Testing

Two statistical procedures were used to decide whether or not observed performance differences are due to a real structural advantage of one approach over the other, and not due to simulation variance.

**Procedure 1: Paired t-test (primary hypothesis test)**

$$H_0: E[SR_B] - E[SR_A] = 0 \quad \text{(no difference in Sharpe ratios)}$$

$$H_1: E[SR_B] - E[SR_A] > 0 \quad \text{(optimization produces higher Sharpe ratio)}$$

$$H_2: E[SR_B] - E[SR_A] < 0 \quad \text{(heuristics produces higher Sharpe ratio)}$$

**Formula 3.15: Paired t-test**

$$t = \frac{\bar{d}}{s_d / \sqrt{n}} \tag{3.15}$$

Where: $d_s = SR_{B,s} - SR_{A,s}$ (difference in Sharpe ratios for simulation $s$); $\bar{d}$ = mean difference across 10,000 simulations; $s_d$ = standard deviation of differences.

**Pre-registered practical significance threshold**

Regardless of the statistical test, this study pre-registers a practical significance level of 0.05 Sharpe units. Even trivially small differences will be detected with high confidence levels with $N = 10,000$ simulation paths alone. A difference in Sharpe ratio of less than 0.05 is deemed practically insignificant irrespective of statistical significance. A 0.05 Sharpe unit increase on a ₦10 billion capital base would be equivalent to a risk-adjusted ₦75–100 million over five years — a significant mark for a fund of this size. A statistically and practically significant finding is only announced when $p < 0.05$ and $\Delta SR \geq 0.05$.

**Procedure 2: BCa Bootstrap Confidence Intervals**

Real estate returns are not normally distributed, since they always exhibit skewness and fat tails. This data structure is directly in violation of the Gaussian assumption of the standard t-test. Thus, a non-parametric complement to the t-test was employed through bias-corrected and accelerated (BCa) bootstrap confidence intervals (Efron & Tibshirani, 1994). The t-test was reported with the 95% BCa confidence interval of $\Delta SR$.