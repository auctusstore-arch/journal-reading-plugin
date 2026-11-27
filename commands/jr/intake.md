---
description: JR tahap 1: gerbang formulir intake, butir wajib, penentuan jenis paper
---

Semua path `scripts/`, `references/`, `assets/` di bawah relatif ke `.claude/skills/journal-reading-builder/`. Jalankan script dari folder itu atau pakai path lengkapnya. Aturan umum (bahasa Indonesia akademik, tanpa em dash, desimal koma, anti-halusinasi) dan daftar kesalahan umum ada di `/jr:salah`.

## Langkah 1. Intake

**Gerbang intake: jangan mulai mengerjakan apa pun sebelum formulir intake diterima.** PDF atau tautan paper saja belum cukup. Tanpa formulir, jangan membaca paper sampai tuntas, jangan mengekstrak, jangan membuat desain Canva, dan jangan memanggil subagen. Yang boleh dilakukan hanya membalas singkat: sebut paper sudah diterima, lalu minta formulir intake (tempel daftar butir di bawah supaya tinggal diisi). Alasannya: bahasa slide, durasi, warna, fokus konsulen, dan status slide menentukan cara kerja sejak langkah pertama, dan mengulang deck jauh lebih mahal daripada menunggu.

Formulir intake datang dari tim dalam bentuk daftar butir seperti ini (titik "." berarti kosong):

```
Alasan / kasus pemicu
Paper
Departemen
Pembimbing
Judul paper
Status slide
Bahasa Slide
Bahasa Presentasi
Asal institusi
Fokus konsulen
Penyaji
Warna template
Presentasi (WIB)
Durasi (menit)
Prodi & semester
Jadwal Zoom
Disetujui pembimbing
```

| Butir | Wajib? | Bila kosong (".") atau tidak ada |
|---|---|---|
| Paper (PDF, DOI, atau tautan full text) | Wajib | Minta. Untuk guideline, PDF wajib. Untuk guideline juga tanyakan apakah PDF edisi sebelumnya (organisasi yang sama) bisa dilampirkan; itu dibutuhkan bila guideline baru tidak memuat bagian perbandingan sendiri. |
| Penyaji | Wajib | Minta. |
| Departemen | Wajib | Minta. |
| Prodi & semester | Wajib | Minta. Bila hanya prodi tanpa semester, pakai apa adanya dan jangan mengarang semester. |
| Presentasi (WIB) | Wajib | Minta. |
| Durasi (menit) | Wajib | Minta; jangan mengasumsikan 30 menit. |
| Bahasa Slide | Wajib | Minta. Menentukan bahasa teks di slide. |
| Bahasa Presentasi | Wajib | Minta. Bahasa presentasi lisan, bisa berbeda dari Bahasa Slide. Menentukan bahasa notes, skrip, dan suara audio. Jika kosong (order lama sebelum 16 November 2026), anggap sama dengan Bahasa Slide dan konfirmasi ke pemesan. |
| Asal institusi | Wajib | Minta. Mengisi `[FK / RS Pendidikan]` di cover. Order lama bisa kosong; tanyakan ke pemesan. |
| Warna template | Wajib | Minta (navy / maroon / hijau). |
| Status slide | Wajib | Minta. "belum" = buat dari awal. Bila PPDS sudah punya draf (PPTX, PDF, tautan Canva/Google Slides), minta berkasnya dan ikuti `references/jalur-draf-klien.md`; jangan membuat desain baru sebelum keputusan perbaiki-di-tempat atau pindah-template (D5). |
| Disetujui pembimbing | Wajib | Minta. Bila "Tidak" atau "belum", sampaikan risikonya (paper bisa diganti) dan tanyakan apakah tetap dikerjakan. |
| Judul paper | Opsional | Ambil dari paper. |
| Pembimbing | Opsional | Baris pembimbing dihilangkan dari cover. Jangan mengarang nama. |
| Alasan / kasus pemicu | Opsional | Kotak kasus pemicu dihapus atau diisi "[perlu diisi]" merah. Jangan mengarang kasus atau identitas pasien. |
| Fokus konsulen | Opsional | Pakai sebaran pertanyaan standar di brief. |
| Format departemen / contoh slide klien | Opsional | Bila klien menempelkan daftar format atau melampirkan contoh deck, baca `references/casp-dan-pakem-klien.md`: pakem klien menjadi kelengkapan minimal dan urutannya diikuti. |
| Jadwal Zoom | Opsional | Tidak dipakai di slide; catat di brief bila ada. |

Aturan gerbang:

- Butir wajib yang kosong atau bertanda "." ditanyakan **sekaligus dalam satu pesan**, lalu tunggu jawabannya. Jangan mengisi sendiri dengan default.
- Butir opsional yang kosong tidak perlu ditanyakan; kerjakan sesuai kolom kanan dan sebutkan di laporan serah terima.
- Setelah formulir lengkap, ulangi ringkas dalam satu baris apa yang akan dikerjakan (paper, penyaji, bahasa, warna, durasi), baru mulai Langkah 2.
- Bila user secara eksplisit meminta mulai tanpa formulir ("kerjakan dulu, datanya menyusul"), boleh mulai dari ekstraksi saja (Langkah 2 dan 3), tetapi jangan membuat desain Canva sampai butir wajib lengkap.

Tentukan jenis paper sejak intake, karena menentukan jalur kerja:

- Studi primer atau SR-MA (termasuk systematic review tanpa meta-analisis): ikuti Langkah 2 sampai 6 di bawah.
- **Guideline, konsensus, atau PNPK**: baca `references/jalur-guideline.md` dan ikuti jalur itu. Slide "Perbandingan dengan Edisi Sebelumnya" wajib dan hanya boleh diisi dari bagian perubahan di guideline baru atau dari PDF edisi lama yang dilampirkan (G2b). Bedanya yang paling penting: setelah ekstraksi, buat peta semua rekomendasi lalu **berhenti dan minta user menyetujui rekomendasi mana yang masuk slide**. Jangan memilih sendiri.
- **Review article yang bukan systematic review (narrative review, scoping review)**: baca `references/jalur-review.md`. Klasifikasikan dulu jenis review-nya dari bagian Metode (R0). Polanya sama dengan guideline: peta isi berisi semua klaim kunci, lalu **user menyetujui klaim mana yang masuk slide**.

- **Case report** (laporan 1 sampai 3 pasien): baca `references/jalur-case-report.md`. Klasifikasikan dulu (C0); case series belum punya jalur.

- **Klien sudah punya draf slide** (berlaku untuk semua jenis paper di atas): baca `references/jalur-draf-klien.md`. Ekstraksi tetap dari paper dulu; draf diaudit terhadap paper (angka salah, klaim berlebihan, bagian kosong), dipetakan ke struktur JR, lalu **user memilih** perbaiki di tempat atau pindah ke template Auctus. File klien tidak pernah diubah langsung. Brief, skrip, audio, dan TLDR tetap dibuat seperti biasa dari slide final.

User story/kebutuhan PPDS adalah input utama: alasan memilih paper, kasus pemicu, dan fokus konsulen masuk ke slide 4, ke mockup pertanyaan, dan ke bagian applicability. Bila PPDS tidak memberi kasus pemicu, hapus kotaknya atau isi "[perlu diisi]" merah dan tandai di laporan akhir. Jangan mengarang kasus atau identitas pasien.
