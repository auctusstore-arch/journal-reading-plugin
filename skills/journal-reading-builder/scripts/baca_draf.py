#!/usr/bin/env python3
"""Baca draf PPTX klien jadi inventaris teks per slide (untuk jalur draf klien).

Pemakaian:
  uv run --with python-pptx python3 scripts/baca_draf.py draf.pptx draf-inventaris.md

Keluaran (markdown): per slide nomor, judul, semua teks (urut atas ke bawah),
isi tabel, speaker notes, jumlah gambar, dan angka yang terdeteksi.
Skrip hanya MEMBACA. Tidak mengubah draf dan tidak menilai kebenaran isi.
Gambar tidak dibaca isinya: tandai slide bergambar, lalu buka manual (render
dengan soffice/pdftoppm bila perlu) untuk figur atau tabel hasil tangkapan layar.
"""
import re
import sys

from pptx import Presentation
from pptx.util import Emu

ANGKA = re.compile(r"\d+(?:[.,]\d+)?\s?(?:%|mmHg|mg|kg|bulan|tahun|hari)?|p\s?[<=>]\s?0[.,]\d+|\d+/\d+")


def teks_shape(sh):
    if sh.has_text_frame:
        t = "\n".join(p.text.strip() for p in sh.text_frame.paragraphs if p.text.strip())
        return t
    return ""


def tabel_shape(sh):
    rows = []
    for r in sh.table.rows:
        rows.append(" | ".join(c.text.strip().replace("\n", " ") for c in r.cells))
    return rows


def urut(shapes):
    return sorted(shapes, key=lambda s: ((s.top or 0) // Emu(300000), s.left or 0))


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    prs = Presentation(sys.argv[1])
    out = [f"# Inventaris draf: {sys.argv[1]}", f"Jumlah slide: {len(prs.slides)}", ""]
    for i, s in enumerate(prs.slides, 1):
        judul = s.shapes.title.text.strip() if s.shapes.title is not None and s.shapes.title.has_text_frame else "(tanpa judul)"
        out.append(f"## Slide {i}. {judul}")
        gambar = 0
        semua = []
        for sh in urut(s.shapes):
            if sh.shape_type == 13:  # picture
                gambar += 1
            if sh.has_text_frame:
                t = teks_shape(sh)
                if t and not (s.shapes.title is not None and sh.shape_id == s.shapes.title.shape_id):
                    out.append(t)
                    semua.append(t)
            if getattr(sh, "has_table", False) and sh.has_table:
                out.append("[tabel]")
                for r in tabel_shape(sh):
                    out.append("  " + r)
                    semua.append(r)
        if gambar:
            out.append(f"[{gambar} gambar: buka manual, bisa figur paper atau tangkapan layar tabel]")
        if s.has_notes_slide:
            n = s.notes_slide.notes_text_frame.text.strip()
            if n:
                out.append("Notes: " + n)
                semua.append(n)
        angka = sorted({m.group(0).strip() for m in ANGKA.finditer("\n".join(semua)) if len(m.group(0).strip()) > 1})
        if angka:
            out.append("Angka terdeteksi: " + "; ".join(angka))
        out.append("")
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"OK: {len(prs.slides)} slide -> {sys.argv[2]}")


if __name__ == "__main__":
    main()
