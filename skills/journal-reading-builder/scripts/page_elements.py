#!/usr/bin/env python3
"""Daftar SEMUA elemen satu halaman desain Canva (teks, bentuk, gambar, grup) beserta
locator, posisi, ukuran, dan warnanya. Dipakai saat perlu mewarnai ulang kotak
(recolor_element), mengganti ikon (update_fill), menghapus baris, atau menaikkan grup
ke lapisan depan; elemen non-teks tidak tampil di list_placeholders.py.

Pakai:
  uv run python3 page_elements.py design.json 12          # halaman 12
  uv run python3 page_elements.py design.json 12 --json    # keluaran mesin

design.json = hasil read-design (open_transaction) yang tersimpan ke file.
"""
import json
import sys


def color(e):
    for p in e.get("paths", []):
        f = ((p.get("fill") or {}).get("color") or {}).get("color", "")
        s = p.get("stroke") or {}
        return f + (f' garis {s.get("weight")} {(s.get("color") or {}).get("color", "")}' if s.get("weight") else "")
    m = ((e.get("fill") or {}).get("media") or {})
    return f'gambar {m.get("mediaId", "")}' if m else ""


def walk(els, depth, out):
    for e in els:
        t = e.get("type")
        text = "".join(r.get("characters", "") for r in e.get("textRegions", [])) if t == "text" else ""
        out.append({"depth": depth, "type": t, "locator_id": e.get("locator_id"), "top": round(e.get("top", 0)), "left": round(e.get("left", 0)),
                    "width": round(e.get("width", 0)), "height": round(e.get("height", 0)), "opacity": round(e.get("opacity", 1), 2), "info": color(e), "text": text})
        if t == "group":
            walk(e.get("children", []), depth + 1, out)
    return out


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    pages = (d.get("design_content") or d)["pages"]
    n = int(sys.argv[2])
    out = walk(pages[n - 1]["elements"], 0, [])
    if "--json" in sys.argv:
        print(json.dumps({"page_id": pages[n - 1]["id"], "elements": out}, ensure_ascii=False, indent=1))
        return
    print(f"halaman {n} · page_id={pages[n - 1]['id']} · {len(out)} elemen")
    for e in out:
        print("  " * e["depth"] + f'{e["type"]:5s} y{e["top"]:5d} x{e["left"]:5d} {e["width"]}x{e["height"]} {e["info"]} | {e["locator_id"]} | {e["text"][:50]!r}'.replace(" | ''", ""))


if __name__ == "__main__":
    main()
