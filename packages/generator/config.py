# packages/generator/config.py
"""
Calibration parameters for Heuristics in Property Portfolio Selection decisions.
This configuration is frozen and represents the pre-registered study parameters.
"""

# SEED for reproducibility
SEED = 42  # DO NOT CHANGE — frozen after first generation

# Risk-free rate based on average 364-day NTB rate (2019-2024) of 8.4%
RISK_FREE_RATE = 0.084

# PenCom regulatory limits
PENCOM_CONSTRAINTS = {
    "max_single_property_pct": 0.05,       # Max 5% of fund in single property
    "max_property_asset_class_pct": 0.30,   # Max 30% total in real estate
    "min_states": 2,                       # Must diversify across >= 2 states
    "min_commercial_lease_years": 7        # Commercial properties must have >= 7-year leases
}

# Transaction cost rates
TRANSACTION_COSTS = {
    "agency_fee_pct": 0.05,       # 5% agency fee
    "legal_fee_pct": 0.05,        # 5% legal fee
    "consent_fee_lagos_pct": 0.10, # 10% Governor's Consent in Lagos
    "consent_fee_other_pct": 0.05  # 5% Governor's Consent in other states
}

# Title risk premiums (additive to systematic index volatility)
TITLE_RISK_PREMIUMS = {
    "C of O": 0.000,
    "Gov Consent": 0.005,
    "Gazette": 0.030,
    "Excision": 0.050,
    "Deed of Assignment": 0.020
}

# Condition risk premiums (additive to systematic index volatility)
CONDITION_RISK_PREMIUMS = {
    "New": 0.000,
    "Good": 0.005,
    "Fair": 0.015,
    "Needs Renovation": 0.030
}

# Vacancy rates by asset type (from Formula 3.2 / CBRE Nigeria 2023)
VACANCY_RATES = {
    "Office": 0.05,
    "Commercial": 0.04,
    "Industrial": 0.05,
    "Residential": 0.06,
    "Mixed-Use": 0.06
}

# Maintenance rates by asset type (from Formula 3.2 / PenCom Annual Reports)
MAINTENANCE_RATES = {
    "Office": 0.10,
    "Commercial": 0.10,
    "Industrial": 0.08,
    "Residential": 0.15,
    "Mixed-Use": 0.12
}

# Gross yield distribution parameters (Asset Type -> Location Tier -> (mean, std))
GROSS_YIELD_PARAMS = {
    "Residential": {
        "Prime": (0.045, 0.005),
        "Secondary": (0.055, 0.005),
        "Emerging": (0.065, 0.008)
    },
    "Commercial": {
        "Prime": (0.075, 0.008),
        "Secondary": (0.085, 0.010),
        "Emerging": (0.095, 0.012)
    },
    "Office": {
        "Prime": (0.080, 0.008),
        "Secondary": (0.090, 0.010),
        "Emerging": (0.100, 0.012)
    },
    "Industrial": {
        "Prime": (0.085, 0.010),
        "Secondary": (0.095, 0.012),
        "Emerging": (0.105, 0.015)
    },
    "Mixed-Use": {
        "Prime": (0.060, 0.006),
        "Secondary": (0.070, 0.008),
        "Emerging": (0.080, 0.010)
    }
}

# Geographic target distribution
GEOGRAPHIC_DISTRIBUTION = {
    "Lagos Island": 0.25,      # 25% of universe
    "Lagos Mainland": 0.15,    # 15%
    "Abuja": 0.20,             # 20%
    "Rivers": 0.18,            # 18%
    "Kano": 0.12,              # 12%
    "Oyo": 0.10                # 10%
}

# Asset type target distribution
ASSET_TYPE_DISTRIBUTION = {
    "Office": 0.28,            # 28% of universe
    "Commercial": 0.22,        # 22%
    "Industrial": 0.18,        # 18%
    "Residential": 0.20,       # 20%
    "Mixed-Use": 0.12          # 12%
}

# Price tier target distribution
PRICE_TIER_DISTRIBUTION = {
    "Accessible": 0.20,        # 20% (₦150M – ₦350M)
    "Core": 0.45,              # 45% (₦350M – ₦800M)
    "Premium": 0.25,           # 25% (₦800M – ₦1.5B)
    "Trophy": 0.10             # 10% (₦1.5B – ₦3.0B)
}

# Price log-normal distributions by tier
PRICE_TIER_PARAMS = {
    "Accessible": {
        "log_mean": 19.253,    # ln(230M)
        "log_sigma": 0.2,
        "floor": 150_000_000.0,
        "ceiling": 350_000_000.0
    },
    "Core": {
        "log_mean": 20.088,    # ln(530M)
        "log_sigma": 0.25,
        "floor": 350_000_000.0,
        "ceiling": 800_000_000.0
    },
    "Premium": {
        "log_mean": 20.820,    # ln(1.1B)
        "log_sigma": 0.25,
        "floor": 800_000_000.0,
        "ceiling": 1_500_000_000.0
    },
    "Trophy": {
        "log_mean": 21.465,    # ln(2.1B)
        "log_sigma": 0.2,
        "floor": 1_500_000_000.0,
        "ceiling": 3_000_000_000.0
    }
}

# Submarkets & Micro-locations definitions
SUBMARKET_LOCATIONS = {
    "Lagos Island": {
        "state": "Lagos",
        "city": "Lagos Island",
        "lga_micro": [
            ("Eti-Osa", "Ikoyi"),
            ("Eti-Osa", "Victoria Island"),
            ("Eti-Osa", "Lekki Phase 1"),
            ("Lagos Island", "Marina")
        ]
    },
    "Lagos Mainland": {
        "state": "Lagos",
        "city": "Lagos Mainland",
        "lga_micro": [
            ("Ikeja", "Ikeja GRA"),
            ("Ikeja", "Oregun"),
            ("Apapa", "Apapa Industrial Area"),
            ("Oshodi-Isolo", "Oshodi"),
            ("Eti-Osa", "Lekki Phase 2")
        ]
    },
    "Abuja": {
        "state": "Abuja",
        "city": "Abuja",
        "lga_micro": [
            ("Municipal", "Maitama"),
            ("Municipal", "Asokoro"),
            ("Municipal", "Wuse II"),
            ("Municipal", "Garki"),
            ("Municipal", "Jabi")
        ]
    },
    "Rivers": {
        "state": "Rivers",
        "city": "Port Harcourt",
        "lga_micro": [
            ("Port Harcourt", "GRA Phase 1"),
            ("Port Harcourt", "GRA Phase 2"),
            ("Port Harcourt", "Trans-Amadi"),
            ("Obio-Akpor", "Rumuola")
        ]
    },
    "Kano": {
        "state": "Kano",
        "city": "Kano",
        "lga_micro": [
            ("Nassarawa", "Bompai"),
            ("Fagge", "Sharada"),
            ("Kano Municipal", "Kano City Centre")
        ]
    },
    "Oyo": {
        "state": "Oyo",
        "city": "Ibadan",
        "lga_micro": [
            ("Ibadan North", "Bodija"),
            ("Ibadan South-West", "Ring Road"),
            ("Ibadan North-West", "Dugbe")
        ]
    }
}

# Citation context for calibration data sources
CALIBRATION_SOURCES = """
1. Knight Frank Nigeria Prime Commercial Report (2023-2024)
2. Knight Frank Nigeria Residential Market Report (2022-2024)
3. CBRE Nigeria Office Market Report & Market Outlook (2022-2023)
4. NBS Real Estate Sector GDP Contribution Reports (2018-2024)
5. CBN Statistical Bulletins & MPR Data Series (2018-2024)
6. PenCom Annual Reports & Investment Guidelines (2020-2024)
"""
