# packages/generator/generate_universe.py
"""
Core generator script for the property universe.
Creates a synthetic property universe of 80 properties based on Nigerian market parameters.
"""

import os
import json
import uuid
import numpy as np
import pandas as pd
import config

def generate_property_universe():
    # Set seed for numpy
    np.random.seed(config.SEED)
    
    # 1. Prepare exact counts to match pre-registered distributions
    n_properties = 80
    
    # Geographic allocation: Lagos Island (20), Lagos Mainland (12), Abuja (16), Rivers (14), Kano (10), Oyo (8)
    regions = (
        ["Lagos Island"] * 20 + 
        ["Lagos Mainland"] * 12 + 
        ["Abuja"] * 16 + 
        ["Rivers"] * 14 + 
        ["Kano"] * 10 + 
        ["Oyo"] * 8
    )
    np.random.shuffle(regions)
    
    # Price tiers allocation: Accessible (16), Core (36), Premium (20), Trophy (8)
    price_tiers = (
        ["Accessible"] * 16 + 
        ["Core"] * 36 + 
        ["Premium"] * 20 + 
        ["Trophy"] * 8
    )
    np.random.shuffle(price_tiers)
    
    # Title statuses: C of O (36), Gov Consent (20), Gazette (12), Excision (8), Deed of Assignment (4)
    titles = (
        ["C of O"] * 36 + 
        ["Gov Consent"] * 20 + 
        ["Gazette"] * 12 + 
        ["Excision"] * 8 + 
        ["Deed of Assignment"] * 4
    )
    np.random.shuffle(titles)
    
    # Conditions: New (16), Good (40), Fair (16), Needs Renovation (8)
    conditions = (
        ["New"] * 16 + 
        ["Good"] * 40 + 
        ["Fair"] * 16 + 
        ["Needs Renovation"] * 8
    )
    np.random.shuffle(conditions)
    
    # Map of asset types to allocate per region to satisfy regional biases and overall counts:
    # Office: 22, Commercial: 18, Industrial: 14, Residential: 16, Mixed-Use: 10
    regional_assets = {
        "Lagos Island": ["Office"] * 10 + ["Commercial"] * 5 + ["Residential"] * 3 + ["Mixed-Use"] * 2,
        "Lagos Mainland": ["Industrial"] * 5 + ["Residential"] * 3 + ["Commercial"] * 2 + ["Office"] * 2,
        "Abuja": ["Office"] * 6 + ["Commercial"] * 4 + ["Residential"] * 4 + ["Mixed-Use"] * 2,
        "Rivers": ["Industrial"] * 5 + ["Commercial"] * 3 + ["Residential"] * 3 + ["Office"] * 2 + ["Mixed-Use"] * 1,
        "Kano": ["Industrial"] * 4 + ["Commercial"] * 3 + ["Residential"] * 1 + ["Office"] * 1 + ["Mixed-Use"] * 1,
        "Oyo": ["Commercial"] * 1 + ["Residential"] * 2 + ["Mixed-Use"] * 4 + ["Office"] * 1
    }
    
    # Shuffle asset types within each region
    for r in regional_assets:
        np.random.shuffle(regional_assets[r])
        
    properties = []
    
    # 2. Generate properties
    for i in range(n_properties):
        prop_id = f"PROP_{i+1:02d}"
        region = regions[i]
        price_tier = price_tiers[i]
        title = titles[i]
        condition = conditions[i]
        
        # Pop asset type for region (guarantees exact overall count and correct regional distribution)
        asset_type = regional_assets[region].pop(0)
        
        # Get location specifics
        loc_data = config.SUBMARKET_LOCATIONS[region]
        state = loc_data["state"]
        city = loc_data["city"]
        
        # Choose a random LGA and Micro-location from options
        lga, micro = loc_data["lga_micro"][np.random.choice(len(loc_data["lga_micro"]))]
        
        # Sample Floor Area
        if asset_type == "Office":
            floor_area = np.random.uniform(500, 5000)
        elif asset_type == "Commercial":
            floor_area = np.random.uniform(400, 4000)
        elif asset_type == "Industrial":
            floor_area = np.random.uniform(1000, 8000)
        elif asset_type == "Residential":
            floor_area = np.random.uniform(200, 1500)
        else:  # Mixed-Use
            floor_area = np.random.uniform(300, 2500)
            
        # Round floor area to 2 decimals
        floor_area = round(floor_area, 2)
        
        # Sample Price from log-normal distribution for the assigned tier
        tier_params = config.PRICE_TIER_PARAMS[price_tier]
        log_mean = tier_params["log_mean"]
        log_sigma = tier_params["log_sigma"]
        floor = tier_params["floor"]
        ceiling = tier_params["ceiling"]
        
        # Resample if outside bounds
        asking_price = 0.0
        while True:
            asking_price = np.random.lognormal(log_mean, log_sigma)
            if floor <= asking_price <= ceiling:
                break
        asking_price = round(asking_price, 2)
        
        # Sample Gross Yield based on asset type and location tier (Prime, Secondary, Emerging)
        # Identify location tier
        if region in ["Lagos Island", "Abuja"]:
            tier = "Prime"
        elif region in ["Lagos Mainland", "Rivers"]:
            tier = "Secondary"
        else:
            tier = "Emerging"
            
        yield_params = config.GROSS_YIELD_PARAMS[asset_type][tier]
        mean_yield, std_yield = yield_params
        
        # Sample gross yield normally, clipped to [0.04, 0.14]
        gross_yield = np.clip(np.random.normal(mean_yield, std_yield), 0.04, 0.14)
        
        # Calculate gross annual rent
        estimated_annual_rent = round(asking_price * gross_yield, 2)
        
        # Sample Year Built based on condition
        current_year = 2026
        if condition == "New":
            year_built = np.random.randint(current_year - 3, current_year + 1)
        elif condition == "Good":
            year_built = np.random.randint(current_year - 10, current_year - 4)
        elif condition == "Fair":
            year_built = np.random.randint(current_year - 20, current_year - 11)
        else:  # Needs Renovation
            year_built = np.random.randint(current_year - 35, current_year - 21)
            
        # Sample Lease Term (in years)
        if asset_type in ["Office", "Commercial", "Industrial"]:
            lease_term_years = np.random.choice([3, 5, 7, 10, 12, 15])
            pencom_lease_compliant = lease_term_years >= 7
        else:
            lease_term_years = 1  # Standard short-term
            pencom_lease_compliant = True  # Always compliant for non-commercial
            
        # Map to one of the 8 market indices based on location and asset class
        # LG_OFF_ISL, LG_RET_ISL, LG_IND_MLN, LG_RES_PRM
        # AB_OFF_CEN, AB_RET_CEN
        # PH_COM_OIL
        # KN_IND_NTH
        
        # Mapping rules
        if state == "Lagos":
            if asset_type == "Office":
                market_index_id = "LG_OFF_ISL"
            elif asset_type == "Commercial":
                market_index_id = "LG_RET_ISL"
            elif asset_type == "Industrial":
                market_index_id = "LG_IND_MLN"
            else:
                market_index_id = "LG_RES_PRM"
        elif state == "Abuja":
            if asset_type == "Office":
                market_index_id = "AB_OFF_CEN"
            else:
                market_index_id = "AB_RET_CEN"
        elif state == "Rivers":
            market_index_id = "PH_COM_OIL"
        elif state == "Kano":
            market_index_id = "KN_IND_NTH"
        else:  # Oyo
            # Map Oyo state properties to Lagos indices as Southwest proxy
            if asset_type == "Office":
                market_index_id = "LG_OFF_ISL"
            elif asset_type == "Commercial":
                market_index_id = "LG_RET_ISL"
            elif asset_type == "Industrial":
                market_index_id = "LG_IND_MLN"
            else:
                market_index_id = "LG_RES_PRM"
                
        # Heuristic triggers
        is_prime_location = region in ["Lagos Island", "Abuja"]
        is_preferred_asset_type = asset_type in ["Office", "Commercial"]
        triggers_anchoring_rule = asking_price > 800_000_000.0
        
        # Heuristic eligibility: C of O or Gov Consent AND Good or New AND not anchoring trigger
        is_heuristic_eligible = (
            title in ["C of O", "Gov Consent"] and 
            condition in ["New", "Good"] and 
            not triggers_anchoring_rule
        )
        
        properties.append({
            "property_id": prop_id,
            "property_code": f"OAU-{prop_id}",
            "location_state": state,
            "location_lga": lga,
            "location_micro": micro,
            "asset_type": asset_type,
            "asking_price": asking_price,
            "estimated_annual_rent": estimated_annual_rent,
            "title_status": title,
            "property_condition": condition,
            "year_built": year_built,
            "floor_area_sqm": floor_area,
            "lease_term_years": int(lease_term_years),
            "market_index_id": market_index_id,
            "is_prime_location": bool(is_prime_location),
            "is_preferred_asset_type": bool(is_preferred_asset_type),
            "triggers_anchoring_rule": bool(triggers_anchoring_rule),
            "is_heuristic_eligible": bool(is_heuristic_eligible),
            "pencom_lease_compliant": bool(pencom_lease_compliant)
        })
        
    df = pd.DataFrame(properties)
    
    # Save config generation metadata
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    config_dir = os.path.join(project_root, "packages", "generator")
    os.makedirs(config_dir, exist_ok=True)
    
    metadata = {
        "seed": config.SEED,
        "n_properties": n_properties,
        "timestamp": pd.Timestamp.now().isoformat()
    }
    
    with open(os.path.join(config_dir, "generation_config.json"), "w") as f:
        json.dump(metadata, f, indent=2)
        
    print(f"Generated {len(df)} properties.")
    return df

if __name__ == "__main__":
    df = generate_property_universe()
    # Save temporary file for calculation step
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    temp_dir = os.path.join(project_root, "packages", "generator", "temp")
    os.makedirs(temp_dir, exist_ok=True)
    df.to_csv(os.path.join(temp_dir, "temp_raw_universe.csv"), index=False)
    print("Universe raw dataframe generated.")
