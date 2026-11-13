#!/usr/bin/env python3
"""Ubah fill.json menjadi potongan operasi edit-design Canva (siap dikirim per call).

Pakai:
  uv run python3 make_ops.py inv.json fill.json outdir/ [--chunk 120]

inv.json  = output list_placeholders.py --json dari desain BARU (bukan template asli).
fill.json = isian, format:
{
  "footer": null,                          # usang: template tidak lagi punya footer nama penyaji. Bila deck lama masih punya, elemen footer DIHAPUS.
  "delete_petunjuk": true,                 # hapus kotak kuning + teks PETUNJUK (default true)
  "texts": { "<locator_id>": "teks baru", ... },
  "notes": { "<page_id>": "speaker notes", ... },
  "delete": ["<locator_id>", ...],          # elemen lain yang dibuang (mis. baris tabel kosong)
  "max_chars": { "<locator_id>": 90 },      # opsional, batas panjang khusus
  "renumber": true                          # nomor slide statis di pojok kanan bawah disesuaikan (default true)
}

Output: outdir/ops_01.json, ops_02.json, ... (list operasi) + laporan cek di stdout:
  - placeholder [..] yang belum diisi (akan tetap terlihat di slide!)
  - teks baru yang masih mengandung "[" atau em dash
  - teks yang jauh lebih panjang dari placeholder aslinya (risiko overflow)
Exit code 1 bila ada placeholder tersisa atau em dash, supaya tidak lolos tanpa sengaja.
"""
import json, os, sys

def main():
    inv = json.load(open(sys.argv[1], encoding="utf-8"))
    fill = json.load(open(sys.argv[2], encoding="utf-8"))
    outdir = sys.argv[3]
    chunk = int(sys.argv[sys.argv.index("--chunk") + 1]) if "--chunk" in sys.argv else 120
    os.makedirs(outdir, exist_ok=True)

    texts = fill.get("texts", {})
    notes = fill.get("notes", {})
    deletes = set(fill.get("delete", []))
    maxc = fill.get("max_chars", {})
    footer = fill.get("footer")
    del_pet = fill.get("delete_petunjuk", True)
    renumber = fill.get("renumber", True)  # nomor slide pojok kanan bawah ikut urutan baru

    known = {t["locator_id"]: (p, t) for p in inv for t in p["texts"]}
    page_ids = {p["page_id"] for p in inv}
    ops, problems, warnings = [], [], []

    for lid in list(texts) + list(deletes):
        if lid not in known:
            problems.append(f"locator tidak dikenal (salah salin / desain lain?): {lid}")

    for p in inv:
        for t in p["texts"]:
            lid, f, old = t["locator_id"], t["flag"], t["text"]
            if lid in deletes:
                ops.append({"type": "delete_element", "locator_id": lid})
                continue
            if f in ("P", "Y") and del_pet:
                ops.append({"type": "delete_element", "locator_id": lid})
                continue
            if (f == "T" and lid not in texts and renumber and t["top"] > 1000
                    and t["left"] > 1500 and old.strip().isdigit()):
                ops.append({"type": "replace_text", "locator_id": lid, "text": f"{p['page_no']:02d}"})
                continue
            if f == "F" and lid not in texts and t["top"] > 1000:  # hanya footer kiri bawah; teks nama di slide penutup tetap diisi lewat texts
                # keputusan 12 Nov 2026: tidak ada teks nama penyaji di kiri bawah slide; sisa footer di deck lama dibuang
                ops.append({"type": "delete_element", "locator_id": lid})
                continue
            if lid in texts:
                new = texts[lid]
                ops.append({"type": "replace_text", "locator_id": lid, "text": new})
                if "[" in new:
                    problems.append(f"hal {p['page_no']} {lid}: teks baru masih ada '[': {new[:60]}")
                limit = maxc.get(lid) or max(int(len(old) * 1.6), len(old) + 25)
                if len(new) > limit and f == "B":
                    warnings.append(f"hal {p['page_no']} {lid}: {len(new)} karakter vs placeholder {len(old)}, cek overflow")
            elif f == "B":
                problems.append(f"hal {p['page_no']} '{p['title']}' {lid}: placeholder belum diisi: {old[:60]}")

    for pid, n in notes.items():
        if pid not in page_ids:
            problems.append(f"page_id notes tidak dikenal: {pid}")
        ops.append({"type": "replace_speaker_notes", "page_id": pid, "notes": n})
    missing_notes = [p["page_no"] for p in inv if p["page_id"] not in notes]
    if missing_notes:
        warnings.append(f"halaman tanpa notes baru (notes template tetap terpakai): {missing_notes}")

    for o in ops:
        s = o.get("text", "") + o.get("notes", "")
        if "\u2014" in s:
            problems.append(f"em dash ditemukan di {o.get('locator_id') or o.get('page_id')}")
        if __import__("re").search(r"\bkita\b", s, __import__("re").I):
            problems.append(f"kata 'kita' ditemukan di {o.get('locator_id') or o.get('page_id')} (aturan pemesan: hindari; pakai pasif atau 'RS setempat', 'pasien lokal')")

    files = []
    for i in range(0, len(ops), chunk):
        fn = os.path.join(outdir, f"ops_{i // chunk + 1:02d}.json")
        json.dump(ops[i:i + chunk], open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        files.append(fn)

    print(f"{len(ops)} operasi -> {len(files)} file: " + ", ".join(os.path.basename(f) for f in files))
    for w in warnings:
        print("PERINGATAN:", w)
    for pr in problems:
        print("MASALAH:", pr)
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
