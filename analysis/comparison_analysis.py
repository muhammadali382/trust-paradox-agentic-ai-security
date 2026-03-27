from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT     = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR  = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

# ── Load CSVs ─────────────────────────────────────────────────────
p1 = pd.read_csv(DATA_DIR / "paper1_metrics.csv")
p2 = pd.read_csv(DATA_DIR / "paper2_metrics.csv")

# ── Paper 1: percent metrics only ────────────────────────────────
p1_pct = p1[p1["Unit"] == "percent"].copy()
p1_labels = [n.replace("_", "\n") for n in p1_pct["Metric_Name"]]
p1_vals   = p1_pct["Value"].tolist()
p1_colors = ["#4E79A7", "#F28E2B", "#59A14F", "#E15759"]

# ── Paper 2: split percent vs count ──────────────────────────────
p2_pct = p2[p2["Unit"] == "percent"].copy()
p2_cnt = p2[p2["Unit"] == "count"].copy()

p2_labels = [n.replace("_", "\n") for n in p2["Metric_Name"]]
p2_vals   = p2["Value"].tolist()
p2_units  = p2["Unit"].tolist()
p2_colors = ["#BCBD22", "#8C564B", "#2CA02C", "#D62728", "#1F77B4", "#9467BD", "#17BECF"]

# ── Figure ────────────────────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.patch.set_facecolor("#FAFAFA")
fig.subplots_adjust(top=0.84, bottom=0.14, left=0.07, right=0.96, wspace=0.45)

# Panel A — Paper 1
x1 = np.arange(len(p1_labels))
bars1 = ax1.bar(x1, p1_vals, color=p1_colors[:len(p1_vals)], width=0.55,
                edgecolor="white", linewidth=1.4)
for bar, v in zip(bars1, p1_vals):
    ax1.text(bar.get_x() + bar.get_width() / 2, v + 1.2,
             f"{v:.1f}%", ha="center", va="bottom",
             fontsize=11, fontweight="bold", color="#222222")
ax1.set_xticks(x1)
ax1.set_xticklabels(p1_labels, fontsize=10)
ax1.set_ylim(0, 118)
ax1.set_ylabel("Vulnerability Rate (%)", fontsize=11)
ax1.set_title("Paper 1 · Dark Side of LLMs\n(Lupinacci et al. 2025)",
              fontsize=12, fontweight="bold", pad=12)
ax1.yaxis.grid(True, linestyle="dotted", alpha=0.55)
ax1.set_axisbelow(True)
ax1.spines[["top", "right"]].set_visible(False)

# Panel B — Paper 2
x2    = np.arange(len(p2_labels))
ax2r  = ax2.twinx()
cnt_i = [i for i, u in enumerate(p2_units) if u == "count"]
pct_i = [i for i, u in enumerate(p2_units) if u == "percent"]

for i in cnt_i:
    ax2.bar(x2[i], p2_vals[i], color=p2_colors[i], width=0.55,
            edgecolor="white", linewidth=1.4)
    ax2.text(x2[i], p2_vals[i] + 2.5, f"{int(p2_vals[i])}",
             ha="center", va="bottom", fontsize=11, fontweight="bold", color="#222222")

for i in pct_i:
    ax2r.bar(x2[i], p2_vals[i], color=p2_colors[i], width=0.55,
             edgecolor="white", linewidth=1.4, hatch="///", alpha=0.85)
    ax2r.text(x2[i], p2_vals[i] + 0.4, f"{p2_vals[i]:.1f}%",
              ha="center", va="bottom", fontsize=11, fontweight="bold", color="#222222")

ax2.set_xticks(x2)
ax2.set_xticklabels(p2_labels, fontsize=10)
ax2.set_ylim(0, 200)
ax2.set_ylabel("Count", fontsize=11)
ax2r.set_ylim(0, 28)
ax2r.set_ylabel("Rate (%)", fontsize=11, color="#9467BD")
ax2r.tick_params(axis="y", labelcolor="#9467BD")
ax2.set_title("Paper 2 · Agentic AI Security Survey\n(Solid = Count  ·  Hatched = Rate %)",
              fontsize=12, fontweight="bold", pad=12)
ax2.yaxis.grid(True, linestyle="dotted", alpha=0.55)
ax2.set_axisbelow(True)
ax2.spines[["top"]].set_visible(False)

fig.suptitle(
    "Fig 03  ·  Comparative Metrics: Dark Side of LLMs vs Agentic AI Security Survey",
    fontsize=13, fontweight="bold"
)

plt.savefig(FIG_DIR / "fig03_comparison_metrics.png", dpi=300, bbox_inches="tight")

# ── Save table ────────────────────────────────────────────────────
combined = pd.concat([
    p1.assign(Paper="Lupinacci_et_al_2025"),
    p2.assign(Paper="Agentic_AI_Survey")
], ignore_index=True)
combined.to_csv(FIG_DIR / "table03_comparison_metrics.csv", index=False)
print("Fig 03 and Table 03 saved.")