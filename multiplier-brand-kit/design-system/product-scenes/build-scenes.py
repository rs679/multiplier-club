import json,os
ic=json.load(open('icons.json'))
FONT=os.getcwd()+'/node_modules/@fontsource-variable'
def icon(n,s=18,col='currentColor'):
    return f"<svg class=ic viewBox='0 0 32 32' width={s} height={s}>{ic[n]}</svg>"
CSS=f"""
@font-face{{font-family:'GeistV';src:url('file://{FONT}/geist/files/geist-latin-wght-normal.woff2');font-weight:100 900}}
@font-face{{font-family:'GeistMonoV';src:url('file://{FONT}/geist-mono/files/geist-mono-latin-wght-normal.woff2');font-weight:100 900}}
:root{{--ink:#0B1210;--mut:#5B6764;--sub:#8A9692;--line:#E3E8E6;--bg:#F2F4F3;--acc:#0B6E61;--teal:#2FB89C;--act:#0E6B5C;--pine:#0F1F1D}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:GeistV,system-ui;font-weight:400;color:var(--ink);-webkit-font-smoothing:antialiased;background:transparent}}
.mono{{font-family:GeistMonoV,monospace;font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--sub);font-weight:500}}
.card{{background:#fff;border:1px solid rgba(11,18,16,.07);border-radius:16px;box-shadow:0 1px 2px rgba(11,18,16,.04),0 28px 56px -16px rgba(11,18,16,.22)}}
.ic{{fill:none;stroke:currentColor;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round;flex:none}}
.ic .a{{fill:var(--acc);stroke:none}} .ic .ac{{stroke:var(--acc)}}
.chip{{display:inline-flex;align-items:center;gap:6px;font-size:12px;font-weight:500;padding:4px 9px;border-radius:8px;background:#EEF3F1;color:#3C524D;white-space:nowrap}}
.chip i{{width:6px;height:6px;border-radius:50%;background:#9AA7A4}}
.chip.g{{background:#E3F2EE;color:#0B6E61}} .chip.g i{{background:var(--teal)}}
.chip.a{{background:#FBF1DC;color:#8A5A10}} .chip.a i{{background:#E0A23A}}
.chip.d{{background:#EDEFF0;color:#55605D}}
.av{{width:30px;height:30px;border-radius:50%;background:#E7EEEB;color:#3C524D;font-size:11px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none}}
.btn{{display:inline-flex;align-items:center;gap:8px;background:var(--act);color:#fff;font-size:13px;font-weight:500;padding:9px 14px;border-radius:9px}}
.btn.o{{background:#fff;color:var(--ink);border:1px solid var(--line)}}
.bar{{height:5px;border-radius:3px;background:#E8EEEC;overflow:hidden}} .bar b{{display:block;height:100%;background:var(--teal);border-radius:3px}}
.tab{{font-size:13px;padding:7px 12px;border-radius:8px;color:var(--mut)}} .tab.on{{background:#0B1210;color:#fff}}
"""
def page(body,w,h,bg='transparent'):
    return f"<html><head><meta charset=utf-8><style>{CSS} html,body{{width:{w}px;height:{h}px;overflow:hidden;background:{bg}}}</style></head><body>{body}</body></html>"
DEALS=[
 ("Private equity","Northbridge Growth Partners III","Control and minority growth investments in mid-market business services across Europe.","USD 250,000","USD 120m","8 years","Open","g",64,"private"),
 ("Real assets","Solstice Solar Portfolio II","Operating solar assets under long-term power purchase agreements in southern Europe.","USD 100,000","USD 45m","10 years","Closing soon","a",88,"real"),
 ("Private credit","Harbourline Senior Credit Fund","Senior secured loans to sponsor-backed mid-market borrowers in Europe and North America.","USD 500,000","USD 200m","5 years","Open","g",41,"credit"),
 ("Venture","Lumen Ventures Fund IV","Early-stage technology investments across financial infrastructure and climate.","USD 250,000","USD 80m","10 years","Fully subscribed","d",100,"venture"),
]
def deal(d,w=None):
    t,n,s,mn,rs,tm,st,cl,pr,_=d
    return f"""<div class=card style="padding:22px 22px 20px;display:flex;flex-direction:column;gap:14px;border-radius:14px;box-shadow:none;border-color:var(--line)">
<div style="display:flex;justify-content:space-between;align-items:center"><span class=mono>{t}</span><span class="chip {cl}"><i></i>{st}</span></div>
<div style="font-size:21px;font-weight:400;letter-spacing:-.01em;line-height:1.2">{n}</div>
<div style="font-size:13.5px;color:var(--mut);line-height:1.5;min-height:40px">{s}</div>
<div class=bar><b style="width:{pr}%"></b></div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;border-top:1px solid var(--line);padding-top:12px">
<div><div class=mono style="margin-bottom:4px">Minimum</div><div style="font-size:14px;font-weight:500">{mn}</div></div>
<div><div class=mono style="margin-bottom:4px">Target raise</div><div style="font-size:14px;font-weight:500">{rs}</div></div>
<div><div class=mono style="margin-bottom:4px">Term</div><div style="font-size:14px;font-weight:500">{tm}</div></div></div></div>"""
# ---------- SCENE A opportunities (overlay, transparent)
A=f"""<div style="position:absolute;left:70px;top:46px;width:1080px;height:660px;border-radius:18px;background:rgba(255,255,255,.55);border:1px solid rgba(11,18,16,.05);transform:translate(26px,26px)"></div>
<div class=card style="position:absolute;left:46px;top:20px;width:1080px;padding:26px 28px;border-radius:18px">
<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px">
<div><div class=mono style="margin-bottom:6px">Investment access</div><div style="font-size:30px;font-weight:300;letter-spacing:-.02em">Opportunities</div></div>
<div style="display:flex;gap:6px;align-items:center"><span class="tab on">All</span><span class=tab>Private equity</span><span class=tab>Real assets</span><span class=tab>Private credit</span><span class=tab>Venture</span></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">{''.join(deal(d) for d in DEALS)}</div></div>"""
open('A.html','w').write(page(A,1200,750))

def peek(): return ''
INNER={}
LAST=''
def shell(inner,h=None,left=46,top=20,w=1080):
    global LAST
    LAST=inner
    return f'<div class=wrap style="position:relative;display:inline-block;margin:60px 90px 100px 60px;width:{w}px"><div style="position:absolute;left:26px;top:26px;right:-26px;bottom:-26px;border-radius:18px;background:rgba(255,255,255,.6);border:1px solid rgba(11,18,16,.05)"></div><div class=card style="position:relative;width:{w}px;padding:26px 28px;border-radius:18px">{inner}</div></div>'
def head(eyebrow,title,right=''):
    return f'<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:20px"><div><div class=mono style="margin-bottom:6px">{eyebrow}</div><div style="font-size:30px;font-weight:300;letter-spacing:-.02em">{title}</div></div><div style="display:flex;gap:10px;align-items:center">{right}</div></div>'
def kpi(label,val,sub,icn):
    return f'<div class=card style="box-shadow:none;border-color:var(--line);border-radius:14px;padding:18px 20px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px"><span class=mono>{label}</span><span style="color:var(--mut)">{icon(icn,20)}</span></div><div style="font-size:32px;font-weight:300;letter-spacing:-.02em;line-height:1">{val}</div><div style="font-size:12.5px;color:var(--mut);margin-top:8px">{sub}</div></div>'
def donut(parts,size=170,sw=22):
    r=(size-sw)/2; c=2*3.14159*r; off=0; segs=''
    for pct,col in parts:
        segs+=f'<circle cx="{size/2}" cy="{size/2}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-dasharray="{c*pct/100-3} {c}" stroke-dashoffset="{-off*c/100}" transform="rotate(-90 {size/2} {size/2})"/>'; off+=pct
    return f'<svg width={size} height={size}>{segs}</svg>'
# B portfolio
rows=[("Northbridge Growth Partners III","Private equity","USD 250,000","Committed","g"),("Solstice Solar Portfolio II","Real assets","USD 200,000","In review","a"),("Harbourline Senior Credit Fund","Private credit","USD 600,000","Funded","g")]
def trow(r):
    return f'<div style="display:grid;grid-template-columns:1.6fr 1fr 1fr 110px;align-items:center;padding:14px 0;border-top:1px solid var(--line);font-size:14px"><div style="font-weight:500">{r[0]}</div><div style="color:var(--mut)">{r[1]}</div><div>{r[2]}</div><div><span class="chip {r[4]}"><i></i>{r[3]}</span></div></div>'
B=peek()+shell(head("Your investments","Portfolio",'<span class="btn o">Download statement</span>')+
 f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:16px">{kpi("Total commitments","USD 1.05m","Across 3 opportunities","report")}{kpi("Open opportunities","6","2 closing this month","curate")}{kpi("Actions needed","2","Documents awaiting signature","sign")}</div>'
 f'<div style="display:grid;grid-template-columns:300px 1fr;gap:16px"><div class=card style="box-shadow:none;border-color:var(--line);border-radius:14px;padding:18px 20px"><div class=mono style="margin-bottom:12px">Allocation</div><div style="display:flex;align-items:center;gap:20px">{donut([(24,"#0E6B5C"),(19,"#2FB89C"),(57,"#0F1F1D")],140,20)}<div style="display:flex;flex-direction:column;gap:10px;font-size:12.5px;color:var(--mut)"><span><i style="display:inline-block;width:8px;height:8px;border-radius:2px;background:#0F1F1D;margin-right:8px"></i>Private credit</span><span><i style="display:inline-block;width:8px;height:8px;border-radius:2px;background:#0E6B5C;margin-right:8px"></i>Private equity</span><span><i style="display:inline-block;width:8px;height:8px;border-radius:2px;background:#2FB89C;margin-right:8px"></i>Real assets</span></div></div></div>'
 f'<div class=card style="box-shadow:none;border-color:var(--line);border-radius:14px;padding:16px 20px 6px"><div class=mono style="margin-bottom:6px">Commitments</div>{"".join(trow(r) for r in rows)}</div></div>')
INNER['B']=LAST;open('B.html','w').write(page(B,1200,750))
# C raise
def invcard(n,k,t):
    return f'<div class=card style="box-shadow:none;border-color:var(--line);border-radius:12px;padding:12px 14px;display:flex;gap:12px;align-items:center"><div class=av>{n[0]}{n.split()[-1][0]}</div><div style="flex:1;min-width:0"><div style="font-size:13.5px;font-weight:500">{n}</div><div style="font-size:12px;color:var(--mut)">{k}</div></div><div style="font-size:13px;color:var(--mut)">{t}</div></div>'
cols=[("Invited","48",[("Alder Family Office","Family office","Open"),("Kestrel Partners","Investment firm","Open"),("Mara Okonkwo","Professional investor","Open")]),
("In review","17",[("Fenwick Capital","Investment firm","Day 3"),("Tomas Reinholt","Professional investor","Day 5"),("Blue Quay Advisory","Adviser-led","Day 2")]),
("Committed","11",[("Sandhurst Trust","Foundation","USD 2.0m"),("Elena Marchetti","Professional investor","USD 500k"),("Oakmere Holdings","Family office","USD 1.5m")])]
def col(t,n,cs,i):
    top='border-top:2px solid var(--teal);' if i==2 else 'border-top:2px solid var(--line);'
    return f'<div style="{top}padding-top:12px"><div style="display:flex;justify-content:space-between;margin-bottom:12px"><span style="font-size:14px;font-weight:500">{t}</span><span class=mono>{n}</span></div><div style="display:flex;flex-direction:column;gap:10px">{"".join(invcard(*c) for c in cs)}</div></div>'
C=peek()+shell(head("Raise overview","Northbridge Growth Partners III",'<span class="chip g"><i></i>Open</span><span class="btn">Share with advisers</span>')+
 f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:18px">{kpi("Target raise","USD 120m","Closing 12 December","reach")}{kpi("Committed","USD 71.4m","11 investors","report")}{kpi("In review","17","Average 4 days","verify")}{kpi("Advisers","23","Introducing investors","adviser")}</div>'
 f'<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px">{"".join(col(*c,i) for i,c in enumerate(cols))}</div>')
INNER['C']=LAST;open('C.html','w').write(page(C,1200,750))
# D clients
cl=[("Amira Haddad","United Arab Emirates","3","Verified","g"),("Daniel Okafor","United Kingdom","2","Verified","g"),("Wei Lim","Malaysia","1","In review","a"),("Sofia Reyes","Mexico","2","Verified","g"),("Lars Eriksen","Norway","1","Invited","d"),("Priya Nair","Singapore","4","Verified","g")]
def crow(r,i):
    bg='background:#F5F8F7;' if i==0 else ''
    return f'<div style="display:grid;grid-template-columns:1.5fr 1.2fr 80px 110px;align-items:center;padding:11px 12px;border-top:1px solid var(--line);font-size:14px;{bg}"><div style="display:flex;gap:12px;align-items:center"><div class=av>{r[0][0]}{r[0].split()[-1][0]}</div><span style="font-weight:500">{r[0]}</span></div><div style="color:var(--mut)">{r[1]}</div><div>{r[2]}</div><div><span class="chip {r[4]}"><i></i>{r[3]}</span></div></div>'
mat=[("Northbridge Growth Partners III","Subscribed","g"),("Solstice Solar Portfolio II","In review","a"),("Harbourline Senior Credit Fund","Subscribed","g")]
D=peek()+shell(head("Client relationships","Clients",'<span class="btn o">Export</span><span class="btn">Invite a client</span>')+
 f'<div style="display:grid;grid-template-columns:1.55fr 1fr;gap:16px"><div class=card style="box-shadow:none;border-color:var(--line);border-radius:14px;padding:8px 0 4px;overflow:hidden"><div style="display:grid;grid-template-columns:1.5fr 1.2fr 80px 110px;padding:10px 12px" class=mono><span>Client</span><span>Country</span><span>Deals</span><span>Identity</span></div>{"".join(crow(r,i) for i,r in enumerate(cl))}</div>'
 f'<div class=card style="box-shadow:none;border-color:var(--line);border-radius:14px;padding:20px"><div style="display:flex;gap:14px;align-items:center;margin-bottom:16px"><div class=av style="width:46px;height:46px;font-size:14px">AH</div><div><div style="font-size:17px;font-weight:500">Amira Haddad</div><div style="font-size:12.5px;color:var(--mut)">Client since March</div></div><span class="chip g" style="margin-left:auto"><i></i>Verified</span></div>'
 f'<div style="border-top:1px solid var(--line);padding-top:14px"><div style="display:flex;align-items:center;gap:10px;margin-bottom:6px;color:var(--ink)">{icon("onboard",22)}<span style="font-size:15px;font-weight:500">Onboarded once</span></div><div style="font-size:13px;color:var(--mut);line-height:1.5;margin-bottom:14px">One verified profile, reused for every opportunity she reviews.</div>'
 + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-top:1px solid var(--line);font-size:13.5px"><span>{m[0]}</span><span class="chip {m[2]}"><i></i>{m[1]}</span></div>' for m in mat)+'</div></div></div>')
INNER['D']=LAST;open('D.html','w').write(page(D,1200,750))
# E document
E=peek()+shell(head("Documents","Subscription agreement",'<span class="chip a"><i></i>Awaiting signature</span>')+
 '<div style="display:grid;grid-template-columns:1.5fr 1fr;gap:18px"><div class=card style="box-shadow:none;border-color:var(--line);border-radius:14px;padding:26px 30px;background:#FCFDFC"><div class=mono style="margin-bottom:10px">Northbridge Growth Partners III</div><div style="font-size:22px;font-weight:400;margin-bottom:14px">Subscription agreement</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:12px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);margin-bottom:14px"><div><div class=mono style="margin-bottom:4px">Applicant</div><div style="font-size:14px">Alder Family Office</div></div><div><div class=mono style="margin-bottom:4px">Commitment</div><div style="font-size:14px">USD 2,000,000</div></div></div>'
 '<div style="font-size:13px;line-height:1.65;color:#33423E"><b style="font-weight:500">1. Subscription.</b> The Applicant irrevocably subscribes for interests in the Fund in the amount stated above, subject to acceptance by the General Partner.<br><br><b style="font-weight:500">2. Representations.</b> The Applicant confirms that it qualifies as a professional investor in its jurisdiction and has reviewed the information memorandum and risk factors.</div>'
 '<div style="margin-top:18px;border:1px solid var(--line);border-radius:10px;padding:14px 16px;background:#fff"><div class=mono style="margin-bottom:8px">Electronic signature</div><div style="font-family:Georgia,serif;font-style:italic;font-size:30px;color:#0B1210;line-height:1.1">Alder Family Office</div><div style="height:1px;background:var(--line);margin:8px 0"></div><div style="display:flex;justify-content:space-between;font-size:11.5px;color:var(--sub)"><span>Authorised signatory</span><span>8 November</span></div></div></div>'
 f'<div style="display:flex;flex-direction:column;gap:14px"><div class=card style="box-shadow:none;border-color:var(--line);border-radius:14px;padding:20px"><div class=mono style="margin-bottom:14px">Progress</div>'
 + ''.join(f'<div style="display:flex;align-items:center;gap:12px;padding:9px 0;font-size:14px;{"font-weight:500;" if s=="Sign" else "color:var(--mut);" if s in ("Fund","Done") else ""}"><span style="width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:1px solid {"var(--teal)" if s in ("Review","Sign") else "var(--line)"};background:{"#E3F2EE" if s=="Review" else "#fff"};color:{"var(--acc)" if s in ("Review","Sign") else "var(--sub)"}">{icon(i,17)}</span>{s}</div>' for s,i in (("Review","review"),("Sign","sign"),("Fund","fund"),("Done","verify")))
 + '</div><div class=card style="box-shadow:none;border-color:var(--line);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;gap:12px"><div style="font-size:14px;line-height:1.5;color:var(--mut)">Your document and the next steps, together.</div><span class="btn" style="justify-content:center">Confirm signature</span></div></div></div>')
INNER['E']=LAST;open('E.html','w').write(page(E,1200,750))
# F onboarding
steps=[("Your details","verify",1),("Verify status","access",2),("Documents","review",0),("Done","sign",0)]
def st(n,i,s):
    act=(n=="Verify status"); done=(n=="Your details")
    return f'<div style="display:flex;gap:14px;align-items:center;padding:12px 0"><span style="width:38px;height:38px;border-radius:50%;border:1px solid {"var(--teal)" if act or done else "var(--line)"};background:{"#E3F2EE" if done else "#fff"};color:{"var(--acc)" if act or done else "var(--sub)"};display:flex;align-items:center;justify-content:center">{icon(i,20)}</span><span style="font-size:15px;{"font-weight:500;" if act else "color:var(--mut);"}">{n}</span></div>'
def opt(t,d,on):
    return f'<div style="border:1px solid {"var(--act)" if on else "var(--line)"};border-radius:12px;padding:16px 18px;display:flex;gap:14px;background:{"#F5FAF8" if on else "#fff"}"><span style="width:18px;height:18px;border-radius:50%;border:1.5px solid {"var(--act)" if on else "#B9C3C0"};display:flex;align-items:center;justify-content:center;margin-top:2px;flex:none">{"<i style=width:8px;height:8px;border-radius:50%;background:var(--act)></i>" if on else ""}</span><div><div style="font-size:15px;font-weight:500">{t}</div><div style="font-size:13px;color:var(--mut);margin-top:3px;line-height:1.45">{d}</div></div></div>'
F=peek()+shell('<div style="display:grid;grid-template-columns:300px 1fr;gap:34px;padding:6px 6px 6px 0"><div style="background:#F2F4F3;border-radius:14px;padding:26px 24px"><div class=mono style="margin-bottom:6px">Getting started</div><div style="font-size:22px;font-weight:300;margin-bottom:12px;letter-spacing:-.01em">Your account setup</div>'+''.join(st(*s[:2],0) if False else st(s[0],s[1],0) for s in steps)+'<div style="margin-top:22px;font-size:12.5px;color:var(--mut);display:flex;gap:8px;align-items:flex-start">'+icon("secure",18)+'<span>Your information is only visible to authorised reviewers.</span></div></div>'
 '<div><div class=mono style="margin-bottom:8px">Step 2 of 4</div><div style="font-size:32px;font-weight:300;letter-spacing:-.02em;margin-bottom:10px">Verify your status</div><div style="font-size:15px;color:var(--mut);margin-bottom:22px;line-height:1.5">Choose the category you would like us to assess for investment access.</div><div style="display:flex;flex-direction:column;gap:12px">'
 +opt("Professional investor","Assessed against the criteria that apply in your country.",True)+opt("Qualified investor","Assessed against the qualified investor criteria that apply to the investment.",False)+'</div><div style="display:flex;justify-content:space-between;align-items:center;margin-top:26px"><span style="font-size:14px;color:var(--mut)">Back</span><span class=btn>Continue to documents</span></div></div></div>',top=60)
INNER['F']=LAST;open('F.html','w').write(page(F,1200,750))

# A rebuilt with wrapper
a_inner=head("Investment access","Opportunities",'<span class="tab on">All</span><span class=tab>Private equity</span><span class=tab>Real assets</span><span class=tab>Private credit</span><span class=tab>Venture</span>')+f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">{"".join(deal(d) for d in DEALS)}</div>'
A2=shell(a_inner); INNER['A']=a_inner
open('A.html','w').write(page(A2,1500,1000))
for k in 'BCDEF':
    h=open(k+'.html').read()
    open(k+'.html','w').write(h.replace('width:1200px;height:750px;overflow:hidden','width:1500px;height:1100px;overflow:hidden'))
# Dark composites (1600x1000)
def card(inner,x,y,w,sc,z=1):
    return f'<div class=card style="position:absolute;left:{x}px;top:{y}px;width:{w}px;padding:26px 28px;border-radius:18px;transform:scale({sc});transform-origin:top left;z-index:{z};box-shadow:0 40px 80px -20px rgba(0,0,0,.55)">{inner}</div>'
BG='background:radial-gradient(900px 640px at 78% 8%,rgba(47,184,156,.34),transparent 60%),radial-gradient(800px 600px at 8% 100%,rgba(14,107,92,.30),transparent 62%),linear-gradient(180deg,#0A1514,#060C0B)'
ARCS='<svg style="position:absolute;inset:0" width=1600 height=1000 fill=none stroke="rgba(255,255,255,.10)" stroke-width=1.2><circle cx=1250 cy=300 r=420 /><circle cx=1010 cy=300 r=420 /></svg>'
G=f'<div style="position:absolute;inset:0;{BG}"></div>{ARCS}'+card(INNER['B'],70,80,1080,1.0,1)+card(INNER['E'],760,330,1080,.92,2)
open('G.html','w').write(page(G,1600,1000,'#060C0B'))
H=f'<div style="position:absolute;inset:0;{BG}"></div>{ARCS}'+card(INNER['C'],60,70,1080,1.0,1)+card(INNER['A'],690,400,1080,.86,2)
open('H.html','w').write(page(H,1600,1000,'#060C0B'))
