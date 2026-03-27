from pathlib import Path
import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "lamps_accuracy_results.csv")

# We have: Dataset,Type,Accuracy,Precision,Recall,F1_Score,Baseline_Accuracy
print("LAMPS accuracy rows:\n", df)

dataset_col = "Dataset"
lamps_acc_col = "Accuracy"
baseline_acc_col = "Baseline_Accuracy"

datasets = df[dataset_col].tolist()
lamps_acc = df[lamps_acc_col].tolist()
baseline_acc = df[baseline_acc_col].tolist()

x = np.arange(len(datasets))
width = 0.35

fig, ax = plt.subplots(figsize=(6, 4))

# Baseline vs LAMPS grouped bars
ax.bar(x - width/2, baseline_acc, width, label="Baseline")
ax.bar(x + width/2, lamps_acc, width, label="LAMPS")

ax.set_ylabel("Accuracy")
ax.set_xlabel("Dataset")
ax.set_xticks(x)
ax.set_xticklabels(datasets)
ax.set_ylim(0, 1.05)
ax.set_title("LAMPS vs Baseline Accuracy on D1/D2")
ax.legend()
plt.tight_layout()

plt.savefig(FIG_DIR / "fig04_lamps_vs_baseline.png", dpi=300)

# Save table for LaTeX (Table 3)
df.to_csv(FIG_DIR / "table03_lamps_metrics.csv", index=False)