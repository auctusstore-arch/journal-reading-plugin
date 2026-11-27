#!/usr/bin/env python3
"""Bangun Panduan Tutor sesi Zoom journal reading (HTML mandiri, satu file) dari tutor.json.

Pakai:
  uv run python3 build_tutor_guide.py tutor.json outdir/

Panduan ini hanya untuk tutor (memuat kunci jawaban dan penilaian kesiapan klien),
jangan dikirim ke klien. Skema tutor.json: references/jalur-zoom.md bagian Z4.
Script memeriksa field wajib, jumlah butir, total menit agenda, dan em dash.
"""
import html, json, os, re, sys

PALETTES = {
    "navy":   {"primary": "#0b2545", "accent": "#13807a", "tint": "#e3f2f0", "soft": "#e6edf5"},
    "maroon": {"primary": "#4a1520", "accent": "#a3313f", "tint": "#f7e8ea", "soft": "#f5eaec"},
    "hijau":  {"primary": "#1e3a2b", "accent": "#3f7d3a", "tint": "#eaf3e6", "soft": "#e8f0e4"},
}
REQUIRED = ["meta", "kebutuhan", "self_rating", "cek_pemahaman", "prioritas", "agenda",
            "review_slide", "simulasi", "perbaikan_kandidat", "checklist_h0"]
COUNTS = {"prioritas": (2, 3), "review_slide": (5, 8), "simulasi": (6, 8), "perbaikan_kandidat": (3, 3)}


def slides_of(p):
    v = p.get("slide")
    if isinstance(v, str):
        v = [v]
    return [str(x).strip() for x in (v or []) if str(x).strip()]


def gaps_of(r):
    g = r.get("gap")
    if g is None:
        return []
    return g if isinstance(g, list) else [g]


def check(t):
    errs, warns = [], []
    for k in REQUIRED:
        if k not in t:
            errs.append(f"field wajib hilang: {k}")
    if errs:
        return errs, warns
    for k, (lo, hi) in COUNTS.items():
        n = len(t[k])
        if not lo <= n <= hi:
            errs.append(f"{k}: {n} butir, harus {lo} sampai {hi}")
    for f in ("penyaji", "paper", "jadwal_presentasi", "jadwal_zoom", "sumber"):
        if not str(t["meta"].get(f, "")).strip():
            errs.append(f"meta.{f} kosong")
    menit = sum(float(a.get("menit", 0)) for a in t["agenda"])
    if not 55 <= menit <= 60:
        errs.append(f"agenda total {menit:g} menit; harus 55 sampai 60 (SOP sesi 60 menit)")
    for vid in t.get("visual", []):
        if vid not in VISUALS:
            errs.append(f"visual '{vid}' belum terdaftar (lihat references/visual-katalog.md); tersedia: {', '.join(VISUALS)}")
    np_ = len(t["prioritas"])
    for i, p in enumerate(t["prioritas"], 1):
        if not slides_of(p):
            errs.append(f"prioritas ke-{i}: field 'slide' kosong (pemetaan gap ke nomor slide wajib)")
    dipakai = set()
    for i, r in enumerate(t["review_slide"], 1):
        for g in gaps_of(r):
            if not isinstance(g, int) or not 1 <= g <= np_:
                errs.append(f"review_slide ke-{i}: gap {g!r} harus angka 1 sampai {np_}")
            else:
                dipakai.add(g)
    for g in range(1, np_ + 1):
        if g not in dipakai:
            warns.append(f"prioritas ke-{g} belum punya review_slide dengan gap={g}; tambahkan titik review untuk slide yang dipetakan")
    for i, s in enumerate(t["simulasi"], 1):
        for f in ("pertanyaan", "jawaban_model", "tanda_lemah"):
            if not str(s.get(f, "")).strip():
                errs.append(f"simulasi ke-{i}: field '{f}' kosong")
    for i, c in enumerate(t["cek_pemahaman"], 1):
        if c.get("status") not in ("benar", "salah", "terbuka", "kosong"):
            errs.append(f"cek_pemahaman ke-{i}: status harus benar, salah, terbuka, atau kosong")
    for r in t["self_rating"]:
        s = r.get("skor")
        if s is not None and not (isinstance(s, (int, float)) and 1 <= s <= 5):
            errs.append(f"self_rating '{r.get('area')}': skor harus 1 sampai 5 atau null")
    raw = json.dumps(t, ensure_ascii=False)
    if "—" in raw:
        errs.append("ada em dash di tutor.json; ganti dengan koma, titik dua, atau kurung")
    if re.search(r"\bkita\b", raw, re.I):
        warns.append("ada kata 'kita'; pakai kalimat pasif atau sapaan langsung")
    if not t["cek_pemahaman"]:
        warns.append("cek_pemahaman kosong: klien belum mengisi form pre-zoom? Tandai di meta.sumber")
    return errs, warns


def esc(s):
    return html.escape(str(s))


def ul(items):
    return "<ul>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"


def bar(skor):
    if skor is None:
        return '<span class="j mid">tidak diisi</span>'
    cls = "bad" if skor <= 2 else "mid" if skor == 3 else "ok"
    return f'<span class="meter"><i style="width:{skor * 20}%" class="{cls}"></i></span><b>{esc(skor)}/5</b>'


VISUAL_KORELASI = """<section><h2><span>A</span>Lampiran: korelasi vs ICC vs Bland-Altman</h2>
<p class="hint">Data sintetis (60 pasien) untuk melatih klien membedakan tiga ukuran. Klik skenario, lalu minta klien menebak angka sebelum melihatnya.</p>
<div id="vz-b" style="display:flex;flex-wrap:wrap;gap:8px;margin:8px 0"></div>
<p id="vz-t" class="hint" style="min-height:44px"></p>
<div class="two"><div><h3>Scatterplot: alat vs laboratorium</h3><svg id="vz-1" viewBox="0 0 300 240" width="100%" role="img" aria-label="Scatterplot dengan garis y sama dengan x"></svg></div>
<div><h3>Bland-Altman: selisih vs rata-rata</h3><svg id="vz-2" viewBox="0 0 300 240" width="100%" role="img" aria-label="Plot Bland-Altman dengan beda rerata dan limits of agreement"></svg></div></div>
<p class="hint">Garis putus abu-abu: y = x. Garis biru: regresi (kiri) atau beda rerata (kanan). Garis titik merah: limits of agreement (rerata selisih ±1,96 SD).</p>
<div class="grid" id="vz-m"></div>
<table><thead><tr><th>Ukuran</th><th>Menjawab</th><th>Buta terhadap</th></tr></thead><tbody>
<tr><td><b>Pearson r</b></td><td>Searah dan lurus atau tidak</td><td>Bias konstan dan proporsional</td></tr>
<tr><td><b>ICC</b></td><td>Konsistensi, termasuk bias rerata (absolute agreement)</td><td>Pola bias dan besar selisih per pasien</td></tr>
<tr><td><b>Bland-Altman</b></td><td>Besar dan arah selisih per pasien, bias, pola</td><td>Tidak memberi satu angka ringkas</td></tr></tbody></table>
<script>
(function(){
function rng(s){return function(){s|=0;s=s+0x6D2B79F5|0;var t=Math.imul(s^s>>>15,1|s);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function gs(r){var u=0,v;while(!u)u=r();v=r();return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v)}
var SC=[{n:"Sepakat baik",f:function(x,e){return x+0.15*e},t:"Titik menempel di garis y = x. Ketiga ukuran setuju."},
{n:"Bias konstan",f:function(x,e){return x+1.5+0.15*e},t:"Alat selalu 1,5 lebih tinggi. Pearson tetap hampir 1, ICC turun, Bland-Altman menunjukkan beda rerata 1,5."},
{n:"Bias proporsional",f:function(x,e){return 1.4*x+0.15*e},t:"Selisih membesar pada kadar tinggi. Pearson tetap tinggi; titik Bland-Altman miring."},
{n:"Banyak error",f:function(x,e){return x+1.2*e},t:"Bias rerata sekitar 0, tetapi selisih per pasien besar. Mirip StatStrip puasa (beda rerata 0,20%, LoA -34,7% sampai 35,1%)."}];
function fm(v,d){return v.toFixed(d).replace(".",",")}
function st(a,b){var n=a.length,m=[],d=[],i,ma=0,mb=0;for(i=0;i<n;i++){m.push((a[i]+b[i])/2);d.push(b[i]-a[i]);ma+=a[i]/n;mb+=b[i]/n}
var sxy=0,sxx=0,syy=0;for(i=0;i<n;i++){sxy+=(a[i]-ma)*(b[i]-mb);sxx+=Math.pow(a[i]-ma,2);syy+=Math.pow(b[i]-mb,2)}
var gm=(ma+mb)/2,ssr=0,sst=0;for(i=0;i<n;i++){ssr+=2*Math.pow(m[i]-gm,2);sst+=Math.pow(a[i]-gm,2)+Math.pow(b[i]-gm,2)}
var ssc=n*(Math.pow(ma-gm,2)+Math.pow(mb-gm,2)),sse=sst-ssr-ssc,msr=ssr/(n-1),msc=ssc,mse=sse/(n-1);
var icc=(msr-mse)/(msr+mse+2*(msc-mse)/n),bias=0;for(i=0;i<n;i++)bias+=d[i]/n;
var sd=0;for(i=0;i<n;i++)sd+=Math.pow(d[i]-bias,2);sd=Math.sqrt(sd/(n-1));
var sl=sxy/sxx;return{m:m,d:d,r:sxy/Math.sqrt(sxx*syy),sl:sl,ic:mb-sl*ma,icc:icc,bias:bias,lo:bias-1.96*sd,hi:bias+1.96*sd}}
function plot(id,pts,lines,xr,yr,xl,yl){var el=document.getElementById(id),X=function(x){return 44+(x-xr[0])/(xr[1]-xr[0])*246},Y=function(y){return 200-(y-yr[0])/(yr[1]-yr[0])*184};
var h='<line x1="44" y1="200" x2="290" y2="200" stroke="currentColor" opacity=".35"/><line x1="44" y1="16" x2="44" y2="200" stroke="currentColor" opacity=".35"/>';
[xr[0],(xr[0]+xr[1])/2,xr[1]].forEach(function(v){h+='<text x="'+X(v)+'" y="214" font-size="10" text-anchor="middle" fill="currentColor" opacity=".7">'+fm(v,0)+'</text>'});
[yr[0],(yr[0]+yr[1])/2,yr[1]].forEach(function(v){h+='<text x="38" y="'+(Y(v)+3)+'" font-size="10" text-anchor="end" fill="currentColor" opacity=".7">'+fm(v,0)+'</text>'});
h+='<text x="167" y="232" font-size="10" text-anchor="middle" fill="currentColor" opacity=".7">'+xl+'</text><text x="8" y="108" font-size="10" fill="currentColor" opacity=".7" transform="rotate(-90 8 108)" text-anchor="middle">'+yl+'</text>';
lines.forEach(function(l){h+='<line x1="'+X(l[0])+'" y1="'+Y(l[1])+'" x2="'+X(l[2])+'" y2="'+Y(l[3])+'" stroke="'+l[4]+'" stroke-width="2" stroke-dasharray="'+l[5]+'"/>'});
pts.forEach(function(p){h+='<circle cx="'+X(p[0])+'" cy="'+Y(p[1])+'" r="3" fill="#2a78d6" opacity=".65"/>'});el.innerHTML=h}
function show(i){var s=SC[i],r=rng(7),a=[],b=[],j,x;for(j=0;j<60;j++){x=3+7*r();a.push(x);b.push(s.f(x,gs(r)))}
var q=st(a,b),p1=[],p2=[];for(j=0;j<60;j++){p1.push([a[j],b[j]]);p2.push([q.m[j],q.d[j]])}
plot("vz-1",p1,[[0,0,14,14,"#888780","6 4"],[0,q.ic,14,q.ic+q.sl*14,"#2a78d6",""]],[0,14],[0,14],"Laboratorium (mmol/L)","Alat (mmol/L)");
plot("vz-2",p2,[[2,q.bias,14,q.bias,"#2a78d6",""],[2,q.hi,14,q.hi,"#c53030","2 3"],[2,q.lo,14,q.lo,"#c53030","2 3"]],[2,14],[-5,6],"Rata-rata kedua alat (mmol/L)","Selisih alat - lab");
document.getElementById("vz-t").textContent=s.t;
document.getElementById("vz-m").innerHTML=[["Pearson r",fm(q.r,2)],["ICC",fm(q.icc,2)],["Beda rerata",fm(q.bias,1)],["Limits of agreement",fm(q.lo,1)+" s.d. "+fm(q.hi,1)]].map(function(c){return "<div><b>"+c[0]+"</b><p style='font-size:22px;font-weight:600;margin:4px 0 0'>"+c[1]+"</p></div>"}).join("");
var bs=document.querySelectorAll("#vz-b button");for(j=0;j<bs.length;j++){bs[j].style.background=j===i?"var(--a)":"none";bs[j].style.color=j===i?"#fff":"var(--a)"}}
var bw=document.getElementById("vz-b");SC.forEach(function(s,i){var b=document.createElement("button");b.className="btn";b.style.margin="0";b.textContent=s.n;b.onclick=function(){show(i)};bw.appendChild(b)});show(3)})();
</script></section>"""


VISUALS = {"korelasi_icc_ba": VISUAL_KORELASI}


def build_html(t, pal):
    m, k = t["meta"], t["kebutuhan"]
    sec = []
    keb = [("Tujuan sesi", k.get("tujuan", "")), ("Kekhawatiran", k.get("kekhawatiran", "")),
           ("Pengalaman JR", k.get("pengalaman", "")), ("Status slide", k.get("status_slide", "")),
           ("Gaya konsulen", k.get("gaya_konsulen", ""))]
    keb_html = "".join(f'<div><b>{esc(a)}</b><p>{esc(c)}</p></div>' for a, c in keb if c)
    sec.append(f'<section><h2><span>1</span>Kebutuhan klien</h2><div class="grid">{keb_html}</div></section>')

    sr = "".join(f'<tr><td>{esc(r["area"])}</td><td class="nw">{bar(r.get("skor"))}</td></tr>' for r in t["self_rating"])
    ada_slide = any(c.get("slide") for c in t["cek_pemahaman"])
    cp = "".join(
        f'<tr><td>{esc(c.get("soal", ""))}</td><td>{esc(c.get("jawaban", ""))}</td>'
        f'<td><span class="j {"ok" if c["status"] == "benar" else "bad" if c["status"] in ("salah", "kosong") else "mid"}">{esc(c["status"])}</span></td>'
        f'<td>{esc(c.get("makna", ""))}</td>'
        + (f'<td class="nw">{esc(c.get("slide", ""))}</td>' if ada_slide else "") + '</tr>' for c in t["cek_pemahaman"])
    th_slide = "<th>Slide terkait</th>" if ada_slide else ""
    pr = "".join(f'<li><b>{esc(p["area"])}</b>: {esc(p["alasan"])} <span class="sl">Bahas di slide {esc(", ".join(slides_of(p)))}</span></li>' for p in t["prioritas"])
    peta = "".join(
        f'<tr><td class="nw"><b>Gap {i}</b></td><td>{esc(p["area"])}</td><td>{esc(", ".join(slides_of(p)))}</td></tr>'
        for i, p in enumerate(t["prioritas"], 1))
    sec.append(f'''<section><h2><span>2</span>Peta gap</h2>
<div class="two"><div><h3>Penilaian diri (pre-zoom)</h3><table><tbody>{sr}</tbody></table></div>
<div><h3>Area prioritas sesi</h3><ol class="pr">{pr}</ol></div></div>
<h3>Peta gap ke slide</h3><div class="tw"><table><thead><tr><th>Gap</th><th>Area</th><th>Slide yang dibahas</th></tr></thead><tbody>{peta}</tbody></table></div>
<h3>Cek pemahaman paper</h3><div class="tw"><table><thead><tr><th>Soal</th><th>Jawaban klien</th><th>Status</th><th>Artinya untuk sesi</th>{th_slide}</tr></thead><tbody>{cp}</tbody></table></div></section>''')

    ag = "".join(f'<tr><td class="nw"><b>{esc(a["menit"])} mnt</b></td><td><b>{esc(a["blok"])}</b></td><td>{esc(a["fokus"])}{(" <span class='sl'>Slide " + esc(a["slide"]) + "</span>") if a.get("slide") else ""}</td></tr>' for a in t["agenda"])
    sec.append(f'<section><h2><span>3</span>Agenda 60 menit</h2><div class="tw"><table><tbody>{ag}</tbody></table></div></section>')

    rs = "".join(f'<label><input type="checkbox" data-id="r{i}"><span><b>{esc(r["slide"])}</b>{"".join(f' <em class="gp">Gap {esc(g)}</em>' for g in gaps_of(r))}: {esc(r["cek"])}</span></label>'
                 for i, r in enumerate(t["review_slide"], 1))
    sec.append(f'<section><h2><span>4</span>Review slide</h2><p class="hint">Cocokkan ke paper atau extract sebelum sesi; centang saat sudah dibahas.</p><div class="ck">{rs}</div></section>')

    for vid in t.get("visual", []):
        sec.append(VISUALS[vid])

    qs = []
    for i, s in enumerate(t["simulasi"], 1):
        lanj = f'<p><b>Pertanyaan lanjutan:</b> {esc(s["lanjutan"])}</p>' if s.get("lanjutan") else ""
        qs.append(f'''<details><summary><span class="qn">{i}</span><span class="qc">{esc(s.get("kategori", ""))}</span>{esc(s["pertanyaan"])}</summary>
<div class="ans"><p><b>Jawaban model:</b> {esc(s["jawaban_model"])}</p><p class="weak"><b>Tanda jawaban lemah:</b> {esc(s["tanda_lemah"])}</p>{lanj}</div></details>''')
    sec.append(f'''<section><h2><span>5</span>Simulasi tanya-jawab</h2>
<p class="hint">Urut dari area prioritas. Ajukan tanpa memberi petunjuk, beri waktu 1 menit, lalu umpan balik dengan teknik jawab 5 langkah. <button onclick="tog()" class="btn">Buka/tutup semua</button></p>{"".join(qs)}</section>''')

    sec.append(f'''<section><h2><span>6</span>Penutup sesi</h2>
<div class="two"><div><h3>Kandidat 3 perbaikan prioritas</h3><ol>{"".join(f"<li>{esc(x)}</li>" for x in t["perbaikan_kandidat"])}</ol>
<p class="hint">Sesuaikan dengan hasil sesi, lalu kirim lewat WhatsApp setelah sesi.</p></div>
<div><h3>Checklist H-0 untuk klien</h3>{ul(t["checklist_h0"])}</div></div>
<h3>Catatan tutor</h3><textarea id="nt" placeholder="Catatan selama sesi (tersimpan di browser ini saja)"></textarea>
<p class="hint">Setelah sesi: publish form post-zoom di admin dan kirim 3 perbaikan prioritas ke klien.</p></section>''')

    meta_rows = [("Penyaji", ", ".join(x for x in (m.get("penyaji"), m.get("prodi"), m.get("departemen")) if x)),
                 ("Paper", m.get("paper", "")), ("Presentasi", f'{m.get("jadwal_presentasi", "")} · {m.get("durasi_menit", "")} menit'),
                 ("Zoom", m.get("jadwal_zoom", "")), ("Layanan", m.get("layanan", "")), ("Sumber panduan", m.get("sumber", ""))]
    meta_html = "".join(f"<div><b>{esc(a)}</b><span>{esc(c)}</span></div>" for a, c in meta_rows if c and c.strip(" ·"))
    key = re.sub(r"\W+", "-", m.get("penyaji", "tutor") + m.get("jadwal_zoom", ""))[:48]
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Panduan Tutor Zoom</title><style>
:root{{--p:{pal["primary"]};--a:{pal["accent"]};--t:{pal["tint"]};--s:{pal["soft"]};--ink:#1d2430;--mut:#5b6472;--bg:#f7f8f6;--card:#fff;--line:#e3e6ea}}
@media (prefers-color-scheme:dark){{:root{{--ink:#e7eaef;--mut:#a5adba;--bg:#12161c;--card:#1b2129;--line:#2c3440;--t:#1f2d2c;--s:#1f2733}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 Inter,system-ui,-apple-system,Segoe UI,sans-serif}}
header{{background:var(--p);color:#fff;padding:36px 16px 56px}}header .in,main{{max-width:960px;margin:0 auto}}
header small{{letter-spacing:.14em;font-weight:700;opacity:.8}}header h1{{font-size:clamp(22px,3.4vw,30px);line-height:1.25;margin:8px 0 6px}}.conf{{display:inline-block;background:#fbdcdc;color:#9b1c1c;border-radius:20px;padding:2px 12px;font-size:12px;font-weight:700;margin-bottom:16px}}
.meta{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}}.meta div{{background:rgba(255,255,255,.1);border-radius:12px;padding:10px 14px}}
.meta b{{display:block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;opacity:.75}}main{{padding:0 16px 64px;margin-top:-32px}}
section{{background:var(--card);border-radius:18px;padding:24px clamp(16px,3vw,32px);margin-bottom:18px;box-shadow:0 6px 24px rgba(10,20,40,.07)}}
h2{{display:flex;align-items:center;gap:12px;font-size:22px;margin:0 0 12px;color:var(--a)}}h2 span{{background:var(--a);color:#fff;border-radius:50%;width:32px;height:32px;display:grid;place-items:center;font-size:15px;flex:none}}
h3{{font-size:16px;margin:16px 0 6px}}ul,ol{{padding-left:20px;margin:6px 0}}li{{margin:3px 0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px}}.grid div{{background:var(--s);border-radius:12px;padding:12px}}.grid b{{color:var(--a);font-size:13px;letter-spacing:.06em;text-transform:uppercase}}.grid p{{margin:4px 0 0}}
.two{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}}
.tw{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:14.5px;margin:6px 0}}th{{background:var(--p);color:#fff;text-align:left;padding:8px 10px}}td{{border-bottom:1px solid var(--line);padding:8px 10px;vertical-align:top}}.nw{{white-space:nowrap}}
.meter{{display:inline-block;width:90px;height:8px;background:var(--s);border-radius:8px;overflow:hidden;margin-right:8px;vertical-align:middle}}.meter i{{display:block;height:100%}}.meter i.ok{{background:#2e9e5b}}.meter i.mid{{background:#d4a017}}.meter i.bad{{background:#c53030}}
.j{{border-radius:20px;padding:2px 10px;font-size:13px;font-weight:600;white-space:nowrap}}.j.ok{{background:#d8f1e3;color:#156a3c}}.j.mid{{background:#fff0c2;color:#7a5a00}}.j.bad{{background:#fbdcdc;color:#9b1c1c}}
.pr li{{margin:6px 0}}details{{border:1px solid var(--line);border-radius:12px;margin:8px 0;padding:0 14px}}summary{{cursor:pointer;padding:12px 0;font-weight:600;list-style:none;display:flex;gap:10px;align-items:baseline}}
summary::-webkit-details-marker{{display:none}}.qn{{color:var(--a);font-weight:800}}.qc{{font-size:11px;letter-spacing:.06em;text-transform:uppercase;background:var(--t);color:var(--a);border-radius:20px;padding:1px 8px;white-space:nowrap}}
.ans p{{margin:4px 0 10px}}.weak{{color:#9b1c1c}}.sl{{display:inline-block;background:var(--t);color:var(--a);border-radius:20px;padding:0 10px;font-size:13px;font-weight:600}}.gp{{font-style:normal;font-size:11px;font-weight:700;background:var(--a);color:#fff;border-radius:20px;padding:1px 8px;margin-left:4px}}.hint{{color:var(--mut);font-size:14px}}.btn{{border:1px solid var(--a);color:var(--a);background:none;border-radius:20px;padding:3px 12px;cursor:pointer;margin-left:6px}}
.ck label{{display:flex;gap:10px;align-items:flex-start;padding:6px 0;cursor:pointer}}.ck input{{margin-top:5px;accent-color:var(--a);width:18px;height:18px;flex:none}}.ck input:checked+span{{color:var(--mut);text-decoration:line-through}}
textarea{{width:100%;min-height:140px;border:1px solid var(--line);border-radius:12px;padding:10px;font:inherit;background:var(--card);color:var(--ink)}}
@media print{{body{{background:#fff}}section{{box-shadow:none;border:1px solid #ddd;break-inside:avoid-page}}.btn{{display:none}}header{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}}}
</style></head><body><header><div class="in"><small>PANDUAN TUTOR SESI ZOOM</small><h1>{esc(m.get("judul_paper", m.get("paper", "")))}</h1>
<span class="conf">Internal tim, memuat kunci jawaban. Jangan dikirim ke klien.</span><div class="meta">{meta_html}</div></div></header>
<main>{"".join(sec)}</main><script>
const K="tutor-{esc(key)}";let st={{}};try{{st=JSON.parse(localStorage.getItem(K)||"{{}}")}}catch(e){{}}
function save(){{try{{localStorage.setItem(K,JSON.stringify(st))}}catch(e){{}}}}
document.querySelectorAll('.ck input').forEach(x=>{{x.checked=!!st[x.dataset.id];x.onchange=()=>{{st[x.dataset.id]=x.checked;save()}}}});
const nt=document.getElementById('nt');nt.value=st.nt||"";nt.oninput=()=>{{st.nt=nt.value;save()}};
function tog(){{const d=[...document.querySelectorAll('details')];const o=!d.every(x=>x.open);d.forEach(x=>x.open=o)}}
window.addEventListener('beforeprint',()=>document.querySelectorAll('details').forEach(x=>x.open=true));
</script></body></html>'''


def main():
    src, outdir = sys.argv[1], sys.argv[2]
    t = json.load(open(src, encoding="utf-8"))
    errs, warns = check(t)
    for w in warns:
        print("PERINGATAN:", w)
    for e in errs:
        print("MASALAH:", e)
    if errs:
        sys.exit(1)
    pal = PALETTES.get(t["meta"].get("warna", "navy"), PALETTES["navy"])
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, (t["meta"].get("nama_file") or "panduan-tutor") + ".html")
    open(path, "w", encoding="utf-8").write(build_html(t, pal))
    print(f"{len(t['simulasi'])} simulasi · {len(t['review_slide'])} titik review slide · {len(t['prioritas'])} prioritas")
    print("OK:", path)


if __name__ == "__main__":
    main()
