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


def build_html(t, pal):
    m, k = t["meta"], t["kebutuhan"]
    sec = []
    keb = [("Tujuan sesi", k.get("tujuan", "")), ("Kekhawatiran", k.get("kekhawatiran", "")),
           ("Pengalaman JR", k.get("pengalaman", "")), ("Status slide", k.get("status_slide", "")),
           ("Gaya konsulen", k.get("gaya_konsulen", ""))]
    keb_html = "".join(f'<div><b>{esc(a)}</b><p>{esc(c)}</p></div>' for a, c in keb if c)
    sec.append(f'<section><h2><span>1</span>Kebutuhan klien</h2><div class="grid">{keb_html}</div></section>')

    sr = "".join(f'<tr><td>{esc(r["area"])}</td><td class="nw">{bar(r.get("skor"))}</td></tr>' for r in t["self_rating"])
    cp = "".join(
        f'<tr><td>{esc(c.get("soal", ""))}</td><td>{esc(c.get("jawaban", ""))}</td>'
        f'<td><span class="j {"ok" if c["status"] == "benar" else "bad" if c["status"] in ("salah", "kosong") else "mid"}">{esc(c["status"])}</span></td>'
        f'<td>{esc(c.get("makna", ""))}</td></tr>' for c in t["cek_pemahaman"])
    pr = "".join(f'<li><b>{esc(p["area"])}</b>: {esc(p["alasan"])}</li>' for p in t["prioritas"])
    sec.append(f'''<section><h2><span>2</span>Peta gap</h2>
<div class="two"><div><h3>Penilaian diri (pre-zoom)</h3><table><tbody>{sr}</tbody></table></div>
<div><h3>Area prioritas sesi</h3><ol class="pr">{pr}</ol></div></div>
<h3>Cek pemahaman paper</h3><div class="tw"><table><thead><tr><th>Soal</th><th>Jawaban klien</th><th>Status</th><th>Artinya untuk sesi</th></tr></thead><tbody>{cp}</tbody></table></div></section>''')

    ag = "".join(f'<tr><td class="nw"><b>{esc(a["menit"])} mnt</b></td><td><b>{esc(a["blok"])}</b></td><td>{esc(a["fokus"])}</td></tr>' for a in t["agenda"])
    sec.append(f'<section><h2><span>3</span>Agenda 60 menit</h2><div class="tw"><table><tbody>{ag}</tbody></table></div></section>')

    rs = "".join(f'<label><input type="checkbox" data-id="r{i}"><span><b>{esc(r["slide"])}</b>: {esc(r["cek"])}</span></label>'
                 for i, r in enumerate(t["review_slide"], 1))
    sec.append(f'<section><h2><span>4</span>Review slide</h2><p class="hint">Cocokkan ke paper atau extract sebelum sesi; centang saat sudah dibahas.</p><div class="ck">{rs}</div></section>')

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
.ans p{{margin:4px 0 10px}}.weak{{color:#9b1c1c}}.hint{{color:var(--mut);font-size:14px}}.btn{{border:1px solid var(--a);color:var(--a);background:none;border-radius:20px;padding:3px 12px;cursor:pointer;margin-left:6px}}
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
