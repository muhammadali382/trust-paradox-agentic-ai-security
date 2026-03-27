from pathlib import Path
import math

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Paths
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

# Load coverage data
df = pd.read_csv(DATA_DIR / "gap_coverage_comparison.csv")
print("Columns in gap_coverage_comparison.csv:", df.columns.tolist())

# Columns: Gap_ID,DarkSide_Coverage_0_2,LAMPS_Coverage_0_2,TrustParadox_Coverage_0_2
gap_id_col = "Gap_ID"
approach_cols = [c for c in df.columns if c != gap_id_col]

# Gap labels (G1..G9)
labels = df[gap_id_col].tolist()
num_gaps = len(labels)

# Angles for spokes
angles = np.linspace(0, 2 * math.pi, num_gaps, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

pretty_cols = {
    "DarkSide_Coverage_0_2": "Dark Side (2025)",
    "LAMPS_Coverage_0_2": "LAMPS (2026)",
    "TrustParadox_Coverage_0_2": "Trust Paradox"
}
colors = {
    "DarkSide_Coverage_0_2": "tab:red",
    "LAMPS_Coverage_0_2": "tab:blue",
    "TrustParadox_Coverage_0_2": "tab:green"
}

for col in approach_cols:
    vals = df[col].tolist()
    vals += vals[:1]
    label = pretty_cols.get(col, col)
    color = colors.get(col, None)
    ax.plot(angles, vals, linewidth=2, color=color, label=label)
    ax.fill(angles, vals, alpha=0.15, color=color)

# Spoke labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=9)

# Radius and grid
ax.set_ylim(0, 2)
ax.set_yticks([0, 1, 2])
ax.set_yticklabels(["0", "1", "2"], fontsize=8)
ax.yaxis.grid(True, linestyle="dotted", alpha=0.6)
ax.xaxis.grid(True, linestyle="dotted", alpha=0.6)

# Centered title
ax.set_title(
    "Gap Coverage Radar: Dark Side vs LAMPS vs Trust Paradox",
    pad=14,
    fontsize=11,
    loc="left"
)

# Legend outside so it doesn’t overlap the plot
ax.legend(
    loc="lower left",
    bbox_to_anchor=(1.05, 0.0),
    fontsize=8,
    borderaxespad=0.5
)

plt.tight_layout()
plt.savefig(FIG_DIR / "fig11_gap_radar_comparison.png", dpi=300)