# System Architecture and Mathematical Framework

This document provides a detailed description of the system architecture, component integrations, data flow, and complete mathematical specifications of the property portfolio research monorepo. It serves as the primary technical reference for understanding how qualitative survey inputs are translated into empirical portfolios, simulated under stochastic return paths, and evaluated against normative asset allocation models.

---

## 1. System Architecture and Design Philosophy

The system is designed as a multi-tier monorepo structured to bridge qualitative behavioral finance research with quantitative financial simulation and interactive visualization. The system architecture consists of three principal tiers, each selected to optimize computational efficiency, data integrity, and visual accessibility:

1.  **Tier 1: Analytical Core (Python 3.10+):** The computational engine of the research. Python was selected for this tier due to its mature scientific stack (Pandas for survey cleaning, NumPy and SciPy for numerical matrix manipulations and SLSQP optimization, and PyPDF for PDF document parsing). This tier contains the entire empirical pipeline: it parses the raw questionnaire spreadsheet, computes individual composite heuristic scores, calibrates the decision weights, constructs the portfolios, executes the stochastically correlated Monte Carlo simulations, runs the hypothesis tests, and generates the LaTeX tables and PNG charts.
2.  **Tier 2: Backend Services (Java 17 / Spring Boot 3.2):** The planned enterprise persistence layer. Spring Boot was selected to provide a robust, type-safe REST API for data persistence. It utilizes Spring Data JPA to map the python-generated JSON property universe and simulation paths to a relational database schema (e.g., PostgreSQL). This tier decouples the heavy mathematical calculations from the UI, ensuring that portfolio configurations, historical covariance matrices, and simulated return paths can be queried via standard REST endpoints.
3.  **Tier 3: Interactive Simulator (Next.js 14 / TypeScript / Tailwind CSS):** The planned visual frontend. Next.js provides a responsive web application designed to democratize portfolio optimization tools for institutional trustees. It fetches portfolio data and simulated paths from the Spring Boot API, rendering the efficient frontier, asset-type allocations, and Monte Carlo paths on interactive dashboards using React charts (Recharts). This allows trustees to dynamically adjust risk-free rates and view the resulting Sharpe ratio performance in real time.

The integration between these tiers follows a strict data serialization contract. The Python analytical engine exports the calibrated property universe, selected portfolio holding lists, and simulated return statistics as structured JSON files. The Spring Boot backend consumes these JSON assets to seed its database, and the Next.js frontend queries the API to populate its UI components, ensuring end-to-end data consistency across the monorepo.

---

## 2. Complete Mathematical Specifications

The computational engine of the project is governed by a sequence of mathematical operations divided into four main phases:

### Phase 1: Heuristic Weight Elicitation and Calibration
Individual composite heuristic scores ($H_{j,k} \in [0, 1]$) are calculated for each of the $N=32$ active respondents across four heuristic dimensions ($j=1,2,3,4$) using primary survey items:

1.  **Title Anchoring Score ($ACS_k$):** Measures the manager's cognitive anchoring on standard legal titles.
    $$ACS_k = \frac{w_1 \cdot B3_k + w_2 \cdot C1_k}{w_1 + w_2}$$
    Where $B3_k$ is the Likert score (1–5) for title non-negotiability, $C1_k$ is the binary choice in Scenario C1 (standard title selection = 1.0, non-standard = 0.0), and $w_1, w_2$ are scale-normalizing weights.
2.  **Location Familiarity Score ($AVCS_k$):** Measures the availability bias regarding prime, highly visible submarkets.
    $$AVCS_k = \frac{w_1 \cdot B1\_rank\_loc_k + w_2 \cdot B2_k + w_3 \cdot C2_k}{w_1 + w_2 + w_3}$$
    Where $B1\_rank\_loc_k$ is the normalized rank of location, $B2_k$ is the Likert agreement on location risk proxying, and $C2_k$ is the choice of the prime submarket in Scenario C2.
3.  **Trend Momentum Score ($RCS_k$):** Measures the representativeness bias in chasing historical returns.
    $$RCS_k = \frac{w_1 \cdot B1\_rank\_sector_k + w_2 \cdot C3_k}{w_1 + w_2}$$
    Where $B1\_rank\_sector_k$ is the normalized rank of recent momentum, and $C3_k$ is the choice of the high-momentum sector in Scenario C3.
4.  **Peer Herding Score ($HCS_k$):** Measures social herding and relative risk mirroring.
    $$HCS_k = \frac{w_1 \cdot B1\_rank\_peer_k + w_2 \cdot B4_k + w_3 \cdot C4_k}{w_1 + w_2 + w_3}$$
    Where $B1\_rank\_peer_k$ is the normalized rank of peer activity, $B4_k$ is the Likert score for peer mirroring, and $C4_k$ is the choice of the peer-mirrored asset in Scenario C4.

The average score for each heuristic across all respondents is calculated:
$$\bar{H}_j = \frac{1}{N} \sum_{k=1}^{N} H_{j,k}$$
The final heuristic selection weights ($\alpha_j$) are calibrated by normalizing these averages to sum to 1.0:
$$\alpha_j = \frac{\bar{H}_j}{\sum_{i=1}^{4} \bar{H}_i}$$

---

### Phase 2: Property Universe Calibration
The 80 properties in the synthetic universe are calibrated using historical indices from CBRE and PenCom market reports. For each property $i$:

1.  **Total Acquisition Cost ($TAC_i$):**
    $$TAC_i = P_i \times (1 + f_{\text{agency}} + f_{\text{legal}} + f_{\text{consent},s_i})$$
    Where $P_i$ is the raw property price, $f_{\text{agency}}$ is the agency fee (0.05), $f_{\text{legal}}$ is the legal fee (0.05), and $f_{\text{consent},s_i}$ is the state-specific title consent fee (ranging from 0.00 for C of O to 0.05 for Excision).
2.  **Net Operating Income ($NOI_i$):**
    $$NOI_i = (GR_i \times (1 - v_{a_i})) - (GR_i \times m_{a_i})$$
    Where $GR_i$ is the gross annual rent, $v_{a_i}$ is the asset-class vacancy rate, and $m_{a_i}$ is the maintenance rate.
3.  **Capitalization Rate ($CR_i$):**
    $$CR_i = \frac{NOI_i}{TAC_i}$$
4.  **Expected Annual Return ($E[R_i]$):**
    $$E[R_i] = CR_i + \mu_{\text{idx}(i)}$$
    Where $\mu_{\text{idx}(i)}$ is the historical annual capital appreciation of property $i$'s market index.
5.  **Total Annual Volatility ($\sigma_i$):**
    $$\sigma_i = \sigma_{\text{idx}(i)} + \delta^{\text{title}}_{\text{tl}_i} + \delta^{\text{cond}}_{\text{cn}_i}$$
    Where $\sigma_{\text{idx}(i)}$ is the historical standard deviation of the assigned market index, and $\delta^{\text{title}}_{\text{tl}_i}, \delta^{\text{cond}}_{\text{cn}_i}$ are risk premiums added for non-standard title status and poor physical condition, respectively.

---

### Phase 3: Portfolio Construction and BIP Optimization

#### Portfolio A (Heuristic-Driven)
Constructed by evaluating all properties using the composite scoring function:
$$H(p_i) = \alpha_1 \cdot TS(p_i) + \alpha_2 \cdot LS(p_i) + \alpha_3 \cdot MS(p_i) + \alpha_4 \cdot PS(p_i)$$
Where $TS, LS, MS, PS$ are property-specific scores for Title (standard = 1.0, non-standard = 0.5/0.0), Location (prime = 1.0, secondary = 0.6, emerging = 0.2), Momentum, and Peer holdings. Properties are filtered to exclude legal risks (EBA heuristic), sorted in descending order of $H(p_i)$, and allocated equal weights ($w_i = 1/k$) under a greedy budget search.

#### Portfolio B (MVO-Optimized)
Formulated as a Binary Integer Programming (BIP) problem that maximizes the portfolio Sharpe ratio under baseline conditions:
$$\text{Maximize } \quad SR_P = \frac{E[R_P] - R_f}{\sigma_P}$$
$$\text{Subject to:} \quad \sum_{i=1}^{80} x_i \cdot TAC_i \leq \text{Budget} \quad (\text{Budget} = \text{₦10 Billion})$$
$$E[R_P] = \sum_{i=1}^{80} w_i x_i E[R_i] \quad \text{where} \quad w_i = \frac{1}{\sum_{j=1}^{80} x_j}$$
$$\sigma_P = \sqrt{\mathbf{x}^T \boldsymbol{\Sigma} \mathbf{x}} \quad \text{where} \mathbf{x} \text{ is the vector of } x_i w_i$$
$$x_i \in \{0, 1\} \quad \forall i \in \{1, \dots, 80\}$$
$$\text{Single-property concentration cap:} \quad TAC_i \cdot x_i \leq 0.05 \times \text{Budget} \quad (\text{₦500 Million})$$
$$\text{State diversification:} \quad \text{unique}(\{\text{state}_i \cdot x_i\}) \geq 2$$
$$\text{Selected asset count constraint:} \quad 5 \leq \sum_{i=1}^{80} x_i \leq 20$$

---

### Phase 4: Monte Carlo Path Simulation
Both portfolios are simulated over a $T=60$ month horizon ($N_{\text{sim}} = 10,000$ paths) under Geometric Brownian Motion (GBM). For each path and each month $\tau$:
$$V_P(\tau) = V_P(\tau - 1) \times (1 + R_P(\tau))$$
Where $R_P(\tau)$ is the portfolio return in month $\tau$:
$$R_P(\tau) = \sum_{i \in \text{selected}} w_i \cdot R_i(\tau)$$
The monthly individual asset returns $R_i(\tau)$ are generated using a correlated multivariate normal distribution:
$$\mathbf{R}(\tau) = \mathbf{CR} + \mathbf{Z} \mathbf{L}^T$$
Where $\mathbf{CR}$ is the monthly vector of expected capitalization yields, $\mathbf{Z}$ is a vector of independent standard normal random variables, and $\mathbf{L}$ is the lower triangular Cholesky decomposition of the covariance matrix $\boldsymbol{\Sigma}$:
$$\boldsymbol{\Sigma} = \mathbf{L} \mathbf{L}^T$$

---

## 3. Critical Analytical and Empirical Quirks

During the implementation and analysis of this project, several unique behaviors and "quirks" were documented. These are described in detail below to clarify the underlying financial and mathematical logic:

### 3.1 The Sharpe Ratio Crossover Phenomenon and Hurdle Rate Risk
A central empirical contribution of this study is the documentation of a critical performance crossover between heuristic-driven and optimized asset allocation models. Standard Modern Portfolio Theory (MPT) assumes that expected returns and covariances are stable and that optimization models consistently outperform qualitative judgment on a risk-adjusted basis. However, in emerging markets like Nigeria, this assumption collapses under high macroeconomic interest rates.

*   **Low Interest Rate Regimes ($R_f < 12.0\%$):** Under the historical baseline rate ($R_f = 8.4\%$), Portfolio B (MVO) achieves a mean Sharpe ratio of 4.9243, while Portfolio A (Heuristic) achieves 2.6753. This results in a Sharpe difference of $\Delta SR = 2.2490$ (BCa 95% CI `[2.2572, 2.3388]`), validating the normative efficiency advantage of mean-variance optimization. The solver achieves this efficiency by selecting assets with extremely low covariance.
*   **High Interest Rate Regimes ($R_f \ge 15.0\%$):** When the risk-free rate rises above 12.0%, the Sharpe ratio advantage reverses. At $R_f = 15.0\%$, the heuristic portfolio outperforms the optimized portfolio (Sharpe = 1.0690 vs. 0.5740). At $R_f = 20.0\%$, the optimized portfolio's Sharpe ratio collapses to **-2.7217**, while the heuristic portfolio remains stable with a minor downside (Sharpe = -0.1480).
*   **The Mathematical Cause of the Collapse:** The Sharpe ratio is defined as excess return divided by portfolio volatility: $SR_P = (E[R_P] - R_f) / \sigma_P$. To minimize portfolio variance ($\sigma_P$), the MVO solver concentrates its capital in low-volatility properties. In this synthetic universe, these are low-return assets (expected returns of 10.0%–11.0%). When the risk-free rate rises to 15.0% or 20.0%, the expected returns of these low-volatility assets fail to clear the hurdle rate, resulting in negative excess returns ($E[R_P] - R_f < 0$). Because the denominator ($\sigma_P$) of the optimized portfolio is very small (1.53%), dividing a negative excess return by a tiny volatility causes the Sharpe ratio to drop precipitously to **-2.7217**.
*   **The Heuristic Buffer:** In contrast, the heuristic portfolio focuses on prime, high-growth, high-nominal-yield properties (expected CAGR of 19.39%). Because its expected returns are high, the portfolio clears the 15.0% hurdle rate, maintaining a positive Sharpe ratio (1.0690). 
*   **Theoretical Implication:** This crossover validates **Gigerenzer's (1999) Ecological Rationality** framework and the concept of **Estimation Risk** (DeMiguel et al., 2009). Simple heuristics that ignore covariance calculations and focus on high nominal yields are more robust to macroeconomic shocks than sensitive optimization models. Under high-interest-rate uncertainty, heuristics are ecologically rational.

### 3.2 The Volatility Suppression Paradox and Covariance Over-Optimization
Normative asset allocation guidelines recommend that institutional investors diversify their capital evenly across different categories (such as states and asset classes) to manage risk. However, the optimized portfolio (Portfolio B) exhibits the opposite behavior, concentrating heavily in a single asset type.

*   **Asset Type Concentration:** Portfolio A (Heuristic) is highly diversified, holding four different asset classes (Asset Type HHI = 0.2222). Portfolio B (MVO) is highly concentrated, allocating **80.0% of its capital to Office Grade A/B assets** (Asset Type HHI = 0.6800).
*   **The Mathematical Cause:** The binary integer programming solver minimizes overall portfolio volatility by identifying properties with low covariance. In our historical index series, office properties in Lagos and Abuja exhibit exceptionally low covariance ($Cov < 0$). Instead of diversifying across different asset classes (e.g., residential or industrial properties, which carry higher individual volatilities), the solver maximizes risk-adjusted return by concentrating holdings in low-covariance office assets.
*   **The Paradox:** While Portfolio B is mathematically "optimal" under baseline conditions, its high concentration in a single asset type exposes the fund to severe **sector-specific structural shocks** (such as a sudden decline in office demand or zoning changes) that are not captured in historical covariance matrices. This illustrates the danger of over-optimization: standard mean-variance solvers suppress volatility by ignoring naive diversification, exposing the fund to unmodeled tail risks.

### 3.3 The Frozen Universe Policy and Longitudinal Research Consistency
To support empirical replication and maintain scientific rigor, this project enforces a strict read-only policy for all files in the `data/frozen/` directory.

*   **The Purpose:** The 80 properties in the synthetic universe serve as the baseline environment for the entire study. Modifying the random seed (default: 42) or changing the calibration parameters in `packages/generator` will regenerate the property universe, altering the expected returns, volatilities, and covariance matrices of the assets.
*   **The Impact:** If the property universe changes, the calibrated survey weights ($\alpha_j$) will map to a different set of properties, altering the compositions of Portfolios A and B. This makes it impossible to compare simulation results across different runs of the pipeline.
*   **The Rule:** The files `property_universe.csv`, `market_indices_returns.csv`, and `property_covariance_matrix.csv` in `data/frozen/` must remain untouched. Any parameter testing or simulation extensions must be run on separate datasets to maintain the longitudinal consistency of the study.
