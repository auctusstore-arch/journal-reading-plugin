---
description: JR tahap 7: sesi Zoom 1-on-1 (form pre-zoom, panduan tutor, form post-zoom)
---

Semua path `scripts/`, `references/`, `assets/` di bawah relatif ke `.claude/skills/journal-reading-builder/`. Jalankan script dari folder itu atau pakai path lengkapnya. Aturan umum (bahasa Indonesia akademik, tanpa em dash, desimal koma, anti-halusinasi) dan daftar kesalahan umum ada di `/jr:salah`.

## Langkah 7. Fase Zoom (sesi 1-on-1)

Dikerjakan untuk order yang memuat Zoom, termasuk Zoom Only yang dibeli tanpa slide. Ikuti `references/jalur-zoom.md`; format form dan blok jawaban di `references/format-form.md`.

1. **Form pre-zoom (Z2).** Tulis bagian personal "Cek pemahaman paper" (4 sampai 6 pilihan ganda berkunci dan 1 soal take-home message) dari `extract.md`, lalu `uv run python3 scripts/build_form.py form-pre.json <outdir>/`. Script menambahkan pertanyaan baku kebutuhan sesi dan penilaian diri. Case report: tulis `"jenis_paper": "case_report"` di `form-pre.json` dan `form-post.json`, dan buat soal sesuai `references/jalur-case-report.md` C7. Serahkan `form-pre-zoom.txt` ke admin untuk ditempel di portal (H-3 sebelum Zoom).
2. **Baca jawaban (Z3).** User menempelkan blok `AUCTUS-JAWABAN v1` dari admin. Petakan kebutuhan, gap (self-rating rendah, soal salah, percaya diri berlebih), dan 2 sampai 3 area prioritas, lalu **petakan tiap prioritas ke nomor slide klien** yang harus dibahas (ekstrak slide per nomor lebih dulu). Setelah itu usulkan visual dari katalog dan tanyakan dulu mana yang perlu dibuat (Z4a).
3. **Panduan tutor (Z4).** Tulis `tutor.json`, lalu `uv run python3 scripts/build_tutor_guide.py tutor.json <outdir>/`. Isinya kebutuhan klien, peta gap beserta tabel Gap ke slide (wajib), agenda 60 menit, titik review slide, 6 sampai 8 simulasi tanya-jawab berurutan prioritas, dan kandidat 3 perbaikan. Hanya untuk tutor.
4. **Form post-zoom (Z5).** Bagian personal "Kebutuhan dokter" (apakah tiap kebutuhan terjawab, 1 sampai 2 soal cek ulang), lalu `build_form.py`. Script menambahkan kepuasan sesi, penilaian diri ulang, dan NPS.

Form post-presentasi (H+1, testimoni dan izin pakai) baku di website; skill tidak membuatnya.
