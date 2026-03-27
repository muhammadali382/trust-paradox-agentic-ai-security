# analysis/trust_hierarchy.py  –  Fig 15 Trust Hierarchy Diagram
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT    = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(28, 15))
fig.patch.set_facecolor("#F0F4F8")
ax.set_xlim(0, 28); ax.set_ylim(0, 15); ax.axis("off")

C_L0="#922B21"; C_L1="#B7770D"; C_L2="#1A5276"; C_L3="#1E6655"
C_CTRL="#4A235A"; C_ARW="#2C3E50"
TC=[C_L0,C_L1,C_L2,C_L3]

def box(x,y,w,h,col,lines,ft=12,fs=10.8,alpha=0.93):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.18",
        lw=2.4,edgecolor="white",facecolor=col,alpha=alpha,zorder=4))
    lines=[lines] if isinstance(lines,str) else lines
    if len(lines)==1:
        ax.text(x+w/2,y+h/2,lines[0],ha="center",va="center",
                fontsize=ft+4,fontweight="bold",color="white",zorder=5)
    else:
        th=h*0.40
        ax.text(x+w/2,y+h-th/2-0.06,lines[0],ha="center",va="center",
                fontsize=ft+4,fontweight="bold",color="white",zorder=5)
        sh=(h-th-0.14)/max(len(lines)-1,1)
        for i,s in enumerate(lines[1:]):
            ax.text(x+w/2,y+h-th-0.14-sh*(i+0.52),s,
                    ha="center",va="center",fontsize=fs+4,color="white",alpha=0.95,zorder=5)

ax.text(14,14.62,"Fig 15  ·  Trust Hierarchy Diagram",
        ha="center",fontsize=26,fontweight="bold",color="#1A1A2E",zorder=10)
ax.text(14,14.14,"Layer 3 (Trust Ctrl)  ·  Trust levels 0–3: "
    "users / orchestrator / specialist agents / external data  |  Trust Paradox Framework",
    ha="center",fontsize=15.5,color="#4A5568",style="italic",zorder=10)

TH=3.00; TG=0.20
TY=[0.50+i*(TH+TG) for i in range(4)]
BADGE_X=1.60; BADGE_W=2.20
ENT_X=3.95;  ENT_R=17.80; ENT_SPAN=ENT_R-ENT_X
CAP_X=17.95; CAP_W=9.80
EGAP=0.20

tier_data=[
  (0,"LEVEL 0\nUNTRUSTED",C_L0,
   ["Attacker /\nMalicious Prompt","RAG / Unverified\nDocuments",
    "External APIs\n& Webhooks","Unverified\nPeer Messages"],
   ["Zero implicit trust — all traffic filtered by L1-A",
    "Injection detection mandatory at every entry point",
    "No direct agent or tool access permitted",
    "Blocked unless explicitly on allowlist"]),
  (1,"LEVEL 1\nVERIFIED EXTERNAL",C_L1,
   ["Enterprise User\n(Authenticated)","Auth External\nAPI","LAMPS Detection\nLayer"],
   ["Read-only prompt submission via hardened pipeline",
    "Verified tool calls only inside L2 sandbox",
    "Cannot delegate tasks to any agent directly",
    "Trust token required: T1-signed JWT"]),
  (2,"LEVEL 2\nINTERNAL AGENTS",C_L2,
   ["Specialist\nAgent A","Specialist\nAgent B","Tool Executor\nSandbox"],
   ["Scoped tool invocation — allowlisted calls only",
    "Agent-to-agent messaging via signed L3 tokens",
    "Read access to knowledge base granted",
    "Trust token: T2-signed cryptographic agent ID"]),
  (3,"LEVEL 3\nTRUSTED CORE",C_L3,
   ["Orchestrator\nAgent","System\nConfiguration"],
   ["Full tool and resource access granted",
    "Cross-agent task delegation authority",
    "System configuration management rights",
    "Trust token: T3-signed HSM certificate"]),
]

for (lvl,lbl,col,ents,caps) in tier_data:
    ty=TY[lvl]; n=len(ents)
    EW=(ENT_SPAN-(n-1)*EGAP)/n
    ax.add_patch(FancyBboxPatch((BADGE_X-0.04,ty+0.06),
        CAP_X+CAP_W-BADGE_X+0.04,TH-0.12,
        boxstyle="round,pad=0.08",lw=2.6,edgecolor=col,
        facecolor=col,alpha=0.07,zorder=2))
    if lvl>0:
        ax.plot([BADGE_X,CAP_X+CAP_W],[ty+0.02,ty+0.02],
                color=col,lw=1.4,linestyle=(0,(5,3)),alpha=0.45,zorder=3)
    ax.add_patch(FancyBboxPatch((BADGE_X,ty+0.14),BADGE_W,TH-0.28,
        boxstyle="round,pad=0.14",lw=0,facecolor=col,alpha=0.90,zorder=4))
    ax.text(BADGE_X+BADGE_W/2,ty+TH/2,lbl,ha="center",va="center",
            fontsize=16,fontweight="bold",color="white",linespacing=1.4,zorder=5)
    for j,ename in enumerate(ents):
        ex=ENT_X+j*(EW+EGAP)
        box(ex,ty+0.22,EW,TH-0.44,col,[ename],ft=12.5,fs=11)
    ax.add_patch(FancyBboxPatch((CAP_X,ty+0.12),CAP_W,TH-0.24,
        boxstyle="round,pad=0.14",lw=2.0,edgecolor=col,
        facecolor=col,alpha=0.07,zorder=3))
    ax.text(CAP_X+0.24,ty+TH-0.28,"Capabilities & Enforcement:",
            ha="left",va="top",fontsize=15,fontweight="bold",color=col,zorder=5)
    sh=(TH-0.56)/max(len(caps),1)
    for k,cap in enumerate(caps):
        ax.text(CAP_X+0.28,ty+TH-0.46-sh*(k+0.5),"▸  "+cap,
                ha="left",va="center",fontsize=14.8,color="#1C2833",zorder=5)

for lvl in range(3):
    mx=10.55; y1=TY[lvl]+TH; y2=TY[lvl+1]
    ax.annotate("",xy=(mx-0.30,y2+0.04),xytext=(mx-0.30,y1-0.04),
        arrowprops=dict(arrowstyle="-|>",color=TC[lvl+1],lw=2.0,mutation_scale=15),zorder=6)
    ax.text(mx-0.06,(y1+y2)/2,"grant",ha="left",va="center",
            fontsize=14,fontweight="bold",color=TC[lvl+1],rotation=90,zorder=7)
    ax.annotate("",xy=(mx+0.30,y1-0.04),xytext=(mx+0.30,y2+0.04),
        arrowprops=dict(arrowstyle="-|>",color=TC[lvl],lw=2.0,mutation_scale=15),zorder=6)
    ax.text(mx+0.54,(y1+y2)/2,"scope",ha="left",va="center",
            fontsize=14,fontweight="bold",color=TC[lvl],rotation=90,zorder=7)

top=TY[3]+TH; HH=0.58
box(BADGE_X,top+0.10,BADGE_W,HH,C_ARW,["TRUST\nTIER"],ft=10)
box(ENT_X,  top+0.10,ENT_SPAN,HH,C_ARW,["ENTITIES  &  COMPONENTS  BY  TRUST  LEVEL"],ft=11)
box(CAP_X,  top+0.10,CAP_W,  HH,C_CTRL,["LAYER 3 — TRUST CTRL  ·  Capabilities & Enforcement"],ft=10.5)

ax.annotate("",xy=(1.22,TY[3]+TH-0.10),xytext=(1.22,TY[0]+0.10),
    arrowprops=dict(arrowstyle="-|>",color=C_L3,lw=2.8,mutation_scale=20),zorder=7)
for lvl in range(4):
    ax.plot(1.22,TY[lvl]+TH/2,"o",ms=13,color=TC[lvl],zorder=8,
            markeredgecolor="white",markeredgewidth=2.0)
    ax.text(1.22,TY[lvl]+TH/2,str(lvl),ha="center",va="center",
            fontsize=15,fontweight="bold",color="white",zorder=9)

lx=2.50
for col,lbl in [(C_L3,"Level 3 — Trusted Core"),(C_L2,"Level 2 — Internal Agents"),
                (C_L1,"Level 1 — Verified External"),(C_L0,"Level 0 — Untrusted")]:
    ax.add_patch(FancyBboxPatch((lx,0.10),0.46,0.36,
        boxstyle="round,pad=0.05",lw=0,facecolor=col,alpha=0.90,zorder=4))
    ax.text(lx+0.60,0.28,lbl,ha="left",va="center",
            fontsize=15.5,fontweight="bold",color=col,zorder=5)
    lx+=5.70
ax.text(14,0.02,"Source: Trust Paradox Framework — Layer 3 (Trust Ctrl)  |  Lupinacci et al. (2025)",
        ha="center",fontsize=13.5,color="#4A5568",style="italic")

plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
plt.savefig(FIG_DIR/"fig15_trust_hierarchy_diagram.png",dpi=300,
            bbox_inches="tight",facecolor=fig.get_facecolor())
print("Fig 15 saved.")