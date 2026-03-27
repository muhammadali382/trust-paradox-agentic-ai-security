import pandas as pd
import matplotlib.pyplot as plt

#Load the csv
df = pd.read_csv("../dataset/attack_results.csv")

#Compute counts per attack vector:
totals = df.shape[0]
vulns = {
    "Direct Prompt Injection": df["Direct_PI_Vulnerable"].sum(),
    "RAG Backdoor": df["RAG_Backdoor_Vulnerable"].sum(),
    "Inter-Agent Trust": df["Inter_Agent_Trust_Vulnerable"].sum()
}
res = {k: totals - v for k, v in vulns.items()}

#Plot Fig 01 (grouped bar: vulnerable vs resistant):
import numpy as np
labels = list(vulns.keys())
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(x - width/2, [vulns[k] for k in labels], width, label="Vulnerable")
ax.bar(x + width/2, [res[k] for k in labels], width, label="Resistant")

ax.set_ylabel("Number of Models")
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=15)
ax.set_title("LLM Vulnerability by Attack Vector")
ax.legend()
plt.tight_layout()

import os

os.makedirs("../figures", exist_ok=True)  # creates folder if it doesn't exist
plt.savefig("../figures/fig01_attack_success_rate.png", dpi=300)

plt.savefig("../figures/fig01_attack_success_rate.png", dpi=300)

#Save Table 1 as CSV for LaTeX import:
df.to_csv("../figures/table01_attack_results.csv", index=False)