#!/usr/bin/env python3
"""Cek tata letak kartu di deck Canva: kartu atas menimpa kotak bawah, bayangan tidak sama ukuran,
teks keluar dari kartu, kartu keluar dari slide.

Pakai:
  uv run python3 cek_tabrakan.py design.json [--fix ops_dir/] [--jarak 30]

design.json = hasil read-design (design_content, sebaiknya dengan open_transaction supaya ada locator_id).
--fix menulis ops_dir/fixNNN.json (resize_element pada bentuk kartu dan bayangan, position_element bayangan)
untuk halaman yang kartunya bisa diperbaiki tanpa memotong teks; satu file per halaman, siap dikirim ke edit-design.

Aturan (dari revisi pemesan 15 November 2026, lihat SKILL.md "Kotak atas menimpa kotak bawah"):
  - kartu atas berakhir minimal --jarak px (default 30) di atas kotak di bawahnya;
  - bayangan (bentuk gelap opasitas sekitar 0,1, bukan anggota grup) sama lebar dan tinggi dengan kartunya,
    digeser top +10 dan left +6;
  - teks di dalam kartu tidak melewati tepi bawah kartu.
Exit 1 bila ada MASALAH.
"""
import json, os, sys


def load(path):
    d = json.load(open(path))
    if isinstance(d, list):  # bungkus teks dari tool-results
        d = json.loads(d[0]["text"])
    return d["design_content"]["pages"]


def fill(e):
    for p in e.get("paths", []):
        c = ((p.get("fill") or {}).get("color") or {}).get("color")
        if c:
            return c.lower()
    return None


def cards(page):
    """Kartu = grup yang anak pertamanya bentuk putih lebar; dikembalikan (grup, bentuk, teks[])."""
    out = []
    for e in page["elements"]:
        if e["type"] != "group":
            continue
        shapes = [c for c in e.get("children", []) if c["type"] == "shape" and fill(c) == "#ffffff" and c["width"] > 300]
        if not shapes:
            continue
        sh = max(shapes, key=lambda c: c["width"] * c["height"])
        out.append((e, sh, [c for c in e.get("children", []) if c["type"] == "text"]))
    return out


def shadows(page):
    return [e for e in page["elements"] if e["type"] == "shape" and (e.get("opacity") or 1) < 0.5 and e["width"] > 300]


def bottom(e):
    return e["top"] + e["height"]


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    pages = load(sys.argv[1])
    gap = int(sys.argv[sys.argv.index("--jarak") + 1]) if "--jarak" in sys.argv else 30
    outdir = sys.argv[sys.argv.index("--fix") + 1] if "--fix" in sys.argv else None
    if outdir:
        os.makedirs(outdir, exist_ok=True)
    problems = 0
    for n, p in enumerate(pages, 1):
        cs = cards(p); shs = shadows(p); msgs = []; ops = []
        for g, sh, texts in cs:
            tb = max((bottom(t) for t in texts), default=sh["top"])
            tabel = len(texts) > 3  # grup baris tabel atau daftar: teks tersebar di luar bentuk utama, bukan kartu
            if tabel:
                continue
            if tb > bottom(sh) - 8:
                msgs.append(f"teks keluar kartu (teks berakhir {tb:.0f}, kartu {bottom(sh):.0f}) di kartu top {sh['top']:.0f} left {sh['left']:.0f}")
            if bottom(sh) > 1010:
                msgs.append(f"kartu keluar slide (berakhir {bottom(sh):.0f})")
            # kotak lain di bawahnya yang tumpang tindih horizontal
            below = [s2 for _, s2, _ in cs if s2 is not sh and s2["top"] > sh["top"] + 40
                     and min(sh["left"] + sh["width"], s2["left"] + s2["width"]) - max(sh["left"], s2["left"]) > 50]
            target = None
            if below:
                nxt = min(below, key=lambda s2: s2["top"])
                # baris daftar selebar sama (mis. Ruang lingkup) memang berjarak rapat; jarak minimal hanya untuk
                # pola kartu atas + kotak lebar di bawah. Tumpang tindih nyata selalu dilaporkan.
                same_row = abs(nxt["width"] - sh["width"]) < 20
                if bottom(sh) > nxt["top"] - (0 if same_row else gap) + 1:
                    msgs.append(f"kartu top {sh['top']:.0f} left {sh['left']:.0f} berakhir {bottom(sh):.0f}, kotak bawah mulai {nxt['top']:.0f} (jarak minimal {gap})")
                    target = nxt["top"] - gap - sh["top"]
                    if target < tb - sh["top"] + 20:
                        msgs.append("  tidak bisa diperbaiki dengan memperkecil kartu: teks terlalu panjang, ringkas teks atau turunkan kotak bawah")
                        target = None
            want_h = target if target else sh["height"]
            if target:
                ops.append({"type": "resize_element", "locator_id": sh["locator_id"], "width": round(sh["width"]), "height": round(want_h)})
            # bayangan pasangan kartu
            cand = [s for s in shs if abs(s["left"] - (sh["left"] + 6)) <= 20 and abs(s["top"] - (sh["top"] + 10)) <= 60]
            if cand:
                s = min(cand, key=lambda s: abs(s["top"] - sh["top"] - 10) + abs(s["left"] - sh["left"] - 6))
                if abs(s["height"] - want_h) > 6 or abs(s["width"] - sh["width"]) > 6 or abs(s["top"] - sh["top"] - 10) > 3:
                    msgs.append(f"bayangan {s['width']:.0f}x{s['height']:.0f} top {s['top']:.0f} tidak sama dengan kartu {sh['width']:.0f}x{want_h:.0f} top {sh['top'] + 10:.0f}")
                    ops.append({"type": "resize_element", "locator_id": s["locator_id"], "width": round(sh["width"]), "height": round(want_h)})
                    ops.append({"type": "position_element", "locator_id": s["locator_id"], "top": round(sh["top"] + 10), "left": round(sh["left"] + 6)})
        # kartu sebaris (top sama, lebar sama) harus sama tinggi
        rows = {}
        for g, sh, texts in cs:
            if len(texts) <= 3 and sh["width"] < 1000:
                rows.setdefault((round(sh["top"] / 10), round(sh["width"] / 10)), []).append(sh)
        for row in rows.values():
            hs = sorted(round(s["height"]) for s in row)
            if len(row) > 1 and hs[-1] - hs[0] > 6:
                msgs.append(f"kartu sebaris (top {row[0]['top']:.0f}) tidak sama tinggi: {hs}")
        if msgs:
            problems += 1
            print(f"Halaman {n}:"); [print("  MASALAH:", m) for m in msgs]
            if outdir and ops and all("locator_id" in o for o in ops):
                json.dump(ops, open(os.path.join(outdir, f"fix{n:03d}.json"), "w"))
    print(f"{problems} halaman bermasalah dari {len(pages)}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
