#!/usr/bin/env python3
"""Ekstrak tabel rekomendasi guideline dari PDF dengan memasangkan kelas dan level
ke tiap rekomendasi berdasarkan POSISI di halaman, bukan urutan teks.

Kenapa perlu: pada PDF dua kolom (mis. guideline AHA/ASA), pdftotext mengeluarkan
kolom COR, LOE, dan teks rekomendasi dalam urutan yang tidak sejajar, sehingga
pemasangan berdasarkan urutan sering tertukar. Script ini membaca koordinat kata.

Pakai:
  uv run --with pymupdf python3 extract_recs.py guideline.pdf recs.json
  uv run --with pymupdf python3 extract_recs.py guideline.pdf recs.json \
      --class-header Class --level-header Level \
      --class-values "I,IIa,IIb,III" --level-values "A,B,C"
  opsi lain: --title-noise "KATA1,KATA2" (kata tepi halaman yang dibuang dari judul tabel)

Default mengikuti sistem AHA/ACC: kepala kolom "COR" dan "LOE", nilai
COR 1 / 2a / 2b / 3: No Benefit / 3: Harm dan LOE A / B-R / B-NR / C-LD / C-EO.

Output recs.json: daftar {page, title, cont, no, cor, loe, text}. `page` adalah
halaman PDF (mulai 1). Laporan di stdout: jumlah per tabel, apakah penomoran
berurutan, dan baris yang kelas/levelnya tidak tepat satu nilai valid (BAD).
Exit 1 bila ada BAD atau penomoran tidak berurutan: periksa tabel itu ke PDF.

Batasan:
  - Tabel harus punya baris kepala berisi kedua kepala kolom dan kata
    "Recommendation(s)" pada satu garis.
  - Rekomendasi harus bernomor ("1.", "2.") di kolom teks.
  - Teks rekomendasi yang terpecah antar kolom bisa menyisipkan kata dari
    header halaman; baca ulang angka penting ke PDF.
  - Guideline tanpa tabel berkelas (naratif, GRADE dalam paragraf) tidak didukung.
"""
import json
import re
import sys
from collections import Counter
from itertools import groupby


def arg(name, default):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def clean(text, vocab):
    """Ambil hanya nilai valid dari teks sel (membuang sub-judul baris seperti 'VKAs')."""
    found = []
    for v in sorted(vocab, key=len, reverse=True):
        pat = r"(?<![\w-])" + re.escape(v) + r"(?![\w-])"
        for m in re.finditer(pat, text):
            found.append((m.start(), v))
        text = re.sub(pat, lambda m: " " * len(m.group()), text)
    return " | ".join(v for _, v in sorted(found))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    import pymupdf

    pdf, out_path = sys.argv[1], sys.argv[2]
    ch, lh = arg("--class-header", "COR"), arg("--level-header", "LOE")
    cvals = [x.strip() for x in arg("--class-values", "1,2a,2b,3: No Benefit,3: Harm").split(",")]
    lvals = [x.strip() for x in arg("--level-values", "A,B-R,B-NR,C-LD,C-EO").split(",")]
    # kata dari teks tepi halaman yang sering terbawa ke judul tabel
    noise = set(arg("--title-noise", "CLINICAL,STATEMENTS,GUIDELINES").split(","))

    out = []
    for pno, page in enumerate(pymupdf.open(pdf), 1):
        W = page.rect.width
        words = [(w[0], w[1], w[2], w[3], w[4].strip()) for w in page.get_text("words")]
        for h in [w for w in words if w[4] == ch]:
            loe = [w for w in words if w[4] == lh and abs(w[1] - h[1]) < 3 and 0 < w[0] - h[0] < 120]
            rech = [w for w in words if w[4].startswith("Recommendation") and abs(w[1] - h[1]) < 3 and 0 < w[0] - h[0] < 200]
            if not loe or not rech:
                continue
            loe, rech = loe[0], rech[0]
            left = h[0] - 30
            right = (W / 2 if h[0] < W / 2 else W) - 5
            col = [w for w in words if left <= w[0] < right and w[1] > h[3] - 1]
            ends = [w[1] for w in col if w[4] in ("Synopsis", "Recommendation-Specific") and w[0] < h[0] + 5]
            ends += [w[1] - 40 for w in words if w[4] == ch and abs(w[0] - h[0]) < 5 and w[1] > h[1] + 5]
            yend = min(ends) if ends else page.rect.height - 45
            col = [w for w in col if w[1] < yend]
            rx = rech[0]
            starts = sorted([w for w in col if re.fullmatch(r"\d{1,2}\.", w[4]) and -14 < w[0] - rx < 8], key=lambda w: w[1])
            above = sorted([w for w in words if left <= w[0] < right and h[1] - 75 < w[1] < h[1] - 2], key=lambda w: (round(w[1]), w[0]))
            ttxt = " ".join(w[4] for w in above)
            m = re.search(r"Recommendations? for (.*?)(?: Referenced| \(Continued\)|$)", ttxt)
            title = m.group(1).strip() if m else "?" + ttxt[-60:]
            title = " ".join(w for w in title.split() if w not in noise)
            title = re.sub(r"\s+AND$", "", title)
            title = re.sub(r"(\w)- (\w)", r"\1-\2", title)
            for i, s in enumerate(starts):
                y0 = s[1] - 2
                y1 = starts[i + 1][1] - 2 if i + 1 < len(starts) else yend
                body = sorted([w for w in col if w[0] >= rx - 3 and y0 <= w[1] < y1], key=lambda w: (round(w[1] / 3), w[0]))
                text = re.sub(r"^\d{1,2}\.\s*", "", " ".join(w[4] for w in body))
                mid = lambda w: (w[1] + w[3]) / 2
                cor = sorted([w for w in col if h[0] - 28 <= w[0] < loe[0] - 12 and y0 <= mid(w) < y1], key=lambda w: (round(w[1]), w[0]))
                lev = sorted([w for w in col if loe[0] - 12 <= w[0] < rx - 6 and y0 <= mid(w) < y1], key=lambda w: (round(w[1]), w[0]))
                out.append({"page": pno, "title": title, "cont": "(Continued)" in ttxt, "no": int(s[4][:-1]),
                            "cor": clean(" ".join(w[4] for w in cor), cvals),
                            "loe": clean(" ".join(w[4] for w in lev), lvals), "text": text})

    bad = [r for r in out if r["cor"] not in cvals or r["loe"] not in lvals]
    problems = len(bad)
    print(f"{len(out)} rekomendasi")
    print("kelas:", dict(Counter(r["cor"] for r in out)))
    print("level:", dict(Counter(r["loe"] for r in out)))
    for title, g in groupby(out, key=lambda r: r["title"]):
        g = list(g)
        ok = [x["no"] for x in g] == list(range(1, len(g) + 1))
        problems += 0 if ok else 1
        print(f'  hal {g[0]["page"]:3d}  n={len(g):2d}  {"urut" if ok else "TIDAK URUT"}  {title}')
    for r in bad:
        print(f'BAD hal {r["page"]} {r["title"][:40]} no {r["no"]}: kelas={r["cor"]!r} level={r["loe"]!r}')
    json.dump(out, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("disimpan:", out_path)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
