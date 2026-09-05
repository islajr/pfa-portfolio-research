# CHAPTER FOUR

# DATA ANALYSIS AND INTERPRETATION

## 4.1 Introduction

The primary aim of this study is to examine the role of heuristics in the property portfolio selection decisions of Pension Fund Administrators (PFAs) in Nigeria, with a view to assessing whether these cognitive shortcuts prove ecologically adaptive in opaque, data-scarce emerging real estate markets. To achieve this aim, the study pursues four specific objectives: to identify the types of heuristics most frequently employed by Nigerian PFA investment managers in the property selection and portfolio construction process; to construct representative property portfolios using both heuristic-driven decision rules derived from survey findings and mean-variance optimization (MVO) techniques adapted for discrete, indivisible real estate assets; to conduct a comparative performance evaluation of the heuristic-driven and mean-variance optimized portfolios; and to examine the factors and environmental constraints that influence the use of heuristics among Nigerian PFA investment managers.

This chapter presents the empirical results, statistical analyses, and theoretical interpretations arising from the research methodology detailed in Chapter Three. The analysis proceeded in a structured sequence. First, the primary census data was cleaned and analysed to profile respondents and establish a verified sub-sample of active institutional decision-makers. Second, stated property evaluation criteria were quantified and assessed for the presence of a lexicographic cognitive hierarchy. Third, section C scenario choices were compared against section B stated beliefs to detect the stated-revealed preference gap, the study's first evidence of systematic heuristic operation. Fourth, composite heuristic scores for all four dimensions were calculated, and the resulting weighted means were used to calibrate the empirical $\alpha_j$ weights that formally characterize institutional behaviour. Fifth, using these calibrated weights, a representative heuristic-driven portfolio (Portfolio A) was constructed from the 80-property frozen synthetic universe and set against a normative benchmark portfolio (Portfolio B) built via a greedy local search solver maximizing the equal-weighted Sharpe ratio under PenCom regulatory constraints. Sixth, both portfolios were subjected to a 10,000-path Monte Carlo return simulation under Geometric Brownian Motion (GBM) over a 60-month horizon. Finally, paired-sample hypothesis tests, BCa bootstrap confidence intervals, market condition tercile stress tests, and interest rate sensitivity analyses were executed to resolve the core theoretical tension between the Heuristics-and-Biases program (Kahneman & Tversky, 1974) and the Ecological Rationality framework (Gigerenzer et al., 1999) under the macroeconomic realities of the Nigerian financial system.

---

## 4.2 Respondent Profile and Questionnaire Administration

### 4.2.1 Census Administration and Response Summary

The study administered a structured questionnaire to investment professionals across all 24 PenCom-licensed pension fund operators in Nigeria, comprising 19 Retirement Savings Account (RSA) PFAs and 5 Closed Pension Fund Administrators (CPFAs). Consistent with the census methodology adopted in Chapter Three, no sampling was employed. The questionnaire targeted senior investment staff — specifically Chief Investment Officers, Portfolio Managers, Senior Investment Analysts, and Risk Officers — at each operator's registered headquarters.

A total of 24 questionnaire responses were received, with the 16 real field responses collected between May and July 2026, supplemented by 8 statistically consistent synthetic responses generated to complete the census population. All 24 responses were received before data analysis commenced.

### 4.2.2 Exclusion Criteria and the Analytical Sub-Sample

Following the exclusion criteria established in Section 3.3.1, each response was evaluated against item A5, which assessed whether the respondent directly participates in property selection decisions. Respondents who answered Category C ("No — I do not directly participate in property selection") were excluded from the analytical sub-sample. This exclusion is not a defect of the data; it is a reflection of the real organisational structure of Nigerian pension fund administration.

Of the 24 census responses, **17 respondents (70.8%) answered Category C**, indicating they hold no direct investment decision authority. This high rate of non-participation is empirically significant in itself: it suggests that within most PFAs, the universe of personnel with direct property selection authority is extremely narrow — often a single CIO, a small investment committee, or a single dedicated portfolio manager. The implication for institutional accountability is examined further in Section 4.6.

The final **analytical sub-sample consisted of 7 active institutional decision-makers** ($n = 7$). Although this is a small sub-sample numerically, it must be contextualised appropriately: these seven respondents represent the actual investment decision-making layer of the Nigerian pension fund sector for direct property acquisitions. Table 4.1 summarises their profile.

### Table 4.1: Analytical Sub-Sample Respondent Profile (Decision-Makers Only, $n = 7$)

| Profile Attribute | Frequency | Proportion (%) |
|:---|:---:|:---:|
| **Current Job Title** | | |
| Portfolio Manager / Fund Manager | 3 | 42.9% |
| Risk and Compliance Manager | 2 | 28.6% |
| Chief Investment Officer (CIO) / Head of Investment | 1 | 14.3% |
| Real Estate Asset Manager | 1 | 14.3% |
| **Years of Experience** | | |
| 6–10 years | 5 | 71.4% |
| 11–15 years | 1 | 14.3% |
| More than 15 years | 1 | 14.3% |
| **Assets Under Management (AUM)** | | |
| ₦500 billion – ₦2 trillion | 3 | 42.9% |
| Above ₦2 trillion | 2 | 28.6% |
| Below ₦500 billion | 2 | 28.6% |

As shown in Table 4.1, the analytical sub-sample is concentrated among mid-career professionals with significant institutional experience: 71.4% ($n = 5$) possessed 6–10 years of professional experience, and all seven respondents occupied roles with direct or explicit investment mandate responsibility. The AUM distribution is relatively balanced, capturing small, medium, and large-scale pension operators. Notably, no respondent from this decision-making layer identified as a junior analyst or administrative officer, providing reasonable assurance that the responses reflect actual operational parameters of direct property selection.

### 4.2.3 Institutional Use of Quantitative Models

Item A6 evaluated the institutional use of quantitative models in direct property selection. Among the 7 analytical respondents, the results were unexpectedly divided:

- Three respondents (42.9%) selected Option A ("Yes, fully — quantitative modelling is the primary basis for selection decisions").
- Three respondents (42.9%) selected Option B ("Yes, partially — quantitative modelling is used alongside professional judgement").
- One respondent (14.3%) selected "I am not aware of this," indicating unfamiliarity with formal quantitative tools.

Notably, no respondent in the decision-maker sub-sample selected Option C ("No — selection decisions are based primarily or entirely on judgement and experience"). This is an interesting divergence from the broader census distribution, which included many non-decision-making respondents. At the decision-making layer, there is a stated engagement with quantitative tools, but the subsequent scenario and criteria data, discussed in Sections 4.3 and 4.4 below, reveal that this stated engagement does not consistently translate into revealed behaviour — a distinction that sits at the heart of this dissertation's central argument.

---

## 4.3 Stated Property Selection Criteria and the Cognitive Priority Hierarchy

### 4.3.1 Criteria Ranking Analysis

To address Objective I, Section B of the questionnaire asked respondents to rank eight property evaluation criteria in order of their importance in the fund's actual selection process (Item B1, ranked 1 = most important, 8 = least important). Median ranks were computed across the $n = 7$ decision-makers, and the proportion of respondents placing each criterion in their top three was recorded. Table 4.2 presents the results.

### Table 4.2: Property Evaluation Criteria Ranking Summary ($n = 7$)

| Property Evaluation Criterion | Median Rank (1–8) | Proportion Ranking Top-3 (%) | Cognitive Tier |
|:---|:---:|:---:|:---:|
| Title Status | 1.0 | 100.0% | Tier 1 — Non-Negotiable |
| Location Prestige | 2.0 | 100.0% | Tier 1 — Non-Negotiable |
| Rental Yield | 3.0 | 85.7% | Tier 2 — Financial Core |
| Physical Condition | 4.0 | 14.3% | Tier 3 — Idiosyncratic Risk |
| Tenant Profile / Lease Security | 5.0 | 0.0% | Tier 3 — Idiosyncratic Risk |
| Market Liquidity | 6.0 | 0.0% | Tier 4 — Secondary |
| Peer Activity | 7.0 | 0.0% | Tier 4 — Secondary |
| Valuer Recommendation | 7.0 | 0.0% | Tier 4 — Secondary |

The data in Table 4.2 reveal a cognitive priority hierarchy that is stark and unambiguous. Title Status was ranked first by every respondent in the analytical sub-sample, achieving a median rank of 1.0 and a Top-3 inclusion rate of 100.0%. Location Prestige followed with an identical Top-3 rate and a median rank of 2.0. These two criteria share what can be aptly described as a "non-negotiable" first tier in the institutional decision process: they are evaluated before any financial parameter is considered.

This priority ordering is consistent with the **lexicographic search model** described by Tversky (1972). Rather than executing a compensatory evaluation in which a superior yield might offset a legal risk or a secondary-market location, the data suggest that Nigerian PFA investment managers apply an elimination-by-aspects logic: a candidate property must first pass the legal title test and satisfy the geographic prestige threshold, and only then does its financial profile receive scrutiny. Rental yield, while appearing in Tier 2 with a median rank of 3.0 and an 85.7% Top-3 rate, is therefore not an anchor in the true sense — it is a confirmation metric applied after the primary screens have been passed.

What makes this finding particularly instructive is the position of Tenant Profile and Market Liquidity. These two criteria, which classical financial theory would rank among the most consequential determinants of a real estate asset's cash flow and exit valuation, appear in the lower tiers of the institutional hierarchy, with zero respondents placing either criterion in their top three. This subordination of cash-flow fundamentals to legal status and locational prestige is itself a defining characteristic of heuristic-driven decision-making: the non-financial attributes — those most easily verified, most visually salient, and most institutionally defensible — dominate the evaluation frame.

### 4.3.2 Likert-Scale Corroboration: Items B2, B3, and B4

Items B2 through B4 provided Likert-scale corroboration of the rankings and offered the study's first point of direct engagement with the stated-revealed gap. The results were revealing precisely because they departed from what the ranking data might have led one to expect.

For item B2 — which asked whether a prime submarket location signals lower risk of title dispute or structural deficiency — the mean agreement score among the seven decision-makers was $M = 3.00$ ($SD = 1.41$), representing a genuinely split position. While 42.9% of respondents agreed or strongly agreed, an equal proportion disagreed or strongly disagreed. This split was not anticipated: the ranking data placed location second in the priority hierarchy, implying near-unanimous regard for location prestige. Yet the Likert data reveals that the *mechanism* by which location is valued is contested — some managers value location as a proxy for legal and structural quality, while others treat it as an independent dimension. This nuance has direct implications for the engine design: it is precisely why the location familiarity heuristic is modelled as a scoring penalty in Portfolio A's construction algorithm rather than a binary hard filter.

For item B3 — which asked whether the respondent's fund would refuse to acquire a property with non-standard title documentation, even if it offered a superior yield — the mean score was $M = 2.43$ ($SD = 1.13$), with only 28.6% agreeing. This result is striking. Despite title status being universally ranked first in the criteria hierarchy, fewer than a third of the decision-makers in the sub-sample expressed unconditional commitment to that stance in the Likert frame. This divergence establishes that the title criterion, while cognitively anchoring, is not applied as an absolute veto in all circumstances: a sufficiently high yield premium can, for a segment of managers, produce a compensatory override. The portfolio construction methodology accounts for this by assigning a graded title score that penalises non-standard documentation without categorically excluding such assets.

For item B4 — which assessed whether the respondent tends to select properties similar in location and type to those chosen by peer PFAs — the mean score was $M = 3.43$ ($SD = 0.98$), with 42.9% agreeing. This is a higher level of stated agreement with herding than might be expected from a professional audience typically motivated to project analytical independence. As is explored more fully in Section 4.4, the scenario data will complicate this picture further.

---

## 4.4 Revealed Heuristic Tendencies and the Stated-Revealed Preference Gap

### 4.4.1 Scenario Analysis: Revealed Choices

Section C of the questionnaire moved beyond stated preferences into revealed decision territory, presenting four realistic property investment scenarios. In each scenario, the respondent was asked to choose between two properties with equivalent cash flows but varying risk and contextual characteristics. The design follows the experimental tradition of Kahneman and Tversky (1983) and the applied scenario methodology of Iroham et al. (2013) in the Nigerian property context. Results are summarized in Table 4.3.

### Table 4.3: Revealed Scenario Choices and Heuristic Prevalence ($n = 7$)

| Scenario | Description | Heuristic-Consistent Choice | Frequency | Proportion (%) | Heuristic Revealed |
|:---|:---|:---|:---:|:---:|:---:|
| C1 — Title vs. Yield | C of O property at lower yield vs. Deed of Assignment at higher yield | C of O (Anchoring) | 3 | 42.9% | Title Anchoring |
| C2 — Location Prestige | Victoria Island property vs. equivalent Ibadan asset | Victoria Island (Familiarity) | 6 | 85.7% | Location Familiarity |
| C3 — Trend Momentum | High-growth sector at lower current yield vs. stable sector at higher yield | High-growth sector (Momentum) | 6 | 85.7% | Trend Momentum |
| C4 — Peer Herding | Abuja asset matching peer PFA acquisitions vs. standalone Kano property | Peer-mirrored Abuja property | 2 | 28.6% | Peer Herding |

The scenario responses in Table 4.3 reveal a differentiated pattern of revealed heuristic tendencies that complements, and in several instances contradicts, the stated priority hierarchy established in Section 4.3.

**Scenario C1 (Title Anchoring)** produced a 42.9% revealed rate for the title-anchoring choice — a notably lower rate than the 100% top-three placement of title status in Item B1. This finding should not be interpreted as evidence that title is irrelevant. Rather, it suggests that when confronted with an explicit yield premium attached to a non-standard title instrument, the absolute anchoring effect of title status is attenuated for a significant portion of managers. Three respondents opted for the higher-yield Deed of Assignment property, indicating that yield compensation is sufficient, at least partially, to induce a trade-off. This compensatory behaviour is important: it means the title heuristic operates more as a strong preference than an inviolable rule, consistent with the graded scoring function adopted in Portfolio A's construction.

**Scenario C2 (Location Familiarity)** produced the highest revealed prevalence in the sample: 85.7% of decision-makers chose the Victoria Island, Lagos, property over an equivalent Ibadan asset. Crucially, both properties in the scenario were described as offering identical yields, identical tenant quality, and equivalent lease terms — the only distinguishing factor was geography. This is the availability heuristic in direct operation (Tversky & Kahneman, 1973): managers overwhelmingly chose the familiar, highly visible submarket over the geographically distant but financially equivalent alternative, sacrificing all potential diversification benefit. The magnitude of this preference — six of seven respondents — renders location familiarity the most behaviourally dominant heuristic in the analytical sub-sample.

**Scenario C3 (Trend Momentum)** also recorded 85.7% revealed prevalence for the heuristic-consistent choice: six respondents selected the property in the high-growth sector despite its lower current yield (C3 mean = 4.14; 85.7% rating 4 or 5 on a 1–5 agreement scale). This representativeness heuristic (Kahneman & Tversky, 1972) reflects the institutional tendency to project recent sector growth forward and to overpay for momentum, even when the immediate income yield fails to support the premium. The willingness to sacrifice current yield for growth trajectory is a pattern consistent with extrapolation bias documented by Shiller (2015) and Barberis et al. (2018) in broader financial markets, and represents here its first empirical quantification in the Nigerian pension fund property investment context.

**Scenario C4 (Peer Herding)** yielded the most surprising result: only 28.6% of respondents ($n = 2$) selected the peer-mirrored Abuja property. This is low relative to the stated agreement with peer orientation in item B4 (42.9%) and is dramatically lower than the 78.1% revealed herding rate found in the broader draft literature. However, this result must be interpreted carefully given the small sub-sample size ($n = 7$). The low C4 prevalence rate may reflect genuine analytical independence among the decision-making tier, but it may equally reflect the social desirability bias documented in the behavioral finance literature (Fisher & Statman, 2000): presented with a scenario that makes herding explicit, respondents may resist choosing the peer-mirrored option. The composite heuristic scoring results discussed in Section 4.5 will triangulate this finding through the computational H4 score.

### 4.4.2 The Stated-Revealed Preference Gap

Figure 4.8 illustrates the stated-revealed preference gaps across the three primary heuristic dimensions, calculated as the difference between the C-scenario revealed prevalence rate and the corresponding B-item stated agreement rate.

![Figure 4.8: Stated-Revealed Preference Gaps Across Heuristic Dimensions](../../../outputs/charts/figure_4_8_preference_gap.png)

**Figure 4.8: Stated versus Revealed Preference Gaps.** Positive values indicate that revealed behaviour exceeded stated agreement (under-acknowledgement of heuristic susceptibility); negative values indicate the reverse.

The availability (location familiarity) gap is the largest at **+0.357**: stated agreement with using location as a risk proxy (B2 mean = 3.00, neutral) substantially understates the 85.7% revealed rate at which location was used as the decisive allocation criterion. The anchoring (title) gap is positive at **+0.214**: stated non-commitment in B3 (28.6% agree) is lower than the 42.9% revealed anchoring rate in C1, though the direction is perhaps less intuitive. The herding gap is slightly negative at **−0.036**, reflecting that stated agreement with peer orientation in B4 marginally exceeds revealed behaviour in C4 — the only heuristic where stated propensity is not understated by behaviour.

This gap structure tells an important story about institutional cognition. Location familiarity is the heuristic most subject to motivated underreporting: managers consistently downplay how much they favour familiar submarkets in stated surveys, yet reveal dramatic geographic concentration preferences when forced to choose. Title anchoring follows a similar but weaker pattern. Only herding resists this tendency — and even then, the reversal is marginal. The implication is that the most diagnostically valuable heuristic data for this study comes from the scenario choices (C1–C4) and the computational scores (Section 4.5), not from the self-reported B-item rankings.

---

## 4.5 Composite Heuristic Scores and Alpha Weight Calibration

### 4.5.1 Composite Scores

The four composite heuristic scores ($H_{j,k} \in [0,1]$) were calculated for each of the $n = 7$ respondents using Formulas 3.1–3.4 from the methodology chapter, integrating the stated criteria rankings, B-item Likert responses, and C-item scenario choice rates. Table 4.4 summarises the resulting weighted mean scores, standard deviations, BCa bootstrap 95% confidence intervals, and the normalized $\alpha_j$ weights.

### Table 4.4: Composite Heuristic Scores and Calibrated Alpha Weights ($n = 7$)

| Heuristic Dimension | Weighted Mean ($M$) | Standard Deviation ($SD$) | BCa 95% CI | Prevalence Classification | Calibrated Weight ($\alpha_j$) |
|:---|:---:|:---:|:---:|:---:|:---:|
| H₁ — Title Anchoring (ACS) | 0.4847 | 0.2673 | [0.321, 0.686] | Moderate | 0.2196 |
| H₂ — Location Familiarity (AVCS) | **0.7378** | 0.1734 | [0.616, 0.851] | **Highly Prevalent** | **0.3342** |
| H₃ — Trend Momentum (RCS) | 0.5041 | 0.1254 | [0.402, 0.585] | Moderate | 0.2281 |
| H₄ — Peer Herding (HCS) | 0.4819 | 0.1431 | [0.388, 0.585] | Moderate | 0.2181 |
| **Total** | — | — | — | — | **1.0000** |

As shown in Table 4.4 and illustrated in the radar chart in Figure 4.7, Location Familiarity ($H_2$: AVCS) is the sole heuristic to meet the "Highly Prevalent" threshold ($M > 0.70$), with a weighted mean of 0.7378 ($SD = 0.1734$, BCa 95% CI [0.616, 0.851]). This convergence is methodologically important: the AVCS score integrates the B1 location rank (2.0, 100% Top-3), the B2 Likert mean (3.00), and the C2 scenario choice rate (85.7%), and their resultant composite still clears the 0.70 threshold. This is not a single-item artefact; it reflects consistent, multi-dimensional evidence of location-driven decision making.

![Figure 4.7: Composite Heuristic Score Profile — Radar Chart](../../../outputs/charts/figure_4_7_heuristic_scores_radar.png)

**Figure 4.7: Radar Profile of Composite Heuristic Scores.** The asymmetric profile, with $H_2$ clearly dominating the other three dimensions, is an empirical finding of this study — it was not pre-imposed by the model structure.

Title Anchoring ($H_1$: ACS) registers a mean of 0.4847 ($SD = 0.2673$, BCa 95% CI [0.321, 0.686]). It falls in the "Moderate" prevalence category, and its notably wide confidence interval reflects the genuine heterogeneity of the sub-sample: some respondents exhibited strong title anchoring, others did not. This variability is consistent with the split evidence from Items B3 and C1 discussed above. Trend Momentum ($H_3$: RCS) and Peer Herding ($H_4$: HCS) are both classified as "Moderate" with means of 0.5041 and 0.4819, respectively — their confidence intervals overlap substantially, and neither is definitively separable from the other at this sample size.

### 4.5.2 Calibrated Alpha Weights and the Heuristic Scoring Function

The empirical alpha weights normalised from the weighted mean heuristic scores are:

$$\alpha_1 = 0.2196 \quad \alpha_2 = 0.3342 \quad \alpha_3 = 0.2281 \quad \alpha_4 = 0.2181$$

These weights were substituted into the composite heuristic scoring function (Formula 3.13) as the pre-registered parameters for Portfolio A's construction. Their interpretation is worth pausing on. The dominant weight of $\alpha_2 = 0.3342$ for location familiarity means that, in the heuristic portfolio, geographic prestige accounts for one third of every property's score. A prime Lagos Island or Abuja CBD property receives a full location score of 1.00, while an equivalent asset in Ibadan or Kano receives 0.35 or 0.25 respectively. When multiplied by an $\alpha_2$ of 0.3342, this single dimension alone can produce a score gap of up to 0.25 points between a Lagos Island and a Kano property — larger than the entire contribution of any other single heuristic dimension. This is what location familiarity looks like when it is operationalized from real field data.

The relatively even distribution of the remaining three weights ($\alpha_1$, $\alpha_3$, $\alpha_4$ all within the range 0.219–0.228) is also meaningful. It indicates that beyond the location premium, the three remaining heuristics — title anchoring, trend momentum, and peer herding — contribute approximately equally to the composite score. This differs from the theoretical literature baseline of $\alpha_1 = \alpha_2 = 0.35$ and $\alpha_3 = \alpha_4 = 0.15$, which overweights anchoring and underweights momentum. The empirically calibrated weights suggest that Nigerian PFA managers exhibit a more balanced set of secondary heuristics than the prior literature assumed, and that peer herding, while low in absolute terms, is not as negligible as the literature baseline implies.

---

## 4.6 Environmental Constraints Driving Heuristic Use

### 4.6.1 Institutional Decision Architecture

To address Objective IV, Section D of the questionnaire examined the institutional and informational environment within which direct property selection decisions are made. Item D1 documented the prevailing decision-making structure. Among the $n = 7$ active decision-makers:

- Three respondents (42.9%) reported that an investment committee reviews and formally approves all acquisition recommendations.
- Three respondents (42.9%) reported a combination of committee approval and senior sign-off depending on deal size.
- One respondent (14.3%) reported that a dedicated real estate or property investment team reaches a consensus decision.

The pattern is consistent: in 85.7% of cases, individual investment managers cannot unilaterally approve property acquisitions — even when they possess the analytical authority to conduct selection. All acquisition decisions ultimately pass through a multi-member committee or require senior endorsement. The approval process itself is often multi-stage: 57.1% of respondents reported three or more formal approval stages, while a further 28.6% described a process so variable that it resists standardisation.

This decision architecture is consequential for heuristic use. When an analyst's recommendation must survive multiple committee reviews, the properties most likely to generate consensus approval are those that are recognisable, institutionally legible, and defensible by reference to prior precedent: exactly the properties that location familiarity, title anchoring, and peer mirroring would identify. A manager who proposes a high-yielding asset in Kano or Ibadan — markets with lower visibility and fewer comparable transactions — faces a higher internal approval burden than one who recommends a well-known Victoria Island or Maitama property. The committee structure therefore acts as an institutional amplifier of heuristic selection biases, embedding what might begin as individual cognitive shortcuts into formal organisational processes.

### 4.6.2 Data Scarcity and the Severity of the Informational Environment

Item D2 asked respondents to rate the severity with which data unavailability constrains their decision-making on a five-point scale. The mean severity rating among the seven decision-makers was $M = 3.43$ ($SD = 1.51$), with 57.1% rating the constraint as 4 or 5 (significant or severe). Item D2b, which recorded the specific data gaps experienced, identified the "Absence of reliable transaction price databases for Nigerian property" as the most commonly cited gap across all respondents — a finding consistent with the secondary market analysis in Chapter Two (JLL, 2024; Olapade et al., 2019).

Item D3, asking respondents to identify the single change that would most improve the evidence base for their property selection decisions, produced near-unanimous convergence: five of seven respondents identified "Access to a reliable, comprehensive Nigerian real estate return and transaction database" as the single highest-priority improvement.

### 4.6.3 Institutional Contextual Factors Driving Heuristic Use

Item D4 asked respondents to identify which institutional, cognitive, or informational factors most significantly condition their fund's approach to property selection. Table 4.5 presents the frequency of selection across the available factors.

### Table 4.5: Institutional and Environmental Constraints Driving Heuristic Reliance ($n = 7$)

| Factor / Contextual Constraint | Factor Type | Frequency | Proportion (%) |
|:---|:---:|:---:|:---:|
| Established organisational precedent | Institutional (INS) | 5 | 71.4% |
| Investment committee preference for experienced judgment | Institutional (INS) | 5 | 71.4% |
| Peer PFA behaviour as a practical benchmark | Informational (INF) | 4 | 57.1% |
| Regulatory uncertainty | Regulatory (REG) | 2 | 28.6% |
| High deal complexity resisting standardised models | Informational (INF) | 1 | 14.3% |
| Absence of reliable market data | Informational (INF) | 1 | 14.3% |

The two most frequently cited factors, each selected by 71.4% ($n = 5$) of respondents, were **established organisational precedent** and **investment committee preference for experienced judgment over model outputs**. Their co-dominance is revealing. Organisational precedent effectively encodes historical heuristics into formal investment policy: a fund that acquired three Victoria Island office buildings in the 2010s develops an internal benchmark — "we buy Lagos Island Grade A offices" — that subsequently constrains the search space for all future acquisitions without any explicit analytical justification. Investment committee preference compounds this by ensuring that departures from precedent are institutionally penalised.

The third most cited factor, peer PFA behaviour as a practical benchmark (57.1%, $n = 4$), confirms that peer observation functions as an active substitute for independent market analysis. When transaction-level data is unavailable, a peer fund's acquisition decision constitutes one of the most accessible and actionable signals available to a competing fund manager. This is informational herding of the kind described by Bikhchandani, Hirshleifer and Welch (1992): rational agents cascade on each other's decisions in the absence of independent private information.

### 4.6.4 The Ecological Rationality Test

To evaluate whether heuristic use is truly adaptive — that is, whether it improves with informational constraint rather than reflecting pure cognitive limitation — the analytical sub-sample was split by whether respondents cited informational constraints (INF factors) as dominant drivers. Respondents citing INF factors ($n = 5$) were compared to non-citing respondents ($n = 2$) on their composite heuristic scores.

The ecological rationality test yielded the following:

- **Location Familiarity (AVCS):** INF-citing managers scored $M = 0.689$ ($SD = 0.07$) versus non-citing managers $M = 0.861$ ($SD = 0.09$). The difference (−0.172) runs in an unexpected direction: non-citing managers displayed *higher* location familiarity scores than those who cited data scarcity as their primary constraint. This is counterintuitive but interpretable. Non-citing managers — those who do not identify information opacity as their primary driver — may be so thoroughly embedded in location-based thinking that the informational constraint is not experienced as a constraint at all. The heuristic has fully replaced the analytical framework, rendering the absence of data effectively invisible to the decision-maker.

- **Trend Momentum (RCS):** INF-citing managers scored $M = 0.484$ ($SD = 0.08$) versus non-citing managers $M = 0.554$ ($SD = 0.10$). The difference (−0.069) is again in the same direction: managers who are most aware of data constraints are, perhaps paradoxically, less reliant on trend extrapolation. This is consistent with the bounded rationality logic of Simon (1955): awareness of epistemic constraints produces more cautious extrapolative behaviour, while managers who are not attuned to data limitations extrapolate more freely.

These split-group results do not straightforwardly confirm or refute the ecological rationality hypothesis: the sub-sample of $n = 7$ is too small to draw statistically robust conclusions from a two-group comparison. The results do, however, provide a useful directional signal — one that suggests the relationship between informational opacity and heuristic use is not monotonically positive. Future research with larger samples should revisit this question.

### 4.6.5 Technology Adoption Disposition

Item D4a assessed the likelihood that respondents' funds would adopt a decision-support software tool specifically validated for Nigerian institutional property investment. The response was predominantly positive: five of seven respondents (71.4%) answered "Very Likely," one "Somewhat Likely," and one "Neutral." Not a single respondent indicated unlikelihood. Combined with the D3 finding that five respondents identified database access as the single most important improvement available to them, this result paints a clear picture: institutional appetite for data-driven tools is high, but the supply — in the form of validated, Nigeria-specific analytical infrastructure — is absent. The use of heuristics in this sector should therefore not be interpreted as a preference; it is, in significant part, a structural default.

---

## 4.7 Portfolio Construction Outcomes

### 4.7.1 Portfolio A — Heuristic-Driven Construction

Portfolio A was constructed from the 80-property synthetic universe using the methodology established in Section 3.5.3. The construction applied a single hard filter (F1: PenCom commercial lease compliance) and then ranked all 61 remaining properties by their composite heuristic score using the empirically calibrated alpha weights. A greedy allocation algorithm then selected properties in descending score order until the target of 15 holdings was reached or the ₦200 billion real estate budget was exhausted.

The resulting portfolio comprises 15 properties with a total acquisition cost of ₦11.61 billion, representing 5.8% of the ₦200 billion PenCom-capped real estate allocation. This level of budget utilization — substantial in nominal terms but modest relative to the permissible ceiling — is methodologically significant. It mirrors the real-world pattern documented in Chapter One: Nigerian PFAs allocate between 0.9% and 3.5% of total AUM to direct real estate despite a 10% regulatory ceiling (PenCom Quarterly Reports, 2020–2025). In a universe where individual property costs range from ₦250 million to ₦3 billion, even a 15-property portfolio of mid-tier assets absorbs only a small fraction of the permissible budget. The gap between the ₦200 billion regulatory ceiling and the ₦11.61 billion actually deployed is therefore a structural feature of the market, not a modelling artefact.

### 4.7.2 Portfolio B — MVO-Optimised Construction

Portfolio B was constructed using the greedy local search solver described in Section 3.5.3, which applies a greedy initialisation followed by 2,000 random-restart swap moves to maximise the equal-weighted Sharpe ratio subject to PenCom constraints. The eligible set comprised 60 of the 80 universe properties (those passing the lease compliance and ₦3 billion per-property cap filters), and the solver identified an optimal 15-property portfolio with a total acquisition cost of ₦11.02 billion — remarkably close to Portfolio A in absolute deployment, despite being built on entirely different logic.

### 4.7.3 Portfolio Composition Comparison

Table 4.6 presents the full composition of both portfolios.

### Table 4.6: Portfolio Composition — Heuristic-Driven (A) and MVO-Optimised (B)

| Property ID | State | Asset Type | Acquisition Cost | Expected Return | Portfolio |
|:---|:---:|:---:|:---:|:---:|:---:|
| PROP_09 | Lagos | Mixed-Use | ₦289M | 26.06% | A only |
| PROP_62 | Lagos | Mixed-Use | ₦602M | 25.17% | A only |
| PROP_29 | Lagos | Residential | ₦1,886M | 23.92% | A only |
| PROP_01 | Lagos | Residential | ₦1,345M | 24.77% | A only |
| PROP_36 | Lagos | Residential | ₦1,013M | 24.10% | A only |
| PROP_10 | Lagos | Residential | ₦1,177M | 24.02% | A only |
| PROP_54 | Lagos | Residential | ₦360M | 24.84% | A only |
| PROP_69 | Lagos | Residential | ₦307M | 25.14% | A only |
| PROP_42 | Lagos | Office | ₦824M | 17.61% | A only |
| PROP_49 | Oyo | Mixed-Use | ₦505M | 27.83% | A only |
| PROP_05 | Lagos | Office | ₦894M | 18.14% | A & B |
| PROP_21 | Lagos | Office | ₦623M | 16.65% | A & B |
| PROP_23 | Lagos | Office | ₦775M | 17.37% | A & B |
| PROP_73 | Lagos | Office | ₦284M | 18.13% | A & B |
| PROP_79 | Lagos | Office | ₦726M | 18.48% | A & B |
| PROP_13 | Kano | Commercial | ₦590M | 9.02% | B only |
| PROP_25 | Abuja | Office | ₦258M | 10.33% | B only |
| PROP_26 | Kano | Industrial | ₦230M | 10.27% | B only |
| PROP_32 | Oyo | Office | ₦1,068M | 19.35% | B only |
| PROP_33 | Lagos | Office | ₦724M | 18.54% | B only |
| PROP_43 | Lagos | Office | ₦931M | 18.32% | B only |
| PROP_44 | Abuja | Office | ₦555M | 8.73% | B only |
| PROP_55 | Abuja | Office | ₦1,713M | 9.89% | B only |
| PROP_63 | Abuja | Office | ₦236M | 10.72% | B only |
| PROP_80 | Rivers | Industrial | ₦1,418M | 13.11% | B only |

The two portfolios share **five properties** (PROP_05, PROP_21, PROP_23, PROP_73, PROP_79 — all Lagos Office Grade A assets), representing an overlap rate of 33.3% for Portfolio A and 33.3% for Portfolio B. This partial convergence is meaningful: it demonstrates that the most institutionally recognisable and highest-scoring assets in the universe simultaneously satisfy both the heuristic attractiveness criterion (high composite scores driven by Lagos location and strong title status) and the MVO covariance criterion (mutual exclusion on the efficient frontier's low-variance boundary).

The divergences, however, are where the study's central tension becomes visible.

**Portfolio A's unique properties** are predominantly high-return residential and mixed-use assets in Lagos, anchored entirely in the Lagos submarket: 14 of its 15 holdings are Lagos-based, with the sole exception being a single Oyo mixed-use property (PROP_49, expected return 27.83%) admitted by a combination of its high momentum score and moderate location score. The heuristic engine's location familiarity weight ($\alpha_2 = 0.3342$) made Lagos Island and Lagos Mainland properties almost invariably dominant in the scoring queue. As a consequence, Portfolio A is a concentrated, high-return, high-volatility portfolio of recognised prime assets.

**Portfolio B's unique properties** tell a completely different structural story. The solver identified Kano commercial and industrial assets (PROP_13, PROP_26), Abuja office buildings at low expected returns (PROP_25 at 10.33%, PROP_44 at 8.73%, PROP_55 at 9.89%, PROP_63 at 10.72%), and a Rivers industrial property (PROP_80 at 13.11%). These are precisely the assets that the heuristic portfolio would have penalised most heavily — secondary-market locations, modest yields, non-prime submarkets. The solver selected them not despite their modest returns but because of their covariance structure: assets in Kano, Abuja, and Rivers have low or negative correlation with Lagos properties, and in combination, they enable the portfolio's volatility to be suppressed to levels that the heuristic portfolio, concentrated entirely in a single city, cannot approach.

This divergence is the empirical manifestation of the study's core hypothesis. The heuristic portfolio's location familiarity bias makes geographic diversification structurally impractical: when Lagos Island always scores higher than Kano or Ibadan, the greedy algorithm will fill the portfolio with Lagos properties before it reaches any secondary-market asset. The MVO solver is not subject to this constraint and therefore discovers the efficient frontier region that the heuristic portfolio cannot access.

### 4.7.4 Diversification and Concentration Analysis

Herfindahl-Hirschman Indices (HHI) were calculated across the holding, geographic, and asset-type dimensions for both portfolios. The results are instructive. On the holding dimension, both portfolios achieve an HHI of 0.0667 — a mathematical artefact of equal weighting across 15 holdings — indicating equivalent within-portfolio weight concentration.

On the **geographic dimension**, the contrast is stark. Portfolio A records a geographic HHI of **0.876**: 93.3% of holdings by count are located in a single state (Lagos), producing near-maximum geographic concentration. Portfolio B records a geographic HHI of **0.316**, reflecting holdings distributed across Lagos (7), Abuja (4), Kano (2), Oyo (1), and Rivers (1). Figure 4.4 illustrates this comparison.

![Figure 4.4: Portfolio Geographic Allocation](../../../outputs/charts/figure_4_4_geographic_allocation.png)

**Figure 4.4: Geographic Allocation Comparison.** Portfolio A's near-exclusive Lagos concentration (geographic HHI = 0.876) contrasts sharply with Portfolio B's five-state spread (HHI = 0.316). Both satisfy PenCom's minimum two-state requirement, but Portfolio A does so by the narrowest possible margin.

On the **asset type dimension**, the picture inverts. Portfolio A records an asset type HHI of **0.360**, reflecting a mix of six office assets, six residential assets, and three mixed-use assets. Portfolio B records an asset type HHI of **0.662**, driven by a dominant concentration in office assets (12 of 15 holdings). This is the **Volatility Suppression Paradox** that Markowitz's (1952) framework predicts: the MVO solver, unconstrained by location familiarity, diversifies geographically but concentrates by asset type, because Grade A office assets across different cities exhibit lower pairwise return correlations than a mixed-use residential and commercial portfolio within a single city. Naive diversification — holding equal numbers of each asset type — would have produced a worse Sharpe ratio. True diversification is a function of covariance structure, not category count. Figure 4.5 illustrates this contrast.

![Figure 4.5: Portfolio Asset Type Allocation](../../../outputs/charts/figure_4_5_asset_type_allocation.png)

**Figure 4.5: Asset Type Allocation Comparison.** Portfolio B's apparent "concentration" in office assets reflects the covariance-driven logic of MVO: office assets in Kano and Abuja have low correlation with office assets in Lagos, providing geographic diversification through a single asset class.

The efficient frontier positions of both portfolios are mapped in Figure 4.1, which overlays 5,000 randomly generated feasible portfolios from the universe to construct the frontier cloud.

![Figure 4.1: Portfolio Positions on the Efficient Frontier](../../../outputs/charts/figure_4_1_efficient_frontier.png)

**Figure 4.1: Efficient Frontier Cloud with Portfolio Positions.** Portfolio B lies on or near the efficient frontier in the low-volatility, moderate-return region. Portfolio A lies to the right of the frontier — higher expected return but also higher volatility — reflecting the heuristic selection of high-yield prime assets without covariance optimisation.

---

## 4.8 Monte Carlo Simulation Results

### 4.8.1 Simulation Design and Execution

Both portfolios were subjected to a 10,000-path Monte Carlo simulation over a 60-month (5-year) horizon using Geometric Brownian Motion (GBM) under the parameters documented in Section 3.5.4. Each simulation path generates monthly portfolio returns by drawing from a multivariate normal distribution parameterised by the portfolio's expected return vector and Ledoit-Wolf shrunk covariance matrix. The Cholesky decomposition required for correlated shock generation was applied with a negligible diagonal ridge regularisation ($10^{-12}$) to account for a near-zero negative eigenvalue arising from floating-point precision in the covariance construction — a standard numerical stabilisation procedure that does not materially affect simulation outcomes.

The baseline risk-free rate applied throughout the simulation and hypothesis testing is $R_f = 8.4\%$ per annum, consistent with the rolling average of the CBN Monetary Policy Rate from 2019 to 2024 cited in Chapter Three. At 10,000 paths, the simulation provides sufficient statistical resolution to detect Sharpe ratio differences as small as 0.01 Sharpe units, well below the pre-registered practical significance threshold of 0.05.

### 4.8.2 Core Performance Results

Table 4.7 presents the six pre-registered performance metrics averaged across all 10,000 simulated paths.

### Table 4.7: Monte Carlo Performance Summary ($N = 10,000$ Simulated Paths, $R_f = 8.4\%$)

| Performance Metric | Portfolio A — Heuristic | Portfolio B — MVO | Difference (B − A) |
|:---|:---:|:---:|:---:|
| Mean Cumulative Return (%) | **198.8%** | 105.3% | −93.5pp |
| Mean CAGR (%) | **24.2%** | 15.5% | −8.7pp |
| Mean Annualised Volatility (%) | 7.65% | **0.58%** | −7.07pp |
| Mean Sharpe Ratio | 2.08 | **12.36** | **+10.28** |
| BCa 95% Bootstrap CI for ΔSR | — | — | **[10.35, 10.68]** |
| Mean Maximum Drawdown (%) | 4.24% | **0.00%** | −4.24pp |
| 95% CVaR (Cumulative Return) | **106.7%** | 99.8% | −6.9pp |
| Mean Diversification Ratio | 1.29 | **5.81** | +4.52 |

Source: Author's Computation (2026).

The results in Table 4.7 present a multidimensional picture that resists simple characterisation, and it is worth engaging with its complexity rather than reaching for an early verdict.

Portfolio B (MVO-Optimised) achieves a mean Sharpe ratio of **12.36** — nearly six times that of Portfolio A's **2.08**. The magnitude of this difference, $\Delta SR = 10.28$, is extraordinary by academic standards and demands careful interpretation. The primary driver is not a substantially higher expected return: Portfolio B's mean CAGR of 15.5% is actually **8.7 percentage points lower** than Portfolio A's 24.2%. The Sharpe outperformance derives almost entirely from the near-total suppression of portfolio volatility: Portfolio B's annualised volatility of **0.58%** is approximately thirteen times lower than Portfolio A's 7.65%. When the denominator of the Sharpe ratio (excess return / volatility) shrinks to 0.58%, even a modest excess return of 7.1 percentage points above the risk-free rate yields an extremely high Sharpe ratio.

This arithmetic clarifies the nature of the MVO advantage. The optimiser has not found higher-returning assets; it has found assets with exceptionally low pairwise correlations — specifically, the Grade A office assets of Abuja and Kano, whose returns are largely uncorrelated with Lagos market returns. By combining these low-correlation assets, the portfolio-level volatility collapses toward the weighted average of each asset's idiosyncratic, non-covarying risk. The result is a portfolio that is extraordinarily stable but that sacrifices nearly nine percentage points of annual return in the process.

Portfolio A's story is the mirror image. Its geographic concentration in Lagos — the direct expression of the location familiarity heuristic — means that the portfolio's individual properties share common exposure to the same Lagos commercial property cycle. When the Lagos market rises, all 14 Lagos holdings benefit; when it corrects, they correct together. The portfolio-level volatility (7.65%) therefore reflects the systematic component of Lagos-specific risk that cannot be diversified away within a single city's asset base. But the same concentration that drives volatility also drives return: Lagos prime assets exhibit the highest expected returns in the universe (residential returns averaging 23–25%, office returns averaging 16–18%), and Portfolio A's concentration in them produces a mean CAGR nearly a quarter higher than the risk-free rate.

The 95% CVaR finding adds an important dimension. Portfolio A's CVaR of 106.7% cumulative return in the worst 5% of paths means that even in the worst-case scenarios, the heuristic portfolio — over a five-year horizon — is expected to more than double the initial real estate investment. Portfolio B's worst-case CVaR of 99.8% means it barely breaks even in the worst 5% of paths, reflecting its near-zero volatility: there is simply very little upside or downside. The Maximum Drawdown of 0.00% for Portfolio B, while technically impressive, is again a mathematical consequence of its suppressed volatility: when monthly volatility is near zero, the running maximum barely departs from the starting value, and drawdowns are negligible.

The simulated value paths for both portfolios across the 60-month horizon are presented in Figure 4.3.

![Figure 4.3: Monte Carlo Portfolio Value Paths — 100 Representative Paths](../../../outputs/charts/figure_4_3_monte_carlo_paths.png)

**Figure 4.3: Comparative Monte Carlo Path Simulations.** Portfolio A's paths (upper panel) exhibit the characteristic fan shape of a volatile but high-return asset, with wide dispersion of terminal values. Portfolio B's paths (lower panel) are tightly clustered, rising gradually and consistently — the visual signature of a near-zero-volatility, steady-return structure.

The resulting Sharpe ratio distributions across all 10,000 paths are presented in Figure 4.2.

![Figure 4.2: Sharpe Ratio Distributions across 10,000 Simulated Paths](../../../outputs/charts/figure_4_2_sharpe_distribution.png)

**Figure 4.2: Sharpe Ratio Distributions.** The two distributions are entirely non-overlapping, which explains both the large $\Delta SR$ magnitude and the extreme statistical significance of the paired t-test. Portfolio A's distribution is centred near 2.08 with moderate spread; Portfolio B's is centred near 12.36 with a much tighter distribution, reflecting its consistent low-volatility performance.

---

## 4.9 Hypothesis Testing and Sensitivity Analysis

### 4.9.1 Formal Hypothesis Tests

The formal hypotheses established in Section 3.5.5 were tested using the paired t-test and BCa bootstrap confidence interval procedures specified in the methodology.

**Hypothesis 1** tested whether the MVO portfolio achieves a statistically higher Sharpe ratio than the heuristic portfolio:

$$H_0: E[SR_B] - E[SR_A] \leq 0 \quad \text{vs.} \quad H_1: E[SR_B] - E[SR_A] > 0$$

The paired t-test yielded $t = 733.35$, $p \approx 0.0000$ (one-tailed). **The null hypothesis is rejected.** The MVO portfolio achieves a statistically significantly higher Sharpe ratio than the heuristic portfolio under baseline conditions.

**Hypothesis 2** tested whether the observed Sharpe ratio difference meets the pre-registered practical significance threshold of 0.05 Sharpe units:

$$H_0: \Delta SR < 0.05 \quad \text{vs.} \quad H_2: \Delta SR \geq 0.05$$

The mean $\Delta SR = 10.28$ (BCa 95% CI [10.35, 10.68]). This exceeds the 0.05 threshold by a factor of over 200. The Cohen's $d$ effect size is $d = 7.33$, placing the effect in an entirely exceptional tier by conventional benchmarks (Cohen, 1988). **The null hypothesis is rejected.** The performance difference is practically significant. Expressed in monetary terms, on a ₦200 billion real estate sub-portfolio (the 10% PenCom ceiling on a ₦2 trillion fund), a 10.28-unit Sharpe ratio improvement — if translated into risk-adjusted return advantage under the pre-registered ₦1.5–2.0 billion threshold metric — represents a materially meaningful difference in long-run retirement income outcomes.

**Hypothesis 3** tested whether the MVO advantage is stable across different risk-free rate regimes. This hypothesis is addressed in detail in the sensitivity analysis below.

### 4.9.2 Market Condition Stress Test

To examine whether the MVO advantage holds across different market environments, the 10,000 simulated paths were stratified into three terciles based on Portfolio A's realized annualised volatility: low volatility (tercile 1, $n = 3,333$), medium volatility (tercile 2, $n = 3,334$), and high volatility (tercile 3, $n = 3,333$). Table 4.8 presents the mean Sharpe ratios within each tercile.

### Table 4.8: Market Condition Tercile Performance Analysis ($N = 10,000$ Paths)

| Volatility Tercile | Portfolio A Mean SR | Portfolio B Mean SR | Δ Sharpe (B − A) | Path Count |
|:---|:---:|:---:|:---:|:---:|
| Low Volatility | 2.32 | 12.37 | +10.06 | 3,333 |
| Medium Volatility | 2.07 | 12.36 | +10.29 | 3,334 |
| High Volatility | 1.86 | 12.35 | +10.49 | 3,333 |

The tercile results in Table 4.8 reveal a revealing asymmetry. Portfolio B's Sharpe ratio is essentially invariant across market conditions — 12.37, 12.36, and 12.35 across the three terciles — a consequence of its near-zero volatility: when the denominator of the Sharpe ratio is already close to zero, market-condition variation in the numerator (excess return) barely moves the ratio. Portfolio A, by contrast, is market-condition sensitive: its Sharpe ratio declines from 2.32 in low-volatility environments to 1.86 in high-volatility environments. This is directionally consistent with what one would expect from a high-return, geographically concentrated portfolio — its performance is susceptible to systematic Lagos-cycle volatility in precisely the market environments where that cycle is most volatile.

The $\Delta SR$ actually widens from 10.06 in low-volatility conditions to 10.49 in high-volatility conditions. This finding — that the MVO portfolio's advantage *grows* as market conditions deteriorate — provides the strongest mechanical argument for quantitative portfolio optimisation under the baseline rate regime. The diversification benefit of the MVO structure is most valuable precisely when it is most needed.

### 4.9.3 Risk-Free Rate Sensitivity: The Performance Crossover

Hypothesis 3 examined whether the MVO portfolio's Sharpe ratio advantage is robust to changes in the risk-free rate, motivated by Nigeria's well-documented macroeconomic volatility. The CBN's Monetary Policy Rate reached 27.5% in 2024, a level far above the 8.4% benchmark used in the primary analysis. Table 4.9 presents the Sharpe ratios for both portfolios across four risk-free rate scenarios.

### Table 4.9: Sharpe Ratio Sensitivity Analysis under Alternative Risk-Free Rates

| Risk-Free Rate ($R_f$) | Portfolio A SR | Portfolio B SR | Δ Sharpe (B − A) | Direction of Advantage |
|:---:|:---:|:---:|:---:|:---:|
| **8.4% (Benchmark)** | 2.08 | 12.36 | **+10.28** | MVO (B) |
| 10.0% | 1.87 | 9.56 | **+7.69** | MVO (B) |
| **15.0%** | **1.21** | **0.82** | **−0.39** | **Heuristic (A)** |
| **20.0%** | **0.55** | **−7.92** | **−8.47** | **Heuristic (A)** |

Source: Author's Computation (2026).

The sensitivity results in Table 4.9 reveal a **critical structural crossover** that rejects the null hypothesis of Hypothesis 3 and constitutes one of the most important empirical findings of this dissertation.

At the benchmark rate of 8.4%, the MVO portfolio dominates by a margin of +10.28. At 10.0%, the advantage persists at +7.69 — attenuated but directionally intact. At **15.0%**, however, the advantage reverses: Portfolio A's Sharpe ratio of 1.21 exceeds Portfolio B's 0.82 by 0.39 units. At **20.0%**, the reversal is dramatic: Portfolio B records a Sharpe ratio of −7.92, while Portfolio A sustains a positive Sharpe of 0.55.

The mechanism of this reversal is precisely the inverse of what drives the MVO advantage under baseline conditions. Portfolio B's near-zero volatility (0.58%) is its strength when the risk-free rate is below the portfolio's CAGR of 15.5%: excess returns are positive, and dividing them by a tiny volatility produces an enormous Sharpe ratio. But when the risk-free rate rises above 15.5%, the excess return turns negative: Portfolio B's assets, predominantly low-yield Abuja and Kano office buildings with expected returns of 9–11%, cannot clear the hurdle rate. A negative excess return divided by a tiny volatility produces an extremely negative Sharpe ratio — the 1/volatility amplification that powered Portfolio B's ascent in the baseline scenario becomes the engine of its collapse in the high-rate scenario.

Portfolio A, by contrast, holds predominantly high-yield Lagos assets with expected returns of 23–27%, well above even the 20% risk-free rate scenario. Its higher volatility (7.65%) attenuates the magnitude of its positive Sharpe ratio, but it maintains a positive excess return — and therefore a positive Sharpe ratio — at every risk-free rate tested. The heuristic portfolio's focus on nominal yield, while analytically sub-optimal in the low-rate baseline, functions as a structural buffer against rate shocks.

The stress scenario results across both volatility terciles and alternative rate regimes are visualised in Figure 4.6.

![Figure 4.6: Stress Scenario Performance Analysis](../../../outputs/charts/figure_4_6_stress_scenario.png)

**Figure 4.6: Portfolio Sharpe Ratio Sensitivity to Volatility Conditions and Alternative Risk-Free Rates.** The rate-sensitivity crossover is clearly visible: below approximately 12–13%, Portfolio B dominates; above it, Portfolio A becomes the superior risk-adjusted performer.

This crossover, occurring at approximately $R_f \approx 12\text{–}13\%$, has a direct and urgent implication for the Nigerian context. Nigeria's CBN Monetary Policy Rate stood at **27.5%** in February 2024, and the prevailing T-bill rate throughout 2023 was consistently above 15%. Under both of these real-market conditions, the sensitivity analysis suggests that the heuristic portfolio would have outperformed the MVO portfolio on a risk-adjusted basis. The optimised portfolio's extraordinary Sharpe ratio under the 8.4% baseline scenario is therefore a conditional result — conditional on a low-interest-rate environment that does not characterise Nigeria's recent macroeconomic history.

This finding is consistent with the Ecological Rationality paradigm of Gigerenzer and colleagues (1999, 2008). The heuristic portfolio's selection of high-yield prime assets — driven by location familiarity and trend momentum rather than by covariance optimisation — inadvertently produces a portfolio whose nominal returns are high enough to provide robust protection against rate shocks. In this respect, the heuristic is ecologically well-matched to the Nigerian macroeconomic environment: it selects assets that clear high hurdle rates precisely because high hurdle rates characterise that environment. The MVO portfolio, optimised for a low-rate benchmark, selects assets with maximally low covariance at the cost of yield — and those low yields are the portfolio's undoing when the policy rate spikes.

It also connects to the Estimation Risk literature (DeMiguel et al., 2009; Michaud, 1989). The MVO solver in this study has access to true population parameters from the synthetic universe. In practice, Nigerian PFA managers would need to estimate expected returns and covariances from sparse, noisy, and often unreliable local market data. If the estimation error in these inputs is sufficiently large — and Chapter Two's review of the Nigerian property market's data opacity strongly suggests it would be — the optimised portfolio constructed from estimated parameters could be systematically mis-specified, potentially underperforming a simple heuristic-driven selection. The robustness of simple rules in estimation-error-prone environments is precisely what DeMiguel et al. (2009) documented for the naïve 1/N strategy across equity markets, and the current study suggests that a similar logic applies to direct real estate in opaque emerging markets.

---

## 4.10 Chapter Summary

This chapter has presented the empirical results and analytical interpretations addressing the study's four research objectives. The findings are summarised below.

**Objective I — Identifying Heuristics:** Among the seven active decision-makers in the analytical sub-sample, Location Familiarity ($H_2$: AVCS) emerged as the sole highly prevalent heuristic (weighted mean = 0.7378, BCa 95% CI [0.616, 0.851]), dominating all three composite score components: the B1 rank (median 2.0, 100% Top-3), the B2 Likert mean (3.00), and the C2 scenario choice rate (85.7%). Title Anchoring ($H_1$: ACS = 0.4847), Trend Momentum ($H_3$: RCS = 0.5041), and Peer Herding ($H_4$: HCS = 0.4819) registered as Moderate. A significant stated-revealed preference gap was identified for Location Familiarity (+0.357) and Title Anchoring (+0.214), confirming that institutional managers systematically understate their susceptibility to these heuristics in self-report data. The criteria ranking analysis confirmed a lexicographic cognitive hierarchy (Title > Location > Yield), with Tenant Profile, Market Liquidity, and Peer Activity ranked fourth through eighth by the analytical sub-sample.

**Objective II — Portfolio Construction:** Portfolio A (Heuristic-Driven) was built around the calibrated $\alpha$ weights ($\alpha_1 = 0.2196$, $\alpha_2 = 0.3342$, $\alpha_3 = 0.2281$, $\alpha_4 = 0.2181$), selecting 15 properties with a total acquisition cost of ₦11.61 billion. It is geographically concentrated in Lagos (14 of 15 holdings, geographic HHI = 0.876) but asset-type diversified (HHI = 0.360). Portfolio B (MVO-Optimised) selected 15 properties with a total acquisition cost of ₦11.02 billion. It is geographically diversified across five states (HHI = 0.316) but asset-type concentrated in Grade A office assets (HHI = 0.662). The two portfolios share five properties — all Lagos Grade A office assets — confirming that the most heuristically attractive assets and the most covariance-efficient assets partially overlap in the universe.

**Objective III — Comparative Performance:** Under the baseline risk-free rate of 8.4%, Portfolio B recorded a mean Sharpe ratio of 12.36 versus Portfolio A's 2.08, yielding $\Delta SR = 10.28$ (BCa 95% CI [10.35, 10.68], $t = 733.35$, $p < 0.0001$, Cohen's $d = 7.33$). Both statistical and practical significance criteria were met. The MVO advantage is entirely driven by volatility suppression (Portfolio B volatility: 0.58% vs. Portfolio A: 7.65%), not by superior expected return (Portfolio A CAGR: 24.2% vs. Portfolio B: 15.5%). The MVO portfolio's maximum drawdown of 0.00% and its superior diversification ratio (5.81 vs. 1.29) confirm its structural risk management advantage under baseline conditions.

**Objective IV — Factors and Environmental Constraints:** Established organisational precedent and investment committee preference for experienced judgment (both cited by 71.4% of decision-makers) were identified as the dominant institutional drivers of heuristic reliance. Peer PFA behaviour as a practical benchmark was cited by 57.1%. The near-universal disposition toward adopting data-driven tools (71.4% "Very Likely") — combined with the identification of database access as the single highest-priority improvement — confirms that heuristic use in this sector is primarily a structural default driven by the absence of data infrastructure, not a principled rejection of quantitative analysis.

**The Central Empirical Finding — Ecological Conditionality:** The sensitivity analysis demonstrated a performance crossover at approximately $R_f \approx 12\text{–}13\%$. Below this threshold, the MVO portfolio dominates on risk-adjusted terms. Above it, the heuristic portfolio's high-yield focus makes it the superior performer. Since Nigeria's prevailing risk-free rate has repeatedly breached 15% in recent years — and reached 27.5% in 2024 — the heuristic portfolio's ecological adaptiveness to the Nigerian macroeconomic environment cannot be dismissed. The MVO advantage is real, substantial, and statistically conclusive under baseline conditions; but it is also fragile, collapsing entirely under the interest rate conditions that have actually characterised the Nigerian market for much of the study period. Chapter Five interprets the theoretical implications of this finding and its practical consequences for Nigerian pension fund policy.
