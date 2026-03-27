from pathlib import Path
import textwrap

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

# Paths
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

# Load + sort
df = pd.read_csv(DATA_DIR / "scenario_mapping.csv")
df = df.sort_values(["Scenario_ID", "Step_Number"])

steps_data = [
    (int(r.Step_Number), r.Step_Label, r.TrustParadox_Layer)
    for r in df.itertuples(index=False)
]

n         = len(steps_data)
box_w     = 4.2
box_h     = 3.0
h_gap     = 1.6
fig_w     = n * (box_w + h_gap) - h_gap + 2.4

step_colors = ["#4E79A7", "#F28E2B", "#59A14F", "#E15759"]

fig, ax = plt.subplots(figsize=(fig_w, 6.5))
fig.patch.set_facecolor("#F7F7F7")

for i, (step_num, label, layer) in enumerate(steps_data):
    x     = i * (box_w + h_gap)
    y     = 0.0
    color = step_colors[i % len(step_colors)]

    # Rounded box
    rect = FancyBboxPatch(
        (x, y), box_w, box_h,
        boxstyle="round,pad=0.10",
        linewidth=2.0,
        edgecolor="white",
        facecolor=color,
        zorder=2,
    )
    ax.add_patch(rect)

    # STEP badge
    ax.text(x + box_w / 2, y + box_h - 0.28,
            f"STEP {step_num}",
            ha="center", va="center",
            fontsize=14, fontweight="bold", color="white", zorder=3)

    # Divider
    ax.plot([x + 0.3, x + box_w - 0.3],
            [y + box_h - 0.56, y + box_h - 0.56],
            color="white", linewidth=1.0, alpha=0.5, zorder=3)

    # Main label
    ax.text(x + box_w / 2, y + box_h * 0.54,
            textwrap.fill(label, width=16),
            ha="center", va="center",
            fontsize=18, fontweight="bold", color="white",
            multialignment="center", zorder=3, linespacing=1.4)

    # Layer tag
    layer_clean = " ".join(layer.split("_")[1:])
    ax.text(x + box_w / 2, y + 0.30,
            textwrap.fill(layer_clean, width=20),
            ha="center", va="center",
            fontsize=12, color="white", alpha=0.92,
            multialignment="center", zorder=3, linespacing=1.3)

    # Arrow to next
    if i < n - 1:
        x_next = (i + 1) * (box_w + h_gap)
        ax.add_patch(FancyArrowPatch(
            (x + box_w + 0.08, y + box_h / 2),
            (x_next - 0.08, y + box_h / 2),
            arrowstyle="-|>",
            mutation_scale=22,
            linewidth=2.0,
            color="#444444",
            zorder=4,
        ))

ax.set_xlim(-0.6, n * (box_w + h_gap) - h_gap + 0.6)
ax.set_ylim(-0.9, box_h + 1.2)
ax.axis("off")

ax.set_title(
    "Fig 08  ·  EchoLeak / SaaS‑700 Attack Chain  →  Trust Paradox Layer Mapping",
    fontsize=13, fontweight="bold", pad=22, loc="center", color="#222222"
)

ax.text(
    (n * (box_w + h_gap) - h_gap) / 2, -0.68,
    "Sources: EchoLeak_2025  ·  SaaS_700_Breach_2025",
    ha="center", va="center", fontsize=9, color="#666666"
)

plt.tight_layout()
plt.savefig(FIG_DIR / "fig08_scenario_attack_chain.png", dpi=300, bbox_inches="tight")