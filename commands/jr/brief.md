---
description: JR tahap 5: Brief dan Checklist Persiapan (DOCX + HTML)
---

Semua path `scripts/`, `references/`, `assets/` di bawah relatif ke `.claude/skills/journal-reading-builder/`. Jalankan script dari folder itu atau pakai path lengkapnya. Aturan umum (bahasa Indonesia akademik, tanpa em dash, desimal koma, anti-halusinasi) dan daftar kesalahan umum ada di `/jr:salah`.

## Langkah 5. Brief & Checklist (DOCX + HTML)

Tulis `brief.json` mengikuti `references/brief-schema.md`. Contoh lengkap dan bagus ada di `references/brief-example.json`. Isinya diambil dari `extract.md` dan hasil appraisal yang sama dengan slide, jadi angka di brief, slide, dan notes harus identik.

Tujuan tiap bagian:

- **Critical appraisal berbasis instrumen (WAJIB breakdown per item).** Tabel validity di brief berisi satu baris per item instrumen (CASP: seluruh pertanyaan validitas sesuai desain; bila diminta klien NOS 7 sampai 8 atau AMSTAR 2 16; AGREE II 23, SANRA 6, dan seterusnya), tiap baris memuat penilaian, bukti berlokasi, dan **alasan mengapa dinilai demikian**. Domain boleh dirangkum di baris tambahan (`rangkuman: true`), tetapi tidak boleh menggantikan item. `build_brief.py` menolak brief yang alasannya kosong atau jumlah barisnya kurang dari item instrumen. Di slide validity, penyajian juga per item: bila tabel template tidak memuat semua item, gandakan halaman validity dan bagi itemnya (alasan singkat di slide, alasan lengkap di speaker notes dan brief). Pertanyaan mockup bagian Appraisal harus mencakup item yang kontroversial atau tidak diberi bintang, atau dijawab Tidak / Belum pasti.

- **Konteks & dasar ilmu.** Hal yang PPDS harus kuasai di luar paper agar tidak gugup saat ditanya, misalnya patofisiologi, mekanisme obat atau tes, posisi guideline atau PNPK, dan istilah metodologi. Ini sering jadi titik lemah PPDS, jadi tulis cukup dalam tetapi padat.
- **Apa yang dipresentasikan.** Satu baris per slide atau kelompok slide: pesan kunci dan alokasi menit. Total menit sedikit di bawah durasi, untuk menyisakan waktu diskusi.
- **Mockup pertanyaan.** Isi 12-16 pertanyaan yang realistis untuk paper ini, bukan generik:
  - minimal 2 soal statistik dengan angka paper;
  - 2 soal tentang kelemahan terbesar;
  - 1 soal dasar ilmu atau patofisiologi;
  - 1 soal applicability di RS Indonesia;
  - 1-2 soal jebakan, yaitu data yang tidak dilaporkan, yang harus dijawab jujur.
  Sesuaikan dengan fokus konsulen dari intake. Jawaban model ditulis 2-4 kalimat mengikuti teknik jawab 5 langkah di `references/bank-pertanyaan-konsulen.md` (klarifikasi bila perlu, jawab inti, bukti berlokasi, akui batasan, dan "belum menemukan datanya, akan dicek" bila tidak tahu; jangan mengarang). Langkah 1 dan 5 dipakai hanya bila relevan untuk pertanyaan itu.
- **Case report:** tidak ada soal statistik; `ringkasan` berisi kasus, diagnosis, terapi, luaran, dan pelajaran (tanpa ukuran efek), pertanyaan memakai daftar C6 di `references/jalur-case-report.md`, minimal 2 soal tentang diagnosis banding atau alasan terapi.
- **Checklist.** Isi 16-24 item yang bisa dicentang dan spesifik paper, misalnya "bandingkan outcome primer dengan NCT0xxxx", bukan hanya "baca paper". Bila tanggal presentasi kurang dari 7 hari lagi, padatkan kelompok waktunya.

Jalankan:
```
uv run --with python-docx python3 scripts/build_brief.py brief.json <outdir>/
```
Script mengecek field wajib, em dash, jumlah kata (target 2.200-4.000), jumlah pertanyaan, dan penanda [CEK]. Buka HTML di browser untuk cek sekilas tampilan dan fungsi centang.
