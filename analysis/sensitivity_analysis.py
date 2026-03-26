import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('../dataset/sensitivity_results.csv')

# --- Chart 1: ASR Heatmap ---
asr_pivot = df.pivot(index='Attack_Type', columns='Prompt_Combo', values='ASR')

plt.figure(figsize=(10, 5))
sns.heatmap(asr_pivot, annot=True, fmt='.2f', cmap='Reds',
            linewidths=0.5, vmin=0, vmax=1,
            cbar_kws={'label': 'Attack Success Rate (ASR)'})
plt.title('Attack Success Rate (ASR) per Prompt Combination\n(Lupinacci et al., 2025)', fontsize=13)
plt.xlabel('Prompt Combination', fontsize=11)
plt.ylabel('Attack Type', fontsize=11)
plt.tight_layout()
plt.savefig('../figures/fig2_sensitivity_heatmap.png', dpi=300)
plt.show()
print("Fig 2 saved.")

# --- Chart 2: FSR vs ASR Comparison ---
fig, ax = plt.subplots(figsize=(10, 5))
colors = {'Direct_Injection': '#d62728',
          'RAG_Backdoor': '#ff7f0e',
          'InterAgent_Trust': '#1f77b4'}

for attack, group in df.groupby('Attack_Type'):
    ax.plot(group['Prompt_Combo'], group['ASR'],
            marker='o', label=f'{attack} - ASR',
            color=colors[attack], linewidth=2)
    ax.plot(group['Prompt_Combo'], group['FSR'],
            marker='s', linestyle='--',
            label=f'{attack} - FSR',
            color=colors[attack], linewidth=1.5, alpha=0.6)

ax.set_xlabel('Prompt Combination', fontsize=11)
ax.set_ylabel('Rate (0.0 - 1.0)', fontsize=11)
ax.set_title('ASR vs FSR per Prompt Combination by Attack Type\n(Lupinacci et al., 2025)', fontsize=13)
ax.legend(fontsize=8, loc='lower right')
ax.set_ylim(0, 1.1)
plt.tight_layout()
plt.savefig('../figures/fig2b_asr_fsr_comparison.png', dpi=300)
plt.show()
print("Fig 2b saved.")
