# CHAPTER THREE

# RESEARCH METHODOLOGY

## 3.1 Preamble

This chapter explicitly details the methods of research employed to investigate the role of heuristics in the property portfolio selection decision process of Nigerian pension funds. Resulting from the lack of available, granular data on the investment portfolios of Nigerian PFAs, and the need for a controlled environment to rigorously isolate and test the heuristics, a methodological choice was made. The study uses a calibrated simulation approach where a synthetic universe of 80 institutional-grade properties will be generated under statistical parameters derived from documented real market publications.

The rest of this chapter outlines the design of the research, data requirements, study population, census methodology, data collection, and data analysis methods, all geared towards achieving the aim of the study.

## 3.2 Research Design

This study will use a purely quantitative research method, in line with its aim and objectives. The design, however, is sequential, as it involves two components: the survey component, and the computational component. The survey component will involve the distribution of structured questionnaires to investment decision-makers across all headquarters of PenCom-licensed PFAs and CPFAs in Nigeria. The findings from this component will inform the parameters of the computational component, where they are calibrated and used to construct a portfolio. Both components are discussed further in subsequent sections of this chapter.

## 3.3 Data Requirements and Study Population

This section details the specifics of required data for this study and information about the study population, including the target population directory and the census methodology.

### 3.3.1 Data Requirements
The data requirement for this study varies by objective, as a single data source would fail to satisfy all the research objectives. Table 3.1 below maps each objective to its specific data requirement, type, and source.

## Table 3.1: Data Requirements Mapped to Research Objectives
| Objective | Data Required | Data Type | Source |
|---|---|---|---|
| I — Identify heuristics | Responses on selection criteria, decision scenarios, institutional practices | Primary qualitative and quantitative | Census questionnaire administered to PFA investment staff |
| II — Efficient frontier deviation | Property-level return and risk parameters; covariance matrix; optimal portfolio weights | Secondary/Synthetic | Calibrated synthetic universe; market publications for calibration |
| III — Comparative performance | Simulated return paths for both portfolios over 60-month horizon; six performance metrics | Synthetic/Computational | Monte Carlo simulation; GBM parameters from market index data |
| IV — Factors driving heuristics | Institutional, informational, and cognitive constraint data | Primary qualitative | Questionnaire Section D; open-ended responses |

Source: Author’s Research (2026)

### 3.3.2 Study Population

The study population comprises all Pension Fund Administrators (PFAs) and Closed Pension Fund Administrators (CPFAs) licensed and regulated by the National Pension Commission (PenCom) in Nigeria as of Q1, 2026. According to the official PenCom Directory, there are exactly 24 licensed pension fund operators in Nigeria at the time of research, consisting of 19 RSA (Open) Pension Fund Administrators and 5 Closed Pension Fund Administrators (CPFAs).

### 3.3.3 Target Population Directory and Census Methodology

Because the target population of licensed pension fund operators in Nigeria is relatively small ($N = 24$) and strictly defined by regulatory licensing, this study does not employ a sampling technique (such as probability or purposive sampling). Instead, the study adopts a **census methodology (complete enumeration)**, targeting the total population of all 24 PenCom-licensed PFAs and CPFAs nationwide.

Conducting a census rather than sampling offers key methodological advantages for this dissertation:
1. **Elimination of Sampling Error:** By enumerating the complete universe of licensed operators, the study eliminates sampling bias and sampling error, ensuring that empirical findings reflect the total institutional population of the Nigerian pension sector.
2. **Comprehensive Sector Coverage:** It ensures representation across both open RSA PFAs managing public pension funds and closed CPFAs managing corporate sponsor schemes, capturing variations in asset scale, governance structures, and direct real estate investment mandates.
3. **Institutional Depth:** Given the high concentration of institutional assets in Nigeria's pension industry, surveying key investment professionals (CIOs, Portfolio Managers, Senior Investment Analysts, and Risk Officers) across all 24 licensed operators guarantees maximum coverage of institutional direct real estate decision-making authority.

Table 3.2 presents the complete directory of the 24 PenCom-licensed pension fund operators constituting the census target population as of Q1 2026.

## Table 3.2: Complete Directory of PenCom-Licensed Pension Operators in Nigeria (Q1 2026)
| # | Operator Name | Category | Headquarters Address |
|---|---|---|---|
| 1 | Access ARM Pensions Limited | RSA PFA | 144, Broad Street / Plot 1298, Akin Adesola Street, Victoria Island, Lagos |
| 2 | CardinalStone Pensions Limited | RSA PFA | 358, Muritala Muhammed Way, Yaba, Lagos |
| 3 | Citizens Pensions Limited | RSA PFA | Plot 1667, Oyin Jolayemi Street, Victoria Island, Lagos |
| 4 | Crusader Sterling Pensions Limited | RSA PFA | 14B, Keffi Street, Off Awolowo Road, Ikoyi, Lagos |
| 5 | FCMB Pensions Limited | RSA PFA | Plot 121, Ahmadu Bello Way, Victoria Island, Lagos |
| 6 | Fidelity Pension Managers Limited | RSA PFA | Plot 1672, Olosa Street, Victoria Island, Lagos |
| 7 | Guaranty Trust Pension Managers Limited | RSA PFA | Plot 1669, Oyin Jolayemi Street, Victoria Island, Lagos |
| 8 | Leadway Pensure PFA Limited | RSA PFA | 121, Abeokuta Expressway, Ipaja / Plot 16, Commercial Avenue, Iganmu, Lagos |
| 9 | NLPC Pension Fund Administrators Limited | RSA PFA | 312, Ikorodu Road, Anthony, Lagos |
| 10 | Norrenberger Pensions Limited | RSA PFA | 11, Dunukofia Street, Area 11, Garki, Abuja |
| 11 | NUPEMCO (Nigeria Universities Pension Management Co. Ltd) | RSA PFA | Plot 813, Ahmadu Bello Way, Central Business District, Abuja |
| 12 | OAK Pensions Limited | RSA PFA | 266, Murtala Muhammed Way, Alagomeji, Yaba, Lagos |
| 13 | PAL Pensions (Pensions Alliance Limited) | RSA PFA | 24, Ikoyi Road, Ikoyi, Lagos |
| 14 | Premium Pension Limited | RSA PFA | Plot 1074, Ahmadu Bello Way, Cadastral Zone A09, Garki II, Abuja |
| 15 | Radix Pension Managers Limited | RSA PFA | 20, Isaac John Street, GRA, Ikeja, Lagos |
| 16 | Stanbic IBTC Pension Managers Limited | RSA PFA | Wealth House, Plot 1678, Olakunle Bakare Close, Victoria Island, Lagos |
| 17 | Tangerine APT Pensions Limited | RSA PFA | 23, Awolowo Road, Ikoyi, Lagos |
| 18 | Trustfund Pensions Plc | RSA PFA | Plot 820, Paschal Dozie Way, Central Business District, Abuja |
| 19 | Veritas Glanvills Pensions Limited | RSA PFA | 102, Lewis Street, Lagos Island, Lagos |
| 20 | Chevron CPFA Limited | CPFA | 2, Chevron Drive, Off Lekki-Epe Expressway, Lekki, Lagos |
| 21 | Nestle Nigeria Trust CPFA Limited | CPFA | 22/24, Industrial Avenue, Ilupeju, Lagos |
| 22 | Progress Trust CPFA Limited | CPFA | No. 1, Abebe Village Road, Iganmu, Lagos |
| 23 | Shell Nigeria CPFA Limited | CPFA | 21/22, Marina, Lagos |
| 24 | TotalEnergies EP Nigeria CPFA Limited | CPFA | Plot 35, Kofo Abayomi Street, Victoria Island, Lagos |

Source: Compiled by Author from National Pension Commission (PenCom) Official Directory (2026).

### 3.3.4 Secondary Data for Market Data Calibration
The function of collecting secondary data for this study is to calibrate the parameters of the
synthetic properties. These parameters include: the expected return, volatility, and correlation
parameters that define each of the market indices to which synthetic properties are assigned. This
distinction is important, because while the properties are synthetic, the risk structure connecting
them to documented market dynamics provides empirical grounding.

The market indices are defined along two dimensions: geography (Lagos Island; Lagos Mainland; Abuja FCT; Rivers State; Kano State; Oyo State) and asset type (Office; Commercial/Retail; Industrial; Residential). The index structure reflects a realistic segmentation of the Nigerian institutional property market.

### 3.3.5 Synthetic Property Universe Design

The property universe will contain 80 institutional-grade synthetic properties. This size is sufficient for the optimizer to make non-trivial choices and for the heuristic engine to reject a meaningful proportion of candidates while retaining a sufficient eligible pool. The size is also consistent with comparable simulation studies in the portfolio optimization literature (DeMiguel et al., 2009).

The universe will be constructed so that the heuristic scoring algorithm and the optimizer can plausibly select different portfolios. For the performance comparison to yield legitimate findings, the universe design has to contain properties that each heuristic will systematically exclude or

down-weight, but that the optimizer may select on the basis of risk-adjusted return. This is the condition that makes the research question testable. It is documented transparently here so that the reader understands that the universe composition follows from the research design, not from convenience.

### 3.3.5.1 Geographic Distribution
The universe will contain properties across five states in Nigeria, distributed as follows:

## Table 3.3: Property Universe Geographic Distribution
| State | Submarket | Target Share |
|---|---|---|
| Lagos | Island (Ikoyi, VI, Lekki) | 25% |
| Lagos | Mainland (Ikeja GRA) | 15% |
| FCT, Abuja | Central (Maitama, Asokoro, Wuse II) | 20% |
| Rivers | Port Harcourt (GRA, Rumuola) | 18% |
| Kano | Bompai/Sharada Industrial | 12% |
| Oyo | Ibadan (Ring Road, Bodija Commercial) | 10% |

The inclusion of non-Lagos/Abuja properties at 40% of the universe is a methodological requirement: without them, geographic availability bias cannot manifest as a measurable differentiator between the two portfolios.

### 3.3.5.2 Asset-type Distribution
Properties are distributed across five institutional asset classes as follows:

## Table 3.4: Property Universe Asset-type Distribution
| Asset Type | Target Share |
|---|---|
| Office Grade A/B | 28% |
| Commercial/Retail | 22% |
| Industrial/Logistics | 20% |
| Institutional Residential | 20% |
| Mixed-Use | 10% |

The deliberate inclusion of multiple asset types is consistent with real world choice scenarios. More significantly, however, this is aimed at testing whether asset preference heuristics impose a cost by excluding this class from consideration.

### 3.3.5.3 Title Status Distribution
The universe will include properties across the full spectrum of Nigerian title quality:

## Table 3.5: Property Universe Title Status Distribution
| Title Status | Target Share | Risk Premium |
|---|---|---|
| Certificate of Occupancy | 45% | 0.0% |
| Governor’s Consent | 25% | 0.5% |
| Gazette | 15% | 3.0% |
| Excision | 10% | 5.0% |
| Deed of Assignment | 5% | 2.0% |
3.3.5.4 Price Range Distribution

Prices span the full institutional range, from ₦150M to ₦3B, and are distributed to activate multiple price-related heuristics. This is detailed in the table below:

## Table 3.6: Property Universe Price Range Distribution
| Tiers | Price Range (₦) | Target Share |
|---|---|---|
| Accessible | 150M - 350M | 20% |
| Core | 350M - 800M | 45% |
| Premium | 800M - 1.5B | 25% |
| Trophy | 1.5B - 3B | 10% |

The presence of ‘premium’ and ‘trophy’ tiers specifically test the anchoring hypothesis that PFAs resist large single commitments above a psychological comfort ceiling. This, in itself, is a finding.

### 3.3.5.5 Property Condition Distribution
Conditions are distributed as detailed in the table below:

## Table 3.7: Property Universe Condition Distribution
| Condition | Target Share |
|---|---|
| New | 20% |
| Good | 50% |
| Fair | 20% |
| Needs Renovation | 10% |

The distribution of properties across multiple conditions is a measured choice to trigger certain heuristics or tendencies. Properties in ‘Fair’ and ‘Needs Renovation’ tier conditions possess lower NOI and cap rates, but some may still offer competitive total returns when located in high-appreciation market segments. The condition preference heuristic will be tested against this distribution.

## 3.4 Data Collection Methods

This section examines the methods of data collection for this study. As noted earlier, a sequenced quantitative approach is used in research design. To facilitate this, the section examines the main data collection instrument: the questionnaire. The questionnaire was chosen as the primary data collection tool because it best provides the necessary bridge between cognitive behaviour observation and computational analysis required by the study. Similarly, PFA investment managers are constrained by time, making a questionnaire more viable for the study population than other methods.

### 3.4.1 Questionnaire Instrument Design

The primary data collection instrument will be a structured questionnaire administered to PFA investment staff. The questionnaire is structured because the study requires responses that are directly comparable across respondents and directly translatable into the composite heuristic scores that feed the portfolio construction algorithm. The questionnaire consists of four sections of varying objectives and question types.

Section A collects data on the profile of the respondents and their fund details. This is important for assessing the quality of responses. Section B establishes the criteria for property selection, seeking to identify the presence of heuristics through the use of ordinal scales. Section C uses investment scenarios to determine the presence or absence of specific heuristics, and Section D is designed to elicit data about the factors that drive heuristic use.

## 3.5 Data Analysis Methods

This section specifies the analytical methods that will be applied to address each research objective. All formulae are numbered sequentially for reference in Chapter Four.

### 3.5.1 Heuristic Identification and Scoring (Objective 1)

This section addresses the identification and measurement of the specific heuristics employed by Nigerian PFA investment managers. Heuristic prevalence will be quantified through composite scores constructed from questionnaire Sections B and C, one composite score per heuristic per respondent. This is a prori index model rooted in the principle of Simple Additive Weighting (SAW) widely established in property investment literature for aggregating divergent decision variables (Hargitay & Yu, 1993).

The composite score formulae aggregate Likert-scale responses (Section B) and scenario responses (Section C), weighted by their theoretical weight on the underlying heuristic construct. Scenario responses carry higher weight (w₂ = 0.6 or w₃ = 0.4) than Likert items where applicable,

reflecting the literature's preference for ‘revealed’ over ‘stated’ measures of cognitive bias (Tversky & Kahneman, 1974).

**Formula 3.1: Anchoring Composite Score (ACS)**

$$
ACS_k = \frac{w_1 \cdot B3_k + w_2 \cdot C1_k}{w_1 + w_2}
$$ Where for respondent $k. B3$  = normalized response to Likert item B3 (title exclusion regardless of yield); $C1$  = normalized response to scenario C1 (anchoring scenario).

**Formula 3.2: Availability Composite Score (AVCS)**

$$
AVCS_k = \frac{w_1 \cdot B1\_rank\_loc_k + w_2 \cdot B2_k + w_3 \cdot C2_k}{w_1 + w_2 + w_3}
$$ Where: $B1_loc$  = inverted, normalized rank assigned to "location prestige" in item B1 (rank 1 = score 1.0; rank 8 = score 0.0); $B2$  = normalized response to Likert item B2 (location as risk proxy); $C2$  = normalized response to scenario C2 (geographic preference scenario).

**Formula 3.3: Representativeness Composite Score (RCS)**

$$
RCS_k = \frac{w_1 \cdot B1\_rank\_sector_k + w_2 \cdot C3_k}{w_1 + w_2}
$$ Where: $B1_{}rank_{}sector$  = inverted, normalized rank assigned to a momentum-relevant criterion in B1; $C3$  = normalized response to scenario C3 (momentum scenario).

**Formula 3.4: Herding Composite Score (HCS)**

$$
HCS_k = \frac{w_1 \cdot B1\_rank\_peer_k + w_2 \cdot B4_k + w_3 \cdot C4_k}{w_1 + w_2 + w_3}
$$ Where: $B1_{}peer$  = inverted, normalized rank assigned to "activity of peer PFAs" in B1; $B4$  = normalized response to Likert item B4 (portfolio similarity to peers); $C4$  = normalized response to scenario C4 (herding scenario).

**Formula 3.5: Population Prevalence Formula**

$$
\bar{H}_j = \frac{1}{N} \sum_{k=1}^{N} H_{j,k}
$$ Where: $H̄$ = mean composite score for heuristic j across all N respondents; $H_{j,k}$ = individual composite score for respondent k on heuristic j. A score of 0.5 represents a neutral midpoint. Scores above 0.5 indicate net heuristic-consistent responses; scores above 0.7 are classified as prevalent.

**Formula 3.6: Calibration of portfolio construction weights**

$$
\alpha_j = \frac{\bar{H}_j}{\sum_{i=1}^{4} \bar{H}_i}
$$ Where: $α$  = portfolio scoring weight for heuristic j (j = 1: anchoring; j = 2: availability; j = 3: representativeness; j = 4: herding), normalized so that $α₁ + α₂ + α₃ + α₄ = 1$. These weights are the direct methodological link between Phase 1 (survey) and Phase 2 (portfolio construction): the empirically observed heuristic weights from the questionnaire calibrate the scoring function used to construct the heuristic portfolio.

### 3.5.2 Financial Metrics Calculation

Before either portfolio can be constructed, individual financial metrics must be computed for each of the 80 properties in the universe. These metrics constitute the inputs to both the heuristic scoring function and the MVO optimizer. All formulae follow standard real estate investment analysis practice as documented in Geltner et al. (2014). This section serves all three objectives:

the metrics are used in portfolio construction (Objectives I and II), optimization (Objective II), and simulation (Objective III).

**Formula 3.7: Total Acquisition Cost (TAC)**
$$
TAC_i = P_i \times (1 + f_{agency} + f_{legal} + f_{consent,s_i})
$$ Where: $Pᵢ$ = asking price of property i (₦); $f_{agency}$ = 0.05 (agency fee, 5%); $f_{legal}$ = 0.05 (legal fee, 5%); $f_{consent,sᵢ}$ = Governor's Consent fee applicable to the state of property i (0.10 for Lagos; 0.05 for all other states). All three cost rates are calibrated from standard Nigerian institutional practice.

**Formula 3.8: Net Operating Income (NOI)**
$$
NOI_i = (GR_i \times (1 - v_{a_i})) - (GR_i \times m_{a_i})
$$ Where: $GRᵢ$ = estimated annual gross rent of property i (₦); $v_{aᵢ}$ = vacancy rate applicable to asset type aᵢ (0.05 for office; 0.04 for commercial; 0.05 for industrial; 0.06 for residential and mixed-use); $m_{aᵢ}$ = maintenance rate applicable to asset type aᵢ (0.10 for office and commercial; 0.08 for industrial; 0.15 for residential; 0.12 for mixed-use). Rates are calibrated from CBRE Nigeria (2023) and PenCom annual report data.

**Formula 3.9: Capitalization Rate**

$$
CR_i = \frac{NOI_i}{TAC_i}
$$

The capitalization rate measures the income yield on total investment cost and is the fundamental measure of current income return for a buy-and-hold investment.

**Formula 3.10: Expected Annual Return**

$$
E[R_i] = CR_i + \mu_{idx(i)}
$$ Where: $μ_{idx(i)}$ = mean annual capital appreciation for the market index to which property i is assigned, estimated as the arithmetic mean of the index's historical capital appreciation observations. This decomposes expected return into its two components: income return (cap rate) and capital return (index mean appreciation).

**Formula 3.11: Total Volatility**

$$
\sigma_i = \sigma_{idx(i)} + \delta^{title}_{tl_i} + \delta^{cond}_{cn_i}
$$ Where: $σ_{idx(i)}$ = standard deviation of annual total returns for property i's market index, computed from the historical index return series; $δ^{title}{tlᵢ}$ = title risk premium (0.000 for C of O; 0.005 for Governor's Consent; 0.030 for Gazette; 0.050 for Excision; 0.020 for Deed of Assignment); $δ^{cond}{cnᵢ}$ = condition risk premium (0.000 for New; 0.005 for Good; 0.015 for Fair; 0.030 for Needs Renovation). These property-specific premiums are added to the general market volatility to capture the extra risk introduced by the building's physical condition and legal title.

**Formula 3.12: Individual Sharpe Ratio**

$$
SR_i = \frac{E[R_i] - R_f}{\sigma_i}
$$ Where: $Rf$ = the approximate average Nigerian T-Bill rate over the study period. The study employs the average rate over the backtest period rather than the current spot rate because the performance comparison is set against the backtest market environment.

### 3.5.3 Portfolio Construction (Objective II)

Two portfolios will be constructed from the 80-property universe. Portfolio A uses the heuristic scoring algorithm calibrated from questionnaire findings (Phase 1 output). Portfolio B uses mean-variance optimization (the normative benchmark). Both portfolios observe PenCom's regulatory constraints.

For computational modelling purposes, a **representative fund AUM of ₦2 trillion** is adopted, derived from the modal AUM bracket reported across the census questionnaire responses (9 of the eligible respondents reported AUM above ₦2 trillion). Under the current PenCom Regulation on Investment of Pension Fund Assets (2024 revision), a maximum of **10% of total fund assets** may be invested in direct real estate. This yields a representative **real estate sub-portfolio budget of ₦200 billion** — the maximum permissible direct real estate allocation for a ₦2 trillion fund. This is the deployment ceiling common to both portfolios, and any property may not individually exceed ₦3 billion (the top of the synthetic universe's Trophy tier).

**Formula 3.13: Composite Heuristic Scoring Function**

$$
H(p_i) = \alpha_1 \cdot TS(p_i) + \alpha_2 \cdot LS(p_i) + \alpha_3 \cdot MS(p_i) + \alpha_4 \cdot PS(p_i)
$$ 
Where: $H(pᵢ) ∈ [0, 1]$ is the composite heuristic score for property i; 
$TS(pᵢ)$ = Title Score (1.0 if C of O; 0.5 if Governor's Consent; 0.0 otherwise); 
$LS(pᵢ)$ = Location Score (1.0 if prime tier; 0.6 if secondary; 0.2 if emerging); 
$MS(pᵢ)$ = Momentum Score, normalized recent return of property i's market index: 
$MS(pᵢ)$ = $(R_{idx(i),recent} − R_min) / (R_max − R_min)$; 
$PS(pᵢ)$ = Peer Score (1.0 if property i is in a submarket where ≥ 2 peer PFAs have reported holdings in the most recent PenCom quarterly data; 0.0 otherwise); 
$α₁–α₄$ = calibration weights from Formula 3.6.

**Formula 3.14: Portfolio Expected Return**

$$
E[R_P] = \sum_{i=1}^{80} w_i x_i E[R_i] \quad \text{where} \quad w_i = \frac{1}{\sum_{j=1}^{80} x_j}
$$
$$
\sigma_P = \sqrt{\mathbf{x}^T \boldsymbol{\Sigma} \mathbf{x}} \quad \text{where} \quad \mathbf{x} \text{ is the vector of } x_i w_i
$$

### 3.5.4 Performance Metrics Calculation

Six performance metrics will be computed for each simulation path across both portfolios. Table 3.8 below presents each metric with its formula and variable definitions.

## Table 3.8: Performance Metric Calculation
| #   | Metric                   | Formula                                                                  | Variables Defined                                                            |
| --- | ------------------------ | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| M1  | Cumulative Return        | $CR = \frac{V_P(60)}{V_P(0)} - 1$                                        | $V_P(0)$ = 1.0 (normalized); $V_P(60)$ = terminal value                      |
| M2  | Annualized Return (CAGR) | $CAGR = (1 + CR)^{1/5} - 1$                                              | $T$ = 5 years                                                                |
| M3  | Annualized Volatility    | $\sigma_P^{ann} = \text{std}(\{R_P(t)\}_{t=1}^{60}) \times \sqrt{12}$    | Monthly returns annualized by $√12$                                          |
| M4  | Sharpe Ratio             | $SR_P = \frac{CAGR - R_f}{\sigma_P^{ann}}$                               | $R_f$ = 0.15                                                                 |
| M5  | Maximum Drawdown         | $MDD = \max_{0 \leq t \leq 60} \frac{V_{peak}(t) - V_P(t)}{V_{peak}(t)}$ | $V_peak(t)$ = running maximum of portfolio value up to month t               |
| M6  | Diversification Ratio    | $DR = \frac{\sum_{i} w_i x_i \sigma_i}{\sigma_P^{ann}}$                  | Weighted avg individual vol / portfolio vol; higher = better diversification |

### 3.5.5 Statistical Significance Testing
To determine whether observed performance differences reflect a genuine structural advantage of one approach over the other, rather than simulation variance, two statistical procedures will be applied.

**Procedure 1:** Paired t-test (primary hypothesis test) H₀: E[SR_B] − E[SR_A] = 0 (no difference in Sharpe ratios) H₁: E[SR_B] − E[SR_A] > 0 (optimization produces higher Sharpe ratio) H2: E[SR_B] − E[SR_A] < 0 (heuristics produces higher Sharpe ratio)

**Formula 3.15: Paired t-test**

$$
t = \frac{\bar{d}}{s_d / \sqrt{n}}
$$

Where: $d  = SR_{B,s} − SR_{A,s}$ (difference in Sharpe ratios for simulation s); $d̄$ = mean difference across 10,000 simulations; $s_d$ = standard deviation of differences.

**Pre-registered practical significance threshold** 

Independent of the statistical test, this study pre-registers a practical significance threshold of $ΔSR$ = 0.05 Sharpe units. Statistical significance alone, with $N$ = 10,000 simulation paths, will detect even trivially small differences at high confidence levels. A Sharpe ratio difference smaller than 0.05 is considered practically negligible regardless of statistical significance. On a representative real estate sub-portfolio budget of ₦200 billion — the 10% PenCom-capped allocation from a ₦2 trillion fund — a 0.05 Sharpe unit improvement translates to approximately ₦1.5–2.0 billion in risk-adjusted value over five years. This is a financially material threshold at institutional scale. A finding is declared both statistically and practically significant only when p < 0.05 and $ΔSR$ ≥ 0.05.

**Procedure 2:** BCa Bootstrap Confidence Intervals Real estate returns are not normally distributed, as they consistently exhibit skewness and fat tails. This data structure directly contradicts the Gaussian assumption underlying the standard t-test. Therefore, bias-corrected and accelerated (BCa) bootstrap confidence intervals will be used as a non-parametric complement to the t-test (Efron & Tibshirani, 1994).The 95% BCa confidence interval for $ΔSR$ will be reported alongside the t-test result.