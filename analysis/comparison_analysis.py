import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load LAMPS dataset
df = pd.read_csv('../dataset/lamps_accuracy_results.csv')

# --- Chart: LAMPS vs Baseline Accuracy ---
x = np.arange(len(df['Dataset']))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width/2, df['Accuracy'] * 100, width,
               label='LAMPS (Proposed)', color='#1f77b4')
bars2 = ax.bar(x + width/2, df['Baseline_Accuracy'] * 100, width,
               label='Baseline (Single Agent)', color='#aec7e8')

# Labels
ax.set_xlabel('Dataset', fontsize=12)
ax.set_ylabel('Accuracy (%)', fontsize=12)
ax.set_title('LAMPS Multi-Agent Defense vs Baseline Accuracy\n(Zeshan et al., 2026)', fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(['D1 (Balanced)', 'D2 (Imbalanced)'], fontsize=11)
ax.set_ylim(80, 102)
ax.legend(fontsize=11)

# Add value labels on bars
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'{bar.get_height():.1f}%', ha='center', fontweight='bold', fontsize=11)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'{bar.get_height():.1f}%', ha='center', fontsize=11)

plt.tight_layout()
plt.savefig('../figures/fig4_defense_comparison.png', dpi=300)
plt.show()
print("Fig 4 saved.")
