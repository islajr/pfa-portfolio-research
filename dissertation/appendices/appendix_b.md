# APPENDIX B: PROPERTY COVARIANCE MATRIX DERIVED FROM SECONDARY MARKET REPORTS

This appendix presents the complete property covariance matrix $\boldsymbol{\Sigma} \in \mathbb{R}^{80 \times 80}$ calibrated for the 80-asset synthetic property universe, explicitly derived from secondary real estate market reports and macroeconomic data series.

The return volatilities, submarket correlation structures, and covariance terms were estimated by synthesizing historical empirical data from:
1. **Jones Lang LaSalle (JLL) Sub-Saharan Africa Real Estate Reports (2020–2025):** Prime Grade A office rent yields and capital appreciation volatility in Lagos and Abuja.
2. **Estate Intel Nigeria Property Monitors (2021–2025):** Prime residential yield growth rates and vacancy rate volatility across Victoria Island, Ikoyi, and Lekki.
3. **Broll Property Group Nigeria Market Overviews (2019–2025):** Commercial retail and office yield parameters for Abuja CBD and Maitama.
4. **Nigerian Institution of Estate Surveyors and Valuers (NIESV) Lagos State Branch Yield Guides (2018–2025):** Secondary market yields for Lagos Mainland (Ikeja, Yaba), Oyo (Ibadan), and Northern commercial hubs (Kano).
5. **Central Bank of Nigeria (CBN) Statistical Bulletins (2015–2025):** Macroeconomic inflation rates, Treasury Bill yield series, and Monetary Policy Rate (MPR) volatility.

---

## B.1 Property Covariance Heatmap

Figure B.1 visualizes the correlation and covariance structure across the 80 property holdings in the universe, reflecting spatial clustering and asset-class linkages.

![Figure B.1: Property Covariance Matrix Heatmap Derived from Market Reports](../../outputs/charts/covariance_heatmap.png)

**Figure B.1: Property Covariance Matrix Heatmap Derived from Market Reports**  
*Source: Secondary Market Data Reports & Author's Calibration, 2026*

---

## B.2 Inter-Submarket Baseline Correlation and Covariance Matrix

Table B.1 details the baseline return correlation coefficients ($\rho$) and annual covariance values ($\sigma_{ik}$) across the major regional property submarket blocks derived from secondary market reports.

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

## B.3 Pairwise Numerical Covariance Sub-Matrix for Selected Portfolio Holdings

Table B.2 presents the numerical annual pairwise covariance values ($\times 10^{-4}$) among the 15 key holdings selected across Portfolio A (Heuristic) and Portfolio B (MVO).

**Table B.2: Numerical Pairwise Covariance Matrix for Key Portfolio Holdings ($\times 10^{-4}$)**

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

*Source: Secondary Market Data Reports & Author's Computation, 2026*
