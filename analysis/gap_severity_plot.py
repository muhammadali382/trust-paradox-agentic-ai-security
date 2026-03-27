from pathlib import Path
import os

import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_DIR / "gap_severity.csv")

print("Columns in gap_severity.csv:", df.columns.tolist())

# Adjust if needed; expected: Gap_ID,Gap_Name,Severity_Score_0_1,Reason
gap_id_col = "Gap_ID"
gap_name_col = "Gap_Name"
sev_col = "Severity_Score_0_1"

# Sort by severity descending
df_sorted = df.sort_values(sev_col, ascending=True)  # horizontal bar: lowest at bottom

plt.figure(figsize=(7, 4))
plt.barh(df_sorted[gap_id_col] + " " + df_sorted[gap_name_col],
         df_sorted[sev_col])
plt.xlabel("Severity (0–1)")
plt.title("Gap Severity Ranking (G1–G9)")
plt.xlim(0, 1.05)
plt.tight_layout()
plt.savefig(FIG_DIR / "fig09_gap_severity_ranking.png", dpi=300)

# Save sorted table for later use (Table 5)
df_sorted.to_csv(FIG_DIR / "table05_gap_severity.csv", index=False)