#!/usr/bin/env python3
"""Bangun Brief & Checklist Persiapan journal reading dari satu brief.json
menjadi DOCX (untuk dicetak/diedit) dan HTML mandiri (checklist bisa dicentang).

Pakai:
  uv run --with python-docx python3 build_brief.py brief.json outdir/

Skema brief.json: lihat references/brief-schema.md (contoh lengkap: references/brief-example.json).
Script memeriksa: field wajib, em dash, jumlah kata (target 2.200-4.000 kata), sisa penanda [CEK].
"""
import html, json, os, re, sys

PALETTES = {
    "navy":   {"primary": "#0b2545", "accent": "#13807a", "tint": "#e3f2f0", "soft": "#e6edf5"},
    "maroon": {"primary": "#4a1520", "accent": "#a3313f", "tint": "#f7e8ea", "soft": "#f5eaec"},
    "hijau":  {"primary": "#1e3a2b", "accent": "#3f7d3a", "tint": "#eaf3e6", "soft": "#e8f0e4"},
}
REQUIRED = ["meta", "ringkasan", "bottom_line", "konteks", "paper", "appraisal",
            "kekuatan", "kelemahan", "rencana_presentasi", "pertanyaan", "checklist", "referensi"]


KP_HEAD = ["No", "Klaim kunci", "Bukti pendukung", "Kekuatan bukti", "Cek sitasi & catatan"]
REC_HEAD = ["No", "Rekomendasi", "COR", "LOE", "Bukti dasar", "Status & catatan"]
CMP_HEAD = ["Topik", "Guideline ini", "Pembanding", "Catatan"]
EDISI_HEAD = ["Topik", "Perubahan", "Edisi sebelumnya", "Edisi ini"]


def is_guideline(b):
    """Mode guideline aktif bila paper.rekomendasi ada (lihat references/jalur-guideline.md)."""
    return bool(b.get("paper", {}).get("rekomendasi"))


def is_review(b):
    """Mode review (narrative/scoping) aktif bila paper.poin_kunci ada (lihat references/jalur-review.md)."""
    return bool(b.get("paper", {}).get("poin_kunci"))


def kp_rows(pa):
    return [[r["no"], (f'[{r["bagian"]}] ' if r.get("bagian") else "") + r["klaim"], r["bukti"], r["kekuatan"],
             " · ".join(x for x in (r.get("cek_sitasi", ""), r.get("catatan", "")) if x)] for r in pa["poin_kunci"]]


def rec_rows(pa):
    return [[r["no"], (f'[{r["bagian"]}] ' if r.get("bagian") else "") + r["teks"], r["cor"], r["loe"], r["bukti"],
             " · ".join(x for x in (r.get("status", ""), r.get("catatan", "")) if x)] for r in pa["rekomendasi"]]


def edisi_rows(pa):
    return [[c.get("topik", ""), c.get("jenis", ""), c.get("lama", ""), c.get("baru", "")] for c in pa.get("perbandingan_edisi", [])]


def cmp_rows(pa):
    return [[c.get("topik", ""), c.get("guideline_ini", c.get("review_ini", "")), c.get("pembanding", ""), c.get("catatan", "")]
            for c in pa.get("perbandingan", [])]


def words(obj):
    if isinstance(obj, str):
        return len(obj.split())
    if isinstance(obj, dict):
        return sum(words(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(words(v) for v in obj)
    return 0


LOKASI = re.compile(r"(\be\d{2,4}\b|hal\.?|halaman|tabel|table|figure|gambar|fig\.|suppl|appendix|lampiran|metode|methods|abstrak|abstract|tidak dilaporkan|not reported)", re.I)
# (kata kunci di meta.tool_appraisal, jumlah minimum baris per item, apakah error bila kurang, nama)
ITEM_MIN = [
    ("newcastle", 7, True, "NOS (7 item cross-sectional, 8 item kohort/case-control)"),
    ("nos", 7, True, "NOS (7 item cross-sectional, 8 item kohort/case-control)"),
    ("amstar", 16, True, "AMSTAR 2 (16 item)"),
    ("agree", 23, True, "AGREE II (23 item; boleh ditambah baris skor domain)"),
    ("sanra", 6, True, "SANRA (6 item)"),
    ("prisma-scr", 6, True, "PRISMA-ScR (6 aspek)"),
    ("quadas", 11, False, "QUADAS-2 (11 signalling question: 3+2+2+4)"),
    ("rob 2", 20, False, "RoB 2 (pertanyaan penuntun per domain, sekitar 20 baris)"),
]


def check_validity(b):
    """Appraisal berbasis instrumen: tiap baris = satu ITEM, wajib ada bukti berlokasi dan alasan penilaian."""
    errs = []
    ap = b.get("appraisal", {})
    rows = ap.get("validity", [])
    tool = b.get("meta", {}).get("tool_appraisal", "").lower()
    for i, v in enumerate(rows, 1):
        nama = v.get("domain", f"baris {i}")
        if not v.get("rangkuman") and (not str(v.get("bukti", "")).strip() or not LOKASI.search(str(v.get("bukti", "")))):
            errs.append(f"validity '{nama}': 'bukti' harus memuat lokasi di paper (hal./tabel/figure) atau 'tidak dilaporkan'")
        al = str(v.get("alasan", "")).strip()
        if len(al.split()) < 8:
            errs.append(f"validity '{nama}': 'alasan' wajib (min 8 kata): jelaskan MENGAPA dinilai demikian, "
                        "hubungkan bukti di paper dengan kriteria item instrumen, bukan mengulang bukti")
    for kunci, minimum, keras, nama in ITEM_MIN:
        if kunci in tool:
            if len(rows) < minimum:
                msg = (f"validity hanya {len(rows)} baris; {nama} harus dibreakdown PER ITEM (min {minimum} baris), "
                       "bukan ringkasan per domain")
                if keras:
                    errs.append(msg)
                else:
                    print("PERINGATAN:", msg)
            break
    return errs


def check(b):
    errs, warns = [], []
    for k in REQUIRED:
        if k not in b:
            errs.append(f"field wajib hilang: {k}")
    pa = b.get("paper", {})
    if is_guideline(b):
        for i, r in enumerate(pa["rekomendasi"], 1):
            for f in ("no", "teks", "cor", "loe", "bukti"):
                if not str(r.get(f, "")).strip():
                    errs.append(f"rekomendasi ke-{i}: field '{f}' kosong")
        sp = b.get("meta", {}).get("sumber_perbandingan", "")
        if not sp:
            errs.append("meta.sumber_perbandingan kosong: tulis sumber perbandingan dengan edisi sebelumnya (bagian atau tabel "
                        "perubahan di guideline ini + halaman, atau PDF edisi lama yang dilampirkan), atau 'edisi pertama' "
                        "bila guideline ini tidak punya edisi sebelumnya")
        elif not sp.lower().startswith("edisi pertama") and not b.get("paper", {}).get("perbandingan_edisi"):
            errs.append("paper.perbandingan_edisi kosong: slide Perbandingan dengan Edisi Sebelumnya wajib pada jalur guideline")
        if not b.get("meta", {}).get("rekomendasi_disetujui"):
            errs.append("meta.rekomendasi_disetujui kosong: tulis siapa yang menyetujui pilihan rekomendasi dan kapan "
                        "(gerbang persetujuan peta rekomendasi belum dilewati?)")
    elif is_review(b):
        for i, r in enumerate(pa["poin_kunci"], 1):
            for f in ("no", "klaim", "bukti", "kekuatan"):
                if not str(r.get(f, "")).strip():
                    errs.append(f"poin kunci ke-{i}: field '{f}' kosong")
        if not b.get("meta", {}).get("poin_disetujui"):
            errs.append("meta.poin_disetujui kosong: tulis siapa yang menyetujui pilihan poin kunci dan kapan "
                        "(gerbang persetujuan peta isi belum dilewati?)")
    elif "paper" in b:
        for f in ("pico", "hasil"):
            if f not in pa:
                errs.append(f"field wajib hilang: paper.{f} (atau paper.rekomendasi untuk guideline, paper.poin_kunci untuk review)")
    errs.extend(check_validity(b))
    raw = json.dumps(b, ensure_ascii=False)
    if "\u2014" in raw:
        errs.append("ada em dash di brief.json; ganti dengan koma, titik dua, atau kurung")
    n = words(b)
    if n < 2200:
        warns.append(f"{n} kata: terlalu pendek untuk brief ukuran sedang (target 2.200-4.000)")
    elif n > 4000 + words(b.get("appraisal", {}).get("validity", [])):
        warns.append(f"{n} kata: terlalu panjang, pangkas (target 2.200-4.000)")
    ceks = len(re.findall(r"\[CEK", raw))
    if ceks:
        warns.append(f"{ceks} penanda [CEK] masih ada; pastikan juga tercantum di 'cek_ulang'")
    q = len(b.get("pertanyaan", []))
    if not 10 <= q <= 16:
        warns.append(f"{q} mockup pertanyaan; target 10-16")
    return errs, warns, n


# ---------------------------------------------------------------- HTML
def esc(s):
    return html.escape(str(s))


def ul(items):
    return "<ul>" + "".join(f"<li>{esc(i)}</li>" for i in items) + "</ul>"


def table(headers, rows, cls=""):
    h = "".join(f"<th>{esc(x)}</th>" for x in headers)
    body = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw"><table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{body}</tbody></table></div>'


def judgement_cls(s, kelas=None):
    """kelas ('ok' | 'mid' | 'bad') menimpa tebakan dari teks; dipakai untuk skor AGREE II (angka/persen)."""
    if kelas in ("ok", "mid", "bad"):
        return kelas
    s = s.lower()
    if any(k in s for k in ("high", "tinggi", "berisiko", "kritis", "buruk")):
        return "bad"
    if any(k in s for k in ("some", "unclear", "sedang", "moderate", "tidak jelas")):
        return "mid"
    return "ok"


def build_html(b, pal):
    m = b["meta"]
    k = b["konteks"]
    pa = b["paper"]
    ap = b["appraisal"]
    sec = []
    sec.append(f'''<section><h2><span>1</span>Ringkasan</h2><p>{esc(b["ringkasan"])}</p>
<div class="bl"><b>Take-home message</b>{esc(b["bottom_line"])}</div></section>''')

    ctx = []
    for key, label in (("penyakit", "Masalah klinis"), ("standar_terapi", "Tata laksana saat ini"),
                       ("mekanisme", "Dasar ilmu / mekanisme")):
        if k.get(key):
            ctx.append(f"<h3>{label}</h3>{ul(k[key])}")
    if k.get("istilah"):
        ctx.append("<h3>Istilah yang wajib dikuasai</h3>" +
                   table(["Istilah", "Arti singkat"], [[i["istilah"], i["arti"]] for i in k["istilah"]]))
    sec.append(f'<section><h2><span>2</span>Konteks & dasar ilmu</h2>{"".join(ctx)}</section>')

    if is_guideline(b):
        parts = ['<section><h2><span>3</span>Isi guideline</h2>']
        if pa.get("ruang_lingkup"):
            parts.append("<h3>Ruang lingkup</h3>" + ul(pa["ruang_lingkup"]))
        parts.append("<h3>Metodologi penyusunan</h3>" + ul(pa["desain"]))
        parts.append(f'<h3>Rekomendasi yang dipresentasikan ({len(pa["rekomendasi"])})</h3>'
                     f'<p class="ov">Dipilih lewat peta rekomendasi, disetujui: {esc(m.get("rekomendasi_disetujui", ""))}</p>'
                     + table(REC_HEAD, rec_rows(pa)))
        if pa.get("perbandingan_edisi"):
            parts.append("<h3>Perbandingan dengan edisi sebelumnya</h3>"
                         + f'<p class="ov">Sumber: {esc(m.get("sumber_perbandingan", ""))}</p>' + table(EDISI_HEAD, edisi_rows(pa)))
        if pa.get("perbandingan"):
            parts.append("<h3>Perbandingan dengan PNPK dan guideline lain</h3>" + table(CMP_HEAD, cmp_rows(pa)))
        if pa.get("tidak_dipresentasikan"):
            parts.append("<h3>Bagian yang tidak dipresentasikan (siap bila ditanya)</h3>" + ul(pa["tidak_dipresentasikan"]))
        if pa.get("angka_kunci"):
            parts.append("<h3>Angka kunci dari studi pendukung</h3>" + ul(pa["angka_kunci"]))
        sec.append("".join(parts) + "</section>")
    elif is_review(b):
        parts = ['<section><h2><span>3</span>Isi review</h2>']
        if pa.get("ruang_lingkup"):
            parts.append("<h3>Ruang lingkup & pertanyaan</h3>" + ul(pa["ruang_lingkup"]))
        parts.append("<h3>Metode penelusuran & penulisan</h3>" + ul(pa["desain"]))
        parts.append(f'<h3>Poin kunci yang dipresentasikan ({len(pa["poin_kunci"])})</h3>'
                     f'<p class="ov">Dipilih lewat peta isi, disetujui: {esc(m.get("poin_disetujui", ""))}</p>'
                     + table(KP_HEAD, kp_rows(pa)))
        if pa.get("perbandingan"):
            parts.append("<h3>Perbandingan dengan guideline, PNPK, dan review lain</h3>" + table(["Topik", "Review ini", "Pembanding", "Catatan"], cmp_rows(pa)))
        if pa.get("tidak_dipresentasikan"):
            parts.append("<h3>Bagian yang tidak dipresentasikan (siap bila ditanya)</h3>" + ul(pa["tidak_dipresentasikan"]))
        if pa.get("angka_kunci"):
            parts.append("<h3>Angka kunci dari sumber primer</h3>" + ul(pa["angka_kunci"]))
        sec.append("".join(parts) + "</section>")
    else:
        pico = pa["pico"]
        pico_html = '<div class="pico">' + "".join(
            f'<div><b>{x}</b><p>{esc(pico.get(x, ""))}</p></div>' for x in ("P", "I", "C", "O")) + "</div>"
        res = table(["Outcome", "Intervensi", "Kontrol", "Efek (95% CI)", "Catatan"],
                    [[r["outcome"], r["intervensi"], r["kontrol"], r["efek"], r.get("catatan", "")] for r in pa["hasil"]])
        sec.append(f'''<section><h2><span>3</span>Isi paper</h2>{pico_html}<h3>Desain & metode</h3>{ul(pa["desain"])}
<h3>Hasil utama</h3>{res}{("<h3>Angka kunci (sudah dihitung ulang)</h3>" + ul(pa["angka_kunci"])) if pa.get("angka_kunci") else ""}</section>''')

    vrows, _last = "", None
    for v in ap["validity"]:
        kel = v.get("kelompok", "")
        kcell = esc(kel) if kel and kel != _last else ""
        _last = kel or _last
        vrows += (f'<tr><td>{kcell}</td><td>{esc(v["domain"])}</td><td><span class="j {judgement_cls(v["penilaian"], v.get("kelas"))}">{esc(v["penilaian"])}</span></td>'
                  f'<td>{esc(v["bukti"])}</td><td>{esc(v["alasan"])}</td></tr>')
    g = ap.get("grade", {})
    sec.append(f'''<section><h2><span>4</span>Critical appraisal</h2>
<h3>Validity ({esc(m.get("tool_appraisal", ""))})</h3>
<div class="tw"><table><thead><tr><th>Kelompok</th><th>Item</th><th>Penilaian</th><th>Bukti di paper</th><th>Mengapa dinilai demikian</th></tr></thead><tbody>{vrows}</tbody></table></div>
<p class="ov"><b>Kesimpulan validity:</b> {esc(ap["validity_overall"])}</p>
<div class="two"><div><h3>Importance</h3>{ul(ap["importance"])}</div><div><h3>Applicability</h3>{ul(ap["applicability"])}</div></div>
{f'<p class="ov"><b>GRADE ({esc(g.get("outcome", "outcome primer"))}): {esc(g.get("rating", ""))}.</b> {esc(g.get("alasan", ""))}</p>' if g else ""}
<div class="two"><div><h3>Kekuatan</h3>{ul(b["kekuatan"])}</div><div><h3>Kelemahan</h3>{ul(b["kelemahan"])}</div></div></section>''')

    plan = table(["Slide", "Pesan yang harus tersampaikan", "Menit"],
                 [[r["slide"], r["pesan"], r["menit"]] for r in b["rencana_presentasi"]], "plan")
    total = sum(float(r["menit"]) for r in b["rencana_presentasi"])
    sec.append(f'''<section><h2><span>5</span>Apa yang dipresentasikan</h2>
<p>Total sekitar {total:g} menit presentasi dari alokasi {esc(m.get("durasi_menit", ""))} menit (sisanya diskusi).</p>{plan}</section>''')

    qs = []
    for i, q in enumerate(b["pertanyaan"], 1):
        qs.append(f'''<details><summary><span class="qn">{i}</span><span class="qc">{esc(q.get("kategori", ""))}</span>{esc(q["pertanyaan"])}</summary>
<div class="ans"><b>Jawaban model:</b> {esc(q["jawaban"])}</div></details>''')
    sec.append(f'''<section><h2><span>6</span>Mockup pertanyaan konsulen</h2>
<p class="hint">Coba jawab dulu dengan suara keras, baru buka jawabannya. <button onclick="tog()" class="btn">Buka/tutup semua</button></p>{"".join(qs)}</section>''')

    ck = []
    cid = 0
    for grp in b["checklist"]:
        items = []
        for it in grp["items"]:
            cid += 1
            items.append(f'<label><input type="checkbox" data-id="c{cid}"><span>{esc(it)}</span></label>')
        ck.append(f'<div class="ckg"><h3>{esc(grp["waktu"])}</h3>{"".join(items)}</div>')
    sec.append(f'''<section><h2><span>7</span>Checklist persiapan</h2>
<div class="prog"><div id="bar"></div></div><p id="cnt" class="hint"></p>{"".join(ck)}</section>''')

    extra = ""
    if b.get("cek_ulang"):
        extra = f'<div class="warn"><b>Wajib dicek ulang ke paper sebelum maju</b>{ul(b["cek_ulang"])}</div>'
    refs = "<ol>" + "".join(f"<li>{esc(r)}</li>" for r in b["referensi"]) + "</ol>"
    sec.append(f'<section><h2><span>8</span>Referensi</h2>{extra}{refs}</section>')

    meta_rows = [("Paper", m.get("sitasi", "")), ("Penyaji", f'{m.get("penyaji", "")}, {m.get("prodi", "")}'),
                 ("Pembimbing", m.get("pembimbing", "")), ("Jadwal", f'{m.get("tanggal", "")} · {m.get("durasi_menit", "")} menit'),
                 ("Desain studi", m.get("desain_studi", ""))]
    meta_html = "".join(f"<div><b>{esc(a)}</b><span>{esc(c)}</span></div>" for a, c in meta_rows if c and c != ", ")
    key = re.sub(r"\W+", "-", m.get("judul_paper", "brief"))[:40]
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Brief Journal Reading</title><style>
:root{{--p:{pal["primary"]};--a:{pal["accent"]};--t:{pal["tint"]};--s:{pal["soft"]};--ink:#1d2430;--mut:#5b6472;--bg:#f7f8f6;--card:#fff;--line:#e3e6ea}}
@media (prefers-color-scheme:dark){{:root{{--ink:#e7eaef;--mut:#a5adba;--bg:#12161c;--card:#1b2129;--line:#2c3440;--t:#1f2d2c;--s:#1f2733}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 Inter,system-ui,-apple-system,Segoe UI,sans-serif}}
header{{background:var(--p);color:#fff;padding:40px 16px 56px}}header .in,main{{max-width:960px;margin:0 auto}}
header small{{letter-spacing:.14em;font-weight:700;opacity:.8}}header h1{{font-size:clamp(22px,3.4vw,32px);line-height:1.25;margin:8px 0 20px}}
.meta{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px}}.meta div{{background:rgba(255,255,255,.1);border-radius:12px;padding:10px 14px}}
.meta b{{display:block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;opacity:.75}}main{{padding:0 16px 64px;margin-top:-32px}}
section{{background:var(--card);border-radius:18px;padding:24px clamp(16px,3vw,32px);margin-bottom:18px;box-shadow:0 6px 24px rgba(10,20,40,.07)}}
h2{{display:flex;align-items:center;gap:12px;font-size:22px;margin:0 0 12px;color:var(--a)}}h2 span{{background:var(--a);color:#fff;border-radius:50%;width:32px;height:32px;display:grid;place-items:center;font-size:15px;flex:none}}
h3{{font-size:16px;margin:18px 0 6px}}ul{{padding-left:20px;margin:6px 0}}li{{margin:3px 0}}
.bl{{background:var(--t);border-left:5px solid var(--a);border-radius:10px;padding:12px 16px;margin-top:12px}}.bl b{{display:block;font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--a)}}
.tw{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:14.5px;margin:6px 0}}th{{background:var(--p);color:#fff;text-align:left;padding:8px 10px}}td{{border-bottom:1px solid var(--line);padding:8px 10px;vertical-align:top}}
.pico{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}}.pico div{{background:var(--s);border-radius:12px;padding:12px}}.pico b{{color:var(--a);font-size:20px}}.pico p{{margin:4px 0 0}}
.two{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}}.ov{{background:var(--s);border-radius:10px;padding:10px 14px}}
.j{{border-radius:20px;padding:2px 10px;font-size:13px;font-weight:600;white-space:nowrap}}.j.ok{{background:#d8f1e3;color:#156a3c}}.j.mid{{background:#fff0c2;color:#7a5a00}}.j.bad{{background:#fbdcdc;color:#9b1c1c}}
details{{border:1px solid var(--line);border-radius:12px;margin:8px 0;padding:0 14px}}summary{{cursor:pointer;padding:12px 0;font-weight:600;list-style:none;display:flex;gap:10px;align-items:baseline}}
summary::-webkit-details-marker{{display:none}}.qn{{color:var(--a);font-weight:800}}.qc{{font-size:11px;letter-spacing:.06em;text-transform:uppercase;background:var(--t);color:var(--a);border-radius:20px;padding:1px 8px;white-space:nowrap}}
.ans{{padding:0 0 12px;color:var(--ink)}}.hint{{color:var(--mut);font-size:14px}}.btn{{border:1px solid var(--a);color:var(--a);background:none;border-radius:20px;padding:3px 12px;cursor:pointer;margin-left:6px}}
.ckg label{{display:flex;gap:10px;align-items:flex-start;padding:6px 0;cursor:pointer}}.ckg input{{margin-top:5px;accent-color:var(--a);width:18px;height:18px;flex:none}}.ckg input:checked+span{{color:var(--mut);text-decoration:line-through}}
.prog{{height:10px;background:var(--s);border-radius:10px;overflow:hidden}}#bar{{height:100%;width:0;background:var(--a);transition:width .3s}}
.warn{{background:#fff4d6;color:#5c4400;border-radius:12px;padding:12px 16px;margin-bottom:12px}}
@media print{{body{{background:#fff}}section{{box-shadow:none;border:1px solid #ddd;break-inside:avoid-page}}details{{break-inside:avoid}}details .ans{{display:block}}.btn{{display:none}}header{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}}}
</style></head><body><header><div class="in"><small>BRIEF & CHECKLIST JOURNAL READING</small><h1>{esc(m.get("judul_paper", ""))}</h1><div class="meta">{meta_html}</div></div></header>
<main>{"".join(sec)}</main><script>
const K="jr-{esc(key)}";let st={{}};try{{st=JSON.parse(localStorage.getItem(K)||"{{}}")}}catch(e){{}}
const bx=[...document.querySelectorAll('.ckg input')];function upd(){{const d=bx.filter(x=>x.checked).length;document.getElementById('bar').style.width=(d/bx.length*100)+'%';document.getElementById('cnt').textContent=d+' dari '+bx.length+' selesai'}}
bx.forEach(x=>{{x.checked=!!st[x.dataset.id];x.onchange=()=>{{st[x.dataset.id]=x.checked;try{{localStorage.setItem(K,JSON.stringify(st))}}catch(e){{}}upd()}}}});upd();
function tog(){{const d=[...document.querySelectorAll('details')];const o=!d.every(x=>x.open);d.forEach(x=>x.open=o)}}
window.addEventListener('beforeprint',()=>document.querySelectorAll('details').forEach(x=>x.open=true));
</script></body></html>'''


# ---------------------------------------------------------------- DOCX
def build_docx(b, pal, path):
    from docx import Document
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Pt, RGBColor, Cm

    def rgb(h):
        h = h.lstrip("#")
        return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

    def shade(cell, hexcolor):
        tcPr = cell._tc.get_or_add_tcPr()
        sh = OxmlElement("w:shd")
        sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), hexcolor.lstrip("#"))
        tcPr.append(sh)

    doc = Document()
    for s in doc.sections:
        s.left_margin = s.right_margin = Cm(2); s.top_margin = s.bottom_margin = Cm(1.8)
    st = doc.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(10.5)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    for lvl, size in ((1, 15), (2, 12)):
        hs = doc.styles[f"Heading {lvl}"]; hs.font.name = "Calibri"; hs.font.size = Pt(size)
        hs.font.color.rgb = rgb(pal["accent"] if lvl == 1 else pal["primary"]); hs.font.bold = True

    def para(text, bold=False, size=None, color=None, italic=False):
        p = doc.add_paragraph(); r = p.add_run(text); r.bold = bold; r.italic = italic
        if size: r.font.size = Pt(size)
        if color: r.font.color.rgb = rgb(color)
        p.paragraph_format.space_after = Pt(4)
        return p

    def bullets(items):
        for i in items:
            p = doc.add_paragraph(str(i), style="List Bullet"); p.paragraph_format.space_after = Pt(2)

    def tbl(headers, rows, widths=None):
        t = doc.add_table(rows=1, cols=len(headers)); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
        for i, h in enumerate(headers):
            c = t.rows[0].cells[i]; c.text = ""; r = c.paragraphs[0].add_run(str(h)); r.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255); r.font.size = Pt(9.5); shade(c, pal["primary"])
        for row in rows:
            cells = t.add_row().cells
            for i, v in enumerate(row):
                cells[i].text = ""; r = cells[i].paragraphs[0].add_run(str(v)); r.font.size = Pt(9.5)
        if widths:
            for row in t.rows:
                for i, w in enumerate(widths):
                    row.cells[i].width = Cm(w)
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        return t

    m, k, pa, ap = b["meta"], b["konteks"], b["paper"], b["appraisal"]
    para("BRIEF & CHECKLIST JOURNAL READING", bold=True, size=9, color=pal["accent"])
    para(m.get("judul_paper", ""), bold=True, size=17, color=pal["primary"])
    mt = doc.add_table(rows=0, cols=2); mt.style = "Table Grid"
    for a, c in (("Paper", m.get("sitasi", "")), ("Penyaji", f'{m.get("penyaji", "")}, {m.get("prodi", "")}'),
                 ("Pembimbing", m.get("pembimbing", "")), ("Jadwal", f'{m.get("tanggal", "")} · {m.get("durasi_menit", "")} menit'),
                 ("Desain studi", m.get("desain_studi", ""))):
        if not c or c == ", ":
            continue
        cells = mt.add_row().cells
        cells[0].text = ""; r = cells[0].paragraphs[0].add_run(a); r.bold = True; r.font.size = Pt(9.5); shade(cells[0], pal["soft"])
        cells[1].text = ""; cells[1].paragraphs[0].add_run(c).font.size = Pt(9.5)
        cells[0].width = Cm(3.5); cells[1].width = Cm(13.5)

    doc.add_heading("1. Ringkasan", 1); para(b["ringkasan"])
    t = doc.add_table(rows=1, cols=1); c = t.rows[0].cells[0]; shade(c, pal["tint"]); c.text = ""
    r = c.paragraphs[0].add_run("Take-home message: "); r.bold = True; r.font.color.rgb = rgb(pal["accent"])
    c.paragraphs[0].add_run(b["bottom_line"])

    doc.add_heading("2. Konteks & dasar ilmu", 1)
    for key, label in (("penyakit", "Masalah klinis"), ("standar_terapi", "Tata laksana saat ini"), ("mekanisme", "Dasar ilmu / mekanisme")):
        if k.get(key):
            doc.add_heading(label, 2); bullets(k[key])
    if k.get("istilah"):
        doc.add_heading("Istilah yang wajib dikuasai", 2)
        tbl(["Istilah", "Arti singkat"], [[i["istilah"], i["arti"]] for i in k["istilah"]], [4, 13])

    if is_guideline(b):
        doc.add_heading("3. Isi guideline", 1)
        if pa.get("ruang_lingkup"):
            doc.add_heading("Ruang lingkup", 2); bullets(pa["ruang_lingkup"])
        doc.add_heading("Metodologi penyusunan", 2); bullets(pa["desain"])
        doc.add_heading(f'Rekomendasi yang dipresentasikan ({len(pa["rekomendasi"])})', 2)
        para(f'Dipilih lewat peta rekomendasi, disetujui: {m.get("rekomendasi_disetujui", "")}', italic=True, size=9.5, color="#5b6472")
        tbl(REC_HEAD, rec_rows(pa), [1.3, 6.2, 1.2, 1.3, 3.8, 3.2])
        if pa.get("perbandingan_edisi"):
            doc.add_heading("Perbandingan dengan edisi sebelumnya", 2)
            para(f'Sumber: {m.get("sumber_perbandingan", "")}', italic=True, size=9.5, color="#5b6472")
            tbl(EDISI_HEAD, edisi_rows(pa), [3, 2, 6, 6])
        if pa.get("perbandingan"):
            doc.add_heading("Perbandingan dengan PNPK dan guideline lain", 2)
            tbl(CMP_HEAD, cmp_rows(pa), [3, 4.7, 4.7, 4.6])
        if pa.get("tidak_dipresentasikan"):
            doc.add_heading("Bagian yang tidak dipresentasikan (siap bila ditanya)", 2); bullets(pa["tidak_dipresentasikan"])
        if pa.get("angka_kunci"):
            doc.add_heading("Angka kunci dari studi pendukung", 2); bullets(pa["angka_kunci"])
    elif is_review(b):
        doc.add_heading("3. Isi review", 1)
        if pa.get("ruang_lingkup"):
            doc.add_heading("Ruang lingkup & pertanyaan", 2); bullets(pa["ruang_lingkup"])
        doc.add_heading("Metode penelusuran & penulisan", 2); bullets(pa["desain"])
        doc.add_heading(f'Poin kunci yang dipresentasikan ({len(pa["poin_kunci"])})', 2)
        para(f'Dipilih lewat peta isi, disetujui: {m.get("poin_disetujui", "")}', italic=True, size=9.5, color="#5b6472")
        tbl(KP_HEAD, kp_rows(pa), [1.3, 5.5, 4.2, 2.5, 3.5])
        if pa.get("perbandingan"):
            doc.add_heading("Perbandingan dengan guideline, PNPK, dan review lain", 2)
            tbl(["Topik", "Review ini", "Pembanding", "Catatan"], cmp_rows(pa), [3, 4.7, 4.7, 4.6])
        if pa.get("tidak_dipresentasikan"):
            doc.add_heading("Bagian yang tidak dipresentasikan (siap bila ditanya)", 2); bullets(pa["tidak_dipresentasikan"])
        if pa.get("angka_kunci"):
            doc.add_heading("Angka kunci dari sumber primer", 2); bullets(pa["angka_kunci"])
    else:
        doc.add_heading("3. Isi paper", 1)
        tbl(["", "PICO"], [[x, pa["pico"].get(x, "")] for x in ("P", "I", "C", "O")], [1.2, 15.8])
        doc.add_heading("Desain & metode", 2); bullets(pa["desain"])
        doc.add_heading("Hasil utama", 2)
        tbl(["Outcome", "Intervensi", "Kontrol", "Efek (95% CI)", "Catatan"],
            [[r["outcome"], r["intervensi"], r["kontrol"], r["efek"], r.get("catatan", "")] for r in pa["hasil"]], [3.4, 2.8, 2.8, 3.6, 4.4])
        if pa.get("angka_kunci"):
            doc.add_heading("Angka kunci (sudah dihitung ulang)", 2); bullets(pa["angka_kunci"])

    doc.add_heading("4. Critical appraisal", 1)
    doc.add_heading(f'Validity ({m.get("tool_appraisal", "")})', 2)
    _vr, _last = [], None
    for v in ap["validity"]:
        kel = v.get("kelompok", "")
        _vr.append([kel if kel and kel != _last else "", v["domain"], v["penilaian"], v["bukti"], v["alasan"]])
        _last = kel or _last
    vt = tbl(["Kelompok", "Item", "Penilaian", "Bukti di paper", "Mengapa dinilai demikian"], _vr, [2.2, 3.0, 2.0, 4.6, 5.2])
    colors = {"ok": "d8f1e3", "mid": "fff0c2", "bad": "fbdcdc"}
    for i, v in enumerate(ap["validity"], 1):
        shade(vt.rows[i].cells[2], colors[judgement_cls(v["penilaian"], v.get("kelas"))])
    p = para(""); p.add_run("Kesimpulan validity: ").bold = True; p.add_run(ap["validity_overall"])
    doc.add_heading("Importance", 2); bullets(ap["importance"])
    doc.add_heading("Applicability", 2); bullets(ap["applicability"])
    g = ap.get("grade")
    if g:
        p = para(""); p.add_run(f'GRADE ({g.get("outcome", "outcome primer")}): {g.get("rating", "")}. ').bold = True; p.add_run(g.get("alasan", ""))
    doc.add_heading("Kekuatan", 2); bullets(b["kekuatan"])
    doc.add_heading("Kelemahan", 2); bullets(b["kelemahan"])

    doc.add_heading("5. Apa yang dipresentasikan", 1)
    tbl(["Slide", "Pesan yang harus tersampaikan", "Menit"], [[r["slide"], r["pesan"], r["menit"]] for r in b["rencana_presentasi"]], [4, 11.5, 1.5])

    doc.add_heading("6. Mockup pertanyaan konsulen", 1)
    para("Tutup kolom jawaban, jawab dengan suara keras, lalu bandingkan.", italic=True, size=9.5, color="#5b6472")
    for i, q in enumerate(b["pertanyaan"], 1):
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1); p.paragraph_format.keep_with_next = True
        r = p.add_run(f"{i}. "); r.bold = True; r.font.color.rgb = rgb(pal["accent"])
        if q.get("kategori"):
            r = p.add_run(f'[{q["kategori"]}] '); r.font.size = Pt(9); r.font.color.rgb = rgb(pal["accent"])
        p.add_run(q["pertanyaan"]).bold = True
        a = doc.add_paragraph(); a.paragraph_format.left_indent = Cm(0.6); a.paragraph_format.space_after = Pt(6)
        ra = a.add_run("Jawaban model: "); ra.italic = True; ra.font.color.rgb = rgb("#5b6472"); a.add_run(q["jawaban"])

    doc.add_heading("7. Checklist persiapan", 1)
    for grp in b["checklist"]:
        doc.add_heading(grp["waktu"], 2)
        for it in grp["items"]:
            p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(1); p.paragraph_format.left_indent = Cm(0.3)
            p.add_run("☐  ").font.size = Pt(12); p.add_run(it)

    doc.add_heading("8. Referensi", 1)
    if b.get("cek_ulang"):
        para("Wajib dicek ulang ke paper sebelum maju:", bold=True, color="#7a5a00"); bullets(b["cek_ulang"])
    for i, r in enumerate(b["referensi"], 1):
        para(f"{i}. {r}", size=9.5)

    sec = doc.sections[0]
    fp = sec.footer.paragraphs[0]; fp.text = f'{m.get("penyaji", "")} · Brief journal reading · {m.get("tanggal", "")}'
    fp.runs[0].font.size = Pt(8); fp.runs[0].font.color.rgb = rgb("#8a93a0")
    doc.save(path)


def main():
    src, outdir = sys.argv[1], sys.argv[2]
    b = json.load(open(src, encoding="utf-8"))
    errs, warns, n = check(b)
    for w in warns:
        print("PERINGATAN:", w)
    for e in errs:
        print("MASALAH:", e)
    if errs:
        sys.exit(1)
    pal = PALETTES.get(b["meta"].get("warna", "navy"), PALETTES["navy"])
    os.makedirs(outdir, exist_ok=True)
    base = b["meta"].get("nama_file") or "brief-journal-reading"
    hp, dp = os.path.join(outdir, base + ".html"), os.path.join(outdir, base + ".docx")
    open(hp, "w", encoding="utf-8").write(build_html(b, pal))
    build_docx(b, pal, dp)
    print(f"{n} kata · {len(b['pertanyaan'])} pertanyaan · {sum(len(g['items']) for g in b['checklist'])} item checklist")
    print("OK:", hp); print("OK:", dp)


if __name__ == "__main__":
    main()
