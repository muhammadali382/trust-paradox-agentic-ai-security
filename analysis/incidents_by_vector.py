from pathlib import Path
import os

import pandas as pd
import matplotlib.pyplot as plt

# Resolve paths relative to repo root
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR = ROOT / "figures"

FIG_DIR.mkdir(exist_ok=True)

# Load incidents_by_vector.csv
df = pd.read_csv(DATA_DIR / "incidents_by_vector.csv")

# If your file uses slightly different column names, adjust here:
# Expected columns: Attack_Vector or Vector, Incident_Share_Percent or Percent_of_Incidents
if "Attack_Vector" in df.columns:
    vec_col = "Attack_Vector"
elif "Vector" in df.columns:
    vec_col = "Vector"
else:
    raise ValueError(f"No vector column found in {df.columns.tolist()}")

if "Incident_Share_Percent" in df.columns:
    pct_col = "Incident_Share_Percent"
elif "Percent_of_Incidents" in df.columns:
    pct_col = "Percent_of_Incidents"
else:
    raise ValueError(f"No percent column found in {df.columns.tolist()}")

# Aggregate if there are multiple sources per vector
agg = (
    df.groupby(vec_col)[pct_col]
      .mean()
      .reset_index()
      .sort_values(pct_col, ascending=False)
)

# Fig 06 – Incidents by Vector (bar chart)
plt.figure(figsize=(7, 4))
plt.bar(agg[vec_col], agg[pct_col])
plt.xticks(rotation=25, ha="right")
plt.ylabel("Share of Incidents (%)")
plt.title("AI/Agent Security Incidents by Attack Vector")
plt.tight_layout()
plt.savefig(FIG_DIR / "fig06_incidents_by_vector.png", dpi=300)

# Save the aggregated table for later LaTeX/Table 4 use
agg.to_csv(FIG_DIR / "table04_incidents_by_vector.csv", index=False)