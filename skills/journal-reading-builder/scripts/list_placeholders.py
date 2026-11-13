#!/usr/bin/env python3
"""Ringkas design_content Canva (hasil read-design yang tersimpan ke file) menjadi
inventaris teks per halaman, untuk dipetakan ke fill.json.

Pakai:
  uv run python3 list_placeholders.py design.json                  # semua teks
  uv run python3 list_placeholders.py design.json --only-brackets  # hanya [..] dan PETUNJUK
  uv run python3 list_placeholders.py design.json --json inv.json  # simpan versi mesin (wajib untuk make_ops)

Baris output: <hal> | <locator_id> | <flag> | y,x | <teks>
flag: B = berisi [placeholder], P = teks PETUNJUK, Y = kotak kuning PETUNJUK (shape),
      F = footer, T = teks tetap. Urutan per halaman: atas ke bawah, kiri ke kanan,
      sehingga sel tabel "[ ]" terbaca per baris.
"""
import json, sys

YELLOW = "#fff2b8"

def load(path):
    d = json.load(open(path, encoding="utf-8"))
    if isinstance(d, dict) and "design_content" in d:
        d = d["design_content"]
    return d["pages"]

def shape_fill(e):
    for p in e.get("paths", []):
        c = ((p.get("fill") or {}).get("color") or {}).get("color", "")
        if c:
            return c.lower()
    return ""

def walk(els, out):
    for e in els:
        t = e.get("type")
        top, left = e.get("top", 0), e.get("left", 0)  # anak grup sudah absolut
        if t == "group":
            walk(e.get("children", []), out)
            continue
        txt = ""
        if t == "text":
            txt = "".join(r.get("characters", "") for r in e.get("textRegions", []))
        elif t == "shape":
            txt = "".join(r.get("characters", "") for tc in e.get("textContents", [])
                          for r in tc.get("textRegions", []))
        item = {"locator_id": e["locator_id"], "type": t, "text": txt,
                "top": round(top), "left": round(left),
                "width": round(e.get("width", 0)), "height": round(e.get("height", 0))}
        if txt.strip():
            out.append(item)
        elif t == "shape" and shape_fill(e) == YELLOW:
            item["text"] = "(kotak kuning PETUNJUK)"
            item["yellow"] = True
            out.append(item)

def flag(it):
    txt = it["text"]
    if it.get("yellow"):
        return "Y"
    if txt.startswith("PETUNJUK"):
        return "P"
    if txt.startswith("[Nama penyaji]") or ("·" in txt and "[Tanggal]" in txt):
        return "F"
    if "[" in txt:
        return "B"
    return "T"

def main():
    path = sys.argv[1]
    only = "--only-brackets" in sys.argv
    machine = []
    for i, p in enumerate(load(path), 1):
        items = []
        walk(p.get("elements", []), items)
        items.sort(key=lambda it: (round(it["top"] / 12), it["left"]))
        print(f"\n=== Halaman {i} · {p.get('title', '')} · page_id={p['id']}")
        for it in items:
            it["flag"] = flag(it)
            if only and it["flag"] not in ("B", "P", "Y"):
                continue
            short = it["text"].replace("\n", " / ")
            if len(short) > 120:
                short = short[:117] + "..."
            print(f"{i:>2} | {it['locator_id']} | {it['flag']} | {it['top']},{it['left']} | {short}")
        machine.append({"page_no": i, "page_id": p["id"], "title": p.get("title", ""),
                        "notes": p.get("notes", ""), "texts": items})
    if "--json" in sys.argv:
        out = sys.argv[sys.argv.index("--json") + 1]
        json.dump(machine, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"\n[disimpan] {out}")

if __name__ == "__main__":
    main()
