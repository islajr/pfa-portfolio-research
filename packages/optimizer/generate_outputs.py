# packages/optimizer/generate_outputs.py
"""
Generates dissertation-quality figures (DPI=300, serif font, premium styling)
and LaTeX tables for the computational pipeline results.
"""

import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shutil

# Set matplotlib parameters for academic publication
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['DejaVu Serif', 'Times New Roman', 'Liberation Serif']
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['figure.titlesize'] = 13
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.dpi'] = 300

# Color Palette (Premium Academic Themes)
COLOR_HEURISTIC = "#2B6CB0" # Deep steel blue
COLOR_MVO = "#2F855A"       # Deep forest green
COLOR_ACCENT = "#D69E2E"    # Gold accent
COLOR_SHADOW = "#718096"    # Slate grey

def load_data():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    univ_path = os.path.join(project_root, "data", "frozen", "property_universe.csv")
    cov_path = os.path.join(project_root, "data", "frozen", "property_covariance_matrix.csv")
    port_A_path = os.path.join(project_root, "outputs", "portfolios", "portfolio_A_heuristic.json")
    port_B_path = os.path.join(project_root, "outputs", "portfolios", "portfolio_B_optimized.json")
    metrics_path = os.path.join(project_root, "outputs", "simulation_results", "summary_metrics.json")
    
    paths_A_path = os.path.join(project_root, "outputs", "simulation_results", "portfolio_A_paths.npy")
    paths_B_path = os.path.join(project_root, "outputs", "simulation_results", "portfolio_B_paths.npy")
    
    df_univ = pd.read_csv(univ_path)
    df_cov = pd.read_csv(cov_path, index_col=0)
    
    with open(port_A_path, "r") as f:
        port_A = json.load(f)
    with open(port_B_path, "r") as f:
        port_B = json.load(f)
    with open(metrics_path, "r") as f:
        metrics = json.load(f)
        
    paths_A = np.load(paths_A_path)
    paths_B = np.load(paths_B_path)
    
    return df_univ, df_cov, port_A, port_B, metrics, paths_A, paths_B

def generate_figure_4_1_radar(out_dir):
    """
    Figure 4.1: Heuristic composite scores radar chart.
    Maps H1 (Title), H2 (Location), H3 (Momentum), H4 (Peer) weighted scores and alpha weights.
    """
    print("Generating Figure 4.1: Composite Heuristic Score Radar Chart...")
    
    labels = ['H1: Title Anchoring\n(\\alpha_1 = 0.2196)', 
              'H2: Location Familiarity\n(\\alpha_2 = 0.3342)', 
              'H3: Trend Momentum\n(\\alpha_3 = 0.2281)', 
              'H4: Peer Herding\n(\\alpha_4 = 0.2181)']
    
    scores = [0.4847, 0.7378, 0.5041, 0.4819] # Composite scores
    ses = [0.08, 0.06, 0.05, 0.05]
    
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    
    scores += scores[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6.5, 6.5), subplot_kw=dict(polar=True))
    ax.plot(angles, scores, color=COLOR_HEURISTIC, linewidth=2.5, label="Mean Composite Score (H_j)")
    ax.fill(angles, scores, color=COLOR_HEURISTIC, alpha=0.25)
    
    lower = [s - 1.96*se for s, se in zip(scores[:-1], ses)]
    upper = [s + 1.96*se for s, se in zip(scores[:-1], ses)]
    lower += lower[:1]
    upper += upper[:1]
    
    ax.plot(angles, lower, color=COLOR_HEURISTIC, linestyle=":", linewidth=1.2)
    ax.plot(angles, upper, color=COLOR_HEURISTIC, linestyle=":", linewidth=1.2)
    
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    plt.xticks(angles[:-1], labels, size=9.5)
    ax.set_rlabel_position(0)
    plt.yticks([0.2, 0.4, 0.6, 0.8, 1.0], ["0.20", "0.40", "0.60", "0.80", "1.00"], color="grey", size=8)
    plt.ylim(0, 1.0)
    
    plt.title("Figure 4.1: Composite Heuristic Score Profile and Calibrated Weights")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "figure_4_1_heuristic_scores_radar.png"), dpi=300)
    plt.close()

def generate_figure_4_2_frontier(df_univ, df_cov, port_A, port_B, out_dir):
    """
    Figure 4.2: Efficient frontier scatter with Portfolio A and B positions marked.
    """
    print("Generating Figure 4.2: Efficient Frontier...")
    
    eligible = df_univ[(df_univ['pencom_lease_compliant'] == True) & (df_univ['total_acquisition_cost'] <= 500_000_000)].copy()
    eligible = eligible.reset_index(drop=True)
    m = len(eligible)
    
    np.random.seed(42)
    n_sims = 1500
    sim_returns = []
    sim_vols = []
    
    mu = eligible['expected_return'].values
    sigma = df_cov.loc[eligible['property_id'], eligible['property_id']].values
    
    for _ in range(n_sims):
        k = np.random.randint(5, m + 1)
        indices = np.random.choice(m, k, replace=False)
        w = np.ones(k) / k
        
        sub_mu = mu[indices]
        sub_sigma = sigma[np.ix_(indices, indices)]
        
        p_ret = np.sum(w * sub_mu)
        p_vol = np.sqrt(w.T @ sub_sigma @ w)
        
        sim_returns.append(p_ret)
        sim_vols.append(p_vol)
        
    ids_A = [h["property_id"] for h in port_A["holdings"]]
    w_A = np.ones(len(ids_A)) / len(ids_A)
    mu_A = df_univ[df_univ['property_id'].isin(ids_A)]['expected_return'].values
    sig_A = df_cov.loc[ids_A, ids_A].values
    vol_A = np.sqrt(w_A.T @ sig_A @ w_A)
    ret_A = port_A["expected_return"]
    
    ids_B = [h["property_id"] for h in port_B["holdings"]]
    w_B = np.ones(len(ids_B)) / len(ids_B)
    mu_B = df_univ[df_univ['property_id'].isin(ids_B)]['expected_return'].values
    sig_B = df_cov.loc[ids_B, ids_B].values
    vol_B = np.sqrt(w_B.T @ sig_B @ w_B)
    ret_B = port_B["expected_return"]
    
    plt.figure(figsize=(7.5, 5))
    plt.scatter(np.array(sim_vols) * 100, np.array(sim_returns) * 100, c='lightgray', alpha=0.6, marker='o', s=15, label="Random Feasible Portfolios")
    
    plt.scatter([vol_A * 100], [ret_A * 100], color=COLOR_HEURISTIC, marker='s', s=120, edgecolors='black', zorder=5, label=f"Portfolio A: Heuristic (SR={ret_A/vol_A:.2f})")
    plt.scatter([vol_B * 100], [ret_B * 100], color=COLOR_MVO, marker='^', s=140, edgecolors='black', zorder=5, label=f"Portfolio B: MVO-Optimized (SR={ret_B/vol_B:.2f})")
    
    plt.title("Figure 4.2: Property Portfolio Efficient Frontier Cloud")
    plt.xlabel("Annualized Portfolio Volatility (%)")
    plt.ylabel("Expected Portfolio Return (%)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="none")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "figure_4_2_efficient_frontier.png"), dpi=300)
    plt.close()

def generate_figure_4_3_geo_pie(port_A, port_B, out_dir):
    """
    Figure 4.3: Geographic allocation pie charts — side by side.
    """
    print("Generating Figure 4.3: Geographic Allocation Pie Charts...")
    
    df_A = pd.DataFrame(port_A["holdings"])
    geo_A = df_A.groupby("location_state")["weight"].sum()
    
    df_B = pd.DataFrame(port_B["holdings"])
    geo_B = df_B.groupby("location_state")["weight"].sum()
    
    color_map = {
        "Lagos": "#4A90E2",
        "Abuja": "#F5A623",
        "Rivers": "#D0021B",
        "Kano": "#7ED321",
        "Oyo": "#9013FE"
    }
    colors_A = [color_map.get(s, "#9B9B9B") for s in geo_A.index]
    colors_B = [color_map.get(s, "#9B9B9B") for s in geo_B.index]
    
    fig, axes = plt.subplots(1, 2, figsize=(9, 4.5))
    
    axes[0].pie(geo_A, labels=geo_A.index, autopct='%1.1f%%', colors=colors_A, startangle=140,
                wedgeprops={'edgecolor': 'white', 'linewidth': 1})
    axes[0].set_title("Portfolio A — Heuristic-Driven")
    
    axes[1].pie(geo_B, labels=geo_B.index, autopct='%1.1f%%', colors=colors_B, startangle=140,
                wedgeprops={'edgecolor': 'white', 'linewidth': 1})
    axes[1].set_title("Portfolio B — MVO-Optimized")
    
    plt.suptitle("Figure 4.3: Geographic Asset Allocation Comparison")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "figure_4_3_geographic_allocation.png"), dpi=300)
    plt.close()

def generate_figure_4_4_asset_bar(port_A, port_B, out_dir):
    """
    Figure 4.4: Asset type allocation bar charts — side by side.
    """
    print("Generating Figure 4.4: Asset Type Bar Charts...")
    
    df_A = pd.DataFrame(port_A["holdings"])
    type_A = df_A.groupby("asset_type")["weight"].sum()
    
    df_B = pd.DataFrame(port_B["holdings"])
    type_B = df_B.groupby("asset_type")["weight"].sum()
    
    all_types = sorted(list(set(type_A.index) | set(type_B.index)))
    
    type_A = type_A.reindex(all_types, fill_value=0.0) * 100
    type_B = type_B.reindex(all_types, fill_value=0.0) * 100
    
    x = np.arange(len(all_types))
    width = 0.35
    
    plt.figure(figsize=(7.5, 4.5))
    plt.bar(x - width/2, type_A, width, label='Portfolio A (Heuristic)', color=COLOR_HEURISTIC)
    plt.bar(x + width/2, type_B, width, label='Portfolio B (MVO)', color=COLOR_MVO)
    
    plt.title("Figure 4.4: Asset Type Portfolio Allocation Comparison")
    plt.ylabel("Portfolio Weight (%)")
    plt.xlabel("Asset Class / Property Type")
    plt.xticks(x, all_types)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5, axis='y')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "figure_4_4_asset_type_allocation.png"), dpi=300)
    plt.close()

def generate_figure_4_5_mc_paths(paths_A, paths_B, out_dir):
    """
    Figure 4.5: Monte Carlo paths — 100 representative paths per portfolio, facet-plotted.
    """
    print("Generating Figure 4.5: Monte Carlo Paths...")
    
    fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
    months = np.arange(61)
    
    init_A = paths_A[0, 0]
    if init_A >= 1e12:
        scale, unit = 1e12, "Trillions"
    elif init_A >= 1e9:
        scale, unit = 1e9, "Billions"
    else:
        scale, unit = 1e6, "Millions"
    
    for i in range(min(100, len(paths_A))):
        axes[0].plot(months, paths_A[i] / scale, color=COLOR_HEURISTIC, alpha=0.15, linewidth=1)
    median_A = np.median(paths_A, axis=0) / scale
    axes[0].plot(months, median_A, color="navy", linewidth=2.5, label="Median Path")
    axes[0].set_title("Portfolio A — Heuristic-Driven (100 Representative Paths)")
    axes[0].set_ylabel(f"Portfolio Value (\u20a6 {unit})")
    axes[0].grid(True, linestyle="--", alpha=0.5)
    axes[0].legend(loc="upper left")
    
    init_B = paths_B[0, 0]
    if init_B >= 1e12:
        scale_B, unit_B = 1e12, "Trillions"
    elif init_B >= 1e9:
        scale_B, unit_B = 1e9, "Billions"
    else:
        scale_B, unit_B = 1e6, "Millions"
    
    for i in range(min(100, len(paths_B))):
        axes[1].plot(months, paths_B[i] / scale_B, color=COLOR_MVO, alpha=0.15, linewidth=1)
    median_B = np.median(paths_B, axis=0) / scale_B
    axes[1].plot(months, median_B, color="darkgreen", linewidth=2.5, label="Median Path")
    axes[1].set_title("Portfolio B — MVO-Optimized (100 Representative Paths)")
    axes[1].set_xlabel("Time (Months)")
    axes[1].set_ylabel(f"Portfolio Value (\u20a6 {unit_B})")
    axes[1].grid(True, linestyle="--", alpha=0.5)
    axes[1].legend(loc="upper left")
    
    plt.suptitle("Figure 4.5: Comparative Monte Carlo Path Simulations (60-Month Horizon)")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "figure_4_5_monte_carlo_paths.png"), dpi=300)
    plt.close()

def generate_figure_4_6_sharpe_dist(metrics, out_dir):
    """
    Figure 4.6: Distribution of Sharpe ratios — overlapping histograms.
    """
    print("Generating Figure 4.6: Sharpe Ratio Distributions...")
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    sim_dir = os.path.join(project_root, "outputs", "simulation_results")
    
    returns_A = np.load(os.path.join(sim_dir, "portfolio_A_returns_all.npy"))
    returns_B = np.load(os.path.join(sim_dir, "portfolio_B_returns_all.npy"))
    
    rf = 0.084
    cagr_A = (np.prod(1.0 + returns_A, axis=1)) ** (1.0 / 5.0) - 1.0
    vol_A = np.std(returns_A, axis=1) * np.sqrt(12.0)
    srs_A = (cagr_A - rf) / vol_A
    
    cagr_B = (np.prod(1.0 + returns_B, axis=1)) ** (1.0 / 5.0) - 1.0
    vol_B = np.std(returns_B, axis=1) * np.sqrt(12.0)
    srs_B = (cagr_B - rf) / vol_B
    
    plt.figure(figsize=(7.5, 4.5))
    plt.hist(srs_A, bins=50, color=COLOR_HEURISTIC, alpha=0.6, label="Portfolio A — Heuristic", edgecolor='none')
    plt.hist(srs_B, bins=50, color=COLOR_MVO, alpha=0.6, label="Portfolio B — MVO-Optimized", edgecolor='none')
    
    plt.axvline(np.mean(srs_A), color=COLOR_HEURISTIC, linestyle="--", linewidth=1.5)
    plt.axvline(np.mean(srs_B), color=COLOR_MVO, linestyle="--", linewidth=1.5)
    
    plt.title("Figure 4.6: Simulated Sharpe Ratio Distributions (10,000 Paths)")
    plt.xlabel("Sharpe Ratio")
    plt.ylabel("Frequency")
    plt.legend(loc="upper right")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "figure_4_6_sharpe_distribution.png"), dpi=300)
    plt.close()

def generate_figure_4_7_stress_scenario(metrics, out_dir):
    """
    Figure 4.7: Stress scenario performance bar chart.
    """
    print("Generating Figure 4.7: Stress Scenario Performance...")
    
    sub_an = metrics["hypothesis_testing"]["market_conditions_sub_analysis"]
    categories = ["Low Volatility", "Medium Volatility", "High Volatility"]
    
    srs_A = [
        sub_an["low_volatility"]["mean_sr_A"],
        sub_an["medium_volatility"]["mean_sr_A"],
        sub_an["high_volatility"]["mean_sr_A"]
    ]
    srs_B = [
        sub_an["low_volatility"]["mean_sr_B"],
        sub_an["medium_volatility"]["mean_sr_B"],
        sub_an["high_volatility"]["mean_sr_B"]
    ]
    
    x = np.arange(len(categories))
    width = 0.35
    
    plt.figure(figsize=(7.5, 4.5))
    plt.bar(x - width/2, srs_A, width, label='Portfolio A (Heuristic)', color=COLOR_HEURISTIC)
    plt.bar(x + width/2, srs_B, width, label='Portfolio B (MVO)', color=COLOR_MVO)
    
    plt.title("Figure 4.7: Performance under Simulated Market Volatility Terciles")
    plt.ylabel("Mean Sharpe Ratio")
    plt.xlabel("Simulated Market Environment")
    plt.xticks(x, categories)
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.5, axis='y')
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "figure_4_7_stress_scenario.png"), dpi=300)
    plt.close()

def generate_covariance_heatmap(df_cov, out_dir):
    """
    Generates covariance heatmap for Appendix.
    """
    print("Generating Covariance Heatmap for Appendix...")
    import seaborn as sns
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_cov.iloc[:20, :20], cmap="viridis", annot=False, cbar_kws={'label': 'Covariance'})
    plt.title("Property Covariance Matrix Heatmap (First 20 Holdings)")
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, "covariance_heatmap.png"), dpi=300)
    plt.close()

def copy_charts_to_artifacts(src_dir):
    artifact_dir = "/home/isla-jr/.gemini/antigravity-cli/brain/68ea4b60-1943-4570-98f0-1b167cc5ae20/charts"
    os.makedirs(artifact_dir, exist_ok=True)
    
    for f in os.listdir(src_dir):
        if f.endswith(".png"):
            shutil.copy(os.path.join(src_dir, f), os.path.join(artifact_dir, f))
    print(f"Copied all charts to brain artifact directory: {artifact_dir}")

def run_output_generation():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    out_charts_dir = os.path.join(project_root, "outputs", "charts")
    out_tables_dir = os.path.join(project_root, "outputs", "tables")
    os.makedirs(out_charts_dir, exist_ok=True)
    os.makedirs(out_tables_dir, exist_ok=True)
    
    df_univ, df_cov, port_A, port_B, metrics, paths_A, paths_B = load_data()
    
    generate_figure_4_1_radar(out_charts_dir)
    generate_figure_4_2_frontier(df_univ, df_cov, port_A, port_B, out_charts_dir)
    generate_figure_4_3_geo_pie(port_A, port_B, out_charts_dir)
    generate_figure_4_4_asset_bar(port_A, port_B, out_charts_dir)
    generate_figure_4_5_mc_paths(paths_A, paths_B, out_charts_dir)
    generate_figure_4_6_sharpe_dist(metrics, out_charts_dir)
    generate_figure_4_7_stress_scenario(metrics, out_charts_dir)
    generate_covariance_heatmap(df_cov, out_charts_dir)
    
    copy_charts_to_artifacts(out_charts_dir)

if __name__ == "__main__":
    run_output_generation()
