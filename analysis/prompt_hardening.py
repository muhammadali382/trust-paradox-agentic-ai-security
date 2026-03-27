# analysis/prompt_hardening.py  –  Fig 14 Prompt Hardening Flow
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT    = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(32, 16))
fig.patch.set_facecolor("#F0F4F8")
ax.set_xlim(0, 32); ax.set_ylim(0, 16); ax.axis("off")

C_INPUT="#C0392B"; C_GATE="#D35400"; C_PROC="#1A5276"
C_OUT="#1E8449";   C_LLM="#6C3483";  C_BLOCK="#922B21"
C_LOG="#2C3E50";   C_PASS="#27AE60"; C_ARW="#2C3E50"

def box(x,y,w,h,color,lines,ft=14,fs=12,alpha=0.94):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.22",
        lw=2.8,edgecolor="white",facecolor=color,alpha=alpha,zorder=3))
    lines=[lines] if isinstance(lines,str) else lines
    if len(lines)==1:
        ax.text(x+w/2,y+h/2,lines[0],ha="center",va="center",
                fontsize=ft+4,fontweight="bold",color="white",zorder=4)
    else:
        th=h*0.36
        ax.text(x+w/2,y+h-th/2-0.07,lines[0],ha="center",va="center",
                fontsize=ft+4,fontweight="bold",color="white",zorder=4)
        sh=(h-th-0.22)/max(len(lines)-1,1)
        for i,s in enumerate(lines[1:]):
            ax.text(x+w/2,y+h-th-0.22-sh*(i+0.52),s,
                    ha="center",va="center",fontsize=fs+4,
                    color="white",alpha=0.95,zorder=4)

def harrow(x1,x2,y,col=C_ARW,lw=3.0,lbl="",lbl_col=None):
    lbl_col=lbl_col or col
    ax.annotate("",xy=(x2,y),xytext=(x1,y),
        arrowprops=dict(arrowstyle="-|>",color=col,lw=lw,mutation_scale=24),zorder=6)
    if lbl:
        ax.text((x1+x2)/2,y+0.28,lbl,ha="center",va="bottom",
                fontsize=15.5,fontweight="bold",color=lbl_col,zorder=7)

def varrow(x,y1,y2,col=C_ARW,lw=2.6,lbl=""):
    ax.annotate("",xy=(x,y2),xytext=(x,y1),
        arrowprops=dict(arrowstyle="-|>",color=col,lw=lw,mutation_scale=20),zorder=6)
    if lbl:
        ax.text(x+0.26,(y1+y2)/2,lbl,ha="left",va="center",
                fontsize=15.5,fontweight="bold",color=col,rotation=90,zorder=7)

ax.text(16,15.60,"Fig 14  ·  Prompt Hardening Flow",
        ha="center",fontsize=28,fontweight="bold",color="#1A1A2E")
ax.text(16,15.08,
    "Layer 1 (Input Guard)  ·  5-stage hardening pipeline: "
    "raw input  →  injection detection  →  partitioning  →  context labeling  "
    "→  allowlist  →  sanitization  →  hardened prompt  →  LLM agent",
    ha="center",fontsize=16,color="#4A5568",style="italic")

BW=3.40; BH=5.40; BY=6.20; CY=BY+BH/2
GAP=0.52
sx=[0.30+i*(BW+GAP) for i in range(7)]
sx.append(sx[6]+BW+GAP)
LLM_W=3.00

box(sx[0],BY,BW,BH,C_INPUT,["RAW INPUT\nSOURCES","① Enterprise User","② Attacker Prompt","③ RAG Documents","④ Peer Agent Msg","⑤ External API Feed"],ft=14,fs=12)
box(sx[1],BY,BW,BH,C_GATE, ["L1-A  INJECTION\nDETECTION","Regex & pattern match","ML classifier (BERT)","Role-separator detect","Ignore-prior detect","▶  PASS  /  BLOCK"],ft=14,fs=12)
box(sx[2],BY,BW,BH,C_PROC, ["L1-B  PROMPT\nPARTITIONING","Split system/user/data","Fence with <<< >>> delim","Isolate RAG context","Tag each segment origin","Build structured zones"],ft=14,fs=12)
box(sx[3],BY,BW,BH,C_PROC, ["L1-C  CONTEXT\nLABELING","Trust levels  0 – 3","user    →  UNTRUSTED","system  →  TRUSTED","RAG     →  EXTERNAL","peer    →  VERIFIED"],ft=14,fs=12)
box(sx[4],BY,BW,BH,C_GATE, ["L1-D  ALLOWLIST\nENFORCEMENT","Block disallowed cmds","Permit safe tool calls","Regex blocklist check","Keyword deny-list scan","▶  PASS  /  BLOCK"],ft=14,fs=12)
box(sx[5],BY,BW,BH,C_PROC, ["L1-E  INPUT\nSANITIZATION","Escape special chars","Strip hidden Unicode","Normalize whitespace","Truncate to max tokens","Strip HTML / markdown"],ft=14,fs=12)
box(sx[6],BY,BW,BH,C_OUT,  ["HARDENED\nPROMPT  ✓","Injection-free input","Trust-labelled zones","Partitioned segments","Safe tool references","Validated & bounded"],ft=14,fs=12)
box(sx[7],BY,LLM_W,BH,C_LLM,["LLM\nAGENT","Receives hardened","prompt only","Executes in L2","Exec Proxy env.","→  Next: Layer 2"],ft=14,fs=12)

harrow(sx[0]+BW,sx[1],CY,col=C_ARW,  lbl="raw input")
harrow(sx[1]+BW,sx[2],CY,col=C_PASS, lbl="PASS ✓",  lbl_col=C_PASS)
harrow(sx[2]+BW,sx[3],CY,col=C_PASS, lbl="partitioned")
harrow(sx[3]+BW,sx[4],CY,col=C_PASS, lbl="labeled")
harrow(sx[4]+BW,sx[5],CY,col=C_PASS, lbl="PASS ✓",  lbl_col=C_PASS)
harrow(sx[5]+BW,sx[6],CY,col=C_PASS, lbl="sanitized")
harrow(sx[6]+BW,sx[7],CY,col=C_OUT,  lbl="✓ hardened",lbl_col=C_OUT)

for si,lbl in [(1,"GATE 1 — Injection Check"),(4,"GATE 2 — Allowlist Check")]:
    ax.add_patch(FancyBboxPatch((sx[si]+0.50,BY+BH+0.14),BW-1.00,0.62,
        boxstyle="round,pad=0.09",lw=0,facecolor=C_GATE,alpha=0.88,zorder=5))
    ax.text(sx[si]+BW/2,BY+BH+0.45,lbl,ha="center",va="center",
            fontsize=15.5,fontweight="bold",color="white",zorder=6)

BLK_BOT=2.10; BLK_H=2.40
for si,lbl in [(1,"Injection Detected"),(4,"Disallowed Pattern")]:
    bx=sx[si]+BW/2
    varrow(bx,BY,BLK_BOT+BLK_H,col=C_BLOCK,lw=2.8,lbl="BLOCK ✗")
    box(bx-1.70,BLK_BOT,3.40,BLK_H,C_BLOCK,
        [lbl,"→  Request dropped","→  Logged to SIEM","→  Alert triggered"],ft=16.5,fs=15.5)

box(10.00,0.30,12.00,1.65,C_LOG,
    ["SECURITY LOG  /  SIEM ALERT",
     "All BLOCK events  ·  Timestamp  ·  Matched pattern  ·  Source IP  ·  Severity level  ·  Action taken"],
    ft=17,fs=15.5)
for si in [1,4]:
    ax.annotate("",xy=(16.00,1.95),xytext=(sx[si]+BW/2,BLK_BOT),
        arrowprops=dict(arrowstyle="-|>",color=C_BLOCK,lw=2.0,
                        connectionstyle="arc3,rad=0.18",mutation_scale=16),zorder=6)

bx1=sx[1]; bx2=sx[5]+BW; bmy=BY+BH+1.00
ax.plot([bx1,bx1,bx2,bx2],[bmy-0.20,bmy,bmy,bmy-0.20],color=C_PROC,lw=2.6,zorder=2)
ax.text((bx1+bx2)/2,bmy+0.18,
    "◀  ─  ─  ─  LAYER 1  ·  INPUT GUARD  ·  5 Hardening Stages  ─  ─  ─  ▶",
    ha="center",va="bottom",fontsize=18,fontweight="bold",color=C_PROC)

stage_meta=[("INPUT",C_INPUT,BW),("GATE 1",C_GATE,BW),("STAGE 2",C_PROC,BW),
            ("STAGE 3",C_PROC,BW),("GATE 2",C_GATE,BW),("STAGE 5",C_PROC,BW),
            ("OUTPUT",C_OUT,BW),("AGENT",C_LLM,LLM_W)]
for i,(lbl,col,w) in enumerate(stage_meta):
    ax.add_patch(FancyBboxPatch((sx[i]+0.46,BY-0.80),w-0.92,0.62,
        boxstyle="round,pad=0.06",lw=0,facecolor=col,alpha=0.90,zorder=3))
    ax.text(sx[i]+w/2,BY-0.49,lbl,ha="center",va="center",
            fontsize=15.5,fontweight="bold",color="white",zorder=4)

ax.text(16,0.10,
    "Source: Trust Paradox Framework — Layer 1 (Input Guard)  |  "
    "Lupinacci et al. (2025)  |  BERT reference: Devlin et al. (2019)",
    ha="center",fontsize=14.5,color="#4A5568",style="italic")

plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
plt.savefig(FIG_DIR/"fig14_prompt_hardening_flow.png",dpi=300,
            bbox_inches="tight",facecolor=fig.get_facecolor())
print("Fig 14 saved.")