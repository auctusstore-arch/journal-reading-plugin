# Jalur draf klien (klien sudah punya draf slide)

Dipakai bila di intake "Status slide" menyatakan PPDS sudah punya draf (PPTX, PDF, atau tautan Canva/Google Slides). Jalur ini bukan pengganti jalur paper: ia ditempelkan di depan Langkah 2 sampai 4. Prinsipnya: **draf adalah klaim yang harus diaudit terhadap paper, bukan sumber kebenaran.** Konsulen mengecek angka ke paper, jadi angka draf yang tidak cocok dengan paper adalah temuan, bukan bahan yang disalin.

## D0. Terima dan klasifikasi draf

Tanyakan sekaligus di satu pesan (bersama butir intake lain yang masih kosong):

1. Bentuk draf: PPTX, PDF, tautan Canva, atau tautan Google Slides.
2. Apakah gaya dan susunan klien harus dipertahankan, atau boleh dipindah ke template Auctus.
3. Apakah ada bagian yang tidak boleh diubah (mis. slide permintaan pembimbing, kasus pemicu klien).

Cek cepat: apakah draf memuat identitas pasien. Bila ya, jangan ikut dibawa ke skrip, audio, atau TLDR; sampaikan ke user.

## D1. Baca draf

- PPTX: `uv run --with python-pptx python3 scripts/baca_draf.py draf.pptx draf-inventaris.md`. Hasilnya teks, tabel, notes, jumlah gambar, dan angka terdeteksi per slide.
- PDF: `pdftotext -layout draf.pdf -` dan render halaman bergambar dengan `pdftoppm -r 120 -png`.
- Tautan Canva: `read-design` (thumbnail dan teks). Tautan Google Slides: baca lewat skill gws.
- Slide bergambar (figur, atau tabel hasil tangkapan layar): buka gambarnya dan baca angkanya secara manual, lalu catat. Jangan menganggap gambar benar.

Simpan di `draf-inventaris.md`. Draf tidak pernah diubah pada tahap ini.

## D2. Baca paper dan ekstrak (tidak berubah)

Langkah 2 dan 3 di SKILL.md (atau jalur guideline/review bila jenis papernya itu) tetap dikerjakan penuh dari paper. **Ekstraksi tidak boleh bersumber dari draf.** Draf hanya dibaca setelah `extract.md` selesai, supaya selisih terlihat dan bukan tertular.

## D3. Audit draf terhadap paper

Buat `audit-draf.md`: satu tabel, satu baris per temuan.

```
| Slide | Jenis temuan | Isi draf | Menurut paper (lokasi) | Dampak | Tindakan |
```

Jenis temuan (pakai persis kata ini):

- **angka salah**: angka draf berbeda dari paper (tabel/hasil, bukan abstrak). Selalu sertakan lokasi paper.
- **angka tak bersumber**: angka tidak ada di paper (mungkin dari sumber lain atau karangan). Jangan dipertahankan tanpa sumber.
- **klaim berlebihan**: klaim lebih kuat dari paper atau dari hasil appraisal (mis. "terbukti" untuk hasil sekunder, RRR tanpa angka absolut).
- **kesimpulan tak didukung**: kesimpulan penyaji tidak mengikuti appraisal.
- **bagian kosong**: komponen JR standar yang tidak ada di draf (lihat pemetaan D4).
- **appraisal keliru**: tool tidak sesuai desain studi, domain dinilai tanpa bukti, atau aturan overall resmi tidak dipakai.
- **tidak konsisten**: angka yang sama berbeda antar slide, atau slide berbeda dari notes.
- **bahasa/format**: text wall, rujukan halaman di subjudul, kata "kita" (lihat `desain-visual.md`). Prioritas rendah, kecuali bila klien minta migrasi ke template.

Aturan:

- Setiap temuan angka wajib punya lokasi paper. Bila tidak bisa memastikan, tandai `[CEK]` dan masukkan ke `cek_ulang`; jangan menyatakan draf salah tanpa bukti.
- Hitung ulang efek yang dipakai draf dengan `scripts/effect_calc.py` bila ada yang meragukan. Selisih hitung dan paper dilaporkan sebagai catatan, bukan dikoreksi diam-diam (aturan Langkah 3).
- Temuan bukan hanya kesalahan: catat juga hal yang **sudah benar dan layak dipertahankan** (mis. kasus pemicu klien yang bagus), supaya perbaikan tidak membuang kerja klien.
- Jangan menulis ulang kalimat klien sebagai "perbaikan" bila hanya gaya. Ubah hanya yang salah atau tidak didukung.

## D4. Petakan ke struktur JR standar

Petakan tiap slide draf ke halaman template (`template-map.md`) yang sesuai desain studi, dalam tabel:

```
| Slide draf | Dipetakan ke | Status |
| 3 | Latar belakang (hal. 5) | ada, perlu koreksi |
| - | Validity (RoB 2) | kosong |
```

Status: **ada, sudah baik** / **ada, perlu koreksi** / **kosong** / **di luar struktur** (slide klien yang tidak punya padanan; tanyakan, jangan dibuang diam-diam). Komponen yang wajib ada pada deck siap presentasi: identitas paper, alasan/kasus pemicu, PICO atau padanan, metode dan alur, hasil utama dengan angka absolut, validity sesuai tool, importance, applicability, kekuatan dan kelemahan, kesimpulan, diskusi. Jalur guideline/review punya susunan sendiri (G5/R5).

## D5. Gerbang keputusan (berhenti dan tanya)

Serahkan `audit-draf.md` ringkas (jumlah temuan per jenis, 5 temuan terpenting) dan pemetaan D4 ke user, lalu minta keputusan **per draf**:

- **Jalur A, perbaiki di tempat.** Gaya dan susunan klien dipertahankan.
  - Draf berupa tautan Canva yang bisa diedit: salin dulu (jangan mengubah file klien), lalu terapkan koreksi dan tambahan dengan `edit-design` di salinan. Slide kosong ditambahkan dari master dengan gaya mengikuti draf bila memungkinkan.
  - Draf berupa PPTX/PDF/Google Slides: **tidak diedit.** Serahkan daftar koreksi per slide siap tempel (teks pengganti persis, lokasi paper) plus teks untuk slide yang kosong. Klien atau tim menerapkannya.
- **Jalur B, pindah ke template Auctus.** Jalankan Langkah 4 normal. Isi slide diambil dari `extract.md` yang sudah diaudit; konten klien yang **sudah benar** (kasus pemicu, urutan argumen, pilihan figur) dipakai ulang, sisanya diganti.

Bila user tidak memilih, usulkan B bila ada 5 temuan "angka salah" atau lebih, atau bila lebih dari separuh komponen standar kosong; usulkan A bila temuannya sedikit dan klien menekankan gayanya. Usulan hanyalah saran: keputusan tetap di user.

## D6. Pengerjaan setelah keputusan

- Jalur A atau B: slide akhir mengikuti Langkah 4e (speaker notes), 4f (QA visual), dan 4g bila besar.
- Brief & Checklist (Langkah 5) dibuat **seperti biasa dari `extract.md`**, ditambah bagian di checklist: "Terapkan koreksi dari audit draf (n temuan)" dan, bila Jalur A lewat daftar koreksi, "Pastikan semua koreksi sudah ditempel ke slide sebelum latihan".
- Skrip, audio, dan TLDR (5b, 5c) dibuat dari slide **final** (setelah koreksi diterapkan), bukan dari draf asli. Pada Jalur A dengan PPTX, skrip dan audio menunggu klien mengonfirmasi koreksi sudah diterapkan, karena skrip harus mengikuti deck.
- Mockup pertanyaan konsulen: tambahkan 1 sampai 2 soal dari kelemahan yang ditemukan di audit draf (mis. angka yang tadinya salah di draf).

## D7. Serah terima

Selain butir Langkah 6, laporkan:

- Jumlah temuan per jenis dan 3 temuan terpenting (angka draf vs angka paper, dengan lokasi).
- Keputusan A atau B dan siapa yang memutuskan.
- Hal klien yang dipertahankan.
- Slide yang tidak bisa dibaca atau diverifikasi (gambar tak terbaca, tangkapan layar).
- Bahwa draf klien tidak diubah. Sertakan `audit-draf.md` dan `draf-inventaris.md` di folder output.

## Kesalahan khas jalur ini

- **Menyalin angka dari draf ke extract.md.** Ekstraksi harus dari paper dulu.
- **Mengubah file klien langsung.** Selalu salinan.
- **Menimpa gaya klien tanpa diminta**, atau sebaliknya mempertahankan slide klien yang appraisalnya keliru demi sopan santun. Angka dan klaim tidak bisa ditawar; gaya bisa.
- **Menyatakan draf salah tanpa lokasi paper.**
- **Membuat skrip dan audio dari draf sebelum koreksi diterapkan.**
