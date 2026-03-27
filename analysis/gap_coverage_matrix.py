from pathlib import Path
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Resolve paths
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

# Load data
df = pd.read_csv(DATA_DIR / "gap_coverage_comparison.csv")

# Columns: Gap_ID,DarkSide_Coverage_0_2,LAMPS_Coverage_0_2,TrustParadox_Coverage_0_2
gap_id_col = "Gap_ID"
approach_cols = [c for c in df.columns if c != gap_id_col]

# Pretty labels for x-axis
pretty_cols = {
    "DarkSide_Coverage_0_2": "Dark Side (2025)",
    "LAMPS_Coverage_0_2": "LAMPS (2026)",
    "TrustParadox_Coverage_0_2": "Trust Paradox"
}
col_labels = [pretty_cols.get(c, c) for c in approach_cols]

# Matrix: rows = gaps, cols = approaches
df_mat = df.set_index(gap_id_col)[approach_cols]

# Figure size scaled by number of gaps
n_gaps = df_mat.shape[0]
height = max(5, 0.5 * n_gaps)
width = 6

plt.figure(figsize=(width, height))
ax = sns.heatmap(
    df_mat,
    annot=True,
    fmt=".0f",
    cmap="YlOrRd",
    vmin=0,
    vmax=2,
    cbar_kws={"label": "Coverage score (0 = none, 2 = strong)"}
)

# Horizontal x-axis labels
ax.set_xticklabels(col_labels, rotation=0, ha="center")

ax.set_title("Gap–Defense Coverage Matrix", pad=16)
ax.set_xlabel("Approach", labelpad=10)
ax.set_ylabel("Gap (G1–G9)", labelpad=10)

plt.tight_layout()
plt.savefig(FIG_DIR / "fig10_gap_defense_matrix.png", dpi=300)

# Save matrix table for reference / LaTeX
df_mat.to_csv(FIG_DIR / "table05_gap_coverage_matrix.csv")