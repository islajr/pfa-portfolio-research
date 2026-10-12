# CHAPTER FIVE

## SUMMARY, CONCLUSIONS AND RECOMMENDATIONS

## 5.1 Preamble

The summary, conclusions and recommendations of the study are given in this chapter. The study focused on the role, performance implications and environmental factors influencing the use of decision-making heuristics in property portfolio selection decisions of Pension Fund Administrators in Nigeria.

The chapter is divided into four major sections. Section 5.2 provides a brief overview of the thesis, presenting the core objectives and review of literature provided in Chapters 1–3, and then detailing the synthesis of empirical findings and their wider structural implications for institutional asset management. The tension between the Heuristics-and-Biases paradigm and the Ecological Rationality paradigm in the context of the Nigerian macroeconomic context is resolved in Section 5.3 with the interpretive conclusions emerging from the empirical research. Recommendations for investment practitioners, regulators and educators are offered in Section 5.4, and are practical and actionable. Last, limitations of the study and future research opportunities are summarized in Section 5.5.

## 5.2 Summary of Thesis

The primary aim of this dissertation was to evaluate whether decision-making heuristics used by Nigerian PFA investment managers lead to suboptimal portfolio choices or represent ecologically rational adaptations to data-scarce emerging real estate markets. The study addressed four specific research objectives:

1. To identify the types of heuristics most frequently employed by Nigerian PFA managers in property selection.
2. To construct representative property portfolios using heuristic decision rules (Portfolio A) and mean-variance optimization (Portfolio B) adapted for discrete real estate assets.
3. To conduct a comparative performance evaluation of the heuristic-driven and mean-variance optimized portfolios across simulated macroeconomic regimes.
4. To examine the environmental constraints and institutional governance factors that drive reliance on heuristics among Nigerian PFA managers.

To achieve these goals the research used a mixed methods approach with a primary field survey of all the pension operators licensed by PenCom and computational portfolio modelling. To obtain the ground truth universe, an 80-property universe was calibrated using secondary real estate market reports (JLL, Estate Intel, Broll, NIESV) and macroeconomic series (CBN MPR and inflation rates). Behavioural responses were processed to generate empirical weighting parameters for the construction of Portfolio A, and a binary integer mean-variance solver was used to construct Portfolio B. A 10,000-path Monte Carlo was used to compare both portfolios under varying risk-free interest rates.

### 5.2.1 Summary of Key Findings

Extensive analysis of the collected research data yielded the following findings in line with the established objectives of the study.

**Prevalence and Elicitation of Heuristics:** Title Legal Status and Submarket Location Prestige were used as mandatory screening filters, establishing a search hierarchy. The high prevalence of Location Familiarity exceeded the threshold for a decision heuristic in a composite heuristic scoring, making it the strongest decision heuristic among the Nigerian PFA managers. Moderate prevalence was observed in the case of Title Anchoring, Trend Momentum, and Peer Herding.

**Portfolio Construction and Concentration Profiles:** Portfolio A (Heuristic) invested ₦11.61 billion in 15 properties, with 93.3% of the funds allocated to Lagos State, the location with the highest empirical weight of familiarity. Portfolio B (MVO) invested ₦11.02 billion in 15 properties with geographic distribution across 5 States. Portfolio B, however, had a higher concentration of capital in Commercial Office assets, illustrating the Volatility Suppression Paradox: MVO can deliver low variance through having high-grade office assets from a variety of markets, but not within a single market.

**Comparative Risk-Adjusted Performance:** At the baseline risk-free rate, the mean Sharpe ratio of Portfolio B was significantly higher than that of Portfolio A. This was attributable entirely to covariance suppression, as Portfolio A performed better in terms of nominal return.

**Macroeconomic Sensitivity and Performance Crossover:** Sensitivity analysis across alternative risk-free interest rates revealed a critical performance crossover at $R_f \approx 12.5\%$:

**a.** In low-interest-rate environments ($R_f < 12.5\%$), Portfolio B's low volatility produces a higher Sharpe ratio.

**b.** In high-interest-rate environments ($R_f \geq 15.0\%$), Portfolio B collapses to negative Sharpe ratios ($-7.9200$ at $R_f = 20.0\%$) because its low-yielding regional assets (8.7%–10.7%) fail to clear the high risk-free hurdle.

**c.** Portfolio A maintains positive Sharpe ratios ($1.2100$ at $R_f = 15.0\%$; $0.5500$ at $R_f = 20.0\%$) because its high nominal returns (24.20% CAGR) provide a robust yield buffer against policy tightening.

**Environmental Constraints and Governance Drivers:** Survey findings confirmed that reliance on heuristics is driven by committee approval requirements (85.7%) and severe real estate data opacity (71.4%). Split-sample testing confirmed that managers facing severe data constraints exhibit significantly higher Location Familiarity scores ($H_2 = 0.7920$ vs. $0.6020$, $p < 0.05$). Furthermore, 79.2% of respondents indicated they are "Very Likely" to adopt validated quantitative decision-support tools if made available.

### 5.2.2 Implication of Findings

The empirical findings of this dissertation carry significant implications for institutional finance theory and pension fund asset allocation:

**a. The Dual-Regime Model of Heuristic Efficacy:** The research shows that the efficacy of decision heuristics cannot be assessed without taking into account the macroeconomic environment. Naïve diversification entails a risk-adjusted efficiency cost in low-interest-rate regimes because it does not account for covariance optimization. In high-inflation emerging markets, such as Nigeria, where interest rates can often be over 15%, however, the heuristic of picking high nominal yields makes perfect sense and is in the best interests of fund capital.

**b. Re-evaluating Diversification in Real Estate:** The diversification concept has been rethought as a result of comparing the Herfindahl-Hirschman Index (HHI) based on geographic concentration (Portfolio A = 0.8760) against asset type concentration (Portfolio B = 0.6620). Often institutional real estate investors think that a mix of residential, commercial and retail properties in the same major city constitutes sufficient diversification. The empirical findings confirm the dominance of spatial covariance: true risk reduction depends on the dispersion of investments over geographically uncorrelated property markets.

**c. Institutional Data Infrastructure as a Policy Priority:** The overwhelming response of managers to the quantitative decision-support tools (79.2%) demonstrates that heuristic reliance is not due to managers' "inertia" or lack of financial skills. Rather, it is a structural default that is imposed by the lack of centralized transaction databases. Addressing real estate data opacity is thus a crucial precondition needed to take forward the quantitative risk management in the Nigerian pension industry.

## 5.3 Conclusions

Based on the empirical findings, this study draws three main conclusions:

**a. Progressive Screening Dominates Institutional Selection:** Nigerian PFA investment managers look for property based on a progressive elimination approach. Non-negotiable screening filters are legal title perfection (Certificate of Occupancy) and submarket location prestige. These preliminary qualitative screens are carried out prior to financial yield assessment of candidate properties.

**b. Heuristics Provide an Adaptive Buffer in High-Inflation Markets:** Mean-variance optimization produces better risk-adjusted efficiency under baseline conditions of low interest rates, but is susceptible to macroeconomic tightening. Optimized portfolios composed of low-yielding assets in regional markets do not meet the hurdle rate in high inflation. The high nominal returns from the focus on prime Lagos assets in the heuristic portfolio (24.20% CAGR) help to protect pension capital from inflation and high interest rates.

**c. Heuristics Represent Ecologically Rational Adaptations:** The study shows that heuristics are not cognitive biases or expressions of financial irrationality but rather ecologically rational adaptations by Nigerian PFA managers. Where there is no clear historical return series and an opaque market, managers can rely on location prestige and title security as intuitive proxies to effectively manage downside risks and navigate the committee approval process.

## 5.4 Recommendations

To translate these empirical insights into actionable policy and practice, recommendations are offered for each of three target groups of stakeholders:

### 5.4.1 For PFA Investment Managers and Executive Leadership

**a. Implement a Multi-Stage Hybrid Selection Framework:** PFA investment teams should formalize a multi-stage acquisition pipeline. In Stage 1, employ the qualitative heuristics (Title Anchoring and Location Familiarity) to screen out high-risk assets. In Stage 2, use the screened asset pool through quantitative means with the goal of minimizing portfolio risk using cross-city geographic diversification.

**b. Expand Inter-City Geographic Allocation:** Investment Committees should include a systematic allocation of real estate funds to secondary cities (Abuja FCT, Port Harcourt, Ibadan, etc.). Portfolio diversification by regional markets offers true spatial covariance reduction and boosts portfolio stability.

**c. Mandatory Continuous Professional Development (MCPD):** Investment analysts and risk officers within PFA investment teams should be required to undergo training in quantitative real estate portfolio management, a requirement to be mandated by executive leadership. Capacity building programs should engage specifically with multi-asset covariance estimation and scenario stress testing in the emerging market context.

### 5.4.2 For Regulatory Bodies (National Pension Commission — PenCom)

**a. Establish Dynamic Hurdle-Rate Guidelines:** PenCom should review real estate allocation guidelines and adjust them to include dynamic, regime-dependent benchmark hurdle rates. The regulatory system should give PFAs flexibility to shift the allocation of properties toward high nominal yield securities during periods of high inflation, given the protective cushion afforded by nominal yields.

**b. Promote a Centralized Institutional Real Estate Database:** A Centralized Institutional Real Estate Database (CIRED) should be sponsored by PenCom in collaboration with the Nigerian Institution of Estate Surveyors and Valuers (NIESV) and the Nigerian Real Estate Regulatory Board (ESVARBON). A stable real estate index will help to demystify the market and speed up the adoption of quantitative risk management tools across the sector.

### 5.4.3 For Educational Institutions and Curriculum Developers

**a. Update Real Estate and Finance Curricula:** Tertiary institutions and the National Universities Commission (NUC) should update the curricula of Estate Management and Finance courses at both undergraduate and postgraduate levels. Financial knowledge should be integrated into training programs, and emerging market quantitative risk modelling included, thereby bridging the gap between academic theory and institutional practice.

## 5.5 Opportunities for Further Research

This study provides insights into institutional real estate allocation, but there are several areas of further research worth highlighting:

**a. Analysis with Actual PFA Transaction Archives:** Future studies should attempt to access confidential, multi-decade historical transaction data from active PFAs for comparison with simulated Monte Carlo results to confirm the accuracy of the simulation.

**b. Cross-Country Comparative Studies in Sub-Saharan Africa:** Extending this methodology to compare PFA real estate selection strategies across other Sub-Saharan African economies (e.g., Ghana, Kenya, South Africa) would provide a test of whether the interest rate sensitivity crossover holds true in different regulatory and inflation regimes.
