# analysis/cloud_deployment.py  –  Fig 12 Trust Paradox Cloud Deployment Model
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import matplotlib.patheffects as pe

ROOT    = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)

fig, ax = plt.subplots(figsize=(26, 13))
fig.patch.set_facecolor("#F0F4F8")
ax.set_xlim(0, 26); ax.set_ylim(0, 13); ax.axis("off")

C_EXT="#C0392B"; C_L1="#1A5276"; C_L2="#1E8449"; C_L3="#6C3483"
C_AG="#BA4A00";  C_TL="#1F618D"; C_CL="#0E6655"
C_PASS="#27AE60"; C_BLK="#E74C3C"; C_ARW="#1C2833"
ZCOL={"ext":C_EXT,"l1":C_L1,"l2":C_L2,"l3":C_L3,"ag":C_AG,"tl":C_TL,"cl":C_CL}

ZY1=1.4; ZY2=12.1; ZH=ZY2-ZY1
RY1=1.65; RY2=11.50; BH=1.00; N=5
GAP=(RY2-RY1-N*BH)/(N-1)
row_y=[RY2-BH-i*(BH+GAP) for i in range(N)]
row_cy=[y+BH/2 for y in row_y]
ZX={"ext":0.20,"l1":3.30,"l2":5.55,"l3":7.80,"ag":10.05,"tl":14.30,"cl":18.30}
ZW={"ext":3.00,"l1":2.15,"l2":2.15,"l3":2.15,"ag":4.10,"tl":3.80,"cl":7.50}

def zone_bg(key,lines):
    x,w,c=ZX[key],ZW[key],ZCOL[key]
    ax.add_patch(FancyBboxPatch((x,ZY1),w,ZH,boxstyle="round,pad=0.08",
        lw=2.2,edgecolor=c,facecolor=c,alpha=0.08,zorder=1))
    ax.text(x+w/2,(ZY2+RY2)/2+0.05,"\n".join(lines),ha="center",va="center",
            fontsize=12.5,color=c,fontweight="bold",zorder=2,linespacing=1.3)

def cbox(x,y,w,h,col,lines,alpha=0.93):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.10",
        lw=1.8,edgecolor="white",facecolor=col,alpha=alpha,zorder=3))
    if not lines: return
    if len(lines)==1:
        ax.text(x+w/2,y+h/2,lines[0],ha="center",va="center",
                fontsize=14,fontweight="bold",color="white",zorder=4)
    else:
        th=h*0.42
        ax.text(x+w/2,y+h-th/2-0.04,lines[0],ha="center",va="center",
                fontsize=13.5,fontweight="bold",color="white",zorder=4)
        sh=(h-th-0.10)/max(len(lines)-1,1)
        for j,s in enumerate(lines[1:]):
            ax.text(x+w/2,y+h-th-0.10-sh*(j+0.55),s,ha="center",va="center",
                    fontsize=12.3,color="white",alpha=0.90,zorder=4)

def layer_box(key,title,subs):
    cbox(ZX[key]+0.10,RY1,ZW[key]-0.20,RY2-RY1,ZCOL[key],[title]+subs,alpha=0.95)

def rbox(key,row,lines,wf=1.0,xo=0.0,col=None):
    cbox(ZX[key]+0.12+xo,row_y[row],(ZW[key]-0.24)*wf,BH,col or ZCOL[key],lines)

def harrow(x1,x2,y,col=C_ARW,lw=2.1):
    ax.annotate("",xy=(x2,y),xytext=(x1,y),
        arrowprops=dict(arrowstyle="-|>",color=col,lw=lw,mutation_scale=17),zorder=6)

def varrow(x,y1,y2,col=C_ARW,lw=1.9):
    ax.annotate("",xy=(x,y2),xytext=(x,y1),
        arrowprops=dict(arrowstyle="-|>",color=col,lw=lw,mutation_scale=15),zorder=6)

def mark(x,y,blocked=False):
    sym,col=("✗",C_BLK) if blocked else ("✓",C_PASS)
    ax.text(x,y,sym,ha="center",va="center",fontsize=19,color=col,fontweight="bold",
            zorder=7,path_effects=[pe.withStroke(linewidth=2,foreground="white")])

for key,lns in [("ext",["EXTERNAL","ZONE"]),("l1",["LAYER 1","Input Guard"]),
                ("l2",["LAYER 2","Exec Proxy"]),("l3",["LAYER 3","Trust Ctrl"]),
                ("ag",["AGENT ZONE"]),("tl",["TOOL ZONE"]),("cl",["CLOUD INFRA"])]:
    zone_bg(key,lns)

ax.text(13,12.65,"Fig 12  ·  Trust Paradox Cloud Deployment Model",
        ha="center",fontsize=20,fontweight="bold",color="#1A1A2E")

layer_box("l1","L1 – Input Guard",
    ["► Injection detection","► Prompt partitioning",
     "► Context labeling","► Allowlist enforce","► Input sanitization"])
layer_box("l2","L2 – Exec Proxy",
    ["► Tool scope enforce","► Sandboxed execution",
     "► Token revocation","► Action logging","► Kill-switch"])
layer_box("l3","L3 – Trust Ctrl",
    ["► Crypto agent ID","► Trust-level tokens",
     "► Message signing","► Boundary enforce","► Priv. prev."])

EXT=[(0,["Enterprise User","Web / API client"],"pass_agent"),
     (1,["Attacker","Crafted prompts / emails"],"block_L1"),
     (2,["RAG Documents","3rd-party / unverified"],"block_L2"),
     (3,["Peer Agent Msg","Inter-agent channel"],"block_L3"),
     (4,["External APIs","Webhooks / SaaS feeds"],"pass_tools")]
for row,lines,_ in EXT: rbox("ext",row,lines)

IW=(ZW["ag"]-0.24)/2-0.05
rbox("ag",0,["Orchestrator Agent","LangGraph / ReAct"])
rbox("ag",1,["Specialist A","Agent A"],wf=0.5,xo=0.0,col="#C0562C")
rbox("ag",1,["Specialist B","Agent B"],wf=0.5,xo=IW+0.10,col="#C0562C")
rbox("ag",2,["LAMPS Multi-Agent","Detection Layer"])

for r,l in enumerate(["Terminal / Bash","RAG Knowledge Base",
                       "Internal APIs","Monitoring / SIEM"]): rbox("tl",r,[l])
for r,l in enumerate(["SaaS Applications","Cloud Storage / S3",
                       "Identity Provider","External Services"]): rbox("cl",r,[l])

EX_R=ZX["ext"]+ZW["ext"]
L1L=ZX["l1"]; L1R=ZX["l1"]+ZW["l1"]; L1C=ZX["l1"]+ZW["l1"]/2
L2L=ZX["l2"]; L2R=ZX["l2"]+ZW["l2"]; L2C=ZX["l2"]+ZW["l2"]/2
L3L=ZX["l3"]; L3R=ZX["l3"]+ZW["l3"]; L3C=ZX["l3"]+ZW["l3"]/2
AGL=ZX["ag"]; AGR=ZX["ag"]+ZW["ag"]
TLL=ZX["tl"]; TLR=ZX["tl"]+ZW["tl"]; CLL=ZX["cl"]

for row,_,flow in EXT:
    cy=row_cy[row]; harrow(EX_R,L1L,cy)
    if   flow=="block_L1": mark(L1C,cy,blocked=True)
    elif flow=="block_L2":
        mark(L1C,cy); harrow(L1R,L2L,cy,col=C_PASS); mark(L2C,cy,blocked=True)
    elif flow=="block_L3":
        mark(L1C,cy); harrow(L1R,L2L,cy,col=C_PASS)
        mark(L2C,cy); harrow(L2R,L3L,cy,col=C_PASS); mark(L3C,cy,blocked=True)
    elif flow=="pass_agent":
        mark(L1C,cy); harrow(L1R,L2L,cy,col=C_PASS)
        mark(L2C,cy); harrow(L2R,L3L,cy,col=C_PASS)
        mark(L3C,cy); harrow(L3R,AGL,cy,col=C_PASS)
    elif flow=="pass_tools":
        mark(L1C,cy); harrow(L1R,L2L,cy,col=C_PASS)
        mark(L2C,cy); harrow(L2R,L3L,cy,col=C_PASS)

ag_cx=ZX["ag"]+ZW["ag"]/2
varrow(ag_cx-0.8,row_y[0],row_y[1]+BH); varrow(ag_cx+0.8,row_y[0],row_y[1]+BH)
varrow(ag_cx,row_y[0],row_y[2]+BH)
for r in range(4): harrow(AGR,TLL,row_cy[r])
for r in range(4): harrow(TLR,CLL,row_cy[r])

items=[(C_EXT,"External Threat"),(C_L1,"L1 Input Guard"),(C_L2,"L2 Exec Proxy"),
       (C_L3,"L3 Trust Ctrl"),(C_AG,"Agent Zone"),(C_TL,"Tool Zone"),
       (C_CL,"Cloud Infra"),(C_PASS,"Allowed ✓"),(C_BLK,"Blocked ✗")]
lx=0.5
for col,lbl in items:
    ax.add_patch(mpatches.Rectangle((lx,0.50),0.32,0.35,
                 facecolor=col,edgecolor="white",lw=0.8,zorder=3))
    ax.text(lx+0.44,0.68,lbl,fontsize=13,va="center",color="#1C2833")
    lx+=2.75

plt.subplots_adjust(left=0,right=1,top=1,bottom=0)
plt.savefig(FIG_DIR/"fig12_cloud_deployment_model.png",dpi=300,bbox_inches="tight",
            facecolor=fig.get_facecolor())
print("Fig 12 saved.")