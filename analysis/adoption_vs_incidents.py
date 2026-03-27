from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Resolve paths
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "dataset"
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

# Load adoption stats
adopt_df = pd.read_csv(DATA_DIR / "adoption_stats.csv")

# Load incident index by year
inc_df = pd.read_csv(FIG_DIR / "table04_incidents_by_year.csv")

# Columns we expect from adoption_stats.csv
year_col = "Year"
use_col = "Percent_Orgs_Using_Agentic_AI"
ctrl_col = "Percent_Orgs_With_Agentic_AI_Security_Controls"

# Merge directly on Year to avoid _x/_y columns
merged = pd.merge(adopt_df, inc_df, on=year_col, how="inner")

# DEBUG: show what columns actually exist
print("Merged columns:", merged.columns.tolist())

# Normalize any IncidentIndex-like column to 'IncidentIndex'
incident_col = None
for c in merged.columns:
    if "IncidentIndex" in c:
        incident_col = c
        break

if incident_col is None:
    raise ValueError(f"No IncidentIndex column found after merge; columns are {merged.columns.tolist()}")

if incident_col != "IncidentIndex":
    merged = merged.rename(columns={incident_col: "IncidentIndex"})

# Sort by year
merged = merged.sort_values(year_col)

# Plot
fig, ax1 = plt.subplots(figsize=(7, 4))

color_use = "tab:blue"
color_ctrl = "tab:green"
color_inc = "tab:red"

years = merged[year_col]

# Left y-axis: adoption and controls
ax1.set_xlabel("Year")
ax1.set_ylabel("Adoption / Controls (%)", color=color_use)

# Convert years to a numeric array for slight offsets
years_num = years.astype(float)

ax1.plot(years_num - 0.05, merged[use_col],
         marker="o", color=color_use, label="Using Agentic AI")
ax1.plot(years_num + 0.05, merged[ctrl_col],
         marker="s", color=color_ctrl, label="With Security Controls")
ax1.tick_params(axis="y", labelcolor=color_use)

# Right y-axis: incident index (no offset needed)
ax2 = ax1.twinx()
ax2.set_ylabel("Incident Index (relative)", color=color_inc)
ax2.plot(years_num, merged["IncidentIndex"],
         marker="^", linestyle="--", color=color_inc, label="Incident Index")
ax2.tick_params(axis="y", labelcolor=color_inc)
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

plt.title("Agentic AI Adoption, Security Controls, and Incident Burden Over Time")
plt.tight_layout()
plt.savefig(FIG_DIR / "fig07_adoption_vs_incidents.png", dpi=300)

merged.to_csv(FIG_DIR / "table04_adoption_vs_incidents.csv", index=False)