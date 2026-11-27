---
name: journal-reading-builder
description: Tim internal Auctus. Membuat paket journal reading lengkap untuk PPDS dari paper + kebutuhan mereka. Hasilnya slide Canva yang benar-benar siap presentasi (dari template journal reading Auctus navy/maroon/hijau) plus Brief & Checklist Persiapan dalam DOCX dan HTML (konteks/dasar ilmu, appraisal, apa yang dipresentasikan, mockup pertanyaan konsulen, checklist H-7 sampai H-0), serta perangkat sesi Zoom 1-on-1 (form pre-zoom, panduan tutor, form post-zoom). Pakai skill ini setiap kali ada permintaan journal reading, telaah jurnal, critical appraisal untuk presentasi, "buatkan slide JR", "bikin PPT journal reading", "brief journal reading", order jasa journal reading dari residen/PPDS, persiapan sesi Zoom journal reading, "form pre-zoom", "panduan tutor", jawaban form AUCTUS-JAWABAN yang ditempel, atau ada PDF paper yang harus dijadikan presentasi ilmiah (studi primer, SR-MA, guideline/konsensus/PNPK, review article, maupun case report), walaupun user tidak menyebut kata "skill" atau "template".
---

# Journal Reading Builder

Tujuan: dari 1 paper + kebutuhan 1 PPDS, hasilkan 6 deliverable yang bisa langsung dipakai tanpa diedit lagi:

1. **Desain Canva** berisi slide journal reading terisi penuh. Tautan Canva itulah yang diserahkan; tidak ada ekspor PPTX atau PDF.
2. **Brief & Checklist Persiapan** dalam `.docx`.
3. **Brief & Checklist Persiapan** dalam `.html` mandiri (checklist bisa dicentang, jawaban mockup bisa dibuka-tutup).
4. **Skrip presentasi** dalam `.txt`, siap dibacakan TTS, untuk didengarkan PPDS sebagai latihan (dibuat setelah slide final).
5. **Audio latihan** per slide (`.mp3`, Edge TTS) dari skrip itu, dibacakan kata demi kata.
6. **Rangkuman TLDR** satu berkas `.txt` (`tldr-jurnal-reading.txt`) yang meringkas journal reading dan audionya (lihat Langkah 5c).

Untuk order yang memuat sesi Zoom (Complete Bundle atau Zoom Only), ada tiga keluaran tambahan: form pre-zoom, panduan tutor, dan form post-zoom (Langkah 7).

"Siap presentasi" artinya tidak ada `[kurung siku]`, kotak kuning PETUNJUK, atau slide validity yang salah desain tersisa. Nomor slide sudah benar (tidak ada footer nama penyaji), figur asli paper sudah ditempel, dan speaker notes berisi poin bicara serta jawaban pertanyaan konsulen. Konsulen akan mengecek angka ke paper, jadi akurasi lebih penting daripada kecepatan. Satu angka karangan bisa mempermalukan PPDS di depan departemennya.

Semua teks keluaran berbahasa Indonesia akademik yang lugas, **tanpa em dash** (pakai koma, titik dua, atau kurung). Desimal pakai koma (8,0%).

Script ada di `scripts/` (termasuk `extract_recs.py` untuk tabel rekomendasi guideline, lihat `references/jalur-guideline.md`; case report lewat `references/jalur-case-report.md`). Contoh perintah di bawah memakai `uv run python3` (wajib di mesin tim Auctus karena python3 polos diblokir hook). Di lingkungan tanpa `uv` (mis. claude.ai), jalankan `python3` biasa dan pasang dependensi dengan `pip install python-docx pillow` bila belum ada. Simpan semua file kerja di scratchpad atau folder kerja order, jangan di repo.

Contoh hasil akhir brief (paper latihan fiktif) ada di `assets/contoh-output/`. Buka untuk melihat standar kualitas dan tampilan yang dituju.

Langkah slide butuh connector Canva yang login ke akun journal reading Auctus (akun tempat template master; ID di `references/template-map.md`). Bila master tidak bisa diakses, minta user menghubungkan connector ke akun itu. Bila connector tidak tersedia, tetap kerjakan brief, lalu buat `fill.json` sebagai teks isian per slide dan beri tahu user bahwa slide harus diisi manual dari template.

---

---

## Pembagian tahap dan paket

Skill ini dipecah menjadi command `/jr:*` (`.claude/commands/jr/`). Script, references, dan assets tetap di folder ini.

| Paket | Pintu masuk | Tahap |
|---|---|---|
| `paket-lengkap` | `/jr:lengkap` | intake, ekstrak, slide, brief, skrip, tldr, zoom |
| `asistensi-slide` | `/jr:asistensi` | intake, ekstrak, slide, brief, skrip, tldr |
| `zoom-1on1` | `/jr:zoom-saja` | intake ringan, ekstrak ringan, zoom |
| `kelas` | - | tidak ada kerja skill |

Tahap: `/jr:intake` (Langkah 1), `/jr:ekstrak` (2-3), `/jr:slide` (4), `/jr:brief` (5), `/jr:skrip` (5b), `/jr:tldr` (5c-6), `/jr:zoom` (7). Router: `/jr:paket`. Aturan umum dan kesalahan yang sering terjadi: `/jr:salah`.

Bila permintaan datang tanpa menyebut paket, tanya paket order lalu arahkan ke pintu masuknya. Jangan mengerjakan apa pun sebelum formulir intake lengkap (`/jr:intake`).
