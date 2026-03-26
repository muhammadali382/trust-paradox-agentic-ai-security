import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv('../dataset/attack_results.csv')

# Count vulnerabilities per attack type
direct = (df['Direct_Injection'] == 'Vulnerable').sum()
rag = (df['RAG_Backdoor'] == 'Vulnerable').sum()
inter = (df['InterAgent_Trust'] == 'Vulnerable').sum()
total = len(df)

# Data for chart
attacks = ['Direct Prompt\nInjection', 'RAG Backdoor\nAttack', 'Inter-Agent\nTrust Exploitation']
vulnerable = [direct, rag, inter]
resistant = [total - direct, total - rag, total - inter]
asr = [round((v/total)*100, 1) for v in vulnerable]

x = np.arange(len(attacks))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, vulnerable, width, label='Vulnerable', color='#d62728')
bars2 = ax.bar(x + width/2, resistant, width, label='Resistant', color='#2ca02c')

# Labels
ax.set_xlabel('Attack Type', fontsize=12)
ax.set_ylabel('Number of LLMs (out of 18)', fontsize=12)
ax.set_title('Attack Success Rate Across 18 LLMs\n(Lupinacci et al., 2025)', fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(attacks, fontsize=11)
ax.set_ylim(0, 22)
ax.legend(fontsize=11)

# Add ASR % labels on top of vulnerable bars
for bar, rate in zip(bars1, asr):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
            f'{rate}%', ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('../figures/fig1_attack_success_rate.png', dpi=300)
plt.show()
print("Fig 1 saved.")
