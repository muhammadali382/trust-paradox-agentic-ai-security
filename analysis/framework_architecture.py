from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT    = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(14, 11))
fig.patch.set_facecolor("#F4F6F9")
ax.set_xlim(0, 14)
ax.set_ylim(0, 11)
ax.axis("off")

C_THREAT = "#C0392B"
C_L1     = "#2471A3"
C_L2     = "#1E8449"
C_L3     = "#7D3C98"
C_AGENT  = "#D35400"
C_ARROW  = "#2C3E50"
C_BLOCK  = "#E74C3C"

def rounded_box(ax, x, y, w, h, color, label, sublabels=None,
                fontsize=11, alpha=0.92):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                 boxstyle="round,pad=0.12", linewidth=1.8,
                 edgecolor="white", facecolor=color, alpha=alpha, zorder=2))
    ty = y + h - 0.34 if sublabels else y + h / 2
    ax.text(x + w/2, ty, label, ha="center", va="center",
            fontsize=fontsize, fontweight="bold", color="white", zorder=3)
    if sublabels:
        step = (h - 0.55) / len(sublabels)
        for i, s in enumerate(sublabels):
            ax.text(x + w/2, y + h - 0.65 - i*step, f"▸  {s}",
                    ha="center", va="center", fontsize=9,
                    color="white", alpha=0.93, zorder=3)

def arrow(ax, x1, y1, x2, y2, color=C_ARROW, lw=2.0, label=""):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color,
                                lw=lw, mutation_scale=16), zorder=4)
    if label:
        ax.text((x1+x2)/2+0.15, (y1+y2)/2, label,
                fontsize=8, color=color, ha="left", va="center", zorder=5)

ax.text(7, 10.65,
        "Fig 03  ·  Trust Paradox Defense Framework Architecture",
        ha="center", fontsize=14, fontweight="bold", color="#1A1A2E")

for (x, y, w, h, lbl) in [
    (0.6,  9.5, 2.4, 0.7, "User / Attacker\nInput"),
    (4.3,  9.5, 2.4, 0.7, "Poisoned RAG\nDocuments"),
    (8.0,  9.5, 2.4, 0.7, "Peer Agent\nMessages"),
    (11.2, 9.5, 2.2, 0.7, "External\nAPI Data"),
]:
    rounded_box(ax, x, y, w, h, C_THREAT, lbl, fontsize=8.5, alpha=0.88)

for cx in [1.8, 5.5, 9.2, 12.3]:
    arrow(ax, cx, 9.5, cx, 8.78, color=C_BLOCK, lw=1.8)

rounded_box(ax, 0.4, 7.5, 13.2, 1.2, C_L1,
    "L1 – Input Guard  (Prompt & Context Governance)",
    sublabels=[
        "Prompt injection detection  |  Context labeling & partitioning",
        "Allowlist enforcement  |  Malicious instruction filtering  |  Input sanitization",
    ])

arrow(ax, 7, 7.5, 7, 6.72, label=" Sanitized input")

rounded_box(ax, 0.4, 5.5, 13.2, 1.15, C_L2,
    "L2 – Execution Proxy  (Tool & API Governance)",
    sublabels=[
        "Tool scope enforcement  |  Least-privilege token management  |  Sandboxed execution",
        "Cross-SaaS anomaly detection  |  Action logging  |  Rate limiting & kill-switch",
    ])

arrow(ax, 7, 5.5, 7, 4.72, label=" Governed actions")

rounded_box(ax, 0.4, 3.5, 13.2, 1.15, C_L3,
    "L3 – Trust Control  (Identity & Inter-Agent Trust Governance)",
    sublabels=[
        "Cryptographic agent identity  |  Trust-level tokens (User / Orchestrator / Specialist / Data)",
        "Inter-agent message signing  |  Privilege escalation prevention  |  Trust boundary enforcement",
    ])

arrow(ax, 7, 3.5, 7, 2.72, label=" Verified request")

rounded_box(ax, 1.2, 1.5, 5.0, 1.1, C_AGENT,
    "LLM Agent (Reasoning Core)",
    sublabels=["ReAct / LangGraph / LangChain"])

rounded_box(ax, 7.8, 1.5, 5.0, 1.1, "#555555",
    "Tools & Environment",
    sublabels=["Terminal  |  APIs  |  RAG  |  SaaS"])

arrow(ax, 6.2, 2.05, 7.8, 2.05, lw=1.6, label=" tool calls")

for i, (c, txt) in enumerate([
    (C_L1,    "L1 covers: G3, G4, G7, G9"),
    (C_L2,    "L2 covers: G1, G3, G5, G6, G9"),
    (C_L3,    "L3 covers: G3, G6, G7, G8"),
    (C_THREAT,"Blocked vectors: Direct PI · RAG Backdoor · Inter-Agent Trust"),
]):
    ax.add_patch(mpatches.Rectangle(
        (0.5, 0.92 - i*0.24), 0.22, 0.16,
        facecolor=c, edgecolor="none", zorder=3))
    ax.text(0.82, 1.0 - i*0.24, txt,
            fontsize=8, va="center", color="#222222")

plt.tight_layout()
plt.savefig(FIG_DIR / "fig03_framework_architecture.png", dpi=300, bbox_inches="tight")
print("Fig 03 saved.")