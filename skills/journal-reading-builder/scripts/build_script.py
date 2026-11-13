#!/usr/bin/env python3
"""Bangun skrip presentasi siap dibacakan TTS dari skrip.json.

Pakai:
  uv run python3 build_script.py skrip.json outdir/ [--wpm 130]

skrip.json:
{
  "durasi_menit": 25,                       # target waktu bicara (opsional)
  "ejaan": {"INTERACT2": "INTERACT dua"},   # ejaan tambahan khusus paper ini (opsional)
  "biarkan": ["AGREE"],                     # singkatan huruf besar yang memang dibaca sebagai kata (opsional)
  "slides": [
    {"slide": 1, "judul": "Pembuka", "paragraf": ["Selamat pagi, Dokter. ..."]},
    ...
  ]
}

Output di outdir/:
  skrip-presentasi.txt                 tiap slide diawali baris "Slide N. Judul." (untuk latihan sambil pindah slide)
  skrip-presentasi-tanpa-penanda.txt   narasi saja, untuk TTS

Yang dikerjakan script:
  - Mengeja singkatan dan simbol medis umum (TDS, mmHg, >=, %, PCC, DVT, ...) ditambah "ejaan" dari JSON.
  - Membuang tanda kurung, titik koma, titik dua, dan garis miring supaya TTS tidak tersendat,
    lalu mengembalikan huruf besar di awal kalimat.
  - Melaporkan sisa karakter non-kata, singkatan huruf besar yang belum dieja, angka desimal bertitik,
    em dash, kalimat terlalu panjang (> 40 kata), dan perkiraan durasi.
Exit 1 bila ada MASALAH (sisa simbol, em dash, kurung siku, singkatan belum dieja, atau kata 'kita').
"""
import json
import os
import re
import sys

EJAAN = [
    (r"4-factor PCC|4-F PCC", "konsentrat kompleks protrombin empat faktor"),
    (r"activated PCC|\baPCC\b", "konsentrat kompleks protrombin teraktivasi"),
    (r"\bPCC\b", "konsentrat kompleks protrombin"),
    (r"\bFFP\b", "plasma beku segar"),
    (r"\bICH\b", "perdarahan intraserebral"),
    (r"\bIVH\b", "perdarahan intraventrikular"),
    (r"\bDVT\b", "trombosis vena dalam"),
    (r"\bVTE\b", "tromboemboli vena"),
    (r"\bUFH\b", "heparin tak terfraksi"),
    (r"\bLMWH\b", "heparin berat molekul rendah"),
    (r"\bDOAC\b", "antikoagulan oral langsung"),
    (r"\bNSAID\b", "obat antiinflamasi nonsteroid"),
    (r"\bCTA\b", "C T angiografi"),
    (r"\bMRA\b", "M R angiografi"),
    (r"\bDSA\b", "angiografi kateter"),
    (r"\bNCCT\b", "C T tanpa kontras"),
    (r"\bEVD\b", "drainase ventrikel eksternal"),
    (r"\bTIK\b|\bICP\b", "tekanan intrakranial"),
    (r"\bTDS\b|\bSBP\b", "tekanan darah sistolik"),
    (r"\bTDD\b|\bDBP\b", "tekanan darah diastolik"),
    (r"\bRCT\b", "uji acak terkontrol"),
    (r"\bSR-MA\b", "telaah sistematis dan meta-analisis"),
    (r"\bITT\b", "intention to treat"),
    (r"\bNNT\b", "number needed to treat"),
    (r"\bNNH\b", "number needed to harm"),
    (r"\bARR\b", "penurunan risiko absolut"),
    (r"\bRRR\b", "penurunan risiko relatif"),
    (r"\bRR\b", "risiko relatif"),
    (r"\bOR\b", "odds ratio"),
    (r"\bHR\b", "hazard ratio"),
    (r"\b95% CI\b|\bIK 95%", "interval kepercayaan sembilan puluh lima persen"),
    (r"\bCOR\b", "kelas rekomendasi"),
    (r"\bLOE\b", "level bukti"),
    (r"\bLOS\b", "lama rawat"),
    (r"\bDNAR\b", "perintah tidak melakukan resusitasi"),
    (r"\bIPC\b", "kompresi pneumatik intermiten"),
    (r"\bEMS\b", "layanan gawat darurat medis"),
    (r"\bCAA\b", "angiopati amiloid serebral"),
    (r"\bPNPK\b", "Pedoman Nasional Pelayanan Kedokteran"),
    (r"\bPPK\b", "panduan praktik klinis"),
    (r"\bJKN\b", "Jaminan Kesehatan Nasional"),
    (r"\bFornas\b", "formularium nasional"),
    (r"\bPPDS\b", "P P D S"),
    (r"\bRS\b", "rumah sakit"),
    (r"\bIV\b", "intravena"),
    (r"\b(SSRI|INR|GCS|EEG|EKG|MRI|ICU|IGD|MIS|TXA|IVT|PT|aPTT|eGFR|BMI|HIV)\b", lambda m: " ".join(m.group(1))),
    (r"\bCT\b", "C T"),
    (r"\bmmHg\b|\bmm Hg\b", "milimeter air raksa"),
    (r"\bmg/dL\b", "miligram per desiliter"),
    (r"\bmmol/L\b", "milimol per liter"),
    (r"\bIU/kg\b", "unit internasional per kilogram"),
    (r"\bmL\b", "mililiter"),
    (r"\bmis\.", "misalnya"),
    (r"\bdll\.?", "dan lain-lain"),
    (r"\bvs\.?\b", "dibanding"),
    (r">=|≥", "paling sedikit "),
    (r"<=|≤", "paling banyak "),
    (r">", "lebih dari "),
    (r"<", "kurang dari "),
    (r"%", " persen"),
    (r"±", " plus minus "),
    (r"dan/atau", "dan atau"),
]


def say(text, extra):
    t = text
    for a, b in extra:
        t = re.sub(a, b, t)
    t = t.replace("(", ", ").replace(")", ",").replace(";", ",").replace(":", ",").replace('"', "")
    for a, b in EJAAN:
        t = re.sub(a, b, t)
    t = t.replace("/", " atau ")
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"\s+([,.])", r"\1", t)
    t = re.sub(r",\s*,", ",", t)
    t = re.sub(r",\s*\.", ".", t).strip().rstrip(",")
    t = re.sub(r"(^|[.?!]\s+)([a-z])", lambda m: m.group(1) + m.group(2).upper(), t)  # huruf awal kalimat setelah penggantian ejaan
    return t if re.search(r"[.?!]$", t) else t + "."


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    src, outdir = sys.argv[1], sys.argv[2]
    wpm = int(sys.argv[sys.argv.index("--wpm") + 1]) if "--wpm" in sys.argv else 130
    d = json.load(open(src, encoding="utf-8"))
    extra = [(r"\b" + re.escape(k) + r"\b", v) for k, v in sorted(d.get("ejaan", {}).items(), key=lambda kv: -len(kv[0]))]
    keep = set(d.get("biarkan", []))
    problems, warns, a, b = [], [], [], []
    nums = [s["slide"] for s in d["slides"]]
    if nums != sorted(nums):
        problems.append("urutan slide tidak naik: skrip harus mengikuti urutan deck")
    for s in d["slides"]:
        ps = [say(p, extra) for p in s["paragraf"] if p.strip()]
        if not ps:
            warns.append(f'slide {s["slide"]}: tanpa narasi')
            continue
        for p in ps:
            for sent in re.split(r"(?<=[.?!])\s+", p):
                if len(sent.split()) > 40:
                    warns.append(f'slide {s["slide"]}: kalimat {len(sent.split())} kata, pecah supaya enak didengar: "{sent[:60]}..."')
        a.append(f'Slide {s["slide"]}. {say(s["judul"], extra)}\n\n' + "\n\n".join(ps))
        b.append("\n\n".join(ps))
    ta, tb = "\n\n\n".join(a) + "\n", "\n\n".join(b) + "\n"
    sym = sorted(set(re.findall(r"[^\w\s.,?!'-]", tb)))
    if sym:
        problems.append(f"karakter yang tidak aman untuk TTS: {sym}")
    if chr(0x2014) in tb or "[" in ta:
        problems.append("ada em dash atau kurung siku")
    if re.search(r"\bkita\b", tb, re.I):
        problems.append("ada kata 'kita' (aturan pemesan: hindari; pakai kalimat pasif atau 'RS setempat', 'pasien lokal')")
    caps = sorted(set(re.findall(r"\b[A-Z]{3,}\d*\b", tb)) - keep)
    if caps:
        problems.append(f"singkatan belum dieja (tambahkan ke 'ejaan' atau 'biarkan'): {caps}")
    dec = sorted(set(re.findall(r"\b\d+\.\d+\b", tb)))
    if dec:
        warns.append(f"angka desimal bertitik (pakai koma atau tulis dengan huruf): {dec[:10]}")
    w = len(tb.split())
    menit = w / wpm
    print(f"{len(a)} slide bernarasi · {w} kata · sekitar {menit:.0f} menit pada {wpm} kata per menit")
    if d.get("durasi_menit") and menit > d["durasi_menit"] * 1.1:
        warns.append(f'durasi {menit:.0f} menit melebihi target {d["durasi_menit"]} menit: pangkas narasi atau jumlah slide')
    for x in warns:
        print("PERINGATAN:", x)
    for x in problems:
        print("MASALAH:", x)
    if problems:
        sys.exit(1)
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, "skrip-presentasi.txt"), "w", encoding="utf-8").write(ta)
    open(os.path.join(outdir, "skrip-presentasi-tanpa-penanda.txt"), "w", encoding="utf-8").write(tb)
    print("OK:", os.path.join(outdir, "skrip-presentasi.txt"))
    print("OK:", os.path.join(outdir, "skrip-presentasi-tanpa-penanda.txt"))


if __name__ == "__main__":
    main()
