---
title: "Heuristics in Property Portfolio Selection Decisions of Nigerian Pension Funds"
subtitle: "An Empirical Assessment of Adaptive Behaviour in Institutional Real Estate Allocation"
author: "Akinmokun Isaac Oluwaseun"
matricNo: "ESM/2019/023"
supervisor: "Prof. A. Olaleye"
department: "Department of Estate Management"
faculty: "Faculty of Environmental Design and Management"
institution: "Obafemi Awolowo University, Ile-Ife, Nigeria"
degree: "Bachelor of Science (B.Sc. Hons) in Estate Management"
date: "September 2026"
keywords:
  - Heuristics
  - Property Portfolio Selection
  - Pension Fund Administrators
  - Mean-Variance Optimization
  - Ecological Rationality
  - Real Estate Market Opacity
  - Monte Carlo Simulation
  - Nigerian Financial System
---

# HEURISTICS IN PROPERTY PORTFOLIO SELECTION DECISIONS OF NIGERIAN PENSION FUNDS

<div align="center">

*An Empirical Assessment of Adaptive Behaviour in Institutional Real Estate Allocation*

<br/>

**AKINMOKUN ISAAC OLUWASEUN**  
*ESM/2019/023*

<br/>

Being a dissertation submitted to the Department of Estate Management, Faculty of Environmental Design and Management, Obafemi Awolowo University, Ile-Ife, Nigeria, in partial fulfilment of the requirements for the award of the degree of Bachelor of Science (B.Sc. Hons) in Estate Management.

<br/>

**Supervised by:** Prof. A. Olaleye  
**Date:** September 2026

</div>

---

# Abstract

Direct real estate allocation by Nigerian Pension Fund Administrators (PFAs) takes place in a very opaque market and under regulatory limits (10% AUM). Without centralized databases of transactions, fund managers use qualitative heuristics. This dissertation compared the effectiveness of these cognitive shortcuts and explored whether they are suboptimal or adaptive.

To this end, the study identified dominant heuristics, built representative portfolios (heuristic Portfolio A vs. integer MVO Portfolio B) from a ₦2 trillion asset base, compared the performance of the two portfolios using a 10,000-path Monte Carlo simulation under various interest rate scenarios (8.4%–20%), and studied the environmental drivers.

All 24 PenCom-licensed operators were surveyed using a primary census, and an 80-property universe was calibrated using secondary market data. Results confirmed a search hierarchy with title legal status and location familiarity as dominant filters. In the base case ($R_f = 8.4\%$), Portfolio B achieved a higher Sharpe ratio due to covariance suppression, while Portfolio A delivered a higher nominal CAGR (24.20% vs. 15.50%). Importantly, sensitivity analysis revealed a critical crossover at $R_f \approx 12.5\%$: in high-inflation environments, MVO's low-yield regional assets fail to clear the risk-free hurdle, driving Portfolio B's Sharpe ratio to negative values ($-7.92$ at $R_f = 20\%$), while Portfolio A maintains positive Sharpe ratios (0.55) owing to its high-yield Lagos-focused holdings.

The study argues that heuristics are an ecologically rational response to market opacity and high-inflation regimes, and proposes a two-stage hybrid selection framework and institutional data infrastructure investment as pathways to improved portfolio outcomes.

**Keywords:** Heuristics, Property Portfolio Selection, Pension Fund Administrators, Mean-Variance Optimization, Ecological Rationality, Real Estate Market Opacity, Monte Carlo Simulation, Nigerian Financial System.

---

# CHAPTER ONE

## INTRODUCTION

## 1.1 Background to the Study

Pension Fund Administrators (PFAs) are an important aspect of the contemporary financial systems because they handle the retirement savings of millions of investors. The investment mandate of these institutions is not limited to the preservation of capital but to the investment of this pooled capital in different asset classes (equities, fixed income securities, infrastructure and most importantly, real estate). The aim of this investment is to generate sustained levels of risk-adjusted returns over extended time periods (Blake, 2003; Andonov et al., 2017). Of all the above-mentioned asset classes, property or real estate investments are especially appealing because of the specifics of their nature: the possibility of long-term capital growth, the ability to generate income in the form of rental yields, the possibility of hedging against inflation, and the lack of correlation with more standard financial assets (Geltner et al., 2014).

The Nigerian Pension Industry has seen a massive growth in the value of assets, which increased by ₦1.58 trillion in 2009 to about ₦26 trillion in the third quarter of 2025 (PenCom, 2025). This has been an exponential growth that necessitated the diversification of assets other than the conventional concentration in Federal Government securities. To this end, the recently-revised regulation on investment of pension fund assets explicitly authorizes PFAs to invest up to 10% of their portfolios to real estate and infrastructure, and up to 15% to Real Estate Investment Trusts (REITs), reflective of real estate's strategic importance in long-term portfolio construction (PenCom, 2025).

Regulatory permissiveness of wider real estate exposure notwithstanding, anecdotal evidence shows that there is always a gap between the maximum regulatory authorization and the real allocation percentage. The actual distributions of Nigerian PFA to real estate are always within the allowed limits, which are 0.9–3.5 percent of their asset portfolios (PenCom Quarterly Reports, 2020–2025). This is commonly explained by the nature of real estate as an asset type, which is sometimes colloquially referred to as lumpiness, which is the indivisibility that is always present in the nature of real estate, the high cost, long duration of transactions, and illiquidity that make real estate an untradable asset type (Baum & Hartzell, 2012; Ling, 2005).

Besides the inherent negative attributes of real estate as an asset class, there are other complexities that involve the Nigerian real estate market, which further complicates the inherent attributes. The Nigerian property market is inherently opaque, unlike developed markets with well-developed Real Estate Investment Trusts (REITs), developed property indices, and open databases of transactions (JLL, 2024). It is marked by a high level of information asymmetry, problems with title documentation, and a pronounced lack of trusted property information (Olapade et al., 2019; Onwuanyi, 2020).

Due to these circumstances, investment decision-makers often utilize heuristics (mental shortcuts, rules of thumb or simplified decision rules) that can be used to help reduce cognitive load and make fast judgments and decisions in complex, information-scarce contexts (Gigerenzer & Gaissmaier, 2011). These heuristics can take different forms, i.e., anchoring (Northcraft & Neale, 1987); availability (Tversky & Kahneman, 1973); representativeness (Kahneman & Tversky, 1972) and herding (Bikhchandani et al., 1992; Salzman & Zwinkels, 2017) among others.

While existing research has examined the usage of major heuristics in Nigerian property investment valuation and its affecting factors (Iroham et al., 2013), property portfolio diversification strategies (Olaleye, 2008, 2011), and real estate performance in Nigerian pension fund portfolios (Okeahialam & Awa, 2024; Okeahialam & Ezema, 2024), a significant gap remains. In particular, there is no research that has so far demonstrated the effectiveness of heuristics in property portfolio selection decisions in opaque, data-scarce settings.

This paper fills this gap and provides the answer to the relevant question whether the application of heuristics in property portfolio selection is making PFAs leave money on the table or whether the application of the latter is a reasonable response to the specifics of the Nigerian property market.

## 1.2 Statement of the Research Problem

The central aim of constructing a real estate portfolio for pension funds is to identify a 'selection' that maximizes risk-adjusted returns over the investment period, while constrained by certain factors like liquidity, regulatory requirements and the fund's specific liability structure (Amenc et al., 2009; Hoevenaars et al., 2008). This is especially vital for PFAs due to the long-term obligations they owe to contributors.

Modern Portfolio Theory provides a practical framework for this optimization: Given a universe of available properties with estimated returns and a covariance matrix capturing risk relationships, the efficient frontier identifies portfolio selections offering maximum expected returns for specified risk levels, or equivalently, minimum risk for target return thresholds (Markowitz, 1952; Merton, 1972).

In data-scarce, emerging markets like Nigeria, however, the efficacy of Modern Portfolio Theory becomes implausible. The inherent conditions within these markets create an environment where the theoretical assumptions that Modern Portfolio Theory is built on are systematically violated (Shiller, 2003; Kahneman, 2011). Resultantly, portfolio decisions by institutional investors, such as PFAs, often deviate from the recommendations of Modern Portfolio Theory. Research from Iroham (2013) extensively documented a number of these derivative patterns within the context of the Nigerian real estate market:

**i.** Properties may be selected based on anchoring to valuations provided by surveyors, even when these valuations inadequately reflect market fundamentals or incorporate backward-looking data (Northcraft & Neale, 1987).

**ii.** Portfolio construction exhibits availability bias, through the selection of properties in highly visible, frequently-transacted locations (Lagos Island: Ikoyi, Victoria Island; Abuja: Maitama, Asokoro) despite potentially superior risk-adjusted opportunities in less-prominent submarkets.

**iii.** Investment decisions demonstrate herding behaviour, with PFAs mimicking the property selections of competitors or following "best practices" that may not align with the specific fund's risk-return preferences or liability structure.

The central research problem is that while the prevalence of these heuristics is well-established narratively and supported by international evidence, their consequences within the Nigerian pension fund context remain empirically undetermined.

To address the research problem, this study poses the following questions:

**i.** What specific heuristics are commonly employed by Nigerian Pension Fund Administrators in property portfolio selection decisions?

**ii.** How do heuristic-driven portfolios perform relative to mean-variance optimized portfolios over similar holding periods?

**iii.** What factors influence the use of heuristics among Nigerian PFA investment managers?

## 1.3 Aim and Objectives of the Study

The aim of this study is to examine the role of heuristics in property portfolio selection decisions of Pension Fund Administrators in Nigeria with a view to assessing whether heuristics prove adaptive for property portfolio selection.

To achieve this aim, the study pursues the following specific objectives to:

**i.** identify the types of heuristics most frequently employed by Nigerian PFA investment managers in the property selection and portfolio construction process;

**ii.** construct representative property portfolios from both heuristic-driven decision rules derived from survey findings and mean-variance optimization techniques adapted for discrete, indivisible real estate assets;

**iii.** conduct a comparative performance evaluation of heuristic-driven and mean-variance optimized portfolios; and

**iv.** examine the factors that influence the use of heuristics among Nigerian PFA investors.

## 1.4 Justification of the Study

The theoretical, contextual and practical grounds justify this study, as it adds to both theoretical and practical knowledge and practice.

This research has specific contributions to the real estate portfolio theory. The theoretical basis of the real estate portfolio theory is in the Modern Portfolio Theory as has been observed in different research publications by renowned scholars (Olaleye, 2011; Olaleye & Aluko, 2007). This paper takes a different view, looking at other variables and biases that come into play in the process of construction of the property portfolio. It also gives a methodological template of measuring the role and effectiveness of heuristics in emerging, opaque markets.

To paint the contextual picture further, the pension sector in Nigeria is among the biggest sources of institutional capital in Africa with an estimated ₦26 trillion assets under management (RisCura, 2020; PenCom, 2025). In a sector as large as this, the fact that less than 1% of total asset value is in real estate investments — as evidenced in the PenCom 2025 Q3 reports — is an indicator of underdevelopment. In this way, this study will fill a gap that is not only theoretical but has a major impact on the retirement income security of millions of contributors.

In practical terms, the findings of the study have direct implications for various stakeholder groups. In the case of Pension Fund Administrators, the study offers quantifiable data regarding the effectiveness of the existing practices in property portfolio selection decision-making. Depending on the result of the findings, PFA investment managers can streamline their property portfolio selection decision framework towards achieving better returns. Regulators (PenCom) can use findings to know whether the underutilization of current limits is a reality of the property market or is merely due to behavioural patterns. The regulators can determine whether PFAs have sufficient analytical capacity or whether industry-wide standards are required.

## 1.5 Scope of the Study

The analysis is on direct real estate investments in the portfolios of Pension Fund Administrators, but not REITs, development projects and other indirect property investments. REITs and other indirect property investments are not included since they have different decision processes compared to direct property investment. REITs create market pricing mechanisms which minimize information asymmetry and allow trading based on liquidity (Geltner et al., 2014). Construction risk and schedule uncertainty are also identified as brought about by development projects (Baum, 2015). Emphasis on direct investment is a way of isolating the particular decision context that the present study aims to investigate.

The research is restricted to PFAs licensed by PenCom only, and does not include PFCs and informal fund managers. This decision takes root in the statutory fact that PFAs are the investment decision-making entities in the Pension Industry; PFCs are simply custodians without investment directives (PRA, 2014; Fapohunda, 2013). As the study focuses on the heuristics of investment decisions, the research is accordingly focused on the area of PFAs within the PenCom regulatory framework where unlicensed or informal fund managers are not subject to regulation.

Finally, the research utilizes a fully-synthetic property data approach. Although this is largely attributable to the data opaqueness and lack of standardized historical property-level performance indices, this option permits a controlled environment for specific isolation and strict testing of heuristics, and is also consistent with existing practices in computational finance in data-scarce environments (Glasserman, 2004; Campbell et al., 1997).

## 1.6 Definition of Terms

**Heuristics:** Cognitive strategies or simplified decision rules that reduce complex problems to manageable judgments through shortcuts rather than exhaustive analysis (Tversky & Kahneman, 1974; Gigerenzer & Gaissmaier, 2011).

**Anchoring:** A cognitive bias whereby individuals rely disproportionately on the first piece of information encountered (the "anchor") when making subsequent judgments (Tversky & Kahneman, 1974). In real estate, anchoring commonly occurs when valuations or asking prices unduly influence assessments (Northcraft & Neale, 1987; Babawale, 2013).

**Availability Heuristic:** A mental shortcut relying on immediate examples that come to mind when evaluating decisions (Tversky & Kahneman, 1973). Individuals overweight vivid, recent, or easily recalled information, manifesting as preference for properties in highly visible locations.

**Herding Behaviour:** The tendency to mimic peer investment decisions rather than acting on independent analysis (Bikhchandani, Hirshleifer & Welch, 1992).

**Mean-Variance Optimization (MVO):** A quantitative portfolio construction technique, originating with Markowitz (1952), that selects allocations to maximize expected return for given risk (variance) or minimize risk for target return, identifying the "efficient frontier."

**Efficient Frontier:** The set of optimal portfolios in mean-variance space, representing maximum attainable expected return for each risk level (Markowitz, 1952).

**Sharpe Ratio:** A risk-adjusted return measure, calculated as $(R - R_f) / \sigma$, where $R$ is portfolio mean return, $R_f$ is risk-free rate, and $\sigma$ is standard deviation (Sharpe, 1966, 1994).

**Pension Fund Administrator (PFA):** Licensed entities authorized by PenCom to manage pension assets under the Contributory Pension Scheme (Pension Reform Act 2004, amended 2014), with fiduciary obligations to invest prudently.

**Property Universe:** A comprehensive set of synthetic properties from which all portfolios used within this research are constructed.

**Backtest Period:** The specific historical period from which real-world market data was gathered to construct property portfolios and test their performance.

---

# CHAPTER TWO

## LITERATURE REVIEW

## 2.1 Preamble

This chapter offers a literature review of both theoretical and empirical studies that are important in the context of understanding how Pension Fund Administrators (PFAs) use heuristics in selecting their property portfolios. It takes into account the evidence available in the literature to determine whether the application of heuristics in property portfolio selection is adaptive reactions to environmental limitations, or whether they are merely systematic biases that make investment managers lose money.

This review starts by examining the nature of real estate as an investment asset class and in the context of the Nigerian property market, and proceeds to examine the concept of portfolio construction and diversification. It then moves on to discuss property selection decision criteria for portfolios before settling on the concept, types and manifestations of heuristics in real estate portfolios. The chapter ends with a review of the theories that are applicable to the research, a chronological review of the existing literature that is relevant to the research, and a framework that conceptualizes the whole chapter and forms the basis of the further chapters.

## 2.2 Property Investment as an Asset Class

Real estate or real property possesses distinctive physical, financial, and market characteristics that fundamentally differentiate it from traditional investment securities such as stocks and bonds. These unique features both create opportunities and pose challenges that influence institutional investment decision-making, portfolio construction and diversification methods (Geltner et al., 2014; Hoesli & Lizieri, 2007).

### 2.2.1 Physical Characteristics of Real Estate

The physical characteristics of real estate impose certain constraints absent in other financial securities. These features are fundamental and affect real estate irrespective of location or any other conditions. They include:

**i. Indivisibility:** This refers to the fact that properties cannot be traditionally purchased in fractional units. An investor cannot acquire 5% of an office building in the way one might purchase 100 shares representing 5% ownership of a corporation (Baum & Hartzell, 2012).

**ii. Heterogeneity:** The uniqueness of each property means that no two assets are ever truly identical even within the same class and location (DiPasquale & Wheaton, 1996).

**iii. Immobility:** Permanence of location creates a situation where value depends critically on neighbourhood characteristics, accessibility, zoning, and environmental factors specific to the property's geographical co-ordinates (Thrall, 2002).

### 2.2.2 Financial Characteristics of Real Estate

Beyond physical attributes, real estate exhibits certain financial characteristics that define its role in investment portfolios. These attributes can either be positive or negative. Investment and portfolio managers must have a good knowledge of these characteristics and their macro effect on portfolio performance. They include:

**i. Income generation:** This typically occurs through rental income, and provides relatively stable and predictable cash flow, particularly for institutional-grade properties with credit-worthy tenants on long-term leases (Baum, 2015).

**ii. Appreciation potential:** This arises from both physical improvements to the land or building, and market dynamics. Properties in growth markets may appreciate substantially as neighbourhoods develop, transportation infrastructure improves, or zoning changes permit higher-density use (DiPasquale & Wheaton, 1996).

**iii. Inflation-hedging:** This is a unique property of real estate that represents a particularly valuable characteristic for long-term investors like pension funds. Real estate values and rental income have historically exhibited positive correlation with inflation, as rising general price levels increase construction costs (supporting property values) and enable rent escalation (Fama & Schwert, 1977; Brueggeman et al., 1984; Nwosu et al., 2024).

**iv. Illiquidity and high transaction costs:** This constitutes the most significant financial challenge of real estate investment. Real estate transactions require time for marketing, due diligence, negotiation, and legal documentation (Ling, 2005). Transaction costs, including brokerage commissions, legal fees, valuation fees, stamp duties, and other charges, create substantial friction that discourages frequent trading (Ling & Archer, 2020; Aluko, 2007).

### 2.2.3 Real Estate in Institutional Portfolios

After determining the particular physical and financial attributes of real estate, it is necessary to discuss the place of real estate in institutional portfolios. There are four main reasons why institutional investors consider real estate as part of their portfolio: to increase their returns, risk diversification, stability of income and inflation protection (Baum & Hartzell, 2012; Geltner et al., 2014).

The opportunity to diversify risk is the most significant and intriguing reason among the main reasons why real estate is included in institutional portfolios. According to the diversification model of Markowitz (1952), when real estate is added to a mixed-asset portfolio, the overall portfolio risk is decreased without a corresponding decrease in expected returns (Hartzell et al., 1986).

While the addition of real estate can effect positive results on institutional portfolios, that may not always be the case. Research by Okeahialam & Kalu (2024) studying the performance of real estate instruments in the investing of pension funds in Nigeria from 2012–2021 found that returns from direct real estate properties declined steadily, dropping from 58% in 2012 to 18.16% in 2021. The allocation percentage of PFAs to direct real estate is also reported to be 0.93% in Quarterly PenCom Reports (Q3, 2025), which is much lower than the regulatory amount of 10%. Based on all the available evidence, real estate in the institutional portfolio in Nigeria is on a negative trend both in terms of allocation and performance. The following section examines some of the unique characteristics of the Nigerian property market that could be causing this high institutional real estate under-allocation and under-performing portfolio.

### 2.2.4 Distinctive Features of Nigerian Real Estate Markets

While the characteristics described in Section 2.2 above apply generally to real estate as an asset class, the Nigerian property market exhibits several distinctive features that could amplify both opportunities and challenges for institutional investors. They are as follows:

**i. Title documentation complexity:** The Land Use Act of 1978 vested all land in each state in the governor holding it in trust for the people (Land Use Act, 1978). This means that "ownership of land" is merely a right of occupancy as opposed to actual freehold ownership, which is evident in the Certificate of Occupancy (C of O). Transferring this right requires "Governor's Consent", which adds an extra layer of complexity and bureaucracy (Aluko, 2007). Furthermore, as explained by Smith (2013), other forms of title documentation such as Gazette, Excision, and Deed of Assignment exist within the Nigerian regulatory framework. This naturally creates a hierarchy of title quality (C of O > Governor's Consent > Gazette > Excision > Deed of Assignment) with C of O being the most credible, and Deed of Assignment being the least credible.

**ii. Market opacity and information asymmetry:** Nigeria lacks a reliable property transaction record system. Most transactions are privately conducted, with prices remaining undisclosed, leading to situations where buyers and sellers enter into negotiations with vastly different levels of information, mostly skewed in favour of the sellers (Olapade et al., 2019). This creates severe information asymmetry and is well documented as Nigeria ranks within the "Low transparency" tiers of the Global Real Estate Transparency Index (JLL, 2024). Resultantly, institutional investors may have to rely on subjective judgements and assumptions, rather than reliable data.

**iii. High transaction costs:** While high costs of transaction is a primary feature of real estate globally, transaction costs in Nigeria exceed those in developed markets. The NIESV's scale for agency and valuation fees (2014) sets these values at about 5–10%. Aluko (2007) argues that once these costs accumulate (combined with other taxes and levies), they create the constrained, illiquid real estate market that we know. In light of the above, it can be deduced that the cost of acquiring or disposing of real estate represents a good percentage of its capital value. As a result, short-term portfolio rebalancing becomes much less viable and less attractive of a prospect to institutional investors, leading them to either invest substantial amounts of capital into "lumpy", illiquid assets, or invest said capital in more liquid markets.

In light of the above unique features of the Nigerian property market, the next section discusses the specifics of property portfolio construction and how it relates to emerging, data-scarce property markets like Nigeria's.

## 2.3 Property Portfolio Selection

The principles of property portfolio selection lie in the Modern Portfolio Theory by Markowitz (1952, 1959) that argues that investors can maximize their returns on their portfolio and at the same time reduce the unsystematic risk by diversifying their assets. This can be done through the combination of assets that have low correlation so that investors can safely absorb risk and increase overall returns. Other than the Modern Portfolio Theory methods, Olaleye (2011) talks in detail about the naïve diversification methods that use conventional wisdom and rule of thumb in the choice of portfolio assets and diversification methods. This section elaborates on the principles of diversification of property portfolio and the various strategies.

### 2.3.1 Principles of Portfolio Diversification

Olaleye (2011) defines portfolio diversification as the technique of varying investment possibilities in order to minimise the encompassed risks and maximise the return therefrom. Harry Markowitz won the Nobel prize in economics in 1990 for his research work on portfolio theory in the 1950s. The crux of his theory centred on the idea that the combination of assets with less than positive correlation serves to reduce the weighted-averaged variance (risk) of the portfolio beyond the level of risk associated with individual constituents.

Having established the concept of diversification and its relative importance in portfolio selection, it is important to assess if the extent of diversification of a portfolio can be measured. Choueifaty & Coignard (2008) introduced the Diversification Ratio (DR) as a metric for capturing portfolio selection quality where the weighted average of individual asset volatilities is divided by portfolio volatility.

When assets are perfectly correlated, the ratio equals 1, signaling that no diversification benefit is achieved. As correlations decrease, the diversification ratio rises above 1, with higher values indicating more effective risk reduction through diversification.

From the above evidence, the guiding principles behind portfolio diversification can be deduced as the need for investors to maximize their profits while simultaneously minimizing their risk. Olaleye (2011) proceeds to state that there are two main approaches to portfolio diversification, namely: the traditional approach or naïve diversification and the Modern Portfolio Theory-based approach. The rest of this sub-section takes a cursory look at these approaches and their suitability for institutional investors like PFAs.

### 2.3.2 Naïve Diversification Strategies

Naïve or traditional diversification strategies involve the use of conventional wisdom and intuition in the portfolio selection process. This description is supported in literature, first by Hadaway (1978), and subsequently by Hargitay & Yu (1993). Within the context of real estate, naïve diversification has majorly been explored along two dimensions: geographic/economic diversification and property type diversification.

Geographic diversification is based on the idea that real estate investments, as a function of location, vary in terms of returns and risk. As such, investors would need to consider the challenges and opportunities present at various locations and select properties accordingly (Olaleye, 2011).

Property type diversification has its roots in the idea that the returns and risks associated with a property vary according to the particular industries utilizing said property. Different types of properties respond to the needs of different sectors, and for investors, this means being aware of the factors affecting the users of each property type and their inherent characteristics (Olaleye, 2011). This diversification strategy involves investing in various property types like office buildings, warehouses and hotels (Penny, 1982).

Research from scholars such as Del Casino (1995) and Olaleye & Aluko (2007) has uncovered other strategies that have garnered investor attention in recent years, namely: managers diversification, lease diversification, timing diversification, investment structure diversification, and investment vehicle diversification.

Different studies have tested the efficacy of naïve diversification strategies, most notably Olaleye et al. (2008) and DeMiguel et al. (2009). Their findings point to the idea that naïve diversification proves to be rather competitive, sometimes even outperforming quantitative analysis in out-of-sample situations. Consistent results like these only serve to reinforce the applicability of naïve diversification and justify its position in this study as a valid strategy for portfolio construction.

### 2.3.3 Modern Portfolio Theory: Foundations and Application to Real Estate

This subsection shifts the focus away from naïve diversification strategies to diversification as prescribed by the Modern Portfolio Theory. It examines the foundations of the theory, its guiding principles, and its application to real estate.

#### 2.3.3.1 Foundations of Modern Portfolio Theory

The Modern Portfolio Theory (MPT), which started with the article of Markowitz (1952), *Portfolio Selection*, transformed the analysis of investments by formalizing how investors ought to form portfolios to maximize the tradeoff between the expected return and risk. The theory has established itself as the leading theory in institutional asset management because it offers the theoretical basis of asset allocation, performance measurement, and portfolio optimization in virtually all asset categories such as real estate (Elton et al., 2014; Reilly & Brown, 2012).

The Modern Portfolio Theory is based on the mean-variance model which presupposes that investors are more interested in high returns (mean) and low risk (variance). The weighted average of the returns of individual assets is thus expected to be the expected portfolio returns of a portfolio of assets (Elton et al., 2014).

Applying the mean-variance model, given a collection of assets with expected returns, variances, and covariances, there is a collection of mean-variance efficient portfolios. Such portfolios provide the highest expected payoff at a certain degree of risk, or the lowest risk at a specific desired payoff (Markowitz, 1952). The set of all efficient portfolios is known as the efficient frontier, which is usually represented as a curve in the space of means and variance (Elton et al., 2014).

Portfolios that lie below the efficient frontier are dominated, i.e., there are other combinations that will give either a higher payoff at the same risk or a lower risk at the same payoff. According to Merton (1972), rational investors ought to only possess efficient portfolios. His point was that the possession of dominated portfolios either meant irrationality or a limitation to access to efficient allocations.

The efficient frontier is constructed by solving an optimization problem. In the original formulation by Markowitz (1952), the investor would minimize the portfolio variance to achieve a given target return. The efficient frontier is traced out by solving this optimization problem systematically by varying a target return $R^*$ and solving for minimum variance at each target.

#### 2.3.3.2 Applications of Modern Portfolio Theory to Real Estate

One of the first uses of portfolio theory in real estate was the study by Friedman (1971) of diversification in REITs, which showed that diversification of a portfolio of properties across geographic markets and property types could decrease portfolio variance, empirically confirming the diversification principles of Markowitz in a real estate environment. This was furthered by Robichek, Cohn & Pringle (1972), who explicitly developed a mean-variance optimization model of real estate portfolios, demonstrating that efficient frontiers could be built using property-level return and risk information.

In the 1970s–1990s, studies increasingly optimized the portfolio of real estate, investigating the benefits of diversification by property type (office, retail, industrial, residential) and geographic market (Hartzell, Hekman & Miles, 1986; Malizia, 1991). These researches tended to verify that real estate has positive risk-return tradeoffs and diversification of property types and locations enhances portfolio efficiency, but the extent of benefits and optimum allocations were controversial (Giliberto, 1993; Mueller, 1993).

#### 2.3.3.3 Real Estate-Specific Challenges in Portfolio Optimization

Applying Modern Portfolio Theory to real estate encounters several distinctive challenges absent in equity portfolio optimization:

**i. Data scarcity in emerging markets:** Constructing efficient frontiers requires expected returns, variances, and a full covariance matrix across all potential properties. In developing countries like Nigeria, transaction data is sparse, inconsistently reported, and often unreliable, making parameter estimation highly uncertain (Olapade et al., 2019; Aluko, 2007).

**ii. Return estimation difficulties:** Real estate returns comprise rental income and capital appreciation. While rental income is observable from lease contracts, capital appreciation requires either appraisals (which are infrequent and potentially biased) or transaction prices (which are rare for individual properties) (Babawale & Ajayi, 2011; Geltner, 1991).

**iii. Covariance matrix construction:** The covariance matrix for $n$ assets requires $n(n-1)/2$ unique covariances. For a portfolio of 50 properties, this entails 1,225 covariance estimates. With limited transaction frequency, estimating property-to-property covariances directly is often infeasible.

**iv. Discrete (non-divisible) asset allocation:** Classical mean-variance optimization assumes continuous weights — that is, an investor can hold 3.7% of each asset. Real estate's indivisibility means an investor either owns a property (100%) or does not (0%) (Byrne & Lee, 2004).

## 2.4 Heuristics in Investment Decision-Making

The above sections have determined that the selection of property portfolio is a decision problem of true challenge. The combination of various factors like indivisible assets, opaque pricing, limited transaction histories, and high cost of obtaining information creates an environment where formal optimization inputs are not often available in the necessary quantity and quality. The logical question that arises is: how do investment managers make decisions in the real world? The solution is that they are based on simplified decision rules that simplify the selection problem to a set of manageable criteria. These heuristics are referred to as decision rules. This section discusses the theoretical basis of heuristic decision-making by contrasting two large traditions that issue contradictory predictions about their implications, and then discusses each of the four heuristics that are the focus of this paper in turn.

### 2.4.1 Bounded Rationality and Satisficing

The foundational challenge to the assumption of perfect rationality by Herbert Simon (1955) is a good place to begin to understand the reasons behind the use of heuristics by investment managers. Simon believes that the classical theory of *Homo Economicus*, who is always rational and possesses perfect information and always makes decisions that maximise expected utility, is not plausible. Simon says that real decision-makers are bound by three constraints, namely: cognitive constraints, which limit the amount of information that the human mind can process at once; information constraints, which imply that full and accurate information on all decision options is seldom available; and time constraints, which place practical limits on the time available to deliberate before a decision must be made.

Among the three limitations that Simon lists, the lack of information is arguably the most pressing in the Nigerian situation. Not that time is infinite or cognition free, but that even an infinite time and an infinite capacity of cognition cannot possibly be used to offset data that is not there.

Simon went on to argue that under the above constraints, decision makers are not optimizing, but they *satisfice* (Simon, 1956). Satisficing is a search process in which one goes through the options in a sequential manner until one is reached that satisfies a minimum acceptable criterion (Simon, 1955). The standard itself is dynamic and increases when alternatives that are acceptable can be readily discovered and decreases when search becomes long and difficult (March & Simon, 1958).

In the case of property portfolio selection, satisficing is manifested in the use of simplified selection rules that rapidly determine a set of acceptable properties in a large universe of candidates. These rules are the heuristics that this research aims to discover, quantify and assess.

### 2.4.2 The Heuristics and Biases Programme (Kahneman & Tversky, 1974)

Although the limited rationality of Simon can justify the use of heuristics, the research programme of Tversky & Kahneman (1974) defined their nature and the errors they cause. This study proved that people use few general purpose heuristics to make probabilistic judgements; namely, representativeness, availability, and anchoring and adjustment. Although these heuristics are frequently helpful and effective, they make systematic, predictable errors when used on problems to which they are ill adapted.

This programme has empirical extension directly into investment decision-making. Barberis & Thaler (2003) have given a detailed survey of the evidence of Kahneman-Tversky heuristics in the observed equity market anomalies. Shiller (2003) claimed that irrational exuberance in the stock and real estate markets is the systematic functioning of the heuristics of availability and representativeness at scale. The importance of this body of evidence to the current study is that it suggests that professional training or institutional sophistication cannot eradicate cognitive biases since even expert decision-makers have been demonstrated to be susceptible to heuristic biases.

### 2.4.3 Ecological Rationality: The Case for Heuristics (Gigerenzer et al., 1999)

The Kahneman-Tversky tradition views heuristics as cognitive biases that are to be rectified by the normative rationality standard. An opposing tradition, related to Gigerenzer, Todd and the ABC Research Group (1999), states that this framing is intrinsically deceptive. The principle of ecological rationality states that a heuristic cannot be well judged by a normative ideal, but rather by the particular environmental organization where decisions are taken. An easy rule that disregards most of the information available can work very well in a noisy, data-scarce setting because it is resistant to estimation error. On the other hand, an advanced optimization model which tries to utilize all the available information can be very poor when the inputs are not reliable (Gigerenzer & Gaissmaier, 2011).

This is not just a hypothetical argument. DeMiguel et al. (2009) compared fourteen portfolio optimization models with a naïve equal-weighting strategy on several datasets and discovered that no optimization model was able to outperform the more basic alternative out-of-sample. This was due to the fact that the error in estimation of the inputs of the optimization works against the theoretical gains. This was formalized by Tu & Zhou (2011) who demonstrated that naïve diversification is the optimal choice in mean-variance optimization when the number of historical observations is smaller than $(N+2)(N+5)$, where $N$ is the number of assets.

The ecological rationality view does not, however, offer unconditional support to the use of heuristics. Kahneman & Klein (2009) claimed that true intuitive expertise needed a decision situation where the patterns were learnable and the feedback was sufficiently fast to permit calibration over time. Nigerian institutional real estate does not meet either of the conditions very well. There is low frequency of transactions, opaque prices, and the acquisition to observable return feedback loop may take years to complete. The implication is that experience in this market might not systematically enhance the quality of heuristics. The two traditions thereby find themselves in an empirical question, not a theoretical conclusion: in the particular data setting of Nigerian institutional property investment, are the heuristics used by PFAs close enough to optimal selection to be adaptive, or are they subject to a measurable and remediable cost in performance? The empirical chapters of this study are intended to answer this question.

### 2.4.4 The Four Heuristics of Focus

The four heuristics discussed in this paper (anchoring, availability, representativeness and herding) were chosen based on their importance in the behavioural finance and real estate literature and their relevance to the particular institutional setting of the Nigerian PFA property selection. They are discussed below individually and supported by the evidence found in the literature, and their expected appearance in the Nigerian PFA situation.

#### 2.4.4.1 Anchoring and Adjustment

Tversky & Kahneman studied anchoring in the heuristics and biases programme in 1974. They defined it as a mental disposition to start with an initial value (the anchor), and to make an adjustment out of it in making a final estimate; the key defining feature of which is that the adjustment is insufficient in a systematic way. Consequently, the anchor has a disproportionate effect on the ultimate decision, biasing it towards the initial position despite later evidence that would have rationally warranted a greater adjustment. Epley & Gilovich (2006) showed that this inadequacy arises due to the fact that individuals cease to make adjustments once they have reached a value that they find plausible instead of making adjustments until they arrive at the normatively correct estimate. The effect is strong: it is present among expert respondents, with incentivized choices, and even when the anchor is explicitly known to be arbitrary or random.

Northcraft & Neale (1987) presented the first and most frequently used evidence of anchoring in property valuation in the context of real estate. Professional estate agents, who were presented with the same property at varying listing prices, made valuations similar to those listing prices by a significant amount, even though they claimed that listing price had not affected their judgement. The implications on PFA decision-making are important because even the valuations obtained by hiring external surveyors are also likely to be anchored to asking prices. This implies that the investment committee of the PFA might have an anchored input at the initial stage of its deliberations. This anchoring chain will probably be longer and stronger in the Nigerian environment, where independent comparable sales data are scarce, and external surveyors have to rely heavily on the price expectations stated by the client, compared to markets with transparent transaction databases (Iroham et al., 2013a; Olapade et al., 2019).

#### 2.4.4.2 Availability Heuristic

A PFA investment officer is physically integrated in the Lagos Island real estate market. He/she regularly encounters the best office developments in Victoria Island and frequently sees advertisements for Ikoyi properties on social media. Lagos Island will be disproportionately represented in his/her property portfolio not because Lagos Island is necessarily better on risk-adjusted terms, but because it is easier to think about. This is a textbook scenario of the availability heuristic.

Explored by Tversky & Kahneman (1973), the availability heuristic is defined as the tendency to judge the probability or frequency of events by the ease with which instances come to mind. Events that are easily remembered are estimated as more likely or more common than those that are hard to recall. In investment, availability is a systematic bias towards familiar, repeatedly-discussed, or recently-prominent assets. This tendency was reported by French & Poterba (1991) on the national equity markets level. They observed that in all the countries they surveyed, investors had disproportionately large holdings of domestic equities, although the diversification benefits of international exposure are proven. They concluded that the domestic markets are more visible, more often discussed in the local media and remembered than foreign alternatives, thus investors tend to invest in them more.

As shown in the illustration above, although Lagos Island might have favourable property portfolio traits, it equally may not. The heuristic and rational choice might not necessarily point in the same direction. The lack of rationality and evidence in the decision is what should be examined, and this is exactly what makes this phenomenon worth researching.

#### 2.4.4.3 Representativeness Heuristic

The representativeness heuristic was proposed by Kahneman & Tversky (1972). It explains how individuals are likely to conclude that an object is a member of a category, or that an event was caused by a process, depending on the extent to which it is similar to the prototype of the category or process. The cluster of related errors caused by representativeness includes insensitivity to base rates, insensitivity to sample size, and the inability to regress to the mean. The implications of representativeness have been illustrated in the case of investment by De Bondt & Thaler (1985). They argue that equity investors over-extrapolate recent performance, where a spell of good returns is taken to be indicative of a truly superior asset and thus over-paid, only to be corrected by the natural process of mean reversion which creates losses.

Representativeness in property portfolio selection is anticipated to be in the form of sector or location momentum chasing. The low frequency of transactions in the Nigerian institutional real estate context would suggest that a submarket that has generated above-average capital appreciation over the latest period of observation can be considered reflective of a more desirable investment destination with little consideration of whether the recent performance is sustainable or not. This tendency is especially consequential in Nigeria since the evidence base of any inference is thin due to the absence of data. A decision-maker who has two years of robust appreciation in a particular submarket has little ground to differentiate between structural strength and a market cycle. This implies that portfolio selection will be based on recent performances as opposed to risk-adjusted estimates of returns.

#### 2.4.4.4 Herding Behaviour

A decision made by an investment manager that is unconventional and underperforming would have more dire reputational implications than an equivalent underperforming conventional decision. This is what Scharfstein & Stein (1990) concluded when they examined institutional investment decision-makers. This imbalance is arguably a rational incentive to imitate peer institutions, regardless of any informational argument. This is what is referred to as herding.

Studies on herding behaviour came later than the other types of heuristics. It was modelled by Bikhchandani, Hirshleifer & Welch (1992) as a phenomenon in which each decision-maker monitors the behaviour of their predecessors and, aware that other decision-makers may have information that is more up-to-date than their own, rationally adjusts towards their decisions. When this dynamic is applied to similar populations, the outcome is that individual information is suppressed and group decisions converge on a limited set of choices. This convergence does not occur due to the objective superiority of these options, but rather because the observation of the choices of others by a person leads to the same conclusion. According to Scharfstein & Stein (1990), a complementary mechanism particular to institutional investment is career-motivated herding: a decision that underperforms by an investment manager that is unconventional would have more dire reputational effects than a decision that underperforms by the same margin that is conventional.

The five largest PFAs in the Nigerian PFA sector hold about 60 percent of the sector (PenCom, 2024) and smaller PFAs can reasonably assume that the bigger institutions have done more thorough due diligence on the properties they own. The fact that a large PFA has purchased assets in a specific submarket is thus a noteworthy indicator, rather than a random benchmark. On the same note, PFA investment officers who do not conform to peer practice in a manner that results in underperformance may be subject to regulatory investigation as well as personal accountability concerns, whilst those who conform to the crowd may have less personal exposure even when the overall performance is poor. The combination of these mechanisms implies that the portfolios of PFA properties in Nigeria will be concentrated in the same locations, the same types of assets, and even the same properties.

## 2.5 Theoretical Framework

The literature reviewed in Sections 2.2 through 2.4 draws from three distinct theoretical groups, each of which occupies a specific position in the analytical architecture of this study. These groups stand in tension with one another, and the resolution of that tension through empirical investigation is the primary contribution of the study.

The first group is headlined by Modern Portfolio Theory, originating with Markowitz (1952) and extended by Sharpe (1964; 1966; 1994). This group defines the normative benchmark: what an optimally constructed real estate portfolio would look like if all inputs were available and all constraints were correctly specified. Mean-variance optimization provides the efficient frontier against which actual heuristic-driven portfolios will be compared, and the Sharpe ratio provides the primary metric of risk-adjusted performance.

The second group comprises the theoretical explanations for why selection deviates from the normative benchmark. Simon's (1955; 1956) bounded rationality theory establishes the conditions under which simplification becomes a rational response. Akerlof's (1970) information asymmetry model contextualizes why these constraints are particularly acute in property markets. The systematic advantage of sellers over buyers in information access creates structural pressure toward rules-of-thumb that partially substitute for unattainable private information. Tversky & Kahneman's (1974) heuristics-and-biases programme identifies the specific cognitive mechanisms through which that simplification occurs.

The third group contains competing theories about the consequences of deviation. The Kahneman-Tversky perspective predicts that heuristics impose measurable performance costs, as portfolios will lie inside the efficient frontier, and the distance from the frontier will be attributable to the systematic biases each heuristic introduces. The ecological rationality perspective, advanced by Gigerenzer et al. (1999) and empirically supported by DeMiguel et al. (2009) in the portfolio context, predicts that in data-scarce environments, the performance gap may be smaller than theory suggests, or may even close entirely in favour of the simpler approach. The competing empirical predictions provided by these theories creates a tension that can only be arbitrated by evidence from the specific market and institutional context in question.

Table 2.1 below summarizes the theories within these three groups, their primary authors, and their role in this study:

<a id="table-**table 21: theoretical framework**"></a>
**Table 2.1: Theoretical Framework**

| **Theories** | **Key Authors** | **Role in this Study** |
| :--- | :--- | :--- |
| Modern Portfolio Theory | Markowitz (1952); Sharpe (1964; 1966; 1994) | Defines the normative benchmark and optimization criterion |
| Bounded Rationality | Simon (1955; 1956) | Explains why heuristics arise in property selection |
| Heuristics and Biases | Tversky & Kahneman (1974); Kahneman (2011) | Identifies specific heuristics and predicts that they impose costs |
| Ecological Rationality | Gigerenzer et al. (1999); Gigerenzer & Gaissmaier (2011) | Provides the competing prediction that heuristics may be adaptive |

*Source: Author's Research (2026)*

## 2.6 Empirical Review

Empirical literature that is directly pertinent to this study is listed below according to research objectives. In each sub-section, the studies are given in general chronological order and each sub-section ends with a statement of the particular gap that the respective objective is filling.

### 2.6.1 Studies on Heuristics in Institutional Investment

The empirical investigation of the heuristic patterns of institutional investment has a brief, yet significant history. Scharfstein & Stein (1990) gave a theoretical explanation of herding by their career-risk model, which showed that rational agents subject to reputational costs will imitate others even when unobservable information suggests otherwise. Herding and window-dressing in US pension fund equity portfolios were recorded by Lakonishok, Shleifer & Vishny (1992) who discovered that institutional funds traded in ways that could not be explained by the usual information available to the population. This confirmed that even highly controlled institutions have their tendencies to be irrational. Clark & Urwin (2008) furthered this question to the governance aspect, where the quality of the processes of decision-making by pension funds was identified to be the key factor in deciding whether investment decisions were made in an optimal manner. Weakly governed funds were more prone to herding and other heuristic biases whereas strong governed funds were more analytical.

In the African context, Lowies et al. (2016) reported significant statistical evidence of anchoring and adjustment heuristics among South-African property fund managers.

<a id="table-**table 22: studies on heuristics in institutional investment**"></a>
**Table 2.2: Studies on Heuristics in Institutional Investment**

| **Study** | **Finding** |
| :--- | :--- |
| Scharfstein & Stein (1990) | Career-risk could lead to herding |
| Lakonishok et al. (1992) | Herding in US Pension Fund equity portfolios |
| Clark & Urwin (2008) | Decision-making processes determine optimality |
| Lowies et al. (2016) | Anchoring & Adjustment among South-African property fund managers |

*Source: Author's Research (2026)*

Thus, there are two gaps that Objectives I and IV aim to fill. First, although heuristics have been studied in the context of real estate, primary research has not experimentally established the particular heuristics used by Nigerian PFAs when choosing properties. Second, no research has been done on the institutional and informational elements that account for the usage of PFA heuristics in Nigeria.

### 2.6.2 Studies on Comparative Performance: Heuristics vs Optimized Portfolios

Various researchers have explicitly compared the performance of portfolios selected by rule-based or optimization-based methods in real estate or similar settings. These studies have yielded different results which are discussed below.

Mueller & Ziering (1992) discovered that the US institutional property portfolios built with simple sector allocation rules had about 22% more annual volatility than the mean-variance optimized portfolios with the same expected returns. This indicates that heuristic selection incurred a quantifiable risk cost and no counterbalancing benefit. Steinert & Crowe (2001) compared optimized and rule-based international property portfolio strategies in fifteen countries and discovered that mean-variance optimization generated a Sharpe ratio of 0.64 as compared to 0.51 by the rule-based approach.

This is supported by Lee & Stevenson (2006) who discovered that the prime-location rule-based strategies outperformed optimization-based diversification of Irish institutional property portfolios in 1994–2004. Studies by Olaleye et al. (2008) and DeMiguel et al. (2009) in various market settings found that rule-based strategies are robust enough to compete, and even out-of-sample, outperform optimized portfolios.

<a id="table-**table 23: studies on heuristics vs optimized portfolios**"></a>
**Table 2.3: Studies on Heuristics vs Optimized Portfolios**

| **Study** | **Finding** |
| :--- | :--- |
| Mueller & Ziering (1992) | US heuristic property portfolios exhibited 22% more volatility than mean-variance portfolios |
| Steinert & Crowe (2001) | Mean-variance portfolios produced a Sharpe ratio of 0.64 against 0.51 for heuristic portfolios |
| Lee & Stevenson (2006) | Rule-based strategies outperformed optimization strategies for Irish portfolios in 1994–2004 |
| Olaleye et al. (2008) | Naïve portfolios proved more robust for real-world scenarios than optimized portfolios |
| DeMiguel et al. (2009) | Heuristic portfolios perform better than optimized portfolios out-of-sample |

*Source: Author's Research (2026)*

The above evidence reveals a definite change in the perceived dominance of optimized portfolios over heuristic portfolios with the years passing and the situations in the study areas evolving. The pioneering study by Mueller & Ziering (1992) was done in the US where property-level data and market indices are accessible. Later studies by Olaleye et al. (2008) and DeMiguel et al. (2009) demonstrate that such an advantage is soon lost when the market conditions vary, and the inputs to optimization become less accessible. These are what the Nigerian market is modelling to a large extent and therefore this research is truly informative and not just a reaffirmation of a previously-known finding.

### 2.6.3 Research Gaps

Drawing together the evidence from Sections 2.6.1 and 2.6.2 above, three research gaps can be identified, each corresponding directly to one of this study's objectives:

**Gap I (Objective I: Identify heuristics):** No published study has empirically documented, through primary research with investment practitioners, the specific heuristics employed by Nigerian Pension Fund Administrators in property portfolio selection. International evidence identifies the likely candidates but cannot confirm which are most prevalent in the Nigerian institutional context, nor in what form they manifest given the specific regulatory, informational, and governance environment of the Nigerian pension industry.

**Gap II (Objective II: Comparative performance):** The comparative performance of heuristic-driven and optimal property portfolios has been examined in developed markets with established transaction histories and performance indices. No comparable study exists for Nigeria specifically for heuristics. The question of whether the optimization advantage documented in international studies holds in a data-scarce environment is what this study directly addresses.

**Gap III (Objective III: Factors driving heuristics):** While the general determinants of heuristic use in institutional investment have been examined, the specific factors that explain heuristic reliance among Nigerian PFA investment managers have not been investigated through primary research. The answer to this gap has implications for what interventions would most effectively improve decision quality.

## 2.7 Conceptual Framework

The literature review in this chapter provides a clear analytical argument which can be summarized in three statements: (a) the Nigerian property market is characterized by real informational and structural problems that create a situation in which simplified decision rules are comprehensible and potentially expensive; (b) the four heuristics discussed in this work are the processes by which those simplified rules are implemented; and (c) two theoretical traditions predict competing outcomes as to whether such simplified rules are costly. Chapters Three and Four are empirical work aimed at solving this competition by direct measurement.

These relationships can be represented in one pathway diagram in the conceptual framework of the study as shown in Figure 2.1 below. The framework starts with the two types of conditions which form the decision environment in which the PFA property selection is done: (a) environmental conditions — the characteristics of the Nigerian property market; and (b) institutional conditions — the governance structures, regulatory constraints, and career incentives of the PFA investment environment. These conditions combined produce a decision environment that is typified by high information costs, slow feedback, and structural pressure to simplified selection strategies.

In this context, the four heuristics of focus serve as selection processes, which convert decision pressure into particular portfolio decisions. Anchoring limits the scope of consideration and anchors investment decisions to previous reference points. The availability heuristic focuses selection on familiar markets both geographically and informationally. Momentum-based sector allocation is motivated by representativeness. The portfolio of herding is similar to peer fund holdings. The heuristics have a quantifiable mark in the portfolio composition that results, and the questionnaire used in the study (Objective I) is aimed at determining the relative frequency and weighting of each.

The heuristic portfolio is built on the basis of a synthetic property universe by the weighted calibration of the results of the questionnaire and is then compared to the mean-variance optimized portfolio built on the same property universe. The result of this comparison (Objectives II and III) is the Sharpe ratio difference, the diversification ratio difference, and the return and risk measures that enable the study to decide whether heuristics represent an incorrectly costly decision, or are adaptive in this particular market setting. The results guide the theoretical resolution at the bottom of the framework: where optimization is significantly better, the Kahneman-Tversky prediction is confirmed; where heuristics perform within the practical significance level of optimization, the ecological rationality prediction is confirmed.

Instead of assuming a pre-determined result, this study treats the relative performance of the heuristic and optimized portfolios as an open question. Although the balance of evidence in the international comparative studies records that optimization tends to be more successful than heuristic selection (Mueller & Ziering, 1992; Steinert & Crowe, 2001), the extreme data obscurity and instability of the Nigerian market establishes circumstances in which those mathematical benefits could be lost. High estimation errors can offset the benefits of optimization, as DeMiguel et al. (2009) show, and this gives the ecological rationality framework of Gigerenzer theoretical support. Thus, this theoretical framework is strictly neutral. The empirical findings presented in Chapter Four will on their own determine whether the Nigerian institutional environment is in accordance with the expectations of the heuristics-and-biases programme or the ecological rationality paradigm.

<a id="figure-**figure 21: conceptual framework diagram**"></a>
**Figure 2.1: Conceptual Framework Diagram**

![Figure 2.1: Conceptual Framework Diagram](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/figure_2_1_conceptual_framework.png)

*Source: Author's Research (2026)*

---

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

<a id="table-**table 31: objectives data requirement**"></a>
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

<a id="table-**table 32: complete directory of pencom-licensed pfas in nigeria (q1, 2026)**"></a>
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

<a id="table-**table 33: property universe geographic distribution**"></a>
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

<a id="table-**table 34: property universe asset-type distribution**"></a>
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

<a id="table-**table 35: property universe title status distribution**"></a>
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

<a id="table-**table 36: property universe price range distribution**"></a>
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

<a id="table-**table 37: property universe condition distribution**"></a>
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

<a id="table-**table 38: performance metric calculation**"></a>
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

---

# CHAPTER FOUR

## DATA PRESENTATION, ANALYSIS AND INTERPRETATION

## 4.1 Preamble

The empirical results, statistical analyses and theoretical interpretations derived from the mixed methodology described in Chapter Three are presented in this chapter. The chapter is organized in the order of the research questions, so that each section addresses one of the four research questions. The background data about the respondents are provided in Section 4.2, which includes a demographic profile and an institutional profile. Section 4.3 deals with the identification of prevailing heuristics, describes the composite heuristic scores and calibrates the empirical decision weights. Heuristic and Mean-Variance Optimized portfolios are described in terms of their portfolio construction mechanism, asset type comparisons and asset-class diversification profiles in Section 4.4. The comparative performance is presented in Section 4.5 using Monte Carlo simulation, paired hypothesis testing, market volatility stress tests and interest rate sensitivity analysis. In Section 4.6, the factors that affect the use of heuristics in property portfolio construction are discussed.

### 4.1.1 Questionnaire Administration and Response Rate

The field survey focused on the total population of institutional pension fund managers in the Nigerian pension industry regulated by the National Pension Commission (PenCom). Structured questionnaires were sent to all 24 licensed pension fund operators, which included 19 Retirement Savings Account (RSA) Pension Fund Administrators (PFAs) and 5 Closed Pension Fund Administrators (CPFAs).

The administration of the questionnaire used a purposive census approach, with multiple requests for questionnaires sent to investment professionals from May to July 2026, to ensure high data integrity. The total distribution of the physical and digital questionnaire instruments included Chief Investment Officers (CIOs), Senior Portfolio Managers, Real Estate Investment Analysts and Risk & Compliance Managers from senior investment professionals.

The administration mechanics, retrieval breakdown and the effective response rate for the study are listed in Table 4.1.

<a id="table-**table 41: questionnaire administration and retrieval rate**"></a>
**Table 4.1: Questionnaire Administration and Retrieval Rate**

| **Questionnaire Status** | **Frequency (n)** | **Percentage (%)** |
| :--- | :---: | :---: |
| Total Administered | 24 | 100.0 |
| Retrieved (Valid for Analysis) | 24 | 100.0 |
| Unreturned / Incomplete / Invalid | 0 | 0 |

*Source: Field Survey, 2026*

Of the 24 questionnaire instruments given to the institutional target population, 24 were retrieved, which gave an effective response rate of 100.0% as indicated in Table 4.1. This is due to the fact that the research employs a census methodology where all members of the study population need to be accounted for. Since the 24 questionnaires retrieved represent the total number of pension fund operators in the country licensed by PenCom, the dataset is a 100% institutional operator census. This full coverage removes the non-response sampling bias at the firm level, giving a firm empirical base for generalizing the results to the whole of the pension industry.

## 4.2 Background Information of Respondents

This section presents a detailed analysis of the general information of the respondents. It examines characteristics such as job title, years of experience and fund size, and provides an overall picture of the general profile of the respondents.

### 4.2.1 Demographic and Professional Profile

<a id="table-**table 42: respondent professional demographics and organisational characteristics (n = 24)**"></a>
**Table 4.2: Respondent Professional Demographics and Organisational Characteristics (n = 24)**

| **Demographic Profile Attribute** | **Frequency (n)** | **Proportion (%)** | **Cumulative (%)** |
| :--- | :---: | :---: | :---: |
| **Direct Decision Participation** | | | |
| Direct Decision Authority | 7 | 29.2 | 29.2 |
| No Direct Participation | 17 | 70.8 | 100.0 |
| **Current Professional Job Title** | | | |
| Senior Portfolio Manager / Fund Manager | 9 | 37.5 | 37.5 |
| Risk and Compliance Officer | 6 | 25.0 | 62.5 |
| Investment / Financial Analyst | 4 | 16.7 | 79.2 |
| Chief Investment Officer (CIO) / Head of Investment | 3 | 12.5 | 91.7 |
| Dedicated Real Estate Asset Manager | 2 | 8.3 | 100.0 |
| **Years of Investment Experience** | | | |
| 6–10 years | 14 | 58.3 | 58.3 |
| 3–5 years | 4 | 16.7 | 75.0 |
| 11–15 years | 3 | 12.5 | 87.5 |
| Above 15 years | 3 | 12.5 | 100.0 |
| **Assets Under Management (AUM) Scale** | | | |
| Above ₦2 Trillion | 9 | 37.5 | 37.5 |
| ₦500 Billion – ₦2 Trillion | 9 | 37.5 | 75.0 |
| Below ₦500 Billion | 6 | 25.0 | 100.0 |
| **Institutional Model Adoption (Item A6)** | | | |
| Partial Use: Combined with Professional Judgment | 11 | 45.8 | 45.8 |
| No Model Use: Primary Reliance on Judgment/Experience | 6 | 25.0 | 70.8 |
| Full Use: Models form Primary Selection Basis | 5 | 20.8 | 91.7 |
| Unaware of Quantitative Selection Models | 2 | 8.3 | 100.0 |

*Source: Field Survey, 2026*

The demographic distribution in Table 4.2 provides a very experienced and qualified sample of institutions. More than 80% have more than 5 years of direct investment management experience, with 25.0% having more than 10 years of senior portfolio leadership experience. As for institutional size, 75.0% of respondents have portfolios of over ₦500 billion, while 37.5% are mega-institutions with portfolios of over ₦2 trillion in assets under management (AUM). This validates the fact that the data is in line with the decisions made by officers of the watch of Nigeria's huge pension asset base of approximately ₦18 trillion.

The most important observation in Table 4.2 is that only 20.8% of the respondents say that quantitative optimization models are used as a basis for the selection of a property. On the other hand, 70.8% base their decision on professional judgment and use some modeling or on qualitative experience alone (25.0%). This verifies that even with the evolution of capital markets, the real estate allocation in Nigerian pension funds is still largely qualitative and heuristic in nature.

## 4.3 Identification and Analysis of Heuristics Employed in Property Portfolio Selection

This section focuses on Objective I which concerns the identification and analysis of the types of decision-making heuristics used by Nigerian PFA investment managers in the selection of properties and the construction of a portfolio.

### 4.3.1 Property Evaluation Criteria Ranking Analysis

In Section B the respondents were asked to rank eight commonly used property evaluation criteria, with 1 being the most important and 8 being the least important. Table 4.3 shows median ranks, proportion of cases in the Top-3 ranks, and cognitive tier classification for the entire census (n = 24).

<a id="table-**table 43: property evaluation criteria ranking summary (n = 24)**"></a>
**Table 4.3: Property Evaluation Criteria Ranking Summary (n = 24)**

| **Property Evaluation Criterion** | **Median Rank (1–8)** | **Top-3 Inclusion (n)** | **Top-3 Proportion (%)** |
| :--- | :---: | :---: | :---: |
| Title Legal Status (e.g., C of O) | 1.5 | 18 | 75.0 |
| Submarket Location Prestige | 3.0 | 18 | 75.0 |
| Expected Rental Yield | 3.0 | 17 | 70.8 |
| Physical Building Condition | 5.0 | 4 | 16.7 |
| Tenant Credit Quality | 4.0 | 3 | 12.5 |
| Secondary Market Liquidity | 6.0 | 5 | 20.8 |
| Valuer Recommendation | 7.0 | 4 | 16.7 |
| Peer PFA Acquisition Activity | 7.0 | 3 | 12.5 |

*Source: Field Survey, 2026*

Table 4.3 shows the empirical rankings of the property selection criteria, which clearly show a hierarchy in property selection criteria. Title Legal Status is the most popular with a median rank of 1.5 and a 75.0% Top-3 inclusion rate. Submarket Location Prestige and Expected Rental Yield are tied for second place with median ranks of 3.0, with 75.0% and 70.8% of respondents choosing them in the Top-3, respectively. On the other hand, tenant credit quality, market liquidity and valuer recommendations are given lesser priority and placed in the lower tiers, with minimal Top-3 placement.

The findings show that Nigerian PFA managers are not considering all the attributes of the assets at the same time in a compensatory financial model. Rather, they use an elimination search strategy (Tversky, 1972). The validation of legal title and the prestige of location are screening filters that are necessary and not subject to negotiation. If a candidate property cannot show a perfected Certificate of Occupancy (C of O) or prime spatial location, it is eliminated from consideration, no matter how much it is expected to yield or how much it is expected to return.

Why is legal title and location prestige more important than cash-flow fundamentals in determining the allocation of pension real estate in Nigeria? In developed markets, legal title is uniform and stable, and the focus is mostly on net operating income (NOI) and cap rates. However, the land administration system in Nigeria is complex due to legal opacity, duplication of land titles and perfection delays as provided in the Land Use Act 1978. Loss of capital may result from court forfeiture or government revocation due to a title defect. Therefore, the choice of legal status to anchor on (title) and prime submarket location is an efficient risk-mitigation strategy in the face of institutional market flaws in the land market. Fund managers are drawn to spatial prestige as an easy-to-understand indicator of legal security, tenant demand resilience and long-term capital preservation.

### 4.3.2 Composite Heuristic Scoring and Empirical Weight Calibration

The responses in Sections B and C were coded into four composite heuristic scores using Formulae 3.1–3.4:

1. **Title Anchoring ($H_1$: ACS):** Measures reliance on legal title perfection as a dominant selection anchor.
2. **Location Familiarity ($H_2$: AVCS):** Measures bias towards prime, highly visible submarkets (e.g., Victoria Island, Ikoyi, Maitama).
3. **Trend Momentum ($H_3$: RCS):** Measures bias towards recent commercial sector growth trends.
4. **Peer Herding ($H_4$: HCS):** Measures institutional mirroring of rival PFA acquisition choices.

The composite heuristic scores, standard errors, prevalence classifications and resulting normalized weight parameters calibrated from the decision-makers are summarized in Table 4.4.

<a id="table-**table 44: composite heuristic scores and empirical weight calibration**"></a>
**Table 4.4: Composite Heuristic Scores and Empirical Weight Calibration**

| **Heuristic Dimension ($j$)** | **Mean Score ($\bar{H}_j$)** | **Standard Error (SE)** | **Prevalence Classification** | **Calibrated Weight ($\alpha_j$)** |
| :--- | :---: | :---: | :--- | :---: |
| $H_1$: Title Anchoring (ACS) | 0.4847 | 0.0800 | Moderate Prevalence | 0.2196 |
| $H_2$: Location Familiarity (AVCS) | **0.7378** | 0.0600 | **High Prevalence** | **0.3342** |
| $H_3$: Trend Momentum (RCS) | 0.5041 | 0.0500 | Moderate Prevalence | 0.2281 |
| $H_4$: Peer Herding (HCS) | 0.4819 | 0.0500 | Moderate Prevalence | 0.2181 |
| **Total Composite Score Vector** | **2.2085** | — | — | **1.0000** |

*Source: Field Survey & Author's Computation, 2026*

Figure 4.1 shows the radar profile of these composite heuristic scores, along with their calibrated weight vectors.

<a id="figure-**figure 41: composite heuristic score profile and calibrated weights**"></a>
**Figure 4.1: Composite Heuristic Score Profile and Calibrated Weights**

![Figure 4.1: Composite Heuristic Score Profile and Calibrated Weights](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/figure_4_1_heuristic_scores_radar.png)

*Source: Field Survey & Author's Computation, 2026*

The dominant decision heuristic among Nigerian PFA managers is Location Familiarity with a mean score of 0.7378 and a high prevalence weight of 0.3342. As seen in Table 4.4 and Figure 4.1, Anchoring (0.4847), Trend Momentum (0.5041) and Peer Herding (0.4819) are moderately prevalent.

This empirical weight distribution illustrates that Location Familiarity accounts for 1/3 of the total property selection weight. These calibrated weights directly determine the construction of the heuristic-driven portfolio (Portfolio A). The heuristic selection algorithm assigns a composite suitability score to each property in the 80-asset universe, which is a linear combination of the properties.

The properties are then ranked and capital is greedily allocated to the highest-scoring properties. The high empirical weight thus strongly favors prime Lagos submarkets, directly reflecting the observed cognitive preferences in the field.

## 4.4 Construction of Heuristic-Driven and Mean-Variance Optimized Portfolios

This section focuses on Objective II — the construction of representative property portfolios based on a set of heuristic decision rules as identified in the survey results (Portfolio A) and a set of mean-variance optimization techniques adapted for discrete real estate assets (Portfolio B) — and the comparative evaluation of the property selection patterns, asset class compositions, and spatial diversification profiles of these portfolios.

### 4.4.1 Secondary Market Data Context and Property Covariance Calibration

Secondary real estate market data was collected from trusted industry sources to connect the dots between the primary survey findings and computational portfolio optimization. They included historical market monitors, Jones Lang LaSalle (JLL) reports, Broll Sub-Saharan Africa Research, Estate Intel, Nigerian Institution of Estate Surveyors and Valuers (NIESV) reports, Central Bank of Nigeria (CBN) statistical bulletins, and PenCom annual reports.

The historical rent yields, capital appreciation rates and return volatilities of Nigeria's major commercial real estate submarkets were determined using secondary market data for the period of the backtest (2018–2024). The asset return parameters used as a basis for the calibration are presented in Appendix B.

The property covariance matrix of the frozen synthetic universe was built using these parameters. The off-diagonal covariance terms are empirical market co-movements:

**Intra-Lagos Prime Assets ($\rho \approx 0.75 - 0.92$):** High positive correlation, due to similar exposure to state FX dynamics, state land policies and macroeconomic liquidity.

**Inter-City Pairs (Lagos vs. Abuja/Kano, $\rho \approx 0.05 - 0.25$):** Low to near-zero correlation because of different economic drivers in the two cities, the federal government presence in Abuja, and the trade patterns in Northern Nigeria.

This secondary-market calibrated covariance matrix forms the mathematical foundation for constructing Portfolio B via Mean-Variance Optimization. In Portfolio A, the properties are simply chosen based on high heuristic scores; in Portfolio B, the goal is to find combinations of assets that yield the least variance in the portfolio, given the highest expected return.

### 4.4.2 Portfolio Selection Mechanics and Capital Allocation Profiles

Both portfolios were allocated capital from a representative ₦2 trillion pension fund asset base. Direct investment in real estate is limited to 10% of the total AUM and the total real estate investment budget is, according to PenCom guidelines, ₦200 billion.

**Portfolio A (Heuristic-Driven):** Properties were ranked by the composite heuristic scores in order to meet the requirements of the lease compliance. The top 15 scoring properties were selected using a greedy algorithm and an investment of ₦11.61 billion (5.8% of the regulatory cap) was made.

**Portfolio B (MVO-Optimized):** Constructed with a binary integer solver to maximize the Sharpe ratio, with 10% overall allocation limit for PenCom and 5% per-asset allocation limit. The solver chose 15 assets that maximise diversification, investing ₦11.02 billion.

### 4.4.3 Portfolio Holdings and Asset Type Comparison

The full property compositions, submarket locations, asset classes and selection results for both portfolios are presented in Table 4.5.

<a id="table-**table 45: holdings and asset allocation profiles of portfolio a (heuristic) and portfolio b (mvo)**"></a>
**Table 4.5: Holdings and Asset Allocation Profiles of Portfolio A (Heuristic) and Portfolio B (MVO)**

| **Property ID** | **Submarket Location** | **Asset Class Type** | **Acquisition Cost (₦ Millions)** | **Expected Return (%)** | **Selection Portfolio** |
| :--- | :--- | :--- | :---: | :---: | :--- |
| PROP_09 | Lagos | Commercial Mixed-Use | ₦289.0M | 26.06 | Portfolio A Only |
| PROP_62 | Lagos | Commercial Mixed-Use | ₦602.0M | 25.17 | Portfolio A Only |
| PROP_29 | Lagos | Luxury Residential | ₦1,886.0M | 23.92 | Portfolio A Only |
| PROP_01 | Lagos | Luxury Residential | ₦1,345.0M | 24.77 | Portfolio A Only |
| PROP_36 | Lagos | Luxury Residential | ₦1,013.0M | 24.10 | Portfolio A Only |
| PROP_10 | Lagos | Luxury Residential | ₦1,177.0M | 24.02 | Portfolio A Only |
| PROP_54 | Lagos | Luxury Residential | ₦360.0M | 24.84 | Portfolio A Only |
| PROP_69 | Lagos | Luxury Residential | ₦307.0M | 25.14 | Portfolio A Only |
| PROP_42 | Lagos | Commercial Office Grade A | ₦824.0M | 17.61 | Portfolio A Only |
| PROP_49 | Oyo | Commercial Mixed-Use | ₦505.0M | 27.83 | Portfolio A Only |
| **PROP_05** | **Lagos** | **Commercial Office Grade A** | **₦894.0M** | **18.14** | **Shared (A & B)** |
| **PROP_21** | **Lagos** | **Commercial Office Grade A** | **₦623.0M** | **16.65** | **Shared (A & B)** |
| **PROP_23** | **Lagos** | **Commercial Office Grade A** | **₦775.0M** | **17.37** | **Shared (A & B)** |
| **PROP_73** | **Lagos** | **Commercial Office Grade A** | **₦284.0M** | **18.13** | **Shared (A & B)** |
| **PROP_79** | **Lagos** | **Commercial Office Grade A** | **₦726.0M** | **18.48** | **Shared (A & B)** |
| PROP_13 | Kano | Commercial Retail | ₦590.0M | 9.02 | Portfolio B Only |
| PROP_25 | Abuja FCT | Commercial Office Grade A | ₦258.0M | 10.33 | Portfolio B Only |
| PROP_26 | Kano | Industrial Warehouse | ₦230.0M | 10.27 | Portfolio B Only |
| PROP_32 | Oyo | Commercial Office Grade B | ₦1,068.0M | 19.35 | Portfolio B Only |
| PROP_33 | Lagos | Commercial Office Grade A | ₦724.0M | 18.54 | Portfolio B Only |
| PROP_43 | Lagos | Commercial Office Grade A | ₦931.0M | 18.32 | Portfolio B Only |
| PROP_44 | Abuja FCT | Commercial Office Grade A | ₦555.0M | 8.73 | Portfolio B Only |
| PROP_55 | Abuja FCT | Commercial Office Grade A | ₦1,713.0M | 9.89 | Portfolio B Only |
| PROP_63 | Abuja FCT | Commercial Office Grade A | ₦236.0M | 10.72 | Portfolio B Only |
| PROP_80 | Rivers | Industrial Logistics | ₦1,418.0M | 13.11 | Portfolio B Only |

*Source: Author's Computation, 2026*

Figure 4.2 plots the positions of Portfolio A and Portfolio B relative to the efficient frontier constructed from 1,500 random feasible portfolios.

<a id="figure-**figure 42: property portfolio efficient frontier cloud**"></a>
**Figure 4.2: Property Portfolio Efficient Frontier Cloud**

![Figure 4.2: Property Portfolio Efficient Frontier Cloud](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/figure_4_2_efficient_frontier.png)

*Source: Author's Computation, 2026*

Table 4.5 demonstrates an asset overlap rate of 33.3% (5 shared properties: PROP_05, PROP_21, PROP_23, PROP_73, PROP_79 — all Lagos Grade A commercial offices). Portfolio B is on the optimal efficient frontier, as shown in Figure 4.2, and has low annual volatility (0.58%) and moderate expected returns (15.5%). Portfolio A, on the other hand, has a greater expected return (24.2%) and lies to the right of the efficient frontier, with much higher volatility (7.65%).

When comparing the types of properties, there are significant differences in structure:

**Portfolio A's Unique Assets:** Luxury residential properties (6 holdings, expected returns 23.9%–25.1%) and commercial mixed-use properties (3 holdings, returns 25.1%–27.8%) with a clear focus on prime submarkets in Lagos. The high location familiarity weight of the heuristic engine gives prime residential and mixed-use properties in Victoria Island and Ikoyi a higher rank than all secondary market properties.

**Portfolio B's Unique Assets:** Industrial Warehouses in Kano (PROP_26), Commercial Retail Assets in Kano (PROP_13), Grade A Offices in Abuja FCT (PROP_25, PROP_44, PROP_55, PROP_63 with expected returns 8.7%–10.7%) and Industrial Logistics Hubs in Rivers State (PROP_80). The MVO solver does not choose these properties for their high nominal yields, but because their return series are close to being uncorrelated with Lagos real estate.

### 4.4.4 Spatial and Asset-Class Diversification Analysis

For the purposes of assessing portfolio diversification, Herfindahl-Hirschman Indices (HHI) were computed by geographic area and by asset category. The concentration metrics are summarized in Table 4.6.

<a id="table-**table 46: portfolio concentration and diversification index summary**"></a>
**Table 4.6: Portfolio Concentration and Diversification Index Summary**

| **Diversification Metric** | **Portfolio A (Heuristic)** | **Portfolio B (MVO)** | **Difference (B − A)** | **Relative Structural Implication** |
| :--- | :---: | :---: | :---: | :--- |
| Individual Holding | 0.0667 | 0.0667 | 0.0000 | Identical Equal-Weighting (N=15) |
| **Geographic State** | **0.8760** | **0.3160** | **−0.5600** | **Portfolio A Highly Concentrated in Lagos** |
| **Asset Class Type** | **0.3600** | **0.6620** | **+0.3020** | **Portfolio B Concentrated in Office Class** |
| Mean Diversification Ratio | 1.2900 | 5.8100 | +4.5200 | Portfolio B Achieves Superior Risk Spread |

*Source: Author's Computation, 2026*

Figures 4.3 and 4.4 illustrate the geographic and asset-type allocations of both portfolios.

<a id="figure-**figure 43: geographic asset allocation comparison**"></a>
**Figure 4.3: Geographic Asset Allocation Comparison**

![Figure 4.3: Geographic Asset Allocation Comparison](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/figure_4_3_geographic_allocation.png)

*Source: Author's Research, 2026*

<a id="figure-**figure 44: asset type portfolio allocation comparison**"></a>
**Figure 4.4: Asset Type Portfolio Allocation Comparison**

![Figure 4.4: Asset Type Portfolio Allocation Comparison](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/figure_4_4_asset_type_allocation.png)

*Source: Author's Computation, 2026*

The key geographic difference between the two portfolios is that Portfolio A is highly geographically concentrated in Lagos State (14 out of 15 holdings; Geographic HHI = 0.8760) while Portfolio B is spread across five states (Geographic HHI = 0.3160). Yet, there is an intriguing inversion across asset type in Figure 4.4: Portfolio B focuses 80.0% of capital in Commercial Office assets (Asset Type HHI = 0.6620), while Portfolio A has a more balanced asset mix, with residential, commercial and mixed-use assets (HHI = 0.3600).

This is an inverse example of the **Volatility Suppression Paradox** in institutional real estate. It may seem logical to non-technical observers that a balance between residential, commercial and mixed-use properties in a portfolio constitutes a more diversified portfolio. But, in the modern world of portfolio theory, it is not the number of asset types that makes for true diversification — it is the covariance of their returns. Portfolio A focuses on assets that are located almost exclusively in Lagos, meaning that all of the assets are subject to the same economic cycle.

On the other hand, Portfolio B is designed to be low volatile (0.58%) with distribution of funds to Grade A offices in various cities (Lagos, Abuja, Kano, Port Harcourt). The total portfolio variance is reduced more effectively by having a geographic mix of office assets than by having a mix of different real estate asset types concentrated in a single city, because returns on Abuja and Kano offices do not correlate positively with Lagos residential.

## 4.5 Comparative Performance Evaluation of Portfolios

This section is dedicated to evaluating the performance of the heuristic-driven portfolio (Portfolio A) and the mean-variance optimized portfolio (Portfolio B) under various simulated macroeconomic scenarios, which is a component of Objective III.

### 4.5.1 Monte Carlo Simulation Results

Both portfolios were simulated with a 60-month (5-year) investment horizon with a base risk-free rate of 8.4% per annum (matching the average CBN Monetary Policy Rate historical benchmark) under the model of Geometric Brownian Motion (GBM).

In Figure 4.5, 100 representative Monte Carlo wealth paths are plotted, and in Figure 4.6, the resulting Sharpe ratio distributions of all 10,000 Monte Carlo paths are plotted.

<a id="figure-**figure 45: comparative monte carlo path simulations (60-month horizon)**"></a>
**Figure 4.5: Comparative Monte Carlo Path Simulations (60-Month Horizon)**

![Figure 4.5: Comparative Monte Carlo Path Simulations](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/figure_4_5_monte_carlo_paths.png)

*Source: Author's Computation, 2026*

<a id="figure-**figure 46: simulated sharpe ratio distributions (10,000 paths)**"></a>
**Figure 4.6: Simulated Sharpe Ratio Distributions (10,000 Paths)**

![Figure 4.6: Simulated Sharpe Ratio Distributions](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/figure_4_6_sharpe_distribution.png)

*Source: Author's Computation, 2026*

Table 4.7 summarizes the key Monte Carlo performance metrics across the 10,000 simulated paths.

<a id="table-**table 47: monte carlo performance summary (n = 10,000 paths, baseline $r_f = 84\%$)**"></a>
**Table 4.7: Monte Carlo Performance Summary (n = 10,000 Paths, Baseline $R_f = 8.4\%$)**

| **Performance Metric** | **Portfolio A (Heuristic)** | **Portfolio B (MVO)** | **Difference (B − A)** | **Hypothesis Test & Significance** |
| :--- | :---: | :---: | :---: | :--- |
| Mean Cumulative Return (%) | **198.80** | 105.30 | −93.50pp | — |
| Mean CAGR (%) | **24.20** | 15.50 | −8.70pp | Portfolio A Dominates Nominal Yield |
| Mean Annual Volatility (%) | 7.65 | **0.58** | −7.07pp | Portfolio B Suppresses Risk by 13× |
| **Mean Sharpe Ratio** | **2.0800** | **12.3600** | **+10.2800** | $t = 733.35$, $p < 0.0001$ (H1 Confirmed) |
| BCa 95% Bootstrap CI | — | — | **[10.35, 10.68]** | Rejects $H_0$: $\Delta SR \leq 0.05$ (H2 Confirmed) |
| Maximum Drawdown (%) | 4.24 | **0.00** | −4.24pp | Portfolio B Zero Downside Risk |
| 95% CVaR Cumulative (%) | **106.70** | 99.80 | −6.90pp | Portfolio A Higher Tail Growth |

*Source: Author's Computation, 2026*

As detailed in Table 4.7 and visualised in Figures 4.5 and 4.6, Portfolio B has a mean Sharpe ratio of 12.3600 under baseline conditions, much higher than the mean Sharpe ratio for Portfolio A of 2.0800. This performance difference is statistically significant ($p < 0.0001$) and practically significant (BCa 95% CI [10.35, 10.68]) and thus supports Hypotheses H1 and H2.

Table 4.7 is important because it points to the trade-off illustrated by this result: The nominal return of Portfolio A is much higher (CAGR of 24.20% compared to CAGR of 15.50% for Portfolio B). The annual volatility of Portfolio A is 7.65%, whereas it is only 0.58% for Portfolio B, so that gives Portfolio B the higher Sharpe ratio.

### 4.5.2 Market Condition Stress Tests and Interest Rate Sensitivity Analysis

Stress tests were performed over different ranges of market volatility and different risk-free interest rates to assess the performance advantage of Portfolio B in different economic conditions.

The volatility range stress test is provided in Table 4.8 and the interest rate sensitivity stress test is provided in Table 4.9 over the range of risk-free rates from 8.4% to 20.0%.

<a id="table-**table 48: volatility range stress analysis (n = 10,000 paths)**"></a>
**Table 4.8: Volatility Range Stress Analysis (n = 10,000 Paths)**

| **Volatility Environment** | **Portfolio A Mean SR** | **Portfolio B Mean SR** | **Delta Sharpe (B − A)** | **Sub-Sample Path Count** |
| :--- | :---: | :---: | :---: | :---: |
| Low Volatility | 2.3200 | 12.3700 | +10.0500 | 3,333 |
| Medium Volatility | 2.0700 | 12.3600 | +10.2900 | 3,334 |
| High Volatility | 1.8600 | 12.3500 | +10.4900 | 3,333 |

*Source: Author's Computation, 2026*

<a id="table-**table 49: risk-free rate sensitivity crossover analysis**"></a>
**Table 4.9: Risk-Free Rate Sensitivity Crossover Analysis**

| **Risk-Free Rate Scenario ($R_f$)** | **Portfolio A Sharpe** | **Portfolio B Sharpe** | **Delta Sharpe (B − A)** | **Dominant Portfolio Advantage** |
| :--- | :---: | :---: | :---: | :--- |
| **8.4% Baseline** | 2.0800 | 12.3600 | **+10.2800** | MVO Portfolio B Dominates |
| **10.0% Scenario** | 1.8700 | 9.5600 | **+7.6900** | MVO Portfolio B Dominates |
| **15.0% Scenario** | **1.2100** | **0.8200** | **−0.3900** | **Heuristic Portfolio A Dominates** |
| **20.0% Scenario** | **0.5500** | **−7.9200** | **−8.4700** | **Heuristic Portfolio A Dominates** |

*Source: Author's Computation, 2026*

Table 4.9 shows that there is a **critical performance crossover** at an interest rate of approximately 12.5%:

**At Low to Moderate Rates ($R_f < 12.5\%$):** Portfolio B (MVO) prevails. The low volatility of Portfolio B (0.58%) yields an outstanding Sharpe ratio, as the risk-free rate is low enough for assets to generate positive excess returns.

**At High Interest Rates ($R_f \geq 15.0\%$):** Portfolio A (Heuristic) wins. The Sharpe ratio of Portfolio A is 1.2100, while the Sharpe ratio of Portfolio B is 0.8200 at 15.0%. At 20.0%, the Sharpe ratio for Portfolio B is negative (−7.9200) while the Sharpe ratio for Portfolio A remains positive (0.5500).

This reversal is the reason why Portfolio B fails in high interest rate environments. Portfolio B's low volatility is due to the fact that it invests in low-yielding office assets in regional markets (with expected returns ranging from 8.7% to 10.7%). As the risk-free rate approaches 15% or 20%, these returns become negative with respect to the risk-free rate, and excess returns become negative. The near-zero volatility (0.58%) means that a negative excess return divided by this tiny volatility yields a very poor Sharpe ratio.

In contrast, Portfolio A is very focused on high-yield prime Lagos assets (23%–27% expected return). Such high yields offer a significant cushion against inflation and higher interest rates, and will continue to do so even in the event of policy tightening.

The finding gives empirical support to the **Ecological Rationality Framework** (Gigerenzer & Gaissmaier, 2011). In low-inflation economies with low interest rates, MVO models are able to achieve maximum risk-adjusted efficiency. In volatile emerging markets such as Nigeria, however, where the CBN Monetary Policy Rate spiked to 27.5% in 2024, using complicated MVO models optimized for low volatility can make portfolios vulnerable to interest rate shocks.

PFA managers adopt straightforward heuristics, based on location prestige and high nominal yields, that create a strong cushion against macroeconomic volatility. These heuristics are not "irrational biases" but rather an adaptive, ecologically rational approach to the economic context of Nigeria, which is characterized by high inflation.

## 4.6 Environmental Constraints and Institutional Drivers Influencing Heuristic Reliance

This section deals with Objective IV by reviewing environmental constraints and institutional governance factors affecting the use of heuristics by Nigerian PFA investment managers.

### 4.6.1 Institutional Governance Architecture

The internal decision-making mechanisms in PFAs were explored in Item D1 of the questionnaire. Of the active decision makers:

- 85.7% reported that property acquisitions need to be formally reviewed and approved by an executive Investment Committee or Board Sub-Committee.
- 57.1% reported that acquisitions have to go through three or more formal approvals before capital is deployed.

This governance model directly supports heuristic decision-making. Managers will naturally be more drawn to properties that are easy to justify, have visible credentials and legal precedents, and when a proposal has to be put before a multi-member board committee, prime Lagos properties with clear title certificates are the ones that are more likely to be approved. The institutional risk aversion posed by secondary market properties in Kano and Ibadan makes them hard to pitch, which creates a career risk asymmetry — where managers tend to play it safe and stick to the properties they know.

### 4.6.2 Data Opacity and Ecological Rationality Testing

The impact of real estate data unavailability was rated on a 5-point scale in Item D2. Most active decision makers (71.4%) agreed that data scarcity is a very serious constraint (rating 4 or 5). Additionally, 79.2% of respondents from the entire census (n = 24) said they were "Very Likely" to use a validated quantitative real estate decision-support tool if it were available.

Table 4.10 shows the composite heuristic scores for the two groups of managers: those who said data scarcity was their main constraint and those who did not.

<a id="table-**table 410: institutional environmental constraints and split-sample heuristic test**"></a>
**Table 4.10: Institutional Environmental Constraints and Split-Sample Heuristic Test**

| **Environmental Constraint Category** | **Freq. (n)** | **Selection Proportion (%)** | **Mean Score, Data Constraint** | **Mean Score, No Data Constraint** |
| :--- | :---: | :---: | :---: | :---: |
| Investment Committee Preference for Experience | 5 | 71.4 | 0.7850 | 0.6200 |
| Absence of Centralized Transaction Return Data | 5 | 71.4 | 0.7920 | 0.6020 |
| Institutional Precedent / Legacy Allocations | 4 | 57.1 | 0.7410 | 0.6350 |
| Peer PFA Acquisition Benchmarking | 3 | 42.9 | 0.5210 | 0.3840 |

*Source: Field Survey & Author's Computation, 2026 ($p < 0.05$)*

Managers with severe data constraints have significantly higher Location Familiarity scores ($\bar{H}_2 = 0.7920$ vs. $0.6020$, $p < 0.05$) as seen in Table 4.10. This validates the assertion that the use of heuristics in the Nigerian pension funds is mainly an adaptive strategy to market opacity. When historical returns and transaction indexes are not available, managers rely on location prestige and peer behaviour as pragmatic and inexpensive proxies for the assessment of risk. The reliance on heuristics is thus not a rejection of quantitative finance, but rather a structural default due to data opacity.

---

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

---

# REFERENCES

Akerlof, G. A. (1970). The market for "lemons": Quality uncertainty and the market mechanism. *The Quarterly Journal of Economics, 84*(3), 488–500.

Aluko, B. T. (2007). Implications of the current trend in mortgage valuation practice in Nigeria. *International Journal of Strategic Property Management, 11*(1), 17–31.

Amenc, N., Martellini, L., & Ziemann, V. (2009). Asset-liability management in private wealth management. *Journal of Portfolio Management, 36*(1), 100–120.

Andonov, A., Bauer, R., & Cremers, M. (2017). Pension fund asset allocation and liability discount rates. *The Review of Financial Studies, 30*(8), 2555–2595.

Babawale, G. K. (2013). Valuation accuracy – the myth, expectation and reality! *African Journal of Economic and Management Studies, 4*(3), 387–406.

Babawale, G. K., & Ajayi, C. A. (2011). Variance in residential property valuation in Lagos, Nigeria. *Property Management, 29*(3), 222–237.

Barberis, N., & Thaler, R. H. (2003). A survey of behavioral finance. *Handbook of the Economics of Finance, 1*, 1053–1128.

Baum, A. E. (2015). *Real estate investment: A strategic approach* (3rd ed.). Routledge, Taylor & Francis Group.

Baum, A., & Hartzell, D. (2012). *Global property investment: Strategies, structures, decisions*. Wiley-Blackwell. <http://site.ebrary.com/id/10509831>

Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). A theory of fads, fashion, custom, and cultural change as informational cascades. *Journal of Political Economy, 100*(5), 992–1026.

Black, F., & Litterman, R. (1992). Global portfolio optimization. *Financial Analysts Journal, 48*(5), 28–43.

Blake, D. (2003). *Pension schemes and pension funds in the United Kingdom* (2nd ed.). Oxford University Press.

Brueggeman, W. B., Chen, A. H., & Thibodeau, T. G. (1984). Real estate investment funds: Performance and portfolio considerations. *Real Estate Economics, 12*(3), 333–354.

Byrne, P., & Lee, S. (2004). Different risk measures: Different portfolio compositions? *Journal of Property Investment & Finance, 22*(6), 501–511.

Campbell, J. Y., Lo, A. W., & MacKinlay, A. C. (1997). *The econometrics of financial markets*. Princeton University Press.

Choueifaty, Y., & Coignard, Y. (2008). Toward maximum diversification. *The Journal of Portfolio Management, 35*(1), 40–51.

Clark, G. L., & Urwin, R. (2008). Best-practice pension fund governance. *Journal of Asset Management, 9*(1), 2–21.

De Bondt, W. F. M., & Thaler, R. H. (1985). Does the stock market overreact? *The Journal of Finance, 40*(3), 793–805.

Del Casino, J. J. (1995). Portfolio diversification considerations. In J. L. Pagliari Jr. (Ed.), *The handbook of real estate portfolio management* (pp. 912–966). IRWIN.

DeMiguel, V., Garlappi, L., & Uppal, R. (2009). Optimal versus naive diversification: How inefficient is the 1/N portfolio strategy? *The Review of Financial Studies, 22*(5), 1915–1953.

DiPasquale, D., & Wheaton, W. C. (1996). *Urban economics and real estate markets*. Prentice Hall.

Efron, B., & Tibshirani, R. J. (1994). *An introduction to the bootstrap* (1st ed.). Chapman and Hall/CRC. <https://doi.org/10.1201/9780429246593>

Elton, E. J., & Gruber, M. J. (1977). Risk reduction and portfolio size: An analytical solution. *The Journal of Business, 50*(4), 415–437.

Elton, E. J., Gruber, M. J., Brown, S. J., & Goetzmann, W. N. (2014). *Modern portfolio theory and investment analysis* (9th ed.). Wiley Custom.

Epley, N., & Gilovich, T. (2006). The anchoring-and-adjustment heuristic: Why the adjustments are insufficient. *Psychological Science, 17*(4), 311–318.

Fama, E. F. (1970). Efficient capital markets: A review of theory and empirical work. *Journal of Finance, 25*(2), 383–417.

Fama, E. F., & Schwert, G. W. (1977). Asset returns and inflation. *Journal of Financial Economics, 5*(2), 115–146.

Fapohunda, T. M. (2013). The pension system and retirement planning in Nigeria. *Mediterranean Journal of Social Sciences, 4*(2), 25–34.

French, K. R., & Poterba, J. M. (1991). Investor diversification and international equity markets. *The American Economic Review, 81*(2), 222–226.

French, K. R., & Roll, R. (1986). Stock return variances: The arrival of information and the reaction of traders. *Journal of Financial Economics, 17*(1), 5–26.

Friedman, M., & Savage, L. J. (1948). The utility analysis of choices involving risk. *Journal of Political Economy, 56*(4), 279–304.

Geltner, D., Miller, N. G., Clayton, J., & Eichholtz, P. (2014). *Commercial real estate: Analysis and investments* (3rd ed.). OnCourse Learning.

Gigerenzer, G., & Gaissmaier, W. (2011). Heuristic decision making. *Annual Review of Psychology, 62*, 451–482.

Gigerenzer, G., Todd, P. M., & ABC Research Group. (1999). *Simple heuristics that make us smart*. Oxford University Press.

Giliberto, S. M. (1993). Measuring real estate returns: The hedged REIT index. *The Journal of Portfolio Management, 19*(3), 94–99.

Glasserman, P. (2004). *Monte Carlo methods in financial engineering*. Springer.

Hadaway, S. C. (1978). Diversification possibilities in agricultural land investments. *The Appraisal Journal*, 529–537.

Hargitay, S. E., & Yu, S. (1993). *Property investment decisions: A quantitative approach*. E & FN Spon.

Hartzell, D., Hekman, J., & Miles, M. (1986). Diversification categories in investment real estate. *AREUEA Journal, 14*(2), 230–254.

Hoesli, M., & Lizieri, C. (2007). *Real estate in the investment portfolio* (Report). Ministry of Finance, Norway. (Unpublished)

Hoesli, M., & MacGregor, B. D. (2000). *Property investment: Principles and practice of portfolio management*. Pearson Education.

Hoevenaars, R. P., Molenaar, R. D., Schotman, P. C., & Steenkamp, T. B. (2008). Strategic asset allocation with liabilities: Beyond stocks and bonds. *Journal of Economic Dynamics and Control, 32*(9), 2939–2970.

Iroham, C. O., Ogunba, O. A., & Oloyede, S. A. (2013a). Relative level of occurrence of the principal heuristics in Nigeria property valuation. *International Journal of Development and Sustainability, 2*(2), 493–504.

Iroham, C. O., Ogunba, O. A., & Oloyede, S. A. (2013b). Usage of major heuristics in property investment valuation in Nigeria. *African Research Review, 7*(4), 93–119.

Iroham, C. O., Ogunba, O. A., Oloyede, S. A., & Omirin, M. M. (2013c). Factors affecting the usage of major heuristics in Nigeria property investment valuation. *Journal of Sustainable Development Studies, 4*(2), 114–133.

Jones Lang LaSalle & LaSalle Investment Management. (2024). *Global Real Estate Transparency Index 2024*. [Online].

Jorion, P. (1985). International portfolio diversification with estimation risk. *The Journal of Business, 58*(3), 259–278.

Jorion, P. (1991). Bayesian and CAPM estimators of the means: Implications for portfolio selection. *Journal of Banking & Finance, 15*(3), 717–727.

Kahneman, D. (2011). *Thinking, fast and slow* (1st paperback ed.). Farrar, Straus and Giroux.

Kahneman, D., & Klein, G. (2009). Conditions for intuitive expertise: A failure to disagree. *American Psychologist, 64*(6), 515–526.

Kahneman, D., & Tversky, A. (1972). Subjective probability: A judgment of representativeness. *Cognitive Psychology, 3*(3), 430–454.

Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica, 47*(2), 263–292.

Lakonishok, J., Shleifer, A., & Vishny, R. W. (1992). The impact of institutional trading on stock prices. *Journal of Financial Economics, 32*(1), 23–43.

Lee, S. L., & Stevenson, S. (2006). Real estate in the mixed-asset portfolio: The question of consistency. *Journal of Property Investment & Finance, 24*(2), 123–135.

Ling, D. C. (2005). A random walk down main street: Can experts predict returns on commercial real estate? *The Journal of Real Estate Research, 27*(2), 137–154.

Ling, D. C., & Archer, W. R. (2020). *Real estate principles: A value approach* (6th ed.). McGraw-Hill Education.

Lowies, G. A., Hall, J. H., & Colete, C. E. (2016). Heuristic-driven bias in property investment decision-making in South Africa. *Journal of Property Investment & Finance, 34*(1), 51–67.

Malizia, E. E. (1991). Forecasting demand for commercial real estate based on the economic fundamentals of U.S. metro markets. *The Journal of Real Estate Research, 6*(3), 251–265.

March, J. G., & Simon, H. A. (1958). *Organizations*. Wiley.

Markowitz, H. (1952). Portfolio selection. *Journal of Finance, 7*(1), 77–91.

Merton, R. C. (1972). An analytic derivation of the efficient portfolio frontier. *The Journal of Financial and Quantitative Analysis, 7*(4), 1851–1872.

Mueller, G. R. (1993). Refining economic diversification strategies for real estate portfolios. *The Journal of Real Estate Research, 8*(1), 55–68.

Mueller, G. R., & Ziering, B. A. (1992). Real estate portfolio diversification using economic diversification. *The Journal of Real Estate Research, 7*(4), 375–386.

National Pension Commission. (2025). *Pension industry statistics: Q3 2025*. National Pension Commission. Retrieved from <https://www.pencom.gov.ng>

National Pension Commission. (2025). *Amended regulation on investment of pension fund assets*. National Pension Commission.

Nigerian Institution of Estate Surveyors and Valuers. (2014). *Approved scale of professional charges for estate surveying and valuation services*. NIESV.

Northcraft, G. B., & Neale, M. A. (1987). Experts, amateurs, and real estate: An anchoring-and-adjustment perspective on property pricing decisions. *Organizational Behavior and Human Decision Processes, 39*(1), 84–97.

Nwosu, A. E., Bello, V. A., Oyetunji, A. K., & Amaechi, C. V. (2024). Dynamics of the inflation-hedging capabilities of real estate investment portfolios in the Nigerian property market. *Buildings, 14*(1), 72. <https://doi.org/10.3390/buildings14010072>

Ogunba, O. A. (2013). *Principles and practice of property valuation in Nigeria* (2nd ed.). Atlantis Books.

Okeahialam, C. O., & Awa, K. N. (2024). Performance of real estate instruments in the investing of pension fund in Nigeria. *International Journal of Environmental Research & Earth Science, 4*(4).

Okeahialam, C. O., & Ezema, C. C. (2024). Application and performance of pension fund in real estate investment financing in Nigeria. *International Journal of Earth Design and Innovation Research, 6*(4), 27–54.

Olaleye, A. (2008). Property market nature and the choice of property portfolio diversification strategies: The Nigeria experience. *Ife Journal of Strategic Property Management, 12*, 35–51.

Olaleye, A. (2011). Property portfolio diversification strategies: A review of the options. *Ife Journal of Environmental Design and Management, 5*, 15–30.

Olaleye, A., & Aluko, B. T. (2007). Evaluating managers' diversification of real estate portfolios: Evidence from Nigeria. *International Journal of Strategic Property Management, 11*(3), 179–189.

Olaleye, A., Aluko, B. T., & Oloyede, S. A. (2008). Evaluating diversification strategies for direct property investment portfolios. *Journal of Real Estate Portfolio Management, 14*(3), 223–231.

Olapade, D. T., Ekemode, B. G., & Olaleye, A. (2019). Considerations for the design and management of property database in opaque markets: Viewpoints from Lagos, Nigeria. *Journal of Property Investment & Finance, 37*(5), 445–454.

Onwuanyi, N. (2020). A review of the property data challenge in Nigeria. *Journal of African Real Estate Research, 5*(2), 15–40.

Pardo, R. (2008). *The evaluation and optimization of trading strategies* (2nd ed.). John Wiley.

Penny, P. (1982). Modern investment theory and real estate analysis. *The Appraisal Journal*, 79–99.

Reilly, F. K., & Brown, K. C. (2012). *Investment analysis and portfolio management* (10th ed.). South-Western Cengage Learning.

RisCura. (2020). *Bright Africa: Pension fund assets*. RisCura. <https://brightafrica.riscura.com/pension-industry/africas-pension-fund-assets/pension-assets-to-gdp>

Robichek, A. A., Cohn, R. A., & Pringle, J. J. (1972). Returns on alternative investment media and implications for portfolio construction. *The Journal of Business, 45*(3), 427–443.

Salzman, D., & Zwinkels, R. C. J. (2017). Behavioral real estate. *Journal of Real Estate Literature, 25*(1), 77–106.

Scharfstein, D. S., & Stein, J. C. (1990). Herd behavior and investment. *The American Economic Review, 80*(3), 465–479.

Sharpe, W. F. (1964). Capital asset prices: A theory of market equilibrium under conditions of risk. *Journal of Finance, 19*(3), 425–442.

Sharpe, W. F. (1966). Mutual fund performance. *Journal of Business, 39*(1), 119–138.

Sharpe, W. F. (1994). The Sharpe ratio. *Journal of Portfolio Management, 21*(1), 49–58.

Shiller, R. J. (2003). From efficient markets theory to behavioral finance. *The Journal of Economic Perspectives, 17*(1), 83–104.

Simon, H. A. (1955). A behavioral model of rational choice. *Quarterly Journal of Economics, 69*(1), 99–118.

Simon, H. A. (1956). Rational choice and the structure of the environment. *Psychological Review, 63*(2), 129–138.

Smith, I. O. (2013). *Practical approach to law of real property in Nigeria* (Rev. ed.). Ecowatch Publications.

Steinert, M., & Crowe, S. (2001). Global real estate investment: Characteristics, optimal portfolio allocation and future trends. *Pacific Rim Property Research Journal, 7*(4), 223–239.

Thrall, G. I. (2002). *Business geography and new real estate market analysis*. Oxford University Press.

Tu, J., & Zhou, G. (2011). Markowitz meets Talmud: A combination of sophisticated and naive diversification strategies. *Journal of Financial Economics, 99*(1), 204–215.

Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology, 5*(2), 207–232.

Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science, 185*(4157), 1124–1131.

---

# APPENDIX A: QUESTIONNAIRE INSTRUMENT

## HEURISTICS IN PROPERTY PORTFOLIO SELECTION DECISIONS OF NIGERIAN PENSION FUNDS

**Questionnaire Survey Instrument · Obafemi Awolowo University, Ile-Ife**

**Faculty of Environmental Design and Management · Department of Estate Management**

**Undergraduate Research Dissertation | 2024/2025 Academic Session**

**Estimated completion time: 12–15 minutes**

---

**Dear Investment Professional,**

You are invited to take part in a research study that will investigate how Pension Fund Administrators select direct real estate investments and decision-making processes that influence the construction of property portfolios.

The research is a section of an undergraduate dissertation in Estate Management at Obafemi Awolowo University. It tries to know the factors and logic models used by seasoned investment experts in the process of assessing and choosing properties for institutional portfolios.

There are no answers that are right or wrong. Your answers are useful specifically because they are based on your personal experience and opinion in the field of work.

Any answers are highly confidential. Only aggregate data will be reported. No researcher, fund or organisation will be named in any publication or communication that results from this study.

---

## SECTION A: Respondent Profile

*This section gathers background information to put your answers into perspective. Everything is handled in a confidential manner. Items indicated by a star (★) are mandatory.*

**A1. What is your current job title? ★**

*Select one option.*

- [ ] **A** — Portfolio Manager / Fund Manager
- [ ] **B** — Investment Analyst (Senior / Principal)
- [ ] **C** — Chief Investment Officer (CIO) / Head of Investments
- [ ] **D** — Director of Research, Strategy, or Risk
- [ ] **E** — Executive / Director with investment oversight responsibility
- [ ] **F** — Other

**A2. How many years of experience do you have in real estate or institutional investment management? ★**

*Select one option.*

- [ ] **A** — Less than 3 years
- [ ] **B** — 3–5 years
- [ ] **C** — 6–10 years
- [ ] **D** — 11–15 years
- [ ] **E** — More than 15 years

**A3. Which of the following best describes your fund's approximate total Assets Under Management (AUM)? ★**

*Select one option. Ranges are broad to preserve confidentiality.*

- [ ] **A** — Below ₦500 billion
- [ ] **B** — ₦500 billion – ₦2 trillion
- [ ] **C** — Above ₦2 trillion
- [ ] **D** — Prefer not to say

**A4. Approximately how many direct real estate properties does your fund currently hold in its portfolio? ★**

*Select one option.*

- [ ] **A** — None (our fund does not currently hold direct property)
- [ ] **B** — 1–3 properties
- [ ] **C** — 4–10 properties
- [ ] **D** — 11–25 properties
- [ ] **E** — More than 25 properties
- [ ] **F** — I do not know / this information is not available to me

**A5. Do you directly participate in property selection decisions? ★**

*Select one option.*

- [ ] **A** — Yes (I have direct decision-making authority over property acquisitions)
- [ ] **B** — Yes (I provide analysis and recommendations that inform decisions, but final authority rests elsewhere)
- [ ] **C** — No (I do not directly participate in property selection)

**A6. Does your fund use a formal quantitative model to assist with property selection decisions? ★**

*Select one option.*

- [ ] **A** — Yes, fully (quantitative modelling is the primary basis for selection decisions)
- [ ] **B** — Yes, partially (quantitative modelling is used alongside professional judgment)
- [ ] **C** — No (selection decisions are based primarily or entirely on judgment and experience)
- [ ] **D** — I am not aware of any quantitative selection models being used

---

## SECTION B: Property Selection Criteria

*This part discusses what influences your fund when considering direct real estate investments. Please answer in relation to what happens in the reality of your organisation in relation to the process of making decisions — not in relation to the way decisions should be made.*

**B1. Please rank the following eight criteria in order of their importance in your fund's property selection process. ★**

*Write 1 next to the most important criterion and 8 next to the least important. Use each number only once.*

| **Criterion** | **Rank** |
| :--- | :---: |
| Location prestige / submarket reputation | ______ |
| Title documentation status (e.g., Certificate of Occupancy, Governor's Consent) | ______ |
| Rental yield / income return | ______ |
| Tenant profile and lease security | ______ |
| Physical condition of the property | ______ |
| Activity of peer PFAs in the same submarket | ______ |
| The valuer's or surveyor's recommendation | ______ |
| Market liquidity / ease of future disposal | ______ |

**B2–B4. Indicate your level of agreement with each of the following statements. ★**

*Circle or tick one response per statement.*

*Scale: 1 = Strongly Disagree → 5 = Strongly Agree*

| **Statement** | **1 Strongly Disagree** | **2 Disagree** | **3 Neutral** | **4 Agree** | **5 Strongly Agree** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **B2.** An Ikoyi, Victoria Island or Maitama property will be less risky to invest in than an equal-value property in a less well-known area, independent of its particular financial nature. | ○ | ○ | ○ | ○ | ○ |
| **B3.** Where there is no Certificate of Occupancy or Governor's Consent on the property, we would not recommend it no matter how good the yield may be. | ○ | ○ | ○ | ○ | ○ |
| **B4.** The choice of property in our fund in the last three years has been generally similar in place and type to that of other PFAs of which we know. | ○ | ○ | ○ | ○ | ○ |

---

## SECTION C: Investment Scenarios

*The following scenarios outline real-life investment situations. In each case, circle the number on the scale to indicate your response. Reflect on what you and your fund would tend to do in practice — not on how you think an ideal response would appear.*

**Scenario C1**

A Grade A office building is under consideration by your fund. The market value was independently valued four months ago at ₦900 million. The property is currently estimated to be worth ₦730 million by citing softer market conditions. The asking price is ₦740 million.

**How strongly does the earlier ₦900 million valuation influence the maximum offer your fund would make?**

| *1 — Not at all (only the current valuation is relevant)* | **1** | **2** | **3** | **4** | **5** | *5 — Very strongly (the earlier valuation significantly shapes our offer)* |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | ○ | ○ | ○ | ○ | ○ | |

**Scenario C2**

In your analysis, you have discovered two commercial properties that have statistically equal risk-adjusted returns: the same cap rates, the same title status, the same tenant mix, and the same building specification.

Property A is in the business district of Victoria Island.

Property B is in a similar business area in Ibadan.

**How likely is your fund to prefer Property A?**

| *1 — No preference (equivalent financials drive equivalent interest)* | **1** | **2** | **3** | **4** | **5** | *5 — Strongly prefer A (Victoria Island location is decisive)* |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | ○ | ○ | ○ | ○ | ○ | |

**Scenario C3**

A particular sector, Grade A office in Abuja, has provided capital appreciation of 18 percent in the last two years, which is significantly higher than the market average of 9 percent.

**How much does this recent performance increase your inclination to target this sector for new acquisitions in the current year?**

| *1 — No effect (recent returns do not alter our allocation view)* | **1** | **2** | **3** | **4** | **5** | *5 — Significantly increases inclination (strong recent performance is a compelling signal)* |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | ○ | ○ | ○ | ○ | ○ | |

**Scenario C4**

You get to know that three of the five largest PFAs by AUM have just purchased Grade A office properties in a particular submarket in Abuja. The returns on these purchases seem to be a little lower than your fund's target hurdle of returns.

**How much does peer activity increase your likelihood of evaluating similar properties in that submarket?**

| *1 — No effect (peer activity does not influence our evaluation)* | **1** | **2** | **3** | **4** | **5** | *5 — Significantly increases likelihood (peer validation is a meaningful signal)* |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | ○ | ○ | ○ | ○ | ○ | |

---

## SECTION D: Decision Process and Institutional Context

*This section will enquire on the way investment decisions are organized in your fund and the real-life aspects that influence your analysis process. Please choose the alternative or alternatives that best characterize the practice of your fund.*

**D1. Which of the following best describes how property selection decisions are typically made at your fund? ★**

*Select one option.*

- [ ] **A** — An individual investment manager or portfolio manager makes the decision directly
- [ ] **B** — A dedicated real estate or property investment team reaches a consensus decision
- [ ] **C** — An investment committee reviews and formally approves all acquisition recommendations
- [ ] **D** — Senior management or the CIO makes the final decision based on a team recommendation
- [ ] **E** — A combination of committee approval and senior sign-off, depending on deal size

**D2. Approximately how many formal approval stages does a property acquisition typically pass through, from initial identification to final sign-off? ★**

*Select one option.*

- [ ] **A** — One stage
- [ ] **B** — Two stages
- [ ] **C** — Three stages
- [ ] **D** — Four or more stages
- [ ] **E** — This varies considerably and there is no standard process

**D3. How severe is the unavailability of data to prevent your fund from formally quantitatively analyzing real estate investment opportunities?**

*Circle or tick one number on the scale below.*

| *1 — Not at all (data is sufficient for our analytical needs)* | **1** | **2** | **3** | **4** | **5** | *5 — Very significantly (data gaps are a serious constraint)* |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| | ○ | ○ | ○ | ○ | ○ | |

**D4. Which of the following specific data gaps most constrain your investment analysis? ★**

*Select all that apply.*

- [ ] Absence of reliable transaction price databases for Nigerian property
- [ ] Limited historical rental yield data by submarket and property type
- [ ] Lack of standardised property valuation and appraisal indices
- [ ] No publicly available capital appreciation benchmarks
- [ ] Insufficient occupancy rate data by asset class and location
- [ ] Difficulty obtaining comparable transactions with disclosed pricing
- [ ] Unreliable macroeconomic projections for use in scenario modelling
- [ ] Weak or inconsistent title documentation on prospective properties
- [ ] No significant data gaps — available data meets our analytical needs

**D5. Which single change would most improve your fund's property selection decision-making? ★**

*Select one option — the one that would have the greatest practical impact.*

- [ ] **A** — Access to a reliable, comprehensive Nigerian real estate return and transaction database
- [ ] **B** — Dedicated in-house analytical staff with quantitative investment expertise
- [ ] **C** — Industry-wide standardisation of property valuation and performance reporting
- [ ] **D** — Clearer regulatory guidance from PenCom on real estate performance benchmarking
- [ ] **E** — Decision-support software designed specifically for Nigerian institutional property investment
- [ ] **F** — Investment committee training in portfolio construction and risk assessment techniques
- [ ] **G** — Reduction in transaction costs, title processing times, or regulatory friction
- [ ] **H** — No change required (our current process is adequate for our needs)

**D6. Which of the following institutional or contextual variables best predict the degree to which your fund is dependent on judgment and experience as opposed to formal quantitative analysis in property selection? ★**

*Select all that apply.*

- [ ] Time pressure (acquisition decisions must be made faster than analysis allows)
- [ ] Absence of reliable market data to support a quantitative approach
- [ ] Lack of in-house quantitative or modelling expertise
- [ ] Investment committee preference for experienced judgment over model outputs
- [ ] Regulatory uncertainty that makes long-term projections unreliable
- [ ] Peer PFA behaviour providing a practical benchmark in the absence of data
- [ ] Established organisational precedent (prior acquisitions set the template)
- [ ] High deal complexity that resists standardised modelling
- [ ] Quantitative analysis is fully used (judgment plays no primary role)

---

**Thank you for completing this questionnaire.**

*Your contribution is deeply appreciated and will directly inform the findings of this research.*

*ioakinmokun@student.oauife.edu.ng · Department of Estate Management, Obafemi Awolowo University, Ile-Ife, 2026.*

---

# APPENDIX B: PROPERTY COVARIANCE MATRIX DERIVED FROM SECONDARY MARKET REPORTS

This appendix presents the complete property covariance matrix $\boldsymbol{\Sigma} \in \mathbb{R}^{80 \times 80}$ calibrated for the 80-asset synthetic property universe, derived from secondary real estate market reports and macroeconomic data series.

The return volatilities, submarket correlation structures, and covariance terms were estimated by synthesizing historical empirical data from Jones Lang LaSalle (JLL, 2020–2025), Estate Intel Property Monitors (2021–2025), Broll Sub-Saharan Africa Research (2019–2025), NIESV Lagos State Branch Property Guides (2018–2025), and Central Bank of Nigeria (CBN) Statistical Bulletins (2015–2025).

---

## B.1 Property Covariance Heatmap and Visual Asset Matrix

Figure B.1 provides a high-resolution, annotated sub-matrix heatmap displaying the exact pairwise annual covariance values ($\times 10^{-4}$) among the 15 primary holdings selected across Portfolio A (Heuristic) and Portfolio B (MVO).

![Figure B.1: Pairwise Property Covariance Sub-Matrix](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/appendix_b_covariance_heatmap.png)

<a id="figure-**figure b1: pairwise property covariance sub-matrix ($\times 10^{-4}$)**"></a>
**Figure B.1: Pairwise Property Covariance Sub-Matrix ($\times 10^{-4}$)**  
*Source: Secondary Market Data Reports & Author's Computation, 2026*

> **Legend & Interpretation Note (Figure B.1):**
> - **Color Scale (YlGnBu):** Dark blue cells indicate high positive covariance ($\sigma_{ik} \ge 300 \times 10^{-4}$), representing strong co-movement among intra-Lagos assets. Light yellow cells indicate low to near-zero covariance ($\sigma_{ik} \le 50 \times 10^{-4}$), representing strong spatial diversification benefits.
> - **Primary Asset Pairs:** `PROP_01` to `PROP_10` (Lagos Residential/Mixed-Use) exhibit high internal covariance ($350\text{--}480 \times 10^{-4}$). Conversely, `PROP_13` (Kano Retail), `PROP_25` / `PROP_44` / `PROP_55` (Abuja Offices), and `PROP_80` (Rivers Logistics) exhibit low cross-city covariances ($14\text{--}48 \times 10^{-4}$), providing the empirical foundation for MVO covariance suppression.

---

## B.2 Inter-Submarket Baseline Correlation and Covariance Matrix

Table B.1 details the baseline return correlation coefficients ($\rho$) and annual covariance values ($\sigma_{ik}$) across major regional property submarkets derived from secondary market reports.

<a id="table-**table b1: inter-submarket return correlation and covariance matrix**"></a>
**Table B.1: Inter-Submarket Return Correlation and Covariance Matrix**

| Submarket Location Block | Lagos Island Prime | Lagos Mainland Commercial | Abuja FCT Grade A | Rivers State Industrial | Kano State Commercial | Oyo State Commercial |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Lagos Island Prime** | **1.0000** (0.0484) | 0.8200 (0.0318) | 0.2200 (0.0048) | 0.1500 (0.0031) | 0.0800 (0.0014) | 0.3500 (0.0076) |
| **Lagos Mainland Commercial** | 0.8200 (0.0318) | **1.0000** (0.0310) | 0.2500 (0.0046) | 0.1800 (0.0031) | 0.1000 (0.0015) | 0.4200 (0.0078) |
| **Abuja FCT Grade A** | 0.2200 (0.0048) | 0.2500 (0.0046) | **1.0000** (0.0121) | 0.3200 (0.0037) | 0.2800 (0.0028) | 0.2000 (0.0025) |
| **Rivers State Industrial** | 0.1500 (0.0031) | 0.1800 (0.0031) | 0.3200 (0.0037) | **1.0000** (0.0169) | 0.2500 (0.0030) | 0.1800 (0.0026) |
| **Kano State Commercial** | 0.0800 (0.0014) | 0.1000 (0.0015) | 0.2800 (0.0028) | 0.2500 (0.0030) | **1.0000** (0.0056) | 0.1500 (0.0013) |
| **Oyo State Commercial** | 0.3500 (0.0076) | 0.4200 (0.0078) | 0.2000 (0.0025) | 0.1800 (0.0026) | 0.1500 (0.0013) | **1.0000** (0.0098) |

*Source: Author's Calibration from Secondary Market Reports, 2026. Diagonal elements display asset variances $\sigma_i^2$; off-diagonal elements show correlation coefficients $\rho_{ik}$ with covariances in parentheses.*

---

## B.3 Explicit Pairwise Numerical Covariance Matrix ($15 \times 15$ Sub-Matrix)

Table B.2 details the exact pairwise numerical annual covariance values ($\times 10^{-4}$) among the 15 primary property holdings selected across Portfolio A and Portfolio B.

<a id="table-**table b2: explicit pairwise numerical covariance sub-matrix for selected portfolio holdings ($\times 10^{-4}$)**"></a>
**Table B.2: Explicit Pairwise Numerical Covariance Sub-Matrix for Selected Portfolio Holdings ($\times 10^{-4}$)**

| Property ID | PROP_01 | PROP_05 | PROP_09 | PROP_10 | PROP_13 | PROP_21 | PROP_23 | PROP_25 | PROP_26 | PROP_29 | PROP_32 | PROP_44 | PROP_55 | PROP_73 | PROP_80 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **PROP_01** | 484.0 | 318.2 | 356.1 | 442.8 | 14.2 | 305.6 | 312.4 | 48.1 | 15.0 | 468.2 | 76.5 | 46.2 | 47.8 | 310.0 | 31.4 |
| **PROP_05** | 318.2 | 310.0 | 280.5 | 312.0 | 15.1 | 288.4 | 294.0 | 46.2 | 14.8 | 320.1 | 78.2 | 45.1 | 46.0 | 292.0 | 30.8 |
| **PROP_09** | 356.1 | 280.5 | 380.0 | 348.0 | 13.8 | 272.0 | 278.5 | 45.0 | 14.2 | 360.5 | 74.0 | 43.8 | 44.9 | 275.2 | 29.5 |
| **PROP_10** | 442.8 | 312.0 | 348.0 | 450.0 | 14.0 | 300.2 | 308.0 | 47.5 | 14.9 | 440.0 | 75.8 | 45.9 | 47.0 | 305.0 | 31.0 |
| **PROP_13** | 14.2 | 15.1 | 13.8 | 14.0 | 56.0 | 14.6 | 14.8 | 28.0 | 25.0 | 14.1 | 13.0 | 27.5 | 28.2 | 14.5 | 30.0 |
| **PROP_21** | 305.6 | 288.4 | 272.0 | 300.2 | 14.6 | 290.0 | 282.5 | 44.8 | 14.5 | 308.0 | 76.0 | 44.0 | 45.2 | 286.0 | 30.2 |
| **PROP_23** | 312.4 | 294.0 | 278.5 | 308.0 | 14.8 | 282.5 | 298.0 | 45.5 | 14.6 | 314.5 | 77.0 | 44.8 | 45.8 | 290.5 | 30.5 |
| **PROP_25** | 48.1 | 46.2 | 45.0 | 47.5 | 28.0 | 44.8 | 45.5 | 121.0 | 28.5 | 47.8 | 25.0 | 115.0 | 118.0 | 45.2 | 37.0 |
| **PROP_26** | 15.0 | 14.8 | 14.2 | 14.9 | 25.0 | 14.5 | 14.6 | 28.5 | 58.0 | 14.8 | 13.5 | 28.0 | 28.6 | 14.4 | 30.5 |
| **PROP_29** | 468.2 | 320.1 | 360.5 | 440.0 | 14.1 | 308.0 | 314.5 | 47.8 | 14.8 | 475.0 | 77.0 | 46.0 | 47.2 | 312.0 | 31.2 |
| **PROP_32** | 76.5 | 78.2 | 74.0 | 75.8 | 13.0 | 76.0 | 77.0 | 25.0 | 13.5 | 77.0 | 98.0 | 24.5 | 25.2 | 76.2 | 26.0 |
| **PROP_44** | 46.2 | 45.1 | 43.8 | 45.9 | 27.5 | 44.0 | 44.8 | 115.0 | 28.0 | 46.0 | 24.5 | 118.0 | 114.5 | 44.5 | 36.2 |
| **PROP_55** | 47.8 | 46.0 | 44.9 | 47.0 | 28.2 | 45.2 | 45.8 | 118.0 | 28.6 | 47.2 | 25.2 | 114.5 | 122.0 | 45.5 | 36.8 |
| **PROP_73** | 310.0 | 292.0 | 275.2 | 305.0 | 14.5 | 286.0 | 290.5 | 45.2 | 14.4 | 312.0 | 76.2 | 44.5 | 45.5 | 295.0 | 30.4 |
| **PROP_80** | 31.4 | 30.8 | 29.5 | 31.0 | 30.0 | 30.2 | 30.5 | 37.0 | 30.5 | 31.2 | 26.0 | 36.2 | 36.8 | 30.4 | 169.0 |

*Source: Author's Computation, 2026*

---

## B.4 Pairwise Covariance Category Summary

Table B.3 categorizes the pairwise return covariances across portfolio holding tiers, summarizing structural risk contributions.

<a id="table-**table b3: pairwise covariance tiers and structural risk contributions**"></a>
**Table B.3: Pairwise Covariance Tiers and Structural Risk Contributions**

| Submarket Pair Category | Asset Pair Examples | Covariance Range ($\times 10^{-4}$) | Mean Correlation ($\bar{\rho}$) | Risk Contribution Implication |
|:---|:---|:---:|:---:|:---|
| **Intra-Lagos Prime** | `PROP_01` & `PROP_10` (Residential)<br>`PROP_05` & `PROP_21` (Office) | 280.5 – 484.0 | 0.8500 | High systematic risk co-movement; dominates Portfolio A volatility. |
| **Lagos vs. Oyo (Regional)** | `PROP_09` & `PROP_49` (Mixed-Use)<br>`PROP_21` & `PROP_32` (Office) | 74.0 – 78.2 | 0.3800 | Moderate spatial correlation; provides mild yield compensation. |
| **Lagos vs. Abuja (Federal)** | `PROP_05` & `PROP_25` (Office)<br>`PROP_10` & `PROP_55` (Office) | 43.8 – 48.1 | 0.2200 | Low correlation; primary engine of MVO covariance suppression. |
| **Lagos vs. Rivers (Industrial)**| `PROP_01` & `PROP_80` (Logistics)<br>`PROP_23` & `PROP_80` (Office) | 29.5 – 31.4 | 0.1500 | Very low correlation; hedges against state-level market shocks. |
| **Lagos vs. Kano (Northern)** | `PROP_01` & `PROP_13` (Retail)<br>`PROP_05` & `PROP_26` (Warehouse)| 13.8 – 15.1 | 0.0800 | Near-zero correlation; provides maximum spatial diversification. |

*Source: Author's Computation & Secondary Market Data Reports, 2026*

---

> **Repository Note:** The complete mathematical data sets, full 80×80 property covariance matrix $\boldsymbol{\Sigma} \in \mathbb{R}^{80 \times 80}$, master 80-property universe catalog, raw field survey results, and computational scripts in Python are permanently archived and publicly accessible at the GitHub repository of this dissertation. The computation results of this research can be fully reproduced by anyone.
>
> **GitHub Repository:** [https://github.com/islajr/pfa-portfolio-research](https://github.com/islajr/pfa-portfolio-research)

---

# APPENDIX C: FROZEN 80-PROPERTY SYNTHETIC UNIVERSE CATALOG

This appendix presents the complete specification catalog and visual distribution profiles for all 80 properties comprising the frozen synthetic property universe ($N=80$).

---

## C.1 Property Universe Risk-Return Profile and Submarket Distribution

Figure C.1 plots the expected annual return ($\mu_i$) against annual volatility ($\sigma_i$) across all 80 properties, color-coded by asset class type.

![Figure C.1: Risk-Return Profile Across 80 Frozen Synthetic Properties](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/appendix_c_risk_return_scatter.png)

<a id="figure-**figure c1: risk-return profile across 80 frozen synthetic properties**"></a>
**Figure C.1: Risk-Return Profile Across 80 Frozen Synthetic Properties**  
*Source: Frozen Synthetic Property Universe Specification, 2026*

> **Legend & Interpretation Note (Figure C.1):**
> - **Luxury Residential (Gold Dots):** Cluster in the high-return (23.5%–25.2%), high-volatility (21.0%–22.5%) upper-right quadrant.
> - **Commercial Office Grade A (Dark Blue Dots):** Cluster in moderate return (16.5%–18.5%) and volatility (16.0%–17.5%) in Lagos, and lower return (8.7%–11.2%) / volatility (10.5%–11.0%) in Abuja.
> - **Industrial Logistics & Warehouses (Purple Dots):** Positioned in low volatility tiers (7.4%–13.2%), offering risk suppression benefits.
> - **Hurdle Lines:** Red dashed line denotes the 15.0% base hurdle rate; grey dotted line denotes the 15.0% medium-volatility threshold.

Figure C.2 details the property count distribution across submarket location states and asset classes.

![Figure C.2: Property Count Distribution by Submarket Location State](https://github.com/islajr/pfa-portfolio-research/raw/master/outputs/charts/appendix_c_submarket_distribution.png)

<a id="figure-**figure c2: property count distribution by submarket location state**"></a>
**Figure C.2: Property Count Distribution by Submarket Location State**  
*Source: Frozen Synthetic Property Universe Specification, 2026*

---

## C.2 Submarket Grouped Property Catalog Tables

> **Legend for Catalog Tables C.1 – C.5:**
> - **Title Status Codes:** `C of O` = Certificate of Occupancy; `GC` = Governor's Consent; `RD` = Registered Deed.
> - **Regulatory Compliance:** All 80 properties (100%) meet PenCom commercial lease compliance guidelines and pass the 5% single-asset allocation cap.

<a id="table-### table c1: lagos state property submarket catalog ($n = 34$)"></a>
### Table C.1: Lagos State Property Submarket Catalog ($n = 34$)

| Property Code | Asset Class Type | Acquisition Cost (₦M) | Expected Return (%) | Volatility (%) | Title Status |
|:---|:---|:---:|:---:|:---:|:---:|
| PROP_01 | Luxury Residential | ₦1,345.0M | 24.77 | 22.0 | C of O |
| PROP_02 | Luxury Residential | ₦1,420.0M | 24.50 | 22.5 | C of O |
| PROP_03 | Commercial Office Grade A | ₦2,100.0M | 17.80 | 17.0 | C of O |
| PROP_04 | Commercial Office Grade A | ₦1,850.0M | 18.10 | 16.8 | C of O |
| PROP_05 | Commercial Office Grade A | ₦894.0M | 18.14 | 17.6 | C of O |
| PROP_06 | Commercial Retail | ₦950.0M | 15.20 | 15.0 | C of O |
| PROP_07 | Commercial Retail | ₦1,120.0M | 14.80 | 15.2 | C of O |
| PROP_08 | Commercial Mixed-Use | ₦1,650.0M | 21.40 | 19.5 | C of O |
| PROP_09 | Commercial Mixed-Use | ₦289.0M | 26.06 | 19.5 | C of O |
| PROP_10 | Luxury Residential | ₦1,177.0M | 24.02 | 21.2 | C of O |
| PROP_19 | Luxury Residential | ₦1,560.0M | 23.80 | 21.8 | C of O |
| PROP_20 | Commercial Office Grade A | ₦2,350.0M | 17.50 | 16.5 | C of O |
| PROP_21 | Commercial Office Grade A | ₦623.0M | 16.65 | 17.0 | C of O |
| PROP_22 | Commercial Office Grade A | ₦1,150.0M | 17.20 | 16.9 | C of O |
| PROP_23 | Commercial Office Grade A | ₦775.0M | 17.37 | 17.3 | C of O |
| PROP_29 | Luxury Residential | ₦1,886.0M | 23.92 | 21.8 | C of O |
| PROP_30 | Commercial Mixed-Use | ₦2,150.0M | 20.50 | 19.0 | C of O |
| PROP_33 | Commercial Office Grade A | ₦724.0M | 18.54 | 17.1 | C of O |
| PROP_34 | Commercial Retail | ₦1,450.0M | 15.60 | 14.8 | C of O |
| PROP_35 | Commercial Retail | ₦1,290.0M | 15.40 | 15.0 | C of O |
| PROP_36 | Luxury Residential | ₦1,013.0M | 24.10 | 21.5 | C of O |
| PROP_41 | Commercial Office Grade A | ₦1,920.0M | 17.90 | 16.7 | C of O |
| PROP_42 | Commercial Office Grade A | ₦824.0M | 17.61 | 17.2 | C of O |
| PROP_43 | Commercial Office Grade A | ₦931.0M | 18.32 | 17.0 | C of O |
| PROP_50 | Luxury Residential | ₦1,720.0M | 24.20 | 21.9 | C of O |
| PROP_51 | Luxury Residential | ₦1,480.0M | 24.40 | 22.1 | C of O |
| PROP_52 | Commercial Office Grade A | ₦2,400.0M | 17.40 | 16.6 | C of O |
| PROP_53 | Commercial Mixed-Use | ₦1,850.0M | 20.80 | 18.9 | C of O |
| PROP_54 | Luxury Residential | ₦360.0M | 24.84 | 22.0 | C of O |
| PROP_60 | Commercial Office Grade A | ₦1,650.0M | 18.00 | 16.9 | C of O |
| PROP_61 | Commercial Retail | ₦1,180.0M | 15.10 | 14.9 | C of O |
| PROP_62 | Commercial Mixed-Use | ₦602.0M | 25.17 | 19.2 | C of O |
| PROP_68 | Luxury Residential | ₦1,620.0M | 24.10 | 21.7 | C of O |
| PROP_69 | Luxury Residential | ₦307.0M | 25.14 | 22.3 | C of O |
| PROP_70 | Commercial Office Grade A | ₦2,250.0M | 17.70 | 16.8 | C of O |
| PROP_73 | Commercial Office Grade A | ₦284.0M | 18.13 | 17.2 | C of O |
| PROP_77 | Commercial Office Grade A | ₦1,780.0M | 17.90 | 16.8 | C of O |
| PROP_78 | Commercial Mixed-Use | ₦1,920.0M | 20.60 | 18.8 | C of O |
| PROP_79 | Commercial Office Grade A | ₦726.0M | 18.48 | 17.1 | C of O |

---

<a id="table-### table c2: abuja fct property submarket catalog ($n = 18$)"></a>
### Table C.2: Abuja FCT Property Submarket Catalog ($n = 18$)

| Property Code | Asset Class Type | Acquisition Cost (₦M) | Expected Return (%) | Volatility (%) | Title Status |
|:---|:---|:---:|:---:|:---:|:---:|
| PROP_11 | Commercial Office Grade A | ₦1,450.0M | 11.20 | 11.0 | GC |
| PROP_12 | Commercial Office Grade A | ₦1,890.0M | 10.80 | 10.8 | C of O |
| PROP_24 | Commercial Office Grade A | ₦1,620.0M | 10.50 | 10.5 | C of O |
| PROP_25 | Commercial Office Grade A | ₦258.0M | 10.33 | 11.0 | C of O |
| PROP_37 | Luxury Residential | ₦2,100.0M | 14.50 | 14.0 | C of O |
| PROP_38 | Commercial Mixed-Use | ₦1,750.0M | 12.80 | 12.2 | C of O |
| PROP_44 | Commercial Office Grade A | ₦555.0M | 8.73 | 10.9 | C of O |
| PROP_45 | Commercial Office Grade A | ₦1,420.0M | 9.50 | 10.6 | C of O |
| PROP_55 | Commercial Office Grade A | ₦1,713.0M | 9.89 | 11.0 | C of O |
| PROP_56 | Commercial Office Grade A | ₦1,980.0M | 9.70 | 10.8 | C of O |
| PROP_63 | Commercial Office Grade A | ₦236.0M | 10.72 | 10.7 | C of O |
| PROP_64 | Luxury Residential | ₦1,820.0M | 14.20 | 13.8 | C of O |
| PROP_71 | Commercial Office Grade A | ₦1,550.0M | 10.20 | 10.6 | C of O |
| PROP_72 | Commercial Mixed-Use | ₦1,420.0M | 12.50 | 12.1 | C of O |

---

<a id="table-### table c3: rivers state property submarket catalog ($n = 10$)"></a>
### Table C.3: Rivers State Property Submarket Catalog ($n = 10$)

| Property Code | Asset Class Type | Acquisition Cost (₦M) | Expected Return (%) | Volatility (%) | Title Status |
|:---|:---|:---:|:---:|:---:|:---:|
| PROP_15 | Industrial Logistics | ₦2,450.0M | 13.50 | 13.0 | C of O |
| PROP_16 | Industrial Logistics | ₦1,980.0M | 13.20 | 13.2 | C of O |
| PROP_28 | Commercial Office Grade B | ₦1,280.0M | 12.90 | 12.5 | C of O |
| PROP_39 | Industrial Logistics | ₦1,650.0M | 13.80 | 13.1 | C of O |
| PROP_46 | Industrial Logistics | ₦2,100.0M | 13.10 | 12.8 | C of O |
| PROP_57 | Commercial Office Grade B | ₦1,450.0M | 12.70 | 12.4 | C of O |
| PROP_65 | Industrial Logistics | ₦1,890.0M | 13.40 | 12.9 | C of O |
| PROP_74 | Industrial Logistics | ₦1,750.0M | 13.60 | 13.0 | C of O |
| PROP_80 | Industrial Logistics | ₦1,418.0M | 13.11 | 13.0 | C of O |

---

<a id="table-### table c4: oyo state property submarket catalog ($n = 10$)"></a>
### Table C.4: Oyo State Property Submarket Catalog ($n = 10$)

| Property Code | Asset Class Type | Acquisition Cost (₦M) | Expected Return (%) | Volatility (%) | Title Status |
|:---|:---|:---:|:---:|:---:|:---:|
| PROP_17 | Commercial Mixed-Use | ₦740.0M | 19.80 | 14.0 | C of O |
| PROP_18 | Commercial Mixed-Use | ₦820.0M | 19.20 | 14.2 | C of O |
| PROP_31 | Commercial Office Grade B | ₦650.0M | 18.90 | 13.8 | C of O |
| PROP_32 | Commercial Office Grade B | ₦1,068.0M | 19.35 | 9.9 | C of O |
| PROP_48 | Commercial Mixed-Use | ₦920.0M | 19.50 | 14.1 | C of O |
| PROP_49 | Commercial Mixed-Use | ₦505.0M | 27.83 | 14.3 | C of O |
| PROP_59 | Commercial Office Grade B | ₦880.0M | 18.70 | 13.9 | C of O |
| PROP_67 | Commercial Mixed-Use | ₦1,050.0M | 19.10 | 14.0 | C of O |
| PROP_76 | Commercial Office Grade B | ₦790.0M | 18.80 | 13.8 | C of O |

---

<a id="table-### table c5: kano state property submarket catalog ($n = 8$)"></a>
### Table C.5: Kano State Property Submarket Catalog ($n = 8$)

| Property Code | Asset Class Type | Acquisition Cost (₦M) | Expected Return (%) | Volatility (%) | Title Status |
|:---|:---|:---:|:---:|:---:|:---:|
| PROP_13 | Commercial Retail | ₦590.0M | 9.02 | 7.5 | RD |
| PROP_14 | Commercial Retail | ₦680.0M | 8.80 | 7.8 | RD |
| PROP_26 | Industrial Warehouse | ₦230.0M | 10.27 | 7.6 | RD |
| PROP_27 | Industrial Warehouse | ₦450.0M | 9.80 | 7.8 | RD |
| PROP_40 | Commercial Retail | ₦520.0M | 9.20 | 7.4 | RD |
| PROP_47 | Industrial Warehouse | ₦380.0M | 10.10 | 7.7 | RD |
| PROP_58 | Commercial Retail | ₦710.0M | 8.90 | 7.6 | RD |
| PROP_66 | Industrial Warehouse | ₦490.0M | 9.90 | 7.7 | RD |
| PROP_75 | Commercial Retail | ₦640.0M | 9.10 | 7.5 | RD |

---

## C.3 Complete Master Property Universe Catalog ($N = 80$)

Table C.6 presents the complete, unabridged master specification catalog for all 80 properties in the synthetic universe.

<a id="table-**table c6: complete ground-truth property universe master catalog ($n = 80$)**"></a>
**Table C.6: Complete Ground-Truth Property Universe Master Catalog ($N = 80$)**

| Property Code | Submarket Location State | Asset Type Class | Total Acquisition Cost (₦ Millions) | Expected Annual Return (%) | Annual Volatility (%) | Title Document Status | PenCom Lease Compliant | Single Asset Ceiling Pass |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| PROP_01 | Lagos State | Luxury Residential | ₦1,345.0M | 24.77 | 22.0 | Certificate of Occupancy | Yes | Pass |
| PROP_02 | Lagos State | Luxury Residential | ₦1,420.0M | 24.50 | 22.5 | Certificate of Occupancy | Yes | Pass |
| PROP_03 | Lagos State | Commercial Office Grade A | ₦2,100.0M | 17.80 | 17.0 | Certificate of Occupancy | Yes | Pass |
| PROP_04 | Lagos State | Commercial Office Grade A | ₦1,850.0M | 18.10 | 16.8 | Certificate of Occupancy | Yes | Pass |
| PROP_05 | Lagos State | Commercial Office Grade A | ₦894.0M | 18.14 | 17.6 | Certificate of Occupancy | Yes | Pass |
| PROP_06 | Lagos State | Commercial Retail | ₦950.0M | 15.20 | 15.0 | Certificate of Occupancy | Yes | Pass |
| PROP_07 | Lagos State | Commercial Retail | ₦1,120.0M | 14.80 | 15.2 | Certificate of Occupancy | Yes | Pass |
| PROP_08 | Lagos State | Commercial Mixed-Use | ₦1,650.0M | 21.40 | 19.5 | Certificate of Occupancy | Yes | Pass |
| PROP_09 | Lagos State | Commercial Mixed-Use | ₦289.0M | 26.06 | 19.5 | Certificate of Occupancy | Yes | Pass |
| PROP_10 | Lagos State | Luxury Residential | ₦1,177.0M | 24.02 | 21.2 | Certificate of Occupancy | Yes | Pass |
| PROP_11 | Abuja FCT | Commercial Office Grade A | ₦1,450.0M | 11.20 | 11.0 | Governor's Consent | Yes | Pass |
| PROP_12 | Abuja FCT | Commercial Office Grade A | ₦1,890.0M | 10.80 | 10.8 | Certificate of Occupancy | Yes | Pass |
| PROP_13 | Kano State | Commercial Retail | ₦590.0M | 9.02 | 7.5 | Registered Deed | Yes | Pass |
| PROP_14 | Kano State | Commercial Retail | ₦680.0M | 8.80 | 7.8 | Registered Deed | Yes | Pass |
| PROP_15 | Rivers State | Industrial Logistics | ₦2,450.0M | 13.50 | 13.0 | Certificate of Occupancy | Yes | Pass |
| PROP_16 | Rivers State | Industrial Logistics | ₦1,980.0M | 13.20 | 13.2 | Certificate of Occupancy | Yes | Pass |
| PROP_17 | Oyo State | Commercial Mixed-Use | ₦740.0M | 19.80 | 14.0 | Certificate of Occupancy | Yes | Pass |
| PROP_18 | Oyo State | Commercial Mixed-Use | ₦820.0M | 19.20 | 14.2 | Certificate of Occupancy | Yes | Pass |
| PROP_19 | Lagos State | Luxury Residential | ₦1,560.0M | 23.80 | 21.8 | Certificate of Occupancy | Yes | Pass |
| PROP_20 | Lagos State | Commercial Office Grade A | ₦2,350.0M | 17.50 | 16.5 | Certificate of Occupancy | Yes | Pass |
| PROP_21 | Lagos State | Commercial Office Grade A | ₦623.0M | 16.65 | 17.0 | Certificate of Occupancy | Yes | Pass |
| PROP_22 | Lagos State | Commercial Office Grade A | ₦1,150.0M | 17.20 | 16.9 | Certificate of Occupancy | Yes | Pass |
| PROP_23 | Lagos State | Commercial Office Grade A | ₦775.0M | 17.37 | 17.3 | Certificate of Occupancy | Yes | Pass |
| PROP_24 | Abuja FCT | Commercial Office Grade A | ₦1,620.0M | 10.50 | 10.5 | Certificate of Occupancy | Yes | Pass |
| PROP_25 | Abuja FCT | Commercial Office Grade A | ₦258.0M | 10.33 | 11.0 | Certificate of Occupancy | Yes | Pass |
| PROP_26 | Kano State | Industrial Warehouse | ₦230.0M | 10.27 | 7.6 | Registered Deed | Yes | Pass |
| PROP_27 | Kano State | Industrial Warehouse | ₦450.0M | 9.80 | 7.8 | Registered Deed | Yes | Pass |
| PROP_28 | Rivers State | Commercial Office Grade B | ₦1,280.0M | 12.90 | 12.5 | Certificate of Occupancy | Yes | Pass |
| PROP_29 | Lagos State | Luxury Residential | ₦1,886.0M | 23.92 | 21.8 | Certificate of Occupancy | Yes | Pass |
| PROP_30 | Lagos State | Commercial Mixed-Use | ₦2,150.0M | 20.50 | 19.0 | Certificate of Occupancy | Yes | Pass |
| PROP_31 | Oyo State | Commercial Office Grade B | ₦650.0M | 18.90 | 13.8 | Certificate of Occupancy | Yes | Pass |
| PROP_32 | Oyo State | Commercial Office Grade B | ₦1,068.0M | 19.35 | 9.9 | Certificate of Occupancy | Yes | Pass |
| PROP_33 | Lagos State | Commercial Office Grade A | ₦724.0M | 18.54 | 17.1 | Certificate of Occupancy | Yes | Pass |
| PROP_34 | Lagos State | Commercial Retail | ₦1,450.0M | 15.60 | 14.8 | Certificate of Occupancy | Yes | Pass |
| PROP_35 | Lagos State | Commercial Retail | ₦1,290.0M | 15.40 | 15.0 | Certificate of Occupancy | Yes | Pass |
| PROP_36 | Lagos State | Luxury Residential | ₦1,013.0M | 24.10 | 21.5 | Certificate of Occupancy | Yes | Pass |
| PROP_37 | Abuja FCT | Luxury Residential | ₦2,100.0M | 14.50 | 14.0 | Certificate of Occupancy | Yes | Pass |
| PROP_38 | Abuja FCT | Commercial Mixed-Use | ₦1,750.0M | 12.80 | 12.2 | Certificate of Occupancy | Yes | Pass |
| PROP_39 | Rivers State | Industrial Logistics | ₦1,650.0M | 13.80 | 13.1 | Certificate of Occupancy | Yes | Pass |
| PROP_40 | Kano State | Commercial Retail | ₦520.0M | 9.20 | 7.4 | Registered Deed | Yes | Pass |
| PROP_41 | Lagos State | Commercial Office Grade A | ₦1,920.0M | 17.90 | 16.7 | Certificate of Occupancy | Yes | Pass |
| PROP_42 | Lagos State | Commercial Office Grade A | ₦824.0M | 17.61 | 17.2 | Certificate of Occupancy | Yes | Pass |
| PROP_43 | Lagos State | Commercial Office Grade A | ₦931.0M | 18.32 | 17.0 | Certificate of Occupancy | Yes | Pass |
| PROP_44 | Abuja FCT | Commercial Office Grade A | ₦555.0M | 8.73 | 10.9 | Certificate of Occupancy | Yes | Pass |
| PROP_45 | Abuja FCT | Commercial Office Grade A | ₦1,420.0M | 9.50 | 10.6 | Certificate of Occupancy | Yes | Pass |
| PROP_46 | Rivers State | Industrial Logistics | ₦2,100.0M | 13.10 | 12.8 | Certificate of Occupancy | Yes | Pass |
| PROP_47 | Kano State | Industrial Warehouse | ₦380.0M | 10.10 | 7.7 | Registered Deed | Yes | Pass |
| PROP_48 | Oyo State | Commercial Mixed-Use | ₦920.0M | 19.50 | 14.1 | Certificate of Occupancy | Yes | Pass |
| PROP_49 | Oyo State | Commercial Mixed-Use | ₦505.0M | 27.83 | 14.3 | Certificate of Occupancy | Yes | Pass |
| PROP_50 | Lagos State | Luxury Residential | ₦1,720.0M | 24.20 | 21.9 | Certificate of Occupancy | Yes | Pass |
| PROP_51 | Lagos State | Luxury Residential | ₦1,480.0M | 24.40 | 22.1 | Certificate of Occupancy | Yes | Pass |
| PROP_52 | Lagos State | Commercial Office Grade A | ₦2,400.0M | 17.40 | 16.6 | Certificate of Occupancy | Yes | Pass |
| PROP_53 | Lagos State | Commercial Mixed-Use | ₦1,850.0M | 20.80 | 18.9 | Certificate of Occupancy | Yes | Pass |
| PROP_54 | Lagos State | Luxury Residential | ₦360.0M | 24.84 | 22.0 | Certificate of Occupancy | Yes | Pass |
| PROP_55 | Abuja FCT | Commercial Office Grade A | ₦1,713.0M | 9.89 | 11.0 | Certificate of Occupancy | Yes | Pass |
| PROP_56 | Abuja FCT | Commercial Office Grade A | ₦1,980.0M | 9.70 | 10.8 | Certificate of Occupancy | Yes | Pass |
| PROP_57 | Rivers State | Commercial Office Grade B | ₦1,450.0M | 12.70 | 12.4 | Certificate of Occupancy | Yes | Pass |
| PROP_58 | Kano State | Commercial Retail | ₦710.0M | 8.90 | 7.6 | Registered Deed | Yes | Pass |
| PROP_59 | Oyo State | Commercial Office Grade B | ₦880.0M | 18.70 | 13.9 | Certificate of Occupancy | Yes | Pass |
| PROP_60 | Lagos State | Commercial Office Grade A | ₦1,650.0M | 18.00 | 16.9 | Certificate of Occupancy | Yes | Pass |
| PROP_61 | Lagos State | Commercial Retail | ₦1,180.0M | 15.10 | 14.9 | Certificate of Occupancy | Yes | Pass |
| PROP_62 | Lagos State | Commercial Mixed-Use | ₦602.0M | 25.17 | 19.2 | Certificate of Occupancy | Yes | Pass |
| PROP_63 | Abuja FCT | Commercial Office Grade A | ₦236.0M | 10.72 | 10.7 | Certificate of Occupancy | Yes | Pass |
| PROP_64 | Abuja FCT | Luxury Residential | ₦1,820.0M | 14.20 | 13.8 | Certificate of Occupancy | Yes | Pass |
| PROP_65 | Rivers State | Industrial Logistics | ₦1,890.0M | 13.40 | 12.9 | Certificate of Occupancy | Yes | Pass |
| PROP_66 | Kano State | Industrial Warehouse | ₦490.0M | 9.90 | 7.7 | Registered Deed | Yes | Pass |
| PROP_67 | Oyo State | Commercial Mixed-Use | ₦1,050.0M | 19.10 | 14.0 | Certificate of Occupancy | Yes | Pass |
| PROP_68 | Lagos State | Luxury Residential | ₦1,620.0M | 24.10 | 21.7 | Certificate of Occupancy | Yes | Pass |
| PROP_69 | Lagos State | Luxury Residential | ₦307.0M | 25.14 | 22.3 | Certificate of Occupancy | Yes | Pass |
| PROP_70 | Lagos State | Commercial Office Grade A | ₦2,250.0M | 17.70 | 16.8 | Certificate of Occupancy | Yes | Pass |
| PROP_71 | Abuja FCT | Commercial Office Grade A | ₦1,550.0M | 10.20 | 10.6 | Certificate of Occupancy | Yes | Pass |
| PROP_72 | Abuja FCT | Commercial Mixed-Use | ₦1,420.0M | 12.50 | 12.1 | Certificate of Occupancy | Yes | Pass |
| PROP_73 | Lagos State | Commercial Office Grade A | ₦284.0M | 18.13 | 17.2 | Certificate of Occupancy | Yes | Pass |
| PROP_74 | Rivers State | Industrial Logistics | ₦1,750.0M | 13.60 | 13.0 | Certificate of Occupancy | Yes | Pass |
| PROP_75 | Kano State | Commercial Retail | ₦640.0M | 9.10 | 7.5 | Registered Deed | Yes | Pass |
| PROP_76 | Oyo State | Commercial Office Grade B | ₦790.0M | 18.80 | 13.8 | Certificate of Occupancy | Yes | Pass |
| PROP_77 | Lagos State | Commercial Office Grade A | ₦1,780.0M | 17.90 | 16.8 | Certificate of Occupancy | Yes | Pass |
| PROP_78 | Lagos State | Commercial Mixed-Use | ₦1,920.0M | 20.60 | 18.8 | Certificate of Occupancy | Yes | Pass |
| PROP_79 | Lagos State | Commercial Office Grade A | ₦726.0M | 18.48 | 17.1 | Certificate of Occupancy | Yes | Pass |
| PROP_80 | Rivers State | Industrial Logistics | ₦1,418.0M | 13.11 | 13.0 | Certificate of Occupancy | Yes | Pass |

*Source: Frozen Synthetic Property Universe Specification, 2026*

---

## C.4 DATA AVAILABILITY & REPOSITORY REFERENCE NOTE

> [!NOTE]
> **Complete Computational Data & Open-Source Repository:**  
> The full numerical datasets, raw field survey responses, complete $80 \times 80$ property covariance matrix (`property_covariance_matrix.csv`), frozen synthetic property universe (`property_universe.csv`), Monte Carlo simulation outputs (10,000 paths), and automated Python optimization scripts (`packages/optimizer/`) supporting this dissertation are fully detailed and preserved within the research monorepo repository.  
> 
> **Repository Data & Code Locations:**  
> - **Local Data Directory:** `data/frozen/` and `outputs/`
> - **Source Code Scripts:** `packages/optimizer/` (Heuristic Engine, Integer MVO Solver, Monte Carlo Simulation)
> - **Visual Assets & High-Resolution Charts:** `outputs/charts/`
> - **Monorepo Version Control Archive:** GitHub Repository (`pfa-portfolio-research`)

---

# APPENDIX D: SECONDARY MARKET CALIBRATION NOTES AND INDEX SOURCES

This appendix documents the secondary real estate market reports, regulatory policy frameworks, and macroeconomic series used to calibrate the empirical return vectors ($\boldsymbol{\mu}$) and property covariance matrix ($\boldsymbol{\Sigma}$) for the study.

---

## D.1 Secondary Market Data Sources

1. **Jones Lang LaSalle (JLL) Sub-Saharan Africa Real Estate Reports (2020–2025):** 
   - Provided baseline rental yield figures (7.5%–9.0%) and capital appreciation rates for Grade A commercial office developments in Victoria Island, Ikoyi, and Lekki, Lagos.
   - Provided commercial lease structure benchmarks (USD-indexed vs. NGN-denominated leases).

2. **Estate Intel Nigeria Property Market Monitors (2021–2025):** 
   - Provided prime residential rent growth series (17.5%–20.0%) and vacancy rate benchmarks across Lagos Island and Abuja FCT submarkets.
   - Provided historical price-per-square-meter series for luxury residential developments.

3. **Broll Property Group Nigeria Market Overviews (2019–2025):** 
   - Provided office yield data (7.0%–8.5%) and government tenancy vacancy rates for Abuja Central Business District (CBD) and Maitama.
   - Provided commercial retail yield benchmarks.

4. **Nigerian Institution of Estate Surveyors and Valuers (NIESV) Lagos State Branch Annual Property Guides (2018–2025):** 
   - Provided secondary market yield benchmarks for Lagos Mainland (Ikeja, Yaba) and regional commercial property yields in Oyo (Ibadan) and Kano states.

5. **Central Bank of Nigeria (CBN) Statistical Bulletins (2015–2025):** 
   - Provided historical Monetary Policy Rates (MPR), Treasury Bill yield series, and headline inflation rates used to establish baseline risk-free benchmarks ($R_f = 8.4\%$) and sensitivity scenarios ($R_f = 10.0\%, 15.0\%, 20.0\%$).

6. **National Pension Commission (PenCom) Annual Reports (2020–2025):** 
   - Provided institutional pension industry AUM figures (₦18+ trillion) and regulatory investment guidelines governing direct real estate caps (10% total allocation ceiling; 5% single-asset limit).
