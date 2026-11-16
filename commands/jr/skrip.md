---
description: JR tahap 5b: skrip presentasi, audio latihan Edge TTS, aturan bahasa
---

Semua path `scripts/`, `references/`, `assets/` di bawah relatif ke `.claude/skills/journal-reading-builder/`. Jalankan script dari folder itu atau pakai path lengkapnya. Aturan umum (bahasa Indonesia akademik, tanpa em dash, desimal koma, anti-halusinasi) dan daftar kesalahan umum ada di `/jr:salah`.

## Langkah 5b. Skrip presentasi (TXT, siap TTS)

Dikerjakan **setelah slide final** (urutan dan isi slide sudah disetujui dan dipilah), karena skrip harus mengikuti deck halaman demi halaman. Bila deck berubah, skrip dibuat ulang.

Tulis `skrip.json` (format di docstring `scripts/build_script.py`): satu entri per slide, berurutan, berisi narasi yang akan diucapkan penyaji. Lalu:

```
uv run python3 scripts/build_script.py skrip.json <outdir>/
```

Hasilnya dua berkas: `skrip-presentasi.txt` (tiap slide diawali "Slide N. Judul." supaya penyaji tahu kapan pindah slide) dan `skrip-presentasi-tanpa-penanda.txt` (narasi saja, untuk TTS).

Aturan menulis narasi:

- **Tanpa kata "kita".** Pakai kalimat pasif atau "RS setempat", "pasien lokal" (lihat `references/desain-visual.md`); `build_script.py` menolak skrip yang memuatnya.
- **Bersih, tanpa pengisi.** Tidak ada "baik", "selanjutnya", "seperti yang kita lihat", atau pengulangan judul slide. Langsung ke isi, dengan sapaan orang pertama.
- **Ditulis untuk telinga.** Kalimat pendek (maksimal sekitar 25 kata), satu gagasan per kalimat, angka penting disebut sekali dengan satuannya. Jangan membacakan tabel sel demi sel: sebut pesan slide, lalu 2 sampai 4 butir terpenting.
- **Angka dan istilah identik dengan slide dan brief.** Skrip bersumber dari `extract.md` yang sama.
- **Singkatan dan simbol dieja.** Script mengeja yang umum (TDS, mmHg, persen, PCC, dan lain-lain); nama studi atau singkatan khusus paper ditambahkan di `ejaan` (mis. "INTERACT2": "INTERACT dua"), dan singkatan yang memang dibaca sebagai kata di `biarkan`. Script berhenti dengan MASALAH bila masih ada simbol atau singkatan huruf besar yang belum dieja.
- **Durasi.** Isi `durasi_menit` dengan waktu bicara (durasi presentasi dikurangi waktu diskusi). Patokan 130 kata per menit; script memberi peringatan bila lebih dari 10% di atas target.
- **Skrip juga masuk ke speaker notes Canva** (aturan 4e): setelah skrip final, tempel narasi tiap slide ke notes halaman yang sama dan commit.
- **Tidak memuat** jawaban pertanyaan konsulen (itu di brief), penanda cek ulang, atau catatan untuk penyaji. Slide yang masih berisi data sementara harus dibereskan dulu, bukan dinarasikan.
- Untuk deck induk (semua rekomendasi masuk), skrip dibuat hanya untuk slide yang lolos pemilahan.
- **Audio latihan (standar): Edge TTS, satu file per slide.** Setelah skrip final:
  ```
  uv run --with edge-tts --with mutagen python3 scripts/build_audio.py skrip-presentasi.txt audio/ --gabung
  ```
  Hasilnya `audio/slide-NNN.mp3`, `latihan-lengkap.mp3`, dan `daftar-audio.txt` (durasi per slide dan total). Dibacakan kata demi kata, gratis, tanpa kuota AI. Suara default `id-ID-ArdiNeural`; `--voice id-ID-GadisNeural` untuk suara perempuan, `--rate -5%` bila terlalu cepat. Slide yang teksnya tidak berubah tidak dibuat ulang, jadi revisi satu slide cukup menjalankan perintah yang sama. Teks skrip terkirim ke layanan Microsoft, jadi skrip tidak boleh memuat identitas pasien. Suara Indonesia mengeja kata Inggris huruf demi huruf ("guideline" terdengar "gui-de-li-ni"), jadi script menulis ulang kata Inggris umum secara fonetik khusus untuk audio (daftar `LAFAL` di script; skrip tidak berubah). Jalankan `--cek-lafal` untuk melihat kata yang dieja ulang; kata salah lafal lain ditambahkan lewat `--lafal lafal.json`, dan bila berlaku umum, ke daftar `LAFAL`. Hasil audio tidak bisa didengarkan dari sesi ini: minta tim mendengarkan satu slide yang padat istilah sebelum diserahkan ke klien.
- NotebookLM hanya bila klien meminta suara yang lebih alami dan menerima kalimat yang tidak persis; pakai prompt dari `references/prompt-notebooklm-audio.md` (sumber notebook hanya file skrip tanpa penanda). ElevenLabs adalah opsi berbayar bila diminta suara premium.

**Aturan bahasa untuk semua keluaran (slide, notes, skrip, brief):** hindari kata "kita", jangan menulis rujukan halaman di subjudul, dan jangan mengisi data yang belum ada dengan asumsi (pakai `[perlu diisi]` merah atau hapus kotaknya). Rincian dan contoh di `references/desain-visual.md` bagian "Gaya bahasa dan isi".
