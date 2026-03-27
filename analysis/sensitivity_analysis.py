from pathlib import Path
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "sensitivity_results.csv")

# We have: Attack_Type, Prompt_Combo, ASR, FSR, MIR
print("Columns in sensitivity_results.csv:", df.columns.tolist())

attack_col = "Attack_Type"
cp_col = "Prompt_Combo"
asr_col = "ASR"

# Pivot to Attack_Type x Prompt_Combo matrix of ASR
pivot = df.pivot_table(
    index=attack_col,
    columns=cp_col,
    values=asr_col
)

plt.figure(figsize=(6, 4))
sns.heatmap(pivot, annot=True, fmt=".2f", cmap="Reds")
plt.title("ASR by Prompt Combination and Attack Type")
plt.xlabel("Prompt Combo")
plt.ylabel("Attack Type")
plt.tight_layout()
plt.savefig(FIG_DIR / "fig02_sensitivity_heatmap.png", dpi=300)

# Save full table for LaTeX (Table 2)
df.to_csv(FIG_DIR / "table02_sensitivity_results.csv", index=False)