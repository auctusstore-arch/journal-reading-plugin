#!/usr/bin/env python3
"""Buat audio latihan per slide dari skrip presentasi, dibacakan kata demi kata (Edge TTS).

Pakai:
  uv run --with edge-tts --with mutagen python3 build_audio.py skrip-presentasi.txt outdir/
  opsi:
    --voice id-ID-ArdiNeural     suara (default; alternatif: id-ID-GadisNeural)
    --rate -5%                   kecepatan relatif (default +0%)
    --slides 1,5,32-35           hanya slide tertentu
    --gabung                     buat juga satu file gabungan (latihan-lengkap.mp3)
    --judul                      bacakan juga baris "Slide N. Judul." sebagai penanda
    --lafal lafal.json           kamus pelafalan tambahan {"kata asli": "ejaan fonetik"} untuk order ini
    --cek-lafal                  hanya tampilkan kata yang akan dieja ulang, tanpa membuat audio

Pelafalan: suara Indonesia mengeja kata Inggris huruf demi huruf ("guideline" terdengar "gui-de-li-ni").
Script menulis ulang kata Inggris umum secara fonetik (daftar LAFAL di bawah) hanya untuk audio; file
skrip tidak berubah. Bila tim mendengar kata lain yang salah lafal, tambahkan lewat --lafal lalu jalankan
ulang: hanya slide yang memuat kata itu yang dibuat ulang.

Masukan harus `skrip-presentasi.txt` keluaran build_script.py (tiap slide diawali baris
"Slide N. Judul."). Teks sudah dieja untuk TTS, jadi dibacakan apa adanya.

Keluaran di outdir/:
  slide-001.mp3, slide-002.mp3, ...   satu file per slide
  latihan-lengkap.mp3                 bila --gabung
  daftar-audio.txt                    nomor slide, judul, durasi, total
  .manifest.json                      sidik teks per slide; slide yang teksnya tidak berubah
                                      tidak dibuat ulang, jadi revisi satu slide cukup satu file

Catatan:
  - Teks skrip dikirim ke layanan Microsoft Edge TTS saat audio dibuat. Jangan memasukkan
    identitas pasien ke skrip.
  - Butuh internet. Gratis dan tidak memakai kuota AI.
Exit 1 bila ada slide yang gagal dibuat.
"""
import asyncio
import hashlib
import json
import os
import re
import sys


# Kata Inggris yang oleh suara Indonesia dieja huruf demi huruf ("guideline" terdengar "gui-de-li-ni").
# Ditulis ulang secara fonetik HANYA untuk audio; file skrip tidak diubah. Urutan: frasa panjang dulu.
LAFAL = [
    ("clinical practice guideline", "klinikal praktis gaidlain"),
    ("American Heart Association", "Amerikan Hart Asosiesyen"),
    ("American Stroke Association", "Amerikan Strok Asosiesyen"),
    ("take-home message", "teik hom mesej"),
    ("number needed to treat", "namber nided tu trit"),
    ("number needed to harm", "namber nided tu harm"),
    ("intention to treat", "intensyen tu trit"),
    ("systematic review", "sistematik riviu"),
    ("level of evidence", "level of evidens"),
    ("risk of bias", "risk of baias"),
    ("odds ratio", "ods resio"),
    ("hazard ratio", "hazard resio"),
    ("confidence interval", "konfidens interval"),
    ("follow-up", "folo ap"),
    ("spot sign", "spot sain"),
    ("guidelines", "gaidlain"),
    ("guideline", "gaidlain"),
    ("reviewer", "riviuer"),
    ("review", "riviu"),
    ("evidence", "evidens"),
    ("outcome", "autkam"),
    ("baseline", "beslain"),
    ("blinding", "blainding"),
    ("trial", "trayel"),
    ("score", "skor"),
    ("shunt", "syan"),
    ("stroke", "strok"),
    ("Delphi", "Delfi"),
    ("AGREE", "egri"),
]


def lafal(text, extra):
    for a, b in sorted(extra, key=lambda kv: -len(kv[0])) + LAFAL:
        text = re.sub(r"(?<![A-Za-z])" + re.escape(a) + r"(?![A-Za-z])", b, text, flags=re.I)
    return text


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def parse(path):
    slides, cur = [], None
    for line in open(path, encoding="utf-8").read().split("\n"):
        m = re.match(r"^Slide (\d+)\. (.*)$", line.strip())
        if m:
            cur = {"n": int(m.group(1)), "judul": m.group(2).rstrip("."), "teks": []}
            slides.append(cur)
        elif cur is not None and line.strip():
            cur["teks"].append(line.strip())
    return slides


def pick(spec):
    out = set()
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out.update(range(int(a), int(b or a) + 1))
    return out


async def synth(text, voice, rate, out, tries=4):
    import edge_tts
    for i in range(tries):
        try:
            await edge_tts.Communicate(text, voice, rate=rate).save(out)
            if os.path.getsize(out) > 1000:
                return True
        except Exception as e:  # jaringan atau batas laju: coba lagi
            err = e
        await asyncio.sleep(3 * (i + 1))
    print("GAGAL:", out, locals().get("err", "file kosong"))
    return False


async def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    src, outdir = sys.argv[1], sys.argv[2]
    voice, rate = arg("--voice", "id-ID-ArdiNeural"), arg("--rate", "+0%")
    only = pick(arg("--slides")) if "--slides" in sys.argv else None
    extra = list(json.load(open(arg("--lafal"), encoding="utf-8")).items()) if "--lafal" in sys.argv else []
    slides = parse(src)
    if not slides:
        print("MASALAH: tidak ada baris 'Slide N. Judul.'; pakai skrip-presentasi.txt, bukan versi tanpa penanda")
        sys.exit(1)
    if "--cek-lafal" in sys.argv:
        from collections import Counter
        c = Counter()
        for sl in slides:
            t = " ".join(sl["teks"])
            for x, y in extra + LAFAL:
                k = len(re.findall(r"(?<![A-Za-z])" + re.escape(x) + r"(?![A-Za-z])", t, flags=re.I))
                if k:
                    c[f"{x} -> {y}"] += k
        for k, v in c.most_common():
            print(f"{v:4d}  {k}")
        return
    os.makedirs(outdir, exist_ok=True)
    mpath = os.path.join(outdir, ".manifest.json")
    man = json.load(open(mpath)) if os.path.exists(mpath) else {}
    sem, failed, made = asyncio.Semaphore(4), [], 0

    async def one(s):
        nonlocal made
        text = "\n\n".join(([f'Slide {s["n"]}. {s["judul"]}.'] if "--judul" in sys.argv else []) + s["teks"])
        out = os.path.join(outdir, f'slide-{s["n"]:03d}.mp3')
        text = lafal(text, extra)
        sig = hashlib.sha1(f"{voice}|{rate}|{text}".encode()).hexdigest()
        if man.get(str(s["n"])) == sig and os.path.exists(out):
            return
        async with sem:
            if await synth(text, voice, rate, out):
                man[str(s["n"])] = sig
                made += 1
            else:
                failed.append(s["n"])

    await asyncio.gather(*[one(s) for s in slides if not only or s["n"] in only])
    json.dump(man, open(mpath, "w"))

    from mutagen.mp3 import MP3
    rows, total = [], 0.0
    for s in slides:
        f = os.path.join(outdir, f'slide-{s["n"]:03d}.mp3')
        if os.path.exists(f):
            d = MP3(f).info.length
            total += d
            rows.append(f'slide-{s["n"]:03d}.mp3\t{int(d // 60)}:{int(d % 60):02d}\t{s["judul"]}')
    rows.append(f"TOTAL\t{int(total // 60)}:{int(total % 60):02d}\t{len(rows)} slide · suara {voice} · kecepatan {rate}")
    open(os.path.join(outdir, "daftar-audio.txt"), "w", encoding="utf-8").write("\n".join(rows) + "\n")
    if "--gabung" in sys.argv:
        with open(os.path.join(outdir, "latihan-lengkap.mp3"), "wb") as w:
            for s in slides:
                f = os.path.join(outdir, f'slide-{s["n"]:03d}.mp3')
                if os.path.exists(f):
                    w.write(open(f, "rb").read())
    print(f"{made} file dibuat, {len(rows) - 1} file tersedia, total {int(total // 60)} menit {int(total % 60)} detik")
    if failed:
        print("MASALAH: slide gagal:", sorted(failed))
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
