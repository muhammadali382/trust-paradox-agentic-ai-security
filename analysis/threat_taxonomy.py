# analysis/threat_taxonomy.py  –  Fig 13 Agentic AI Threat Taxonomy
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT    = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(25, 13))
fig.patch.set_facecolor("#EAECEE")
ax.set_xlim(0, 25); ax.set_ylim(0, 13); ax.axis("off")

C_ROOT="#1A252F"; C_SA="#1A5276"; C_MA="#6C3483"
C_DIR="#C0392B";  C_IND="#D35400"; C_LEAF="#1E6655"

def box(x,y,w,h,color,lines,ft=11,fs=9.5,alpha=0.94):
    ax.add_patch(FancyBboxPatch((x,y),w,h,
        boxstyle="round,pad=0.14",lw=2.2,
        edgecolor="white",facecolor=color,alpha=alpha,zorder=3))
    if not lines: return
    lines=[lines] if isinstance(lines,str) else lines
    if len(lines)==1:
        ax.text(x+w/2,y+h/2,lines[0],ha="center",va="center",
                fontsize=ft,fontweight="bold",color="white",zorder=4)
    else:
        th=h*0.42
        ax.text(x+w/2,y+h-th/2-0.04,lines[0],ha="center",va="center",
                fontsize=ft,fontweight="bold",color="white",zorder=4)
        sh=(h-th-0.10)/max(len(lines)-1,1)
        for i,s in enumerate(lines[1:]):
            ax.text(x+w/2,y+h-th-0.10-sh*(i+0.52),s,
                    ha="center",va="center",fontsize=fs,
                    color="white",alpha=0.93,zorder=4)

def connector(x1,y1,x2,y2,col,lw=2.2):
    mid=(y1+y2)/2
    ax.plot([x1,x1,x2],[y1,mid,mid],color=col,lw=lw,
            solid_capstyle="round",solid_joinstyle="round",zorder=2)
    ax.annotate("",xy=(x2,y2),xytext=(x2,mid+0.01),
        arrowprops=dict(arrowstyle="-|>",color=col,lw=lw,mutation_scale=15),zorder=3)

# ── TITLE ─────────────────────────────────────────────────────────
ax.text(12.5,12.62,"Fig 13  ·  Agentic AI Threat Taxonomy",
        ha="center",fontsize=19,fontweight="bold",color="#1A1A2E")
ax.text(12.5,12.18,
    "9 attack vectors across Single-Agent & Multi-Agent architectures  "
    "→  Trust Paradox Framework layers  (Lupinacci et al., 2025)",
    ha="center",fontsize=10.5,color="#4A5568",style="italic")

# ── LEAF GRID ─────────────────────────────────────────────────────
LW=2.20
lx=[0.30,2.80,5.60,8.10,11.30,13.80,16.60,19.10,21.60]
LY_TOP=8.10; LY_BOT=4.80; LH=LY_TOP-LY_BOT

# ── LEVEL-2 ───────────────────────────────────────────────────────
L2Y,L2H=8.82,0.70
sa_dir=dict(x=0.30, w=4.70,col=C_DIR,lbl="Direct Attack")
sa_ind=dict(x=5.60, w=4.70,col=C_IND,lbl="Indirect Attack")
ma_dir=dict(x=11.30,w=4.70,col=C_DIR,lbl="Direct Attack")
ma_ind=dict(x=16.60,w=7.20,col=C_IND,lbl="Indirect Attack")
for d in [sa_dir,sa_ind,ma_dir,ma_ind]:
    box(d["x"],L2Y,d["w"],L2H,d["col"],d["lbl"],ft=12.5)

# ── LEVEL-1 ───────────────────────────────────────────────────────
L1Y,L1H=10.02,0.82
sa=dict(x=0.30, w=10.0,col=C_SA,lbl=["Single-Agent System","1 LLM + tool chain"])
ma=dict(x=11.30,w=12.5,col=C_MA,lbl=["Multi-Agent System","Orchestrator + Specialist agents"])
for d in [sa,ma]:
    box(d["x"],L1Y,d["w"],L1H,d["col"],d["lbl"],ft=13.5,fs=10.5)

# ── ROOT ──────────────────────────────────────────────────────────
ROOT_CX=12.40; ROOT_W=8.6; ROOT_X=ROOT_CX-ROOT_W/2
box(ROOT_X,11.22,ROOT_W,0.84,C_ROOT,
    ["Agentic AI Threat Taxonomy",
     "Paper 1  ·  18 LLMs × 3 primary attack vectors"],
    ft=14.5,fs=10.5,alpha=0.97)

# ── CONNECTORS ────────────────────────────────────────────────────
connector(ROOT_CX,11.22, sa["x"]+sa["w"]/2, L1Y+L1H, C_SA,lw=2.5)
connector(ROOT_CX,11.22, ma["x"]+ma["w"]/2, L1Y+L1H, C_MA,lw=2.5)
connector(sa["x"]+sa["w"]/2,L1Y,sa_dir["x"]+sa_dir["w"]/2,L2Y+L2H,C_DIR,lw=2.0)
connector(sa["x"]+sa["w"]/2,L1Y,sa_ind["x"]+sa_ind["w"]/2,L2Y+L2H,C_IND,lw=2.0)
connector(ma["x"]+ma["w"]/2,L1Y,ma_dir["x"]+ma_dir["w"]/2,L2Y+L2H,C_DIR,lw=2.0)
connector(ma["x"]+ma["w"]/2,L1Y,ma_ind["x"]+ma_ind["w"]/2,L2Y+L2H,C_IND,lw=2.0)

# ── LEAF NODES ────────────────────────────────────────────────────
leaf_defs=[
    (0,sa_dir,["DPI","Direct Prompt Injection","94.4%  (17/18 LLMs)","Explicit malicious cmd","No document needed","▶ Blocked: L1 ✓"]),
    (1,sa_dir,["SPO","System Prompt Override","Jailbreak via user turn","Ignores safety rules","Overrides sys context","▶ Blocked: L1 ✓"]),
    (2,sa_ind,["RBA","RAG Backdoor Attack","83.3%  (15/18 LLMs)","Hidden in vector store","No direct user craft","▶ Blocked: L1+L2 ✓"]),
    (3,sa_ind,["TOP","Tool Output Poisoning","Malicious API response","Injected post-execution","Evades input filters","▶ Blocked: L2 ✓"]),
    (4,ma_dir,["IAI","Interface Agent Injection","Targets entry-point agent","Cascades to all agents","Multi-hop propagation","▶ Blocked: L1 ✓"]),
    (5,ma_dir,["PE","Privilege Escalation","Claims higher trust rank","Bypasses role limits","Horizontal escalation","▶ Blocked: L3 ✓"]),
    (6,ma_ind,["IATE","Inter-Agent Trust Exploit.","100%  (18/18 LLMs)","Peer agent as vector","Exploits agent trust","▶ Blocked: L3 ✓"]),
    (7,ma_ind,["RAGP","RAG Poisoning (Propagated)","Cross-agent cascade","No user interaction","Entire system at risk","▶ Blocked: L1+L2 ✓"]),
    (8,ma_ind,["OC","Orchestrator Compromise","Hijacks all sub-agents","Highest blast radius","Full lateral movement","▶ Blocked: L2+L3 ✓"]),
]
for (li,parent,lines) in leaf_defs:
    x=lx[li]
    box(x,LY_BOT,LW,LH,C_LEAF,lines[1:],ft=10.5,fs=9.5)
    ax.add_patch(FancyBboxPatch((x,LY_TOP-0.48),LW,0.48,
        boxstyle="round,pad=0.06",lw=0,
        edgecolor="none",facecolor=C_LEAF,alpha=1.0,zorder=5))
    ax.text(x+LW/2,LY_TOP-0.24,lines[0],ha="center",va="center",
            fontsize=12,fontweight="bold",color="white",zorder=6)
    connector(parent["x"]+parent["w"]/2,L2Y,
              x+LW/2,LY_TOP,parent["col"],lw=1.9)

# ── DIVIDER ───────────────────────────────────────────────────────
ax.plot([0.25,24.75],[4.55,4.55],color="#ABB2B9",lw=1.6,
        linestyle=(0,(6,4)),zorder=2)
ax.text(0.3,4.40,"▼  Key Vulnerability Metrics — Paper 1 Benchmark",
        fontsize=10.5,color="#566573",fontweight="bold",va="top")

# ── STATS BAR ─────────────────────────────────────────────────────
stats=[
    (C_DIR,"Direct Prompt Injection (DPI)",
     "17 / 18 models exploited in benchmark","94.4%"),
    (C_IND,"RAG Backdoor Attack (RBA)",
     "15 / 18 models exploited in benchmark","83.3%"),
    (C_MA, "Inter-Agent Trust Exploitation (IATE)",
     "18 / 18 models exploited — highest severity","100.0%"),
]
SW=7.70; SH=2.95
for i,(col,name,detail,pct) in enumerate(stats):
    sx=0.35+i*(SW+0.20)
    ax.add_patch(FancyBboxPatch((sx,0.85),SW,SH,
        boxstyle="round,pad=0.16",lw=2.2,
        edgecolor="white",facecolor=col,alpha=0.91,zorder=3))
    ax.text(sx+SW/2,3.43,pct,ha="center",va="center",
            fontsize=28,fontweight="bold",color="white",zorder=4)
    ax.text(sx+SW/2,2.70,name,ha="center",va="center",
            fontsize=11.5,fontweight="bold",color="white",zorder=4)
    ax.text(sx+SW/2,2.18,detail,ha="center",va="center",
            fontsize=9.5,color="white",alpha=0.92,zorder=4)
    pval=float(pct.replace("%",""))/100
    ax.add_patch(FancyBboxPatch((sx+0.28,1.08),SW-0.56,0.56,
        boxstyle="round,pad=0.06",lw=1.5,
        edgecolor="white",facecolor="white",alpha=0.18,zorder=4))
    ax.add_patch(FancyBboxPatch((sx+0.28,1.08),(SW-0.56)*pval,0.56,
        boxstyle="round,pad=0.06",lw=0,
        edgecolor="none",facecolor="white",alpha=0.35,zorder=5))

ax.text(12.5,0.52,
    "Source: Lupinacci et al. (2025)  ·  Paper 1 — Multi-LLM Agentic Security Benchmark  "
    "|  L1 = Input Guard  ·  L2 = Exec Proxy  ·  L3 = Trust Ctrl",
    ha="center",fontsize=9,color="#4A5568",style="italic")

plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
plt.savefig(FIG_DIR/"fig13_threat_taxonomy.png",dpi=300,
            bbox_inches="tight",facecolor=fig.get_facecolor())
print("Fig 13 saved.")