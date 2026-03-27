import os
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV (path is from analysis/ folder)
df = pd.read_csv("../dataset/incidents_timeline.csv")

# We have Year and Incident_Index, so just use those directly
# If there are multiple rows per year, aggregate (mean) the index
year_index = (
    df.groupby("Year")["Incident_Index"]
      .mean()
      .reset_index()
      .rename(columns={"Incident_Index": "IncidentIndex"})
)

# Plot Fig 05 – Incident Timeline (using the index as y-axis)
plt.figure(figsize=(6, 4))
plt.plot(year_index["Year"], year_index["IncidentIndex"], marker="o")
plt.xlabel("Year")
plt.ylabel("Incident Index (relative)")
plt.title("AI/Agent Security Incident Index Over Time")
plt.grid(True)
plt.tight_layout()

# Ensure figures directory exists
os.makedirs("../figures", exist_ok=True)

# Save figure
plt.savefig("../figures/fig05_incidents_timeline.png", dpi=300)

# Save the aggregated table for use in Table 4
year_index.to_csv("../figures/table04_incidents_by_year.csv", index=False)