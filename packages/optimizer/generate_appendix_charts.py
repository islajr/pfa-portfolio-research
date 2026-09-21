# packages/optimizer/generate_appendix_charts.py
"""
Generates dissertation-quality visual assets for Appendix B and Appendix C:
1. Annotated 15x15 Pairwise Covariance Heatmap (Appendix B)
2. 80-Property Risk-Return Scatter Plot with Asset Class Legend (Appendix C)
3. Submarket Asset Class Distribution & Valuation Breakdown (Appendix C)
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import shutil

# Matplotlib Academic Parameters
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['DejaVu Serif', 'Times New Roman', 'Liberation Serif']
plt.rcParams['font.size'] = 9.5
plt.rcParams['axes.labelsize'] = 10.5
plt.rcParams['axes.titlesize'] = 11.5
plt.rcParams['xtick.labelsize'] = 8.5
plt.rcParams['ytick.labelsize'] = 8.5
plt.rcParams['legend.fontsize'] = 8.5
plt.rcParams['figure.dpi'] = 300

# Color Palettes
PALETTE_ASSET_TYPES = {
    "Commercial Office Grade A": "#2B6CB0", # Steel blue
    "Commercial Office Grade B": "#4299E1", # Lighter blue
    "Luxury Residential": "#D69E2E",        # Gold
    "Commercial Mixed-Use": "#DD6B20",     # Terracotta
    "Commercial Retail": "#38A169",        # Forest green
    "Industrial Logistics": "#805AD5",     # Purple
    "Industrial Warehouse": "#9F7AEA"      # Lavender
}

def load_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    univ_path = os.path.join(project_root, "data", "frozen", "property_universe.csv")
    cov_path = os.path.join(project_root, "data", "frozen", "property_covariance_matrix.csv")
    
    df_univ = pd.read_csv(univ_path)
    df_cov = pd.read_csv(cov_path, index_col=0)
    return df_univ, df_cov

def generate_appendix_b_heatmap(df_cov, out_dir):
    """
    Appendix B: Annotated 15x15 Pairwise Covariance Heatmap for primary holdings.
    """
    print("Generating Appendix B Annotated Covariance Heatmap...")
    selected_ids = [
        "PROP_01", "PROP_05", "PROP_09", "PROP_10", "PROP_13",
        "PROP_21", "PROP_23", "PROP_25", "PROP_26", "PROP_29",
        "PROP_32", "PROP_44", "PROP_55", "PROP_73", "PROP_80"
    ]
    
    sub_cov = df_cov.loc[selected_ids, selected_ids] * 10000 # Convert to x10^-4 units for legibility
    
    plt.figure(figsize=(9.5, 7.5))
    ax = sns.heatmap(
        sub_cov, 
        annot=True, 
        fmt=".1f", 
        cmap="YlGnBu", 
        cbar_kws={'label': r'Covariance ($\times 10^{-4}$)'},
        linewidths=0.5,
        linecolor='white'
    )
    
    plt.title("Figure B.1: Pairwise Property Covariance Sub-Matrix ($\times 10^{-4}$)", pad=12)
    plt.xlabel("Selected Portfolio Holdings")
    plt.ylabel("Selected Portfolio Holdings")
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "appendix_b_covariance_heatmap.png"), dpi=300)
    plt.close()

def generate_appendix_c_risk_return(df_univ, out_dir):
    """
    Appendix C: 80-Property Risk-Return Profile Scatter Plot.
    """
    print("Generating Appendix C Risk-Return Scatter Plot...")
    plt.figure(figsize=(9, 5.5))
    
    for asset_type, color in PALETTE_ASSET_TYPES.items():
        subset = df_univ[df_univ['asset_type'] == asset_type]
        if not subset.empty:
            plt.scatter(
                subset['annual_volatility'] * 100, 
                subset['expected_return'] * 100, 
                c=color, 
                label=asset_type, 
                alpha=0.85, 
                s=45, 
                edgecolors='black', 
                linewidth=0.5
            )
            
    plt.axvline(x=15.0, color='grey', linestyle=':', alpha=0.7, label='Medium Volatility Threshold (15%)')
    plt.axhline(y=15.0, color='red', linestyle='--', alpha=0.7, label='Base Hurdle Rate (15%)')
    
    plt.title("Figure C.1: Risk-Return Profile Across 80 Frozen Synthetic Properties", pad=12)
    plt.xlabel("Annual Return Volatility (%)")
    plt.ylabel("Expected Annual Return (%)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="lightgrey", bbox_to_anchor=(1.01, 1))
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "appendix_c_risk_return_scatter.png"), dpi=300)
    plt.close()

def generate_appendix_c_distribution(df_univ, out_dir):
    """
    Appendix C: Submarket Asset Class Distribution Bar Chart.
    """
    print("Generating Appendix C Submarket Distribution Chart...")
    ct = pd.crosstab(df_univ['location_state'], df_univ['asset_type'])
    
    # Reindex states logically
    states_order = ["Lagos", "Abuja", "Rivers", "Oyo", "Kano"]
    ct = ct.reindex([s for s in states_order if s in ct.index])
    
    colors = [PALETTE_ASSET_TYPES.get(col, "#9B9B9B") for col in ct.columns]
    
    ax = ct.plot(kind='bar', stacked=True, figsize=(8.5, 4.8), color=colors, edgecolor='white', linewidth=0.8)
    
    plt.title("Figure C.2: Property Count Distribution by Submarket Location State", pad=12)
    plt.xlabel("Submarket Location State")
    plt.ylabel("Number of Properties ($N=80$)")
    plt.xticks(rotation=0)
    plt.legend(title="Asset Class Type", bbox_to_anchor=(1.01, 1), loc='upper left', frameon=True)
    plt.grid(True, linestyle="--", alpha=0.5, axis='y')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "appendix_c_submarket_distribution.png"), dpi=300)
    plt.close()

def copy_charts_to_artifacts(src_dir):
    artifact_dir = "/home/isla-jr/.gemini/antigravity-cli/brain/68ea4b60-1943-4570-98f0-1b167cc5ae20/charts"
    os.makedirs(artifact_dir, exist_ok=True)
    for f in os.listdir(src_dir):
        if f.startswith("appendix_"):
            shutil.copy(os.path.join(src_dir, f), os.path.join(artifact_dir, f))
    print(f"Copied appendix charts to brain artifact directory: {artifact_dir}")

def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    out_dir = os.path.join(project_root, "outputs", "charts")
    os.makedirs(out_dir, exist_ok=True)
    
    df_univ, df_cov = load_data()
    generate_appendix_b_heatmap(df_cov, out_dir)
    generate_appendix_c_risk_return(df_univ, out_dir)
    generate_appendix_c_distribution(df_univ, out_dir)
    copy_charts_to_artifacts(out_dir)

if __name__ == "__main__":
    main()
