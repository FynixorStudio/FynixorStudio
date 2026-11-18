import math, os
OUT = "/home/claude/fx2/assets"
NAVY="#0E1A2B"; NAVY2="#16263D"; LINE="#24374F"
FLAME="#FF4D2E"; DEEP="#C2331B"; GOLD="#FFC233"; MIST="#E8EDF4"; STEEL="#8A9AB0"; GREEN="#3DDC97"
SANS="'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"

def w(name, s):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(s)

# ---------- geometric logotype ----------
LET = {
 "F": ["M12 88V12H60","M12 48H48"],
 "Y": ["M8 8L32 46L56 8","M32 46V88"],
 "N": ["M12 88V8L52 88V8"],
 "I": ["M32 8V88"],
 "X": ["M8 8L56 88","M56 8L8 88"],
 "O": ["M20 8H44L56 20V76L44 88H20L8 76V20Z"],
 "R": ["M12 88V8H44L56 20V36L44 48H12","M32 48L56 88"],
}
def wordmark(x, y, scale=1.0, color=MIST, stroke=12, gap=15):
    out=[]; cx=0
    for ch in "FYNIXOR":
        adv = 64 if ch!="I" else 64
        paths="".join(f'<path d="{p}"/>' for p in LET[ch])
        out.append(f'<g transform="translate({cx},0)">{paths}</g>')
        cx += adv+gap
    total = cx-gap
    g = (f'<g transform="translate({x},{y}) scale({scale})" fill="none" stroke="{color}" '
         f'stroke-width="{stroke}" stroke-linejoin="miter" stroke-miterlimit="2.5" stroke-linecap="butt">'
         + "".join(out) + '</g>')
    return g, total*scale

def mark(x, y, s=1.0):
    # fan of feathers rising from a base point
    bx, by = 100, 196
    blades=[(-62,128,15,DEEP),(62,128,15,DEEP),(-31,164,17,FLAME),(31,164,17,FLAME),(0,196,19,GOLD)]
    polys=[]
    for ang,L,wd,col in blades:
        a=math.radians(ang)
        def P(d,off):
            # d along blade, off perpendicular
            px = bx + math.sin(a)*d + math.cos(a)*off
            py = by - math.cos(a)*d + math.sin(a)*off
            return f"{px:.1f},{py:.1f}"
        pts=[P(0,0),P(L*0.42,wd),P(L,0),P(L*0.42,-wd)]
        polys.append(f'<polygon points="{" ".join(pts)}" fill="{col}"/>')
    base=f'<polygon points="100,176 114,192 100,208 86,192" fill="{MIST}"/>'
    return f'<g transform="translate({x},{y}) scale({s})">{"".join(polys)}{base}</g>'

# ---------- banner ----------
def banner():
    wm, wmw = wordmark(400, 92, 1.12)
    taglines=["Website, bot, script, dan automation.",
              "Dibangun dari nol, dirawat sampai jalan.",
              "Android, Windows RDP, Linux, dan cloud."]
    tl="".join(f'<text x="404" y="316" class="tag t{i}">{t}</text>' for i,t in enumerate(taglines))
    embers="".join(
      f'<rect class="ember e{i}" x="{x}" y="{y}" width="{s}" height="{s}" fill="{c}" transform="rotate(45 {x} {y})"/>'
      for i,(x,y,s,c) in enumerate([(120,330,6,GOLD),(190,352,5,FLAME),(250,340,4,GOLD),(90,350,4,FLAME)]))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="400" viewBox="0 0 1200 400" role="img" aria-label="Fynixor Studio">
<defs>
  <pattern id="hex" width="51.96" height="90" patternUnits="userSpaceOnUse">
    <path d="M0 15L25.98 0L51.96 15M0 15V45M51.96 15V45M0 45L25.98 60L51.96 45M25.98 60V90" fill="none" stroke="{MIST}" stroke-opacity=".07" stroke-width="1.2"/>
  </pattern>
  <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".45" stop-color="#fff" stop-opacity=".15"/><stop offset="1" stop-color="#fff"/></linearGradient>
  <mask id="m"><rect width="1200" height="400" fill="url(#fade)"/></mask>
  <style>
    .tag{{font:500 27px {SANS};fill:{MIST};opacity:0}}
    .meta{{font:500 17px {SANS};fill:{STEEL}}}
    .studio{{font:700 30px {SANS};fill:{GOLD};letter-spacing:.5px}}
    .t0{{animation:cyc 12s infinite}} .t1{{animation:cyc 12s infinite 4s}} .t2{{animation:cyc 12s infinite 8s}}
    @keyframes cyc{{0%{{opacity:0;transform:translateY(6px)}}6%,28%{{opacity:1;transform:none}}34%,100%{{opacity:0;transform:translateY(-6px)}}}}
    .ember{{opacity:0;animation:rise 7s ease-out infinite}}
    .e1{{animation-delay:1.6s}} .e2{{animation-delay:3.2s}} .e3{{animation-delay:4.8s}}
    @keyframes rise{{0%{{opacity:0;transform:translateY(0)}}15%{{opacity:.9}}100%{{opacity:0;transform:translateY(-150px)}}}}
    @media (prefers-reduced-motion:reduce){{.t0{{animation:none;opacity:1}}.ember{{display:none}}}}
  </style>
</defs>
<rect width="1200" height="400" fill="{NAVY}"/>
<rect width="1200" height="400" fill="url(#hex)" mask="url(#m)"/>
<rect y="396" width="1200" height="4" fill="{FLAME}"/>
<rect x="0" y="396" width="400" height="4" fill="{GOLD}"/>
{mark(70,70,1.3)}
{embers}
{wm}
<text x="404" y="252" class="studio">Studio</text>
<rect x="516" y="240" width="{wmw-116:.0f}" height="2" fill="{LINE}"/>
{tl}
<text x="1120" y="366" text-anchor="end" class="meta">Sejak 2023, Indonesia</text>
</svg>'''

# ---------- section header ----------
def header(title, sub):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="84" viewBox="0 0 1200 84" role="img" aria-label="{title}">
<style>.h{{font:800 34px {SANS};fill:{MIST}}}.s{{font:400 18px {SANS};fill:{STEEL}}}</style>
<rect width="1200" height="84" fill="{NAVY}"/>
<polygon points="40,26 52,42 40,58 28,42" fill="{FLAME}"/>
<polygon points="40,34 46,42 40,50 34,42" fill="{GOLD}"/>
<text x="72" y="53" class="h">{title}</text>
<text x="1160" y="51" text-anchor="end" class="s">{sub}</text>
<rect x="0" y="80" width="1200" height="4" fill="{NAVY2}"/>
<rect x="0" y="80" width="120" height="4" fill="{FLAME}"/>
</svg>'''

# ---------- units ----------
UNITS=[("Vorhex Store","Produk digital: panel, cloud dan RDP, script, SMM","Aktif","on"),
       ("Lumina Worksite","Jasa pembuatan website, bot, script, dan sistem custom","Aktif","on"),
       ("VTuber Agency","Pengembangan talent dan content creator","Dalam pengembangan","dev"),
       ("MBD","Riset dan tools keamanan, hanya pada sistem sendiri atau yang berizin","Dalam pengembangan","dev"),
       ("Finansial dan trading","Masih sebatas rencana, belum berjalan","Rencana","plan")]
def units():
    rh=92; H=rh*len(UNITS)+8
    rows=[]
    for i,(n,d,st,k) in enumerate(UNITS):
        y=4+i*rh
        col={"on":GREEN,"dev":GOLD,"plan":STEEL}[k]
        dim = .55 if k=="plan" else 1
        if k=="on": dot=f'<circle cx="930" cy="{y+46}" r="7" fill="{col}"/>'
        elif k=="dev": dot=f'<circle cx="930" cy="{y+46}" r="6" fill="none" stroke="{col}" stroke-width="3"/><path d="M930 {y+40}A6 6 0 0 1 930 {y+52}Z" fill="{col}"/>'
        else: dot=f'<circle cx="930" cy="{y+46}" r="6" fill="none" stroke="{col}" stroke-width="2" stroke-dasharray="3 3"/>'
        rows.append(f'''<g opacity="{dim}">
<rect x="40" y="{y+22}" width="5" height="48" fill="{col}"/>
<text x="68" y="{y+45}" class="n">{n}</text>
<text x="68" y="{y+70}" class="d">{d}</text>
{dot}<text x="950" y="{y+52}" class="st" fill="{col}">{st}</text>
</g>''')
        if i<len(UNITS)-1: rows.append(f'<rect x="40" y="{y+rh-1}" width="1120" height="1" fill="{LINE}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{H}" viewBox="0 0 1200 {H}" role="img" aria-label="Unit Fynixor Studio">
<style>.n{{font:700 28px {SANS};fill:{MIST}}}.d{{font:400 18px {SANS};fill:{STEEL}}}.st{{font:600 18px {SANS}}}</style>
<rect width="1200" height="{H}" fill="{NAVY}"/>
{''.join(rows)}
</svg>'''

# ---------- services ----------
def icon(kind, cx, cy, c1, c2):
    s=f'fill="none" stroke="{c1}" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round"'
    if kind=="web":
        return f'<g {s}><rect x="{cx-30}" y="{cy-22}" width="60" height="44" rx="3"/><path d="M{cx-30} {cy-8}H{cx+30}"/></g><circle cx="{cx-21}" cy="{cy-15}" r="2.4" fill="{c2}"/><circle cx="{cx-13}" cy="{cy-15}" r="2.4" fill="{c2}"/>'
    if kind=="bot":
        return f'<g {s}><rect x="{cx-26}" y="{cy-16}" width="52" height="38" rx="5"/><path d="M{cx} {cy-16}V{cy-27}"/></g><circle cx="{cx}" cy="{cy-29}" r="3.5" fill="{c2}"/><circle cx="{cx-10}" cy="{cy+3}" r="4" fill="{c2}"/><circle cx="{cx+10}" cy="{cy+3}" r="4" fill="{c2}"/>'
    if kind=="code":
        return f'<g {s}><path d="M{cx-12} {cy-18}L{cx-32} {cy}L{cx-12} {cy+18}"/><path d="M{cx+12} {cy-18}L{cx+32} {cy}L{cx+12} {cy+18}"/></g><path d="M{cx+5} {cy-22}L{cx-5} {cy+22}" stroke="{c2}" stroke-width="3.5" stroke-linecap="round"/>'
    if kind=="db":
        return f'<g {s}><ellipse cx="{cx}" cy="{cy-17}" rx="26" ry="8"/><path d="M{cx-26} {cy-17}V{cy+15}C{cx-26} {cy+27} {cx+26} {cy+27} {cx+26} {cy+15}V{cy-17}"/><path d="M{cx-26} {cy-1}C{cx-26} {cy+10} {cx+26} {cy+10} {cx+26} {cy-1}" stroke="{c2}"/></g>'
    if kind=="tool":
        pts=[(cx+30*math.cos(math.radians(a)), cy+30*math.sin(math.radians(a))) for a in range(0,360,45)]
        return f'<g {s}><circle cx="{cx}" cy="{cy}" r="17"/>'+"".join(f'<path d="M{cx+22*math.cos(math.radians(a)):.1f} {cy+22*math.sin(math.radians(a)):.1f}L{cx+31*math.cos(math.radians(a)):.1f} {cy+31*math.sin(math.radians(a)):.1f}"/>' for a in range(0,360,45))+f'</g><circle cx="{cx}" cy="{cy}" r="5" fill="{c2}"/>'
SERV=[("web","Website","Landing page sampai web app, lengkap dengan tampilan"),
      ("bot","Bot","Telegram dan WhatsApp untuk kebutuhan nyata"),
      ("code","Automation","Script yang menggantikan kerjaan berulang"),
      ("db","Backend","API, MySQL, dan Firebase"),
      ("tool","Perawatan","Perbaikan dan pengembangan lanjutan")]
def services():
    colw=1120/5; H=250; out=[]
    for i,(k,t,d) in enumerate(SERV):
        x0=40+i*colw; cx=x0+colw/2
        out.append(icon(k,cx,76,GOLD,FLAME))
        out.append(f'<text x="{cx}" y="150" text-anchor="middle" class="t">{t}</text>')
        # wrap description
        words=d.split(); lines=[]; cur=""
        for wd in words:
            if len(cur+" "+wd)>23 and cur: lines.append(cur); cur=wd
            else: cur=(cur+" "+wd).strip()
        lines.append(cur)
        for j,l in enumerate(lines):
            out.append(f'<text x="{cx}" y="{178+j*22}" text-anchor="middle" class="d">{l}</text>')
        if i: out.append(f'<rect x="{x0}" y="36" width="1" height="178" fill="{LINE}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{H}" viewBox="0 0 1200 {H}" role="img" aria-label="Layanan Lumina Worksite">
<style>.t{{font:700 21px {SANS};fill:{MIST}}}.d{{font:400 17px {SANS};fill:{STEEL}}}</style>
<rect width="1200" height="{H}" fill="{NAVY}"/>
{''.join(out)}
</svg>'''

# ---------- stack ----------
STACK=[("Bahasa",["PHP","JavaScript","Node.js","Python","HTML","CSS"],FLAME),
       ("Data",["MySQL","Firebase"],GOLD),
       ("Bot",["Telegraf.js","GramJS","Baileys"],FLAME),
       ("Lingkungan",["Termux","Windows RDP","Linux","Git","GitHub Actions"],GOLD)]
def stack():
    rowh=70; H=rowh*len(STACK)+36; out=[]
    for i,(cat,items,c) in enumerate(STACK):
        y=30+i*rowh
        out.append(f'<text x="40" y="{y+30}" class="c">{cat}</text>')
        x=230
        for it in items:
            wd=len(it)*10.4+40
            out.append(f'<rect x="{x:.0f}" y="{y}" width="{wd:.0f}" height="46" rx="6" fill="{NAVY2}" stroke="{LINE}"/><rect x="{x:.0f}" y="{y+11}" width="4" height="24" fill="{c}"/><text x="{x+wd/2+2:.0f}" y="{y+30}" text-anchor="middle" class="p">{it}</text>')
            x+=wd+12
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{H}" viewBox="0 0 1200 {H}" role="img" aria-label="Tech stack">
<style>.c{{font:600 19px {SANS};fill:{STEEL}}}.p{{font:600 18px {SANS};fill:{MIST}}}</style>
<rect width="1200" height="{H}" fill="{NAVY}"/>
{''.join(out)}
</svg>'''

# ---------- contact tiles ----------
def tile(name, handle, color):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="290" height="92" viewBox="0 0 290 92" role="img" aria-label="{name}">
<style>.a{{font:700 24px {SANS};fill:{MIST}}}.b{{font:400 16px {SANS};fill:{STEEL}}}</style>
<clipPath id="r"><rect width="290" height="92" rx="8"/></clipPath>
<g clip-path="url(#r)"><rect width="290" height="92" fill="{NAVY}"/><rect width="8" height="92" fill="{color}"/></g>
<text x="30" y="42" class="a">{name}</text>
<text x="30" y="66" class="b">{handle}</text>
</svg>'''

def footer():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="150" viewBox="0 0 1200 150" role="img" aria-label="Fynixor Studio">
<style>.f{{font:500 16px {SANS};fill:{STEEL}}}.g{{font:700 22px {SANS};fill:{MIST}}}</style>
<rect width="1200" height="150" fill="{NAVY}"/>
{mark(566,6,0.34)}
<text x="600" y="108" text-anchor="middle" class="g">Fynixor Studio</text>
<text x="600" y="132" text-anchor="middle" class="f">Satu orang, banyak arah. © 2026</text>
<rect y="146" width="1200" height="4" fill="{FLAME}"/><rect y="146" width="400" height="4" fill="{GOLD}"/>
</svg>'''

w("banner.svg", banner())
for k,(t,s) in {"h-tentang":("Tentang","Studio digital satu orang"),
                "h-unit":("Unit","Yang jalan dan yang masih disiapkan"),
                "h-layanan":("Layanan","Lewat Lumina Worksite"),
                "h-teknologi":("Teknologi","Yang dipakai sehari-hari"),
                "h-aktivitas":("Aktivitas","Dari GitHub"),
                "h-kontak":("Kontak","Terbuka untuk kerja sama")}.items():
    w(k+".svg", header(t,s))
w("units.svg", units()); w("services.svg", services()); w("stack.svg", stack()); w("footer.svg", footer())
w("c-fiverr.svg", tile("Fiverr","fiverr.com/fynixorstudio","#1DBF73"))
w("c-telegram.svg", tile("Telegram","@fynixorstudio","#2AABEE"))
w("c-email.svg", tile("Email","fynixorstudio@gmail.com",GOLD))
w("c-instagram.svg", tile("Instagram","@fynixorstudio",FLAME))
print(sorted(os.listdir(OUT)))
