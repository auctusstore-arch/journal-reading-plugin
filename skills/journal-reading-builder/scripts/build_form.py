#!/usr/bin/env python3
"""Bangun blok form Zoom (AUCTUS-FORM v1) siap tempel ke portal Journal Reading.

Pakai:
  uv run python3 build_form.py form.json outdir/

form.json hanya berisi bagian PERSONAL (spesifik paper/klien). Pertanyaan baku
(ID `inti`, lihat references/format-form.md) disisipkan otomatis supaya metrik
lintas order bisa dibandingkan.

  {
    "jenis": "pre_zoom" | "post_zoom",
    "penyaji": "dr. Nama",                  dipakai di pengantar bawaan
    "paper_singkat": "Shamoun 2026",        dipakai di judul bawaan
    "jenis_paper": "case_report",            opsional, label penilaian diri untuk laporan kasus
    "judul": "...",                          opsional, menimpa judul bawaan
    "pengantar": "...",                      opsional, menimpa pengantar bawaan
    "bagian": [ {"judul": "...", "deskripsi": "...", "pertanyaan": [ ... ]} ]
  }

Format pertanyaan: references/format-form.md. Keluaran: outdir/form-pre-zoom.txt
atau outdir/form-post-zoom.txt. Exit 1 dengan MASALAH bila melanggar kontrak.
"""
import json, os, re, sys

TIPE = {"pilihan", "pilihan_banyak", "skala", "teks_pendek", "teks_panjang"}
ID_RE = re.compile(r"^[a-z0-9_]{1,40}$")
EM = "—"


def skala(label_min="Belum yakin", label_max="Sangat yakin", mn=1, mx=5):
    return {"min": mn, "max": mx, "label_min": label_min, "label_max": label_max}


SELF = [
    ("self_pico", "Menjelaskan PICO dan pertanyaan penelitian paper ini"),
    ("self_desain", "Menjelaskan desain studi dan alur partisipan"),
    ("self_statistik", "Membaca ukuran efek (RR, OR, HR, NNT, interval kepercayaan, nilai p)"),
    ("self_appraisal", "Menjelaskan penilaian tool appraisal item per item"),
    ("self_applicability", "Menilai apakah hasil paper bisa diterapkan di RS sendiri"),
    ("self_spontan", "Menjawab pertanyaan spontan konsulen dengan tenang"),
]


# Label pengganti untuk case report; id sama supaya perbandingan pre dan post tetap jalan.
SELF_CASE = {
    "self_pico": "Menjelaskan mengapa kasus ini penting dan apa yang baru",
    "self_desain": "Menceritakan kasus runtut sesuai linimasa",
    "self_statistik": "Menjelaskan diagnosis banding dan arti hasil pemeriksaan",
    "self_applicability": "Menilai apakah pelajaran kasus bisa diterapkan di RS sendiri",
}


def self_section(judul, deskripsi, jenis_paper=None):
    ganti = SELF_CASE if jenis_paper == "case_report" else {}
    return {"judul": judul, "deskripsi": deskripsi, "pertanyaan": [
        {"id": i, "inti": i, "tipe": "skala", "teks": ganti.get(i, t), "skala": skala()} for i, t in SELF]}


def core_pre(jenis_paper=None):
    kebutuhan = {"judul": "Kebutuhan sesi", "pertanyaan": [
        {"id": "tujuan_sesi", "inti": "tujuan_sesi", "tipe": "teks_panjang",
         "teks": "Apa yang paling ingin dokter dapatkan dari sesi Zoom ini?",
         "bantuan": "Contoh: latihan menjawab pertanyaan statistik, cek slide, memahami tool appraisal."},
        {"id": "kekhawatiran", "inti": "kekhawatiran", "tipe": "teks_panjang",
         "teks": "Bagian mana yang paling dokter khawatirkan saat presentasi nanti?"},
        {"id": "pengalaman_jr", "inti": "pengalaman_jr", "tipe": "pilihan",
         "teks": "Sudah berapa kali dokter membawakan journal reading?",
         "opsi": ["Ini yang pertama", "1 sampai 2 kali", "3 kali atau lebih"]},
        {"id": "status_slide", "inti": "status_slide", "tipe": "pilihan",
         "teks": "Bagaimana kondisi slide saat ini?",
         "opsi": ["Belum mulai", "Draf sebagian", "Draf lengkap, belum dilatih", "Sudah final dan sudah latihan"]},
        {"id": "gaya_konsulen", "inti": "gaya_konsulen", "tipe": "pilihan_banyak", "wajib": False,
         "teks": "Konsulen penguji biasanya sering bertanya tentang apa?",
         "opsi": ["Statistik dan angka", "Metodologi dan bias", "Dasar ilmu dan patofisiologi",
                  "Penerapan di RS dan Indonesia", "Alasan memilih paper", "Belum tahu"]},
    ]}
    return [kebutuhan, self_section("Penilaian diri",
            "Seberapa yakin dokter saat ini? Tidak ada jawaban benar atau salah; ini untuk menentukan fokus sesi.", jenis_paper)]


def core_post_head(jenis_paper=None):
    return [{"judul": "Sesi Zoom", "pertanyaan": [
        {"id": "kebutuhan_terpenuhi", "inti": "kebutuhan_terpenuhi", "tipe": "skala",
         "teks": "Seberapa terpenuhi kebutuhan yang dokter tulis sebelum sesi?",
         "skala": skala("Tidak terpenuhi", "Sepenuhnya terpenuhi")},
        {"id": "kejelasan_umpan_balik", "inti": "kejelasan_umpan_balik", "tipe": "skala",
         "teks": "Umpan balik tutor jelas dan bisa langsung dipakai.",
         "skala": skala("Sangat tidak setuju", "Sangat setuju")},
        {"id": "rating_tutor", "inti": "rating_tutor", "tipe": "skala",
         "teks": "Penilaian keseluruhan dokter terhadap tutor.",
         "skala": skala("Kurang", "Sangat baik")},
    ]}, self_section("Penilaian diri setelah sesi", "Pertanyaan yang sama dengan sebelum sesi, untuk melihat perubahannya.", jenis_paper)]


def core_post_tail():
    return [{"judul": "Penutup", "pertanyaan": [
        {"id": "kesiapan_maju", "inti": "kesiapan_maju", "tipe": "skala",
         "teks": "Seberapa siap dokter maju presentasi sekarang?", "skala": skala("Belum siap", "Sangat siap")},
        {"id": "masih_kurang", "inti": "masih_kurang", "tipe": "teks_panjang", "wajib": False,
         "teks": "Apa yang masih terasa kurang dan perlu kami bantu?"},
        {"id": "nps", "inti": "nps", "tipe": "skala",
         "teks": "Seberapa mungkin dokter merekomendasikan layanan ini ke teman sejawat?",
         "skala": skala("Tidak mungkin", "Sangat mungkin", 0, 10)},
    ]}]


def assemble(src):
    jenis = src.get("jenis")
    if jenis not in ("pre_zoom", "post_zoom"):
        sys.exit("MASALAH: jenis harus pre_zoom atau post_zoom")
    penyaji = src.get("penyaji", "dokter")
    ps = src.get("paper_singkat", "")
    personal = src.get("bagian", [])
    if jenis == "pre_zoom":
        judul = src.get("judul") or f"Sebelum Zoom: persiapan journal reading {ps}".strip()
        pengantar = src.get("pengantar") or (
            f"Halo {penyaji}, form singkat ini (sekitar 7 menit) membantu tutor menyiapkan sesi Zoom sesuai kebutuhan dokter. "
            "Bagian cek pemahaman bukan ujian dan tidak dinilai; jawab saja apa adanya tanpa membuka paper, supaya sesi fokus ke bagian yang paling perlu.")
        bagian = core_pre(src.get("jenis_paper")) + personal
    else:
        judul = src.get("judul") or f"Setelah Zoom: umpan balik sesi {ps}".strip()
        pengantar = src.get("pengantar") or (
            f"Terima kasih {penyaji} sudah mengikuti sesi. Form ini (sekitar 3 menit) membantu kami menilai apakah sesi sudah menjawab kebutuhan dokter.")
        bagian = core_post_head(src.get("jenis_paper")) + personal + core_post_tail()
    return {"versi": 1, "jenis": jenis, "judul": judul, "pengantar": pengantar, "bagian": bagian}


def validate(f):
    errs = []

    def lim(val, n, where):
        if not isinstance(val, str) or not val.strip():
            errs.append(f"{where}: kosong")
        elif len(val) > n:
            errs.append(f"{where}: {len(val)} karakter, maks {n}")

    lim(f["judul"], 120, "judul")
    lim(f["pengantar"], 800, "pengantar")
    if not 1 <= len(f["bagian"]) <= 8:
        errs.append(f"{len(f['bagian'])} bagian; harus 1 sampai 8")
    ids, total = set(), 0
    for bi, b in enumerate(f["bagian"], 1):
        lim(b.get("judul", ""), 120, f"bagian {bi} judul")
        if b.get("deskripsi") is not None:
            lim(b["deskripsi"], 500, f"bagian {bi} deskripsi")
        qs = b.get("pertanyaan", [])
        if not qs:
            errs.append(f"bagian {bi}: tidak ada pertanyaan")
        for q in qs:
            total += 1
            qid = q.get("id", "")
            w = f"pertanyaan '{qid}'"
            if not ID_RE.match(str(qid)):
                errs.append(f"{w}: id tidak valid (pola a-z, 0-9, _ maks 40)")
            if qid in ids:
                errs.append(f"{w}: id dobel")
            ids.add(qid)
            t = q.get("tipe")
            if t not in TIPE:
                errs.append(f"{w}: tipe '{t}' tidak dikenal")
            lim(q.get("teks", ""), 500, f"{w} teks")
            if q.get("bantuan") is not None:
                lim(q["bantuan"], 300, f"{w} bantuan")
            opsi = q.get("opsi")
            if t in ("pilihan", "pilihan_banyak"):
                if not isinstance(opsi, list) or not 2 <= len(opsi) <= 8:
                    errs.append(f"{w}: opsi harus 2 sampai 8")
                else:
                    for o in opsi:
                        lim(o, 200, f"{w} opsi")
                    if len(set(opsi)) != len(opsi):
                        errs.append(f"{w}: opsi dobel")
            elif opsi is not None:
                errs.append(f"{w}: opsi hanya untuk pilihan/pilihan_banyak")
            sk = q.get("skala")
            if t == "skala":
                if not isinstance(sk, dict) or sk.get("min") not in (0, 1) or not isinstance(sk.get("max"), int) or not 2 <= sk["max"] <= 10:
                    errs.append(f"{w}: skala butuh min 0/1 dan max 2 sampai 10")
                else:
                    lim(sk.get("label_min", ""), 40, f"{w} label_min")
                    lim(sk.get("label_max", ""), 40, f"{w} label_max")
            tu = q.get("tutor")
            if tu:
                kunci = tu.get("kunci")
                if kunci is not None:
                    ks = kunci if isinstance(kunci, list) else [kunci]
                    if t not in ("pilihan", "pilihan_banyak"):
                        errs.append(f"{w}: kunci hanya untuk pilihan/pilihan_banyak")
                    elif any(k not in (opsi or []) for k in ks):
                        errs.append(f"{w}: kunci harus persis salah satu opsi")
                if tu.get("catatan") is not None:
                    lim(tu["catatan"], 500, f"{w} catatan tutor")
    if not 1 <= total <= 30:
        errs.append(f"{total} pertanyaan; maks 30")
    raw = json.dumps(f, ensure_ascii=False)
    if EM in raw:
        errs.append("ada em dash; ganti dengan koma, titik dua, atau kurung")
    # Kunci jawaban tidak boleh bocor ke teks yang dilihat klien.
    for b in f["bagian"]:
        for q in b.get("pertanyaan", []):
            if re.search(r"\b(kunci|jawaban benar)\b", q.get("teks", "") + q.get("bantuan", ""), re.I):
                errs.append(f"pertanyaan '{q.get('id')}': teks menyebut kunci/jawaban benar; pindahkan ke field tutor")
    return errs, total


def main():
    src, outdir = sys.argv[1], sys.argv[2]
    f = assemble(json.load(open(src, encoding="utf-8")))
    errs, total = validate(f)
    for e in errs:
        print("MASALAH:", e)
    if errs:
        sys.exit(1)
    personal = sum(1 for b in f["bagian"] for q in b["pertanyaan"] if not q.get("inti"))
    berkunci = sum(1 for b in f["bagian"] for q in b["pertanyaan"] if (q.get("tutor") or {}).get("kunci"))
    os.makedirs(outdir, exist_ok=True)
    name = "form-pre-zoom.txt" if f["jenis"] == "pre_zoom" else "form-post-zoom.txt"
    path = os.path.join(outdir, name)
    block = "=== AUCTUS-FORM v1 ===\n" + json.dumps(f, ensure_ascii=False, indent=1) + "\n=== AKHIR AUCTUS-FORM ===\n"
    open(path, "w", encoding="utf-8").write(block)
    print(f"{total} pertanyaan ({personal} personal, {berkunci} berkunci)")
    print("OK:", path)


if __name__ == "__main__":
    main()
