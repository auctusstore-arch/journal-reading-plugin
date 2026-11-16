---
description: JR tahap 2-3: baca paper, extract.md, hitung ulang efek, appraisal per item
---

Semua path `scripts/`, `references/`, `assets/` di bawah relatif ke `.claude/skills/journal-reading-builder/`. Jalankan script dari folder itu atau pakai path lengkapnya. Aturan umum (bahasa Indonesia akademik, tanpa em dash, desimal koma, anti-halusinasi) dan daftar kesalahan umum ada di `/jr:salah`.

## Langkah 2. Baca paper sampai tuntas dan ekstrak data

Baca seluruh PDF, termasuk tabel, figur, supplementary bila ada, dan bagian Funding/COI. Buat `extract.md` di folder kerja berisi:

- Identitas: judul persis, penulis, jurnal, tahun;vol(no):hal, DOI, registrasi (NCT/PROSPERO), pendanaan dan COI.
- Desain studi. Ini menentukan halaman validity dan tool appraisal:
  - RCT: RoB 2.
  - Kohort/case-control/cross-sectional: NOS.
  - Akurasi diagnostik: QUADAS-2.
  - SR/MA: AMSTAR 2.
  - Guideline/konsensus: AGREE II, lewat jalur khusus di `references/jalur-guideline.md` (ekstraksi G1, peta rekomendasi dan gerbang persetujuan G2, pendalaman G3, appraisal G4, susunan slide G5). Langkah 2 sampai 4a di file ini diganti jalur itu; Langkah 4b sampai 6 tetap berlaku.
  - Narrative review: SANRA. Scoping review: kelengkapan pelaporan PRISMA-ScR. Keduanya lewat `references/jalur-review.md` (klasifikasi R0, ekstraksi R1, peta isi dan gerbang persetujuan R2, cek sitasi R3, appraisal R4, susunan slide R5), dengan pengaturan langkah yang sama seperti guideline.
- PICO, metode, alur partisipan (angka tiap kotak CONSORT/STARD/PRISMA), Table 1, outcome primer dan sekunder, serta harm.
- Untuk tiap angka: lokasi persisnya (mis. "Tabel 2, hal. 6"). Lokasi ini dipakai di slide validity, di speaker notes, dan di brief.

Aturan anti-halusinasi:

- Angka yang tidak ada di paper tidak boleh diisi. Tulis "tidak dilaporkan" dan jadikan bahan appraisal.
- Bila ragu membaca angka (PDF hasil scan, tabel terpotong), tandai `[CEK: ...]` dan masukkan ke `cek_ulang`.
- Indeksasi/quartile jurnal dan status guideline tidak boleh ditebak. Tulis apa yang bisa diverifikasi, sisanya tandai `[CEK]`.

Jangan lanjut ke slide sebelum ekstraksi lengkap. Semua deliverable bersumber dari `extract.md`, sehingga slide dan brief konsisten.

## Langkah 3. Hitung ulang dan nilai

1. Hitung ulang ukuran efek dari angka mentah dengan `scripts/effect_calc.py`:
   - `binary` untuk outcome dikotomus: RR, OR, ARR, NNT/NNH dengan CI.
   - `diag` untuk sensitivitas, spesifisitas, PPV, NPV, dan LR.
   - `mean` untuk MD dan SMD.
   Bila hasilnya berbeda dari paper, laporkan angka paper di slide. Selisihnya jadi catatan appraisal, bukan dikoreksi diam-diam. Hitung juga NNT lokal: 1 / (risiko dasar lokal x RRR). Bila risiko dasar lokal tidak diketahui, pakai contoh skenario dan sebut sebagai asumsi.
2. **Bila klien meminta checklist CASP** (atau pakemnya memuat CASP), pakai CASP sebagai tool utama dengan jawaban Ya, Tidak, Belum pasti beserta bukti per pertanyaan; pilih checklist menurut desain studi (RCT 11, kohort 12, SR 10, dan seterusnya) dan tampilkan NOS, RoB 2, atau tool lain hanya sebagai pembanding. Rincian pertanyaan dan bentuk slide: `references/casp-dan-pakem-klien.md`. Selain itu, nilai validity dengan tool yang sesuai desain, **per item instrumen, bukan per domain** (berlaku untuk NOS, AGREE II, AMSTAR 2, QUADAS-2, RoB 2, SANRA, PRISMA-ScR). Contoh: domain Selection pada NOS dinilai item demi item (representativeness, pemilihan kelompok non-exposed, penentuan exposure, outcome belum ada di awal), masing-masing dengan keputusan sendiri. Untuk **setiap item** catat tiga hal: (a) penilaian dengan istilah tool, (b) **bukti**: apa yang tertulis di paper beserta lokasinya (hal./tabel/figure) atau "tidak dilaporkan", dan (c) **alasan**: mengapa bukti itu menghasilkan penilaian tersebut, dihubungkan ke kriteria item di instrumen (bukan mengulang bukti). Konsulen sering bertanya "kenapa item ini bintang/skornya segini", dan PPDS harus bisa menjawab dari catatan ini. Ikuti aturan overall resmi tool (mis. RoB 2: satu domain High membuat overall High; AMSTAR 2: satu kelemahan kritis membuat overall Low). Rincian format dan batas minimum: `references/brief-schema.md`, bagian "Appraisal berbasis instrumen".
3. Tentukan importance (besar efek vs MCID, presisi CI), applicability (populasi, ketersediaan, Fornas/JKN, PNPK), dan GRADE untuk outcome primer.
4. Tulis kesimpulan penyaji yang boleh berbeda dari penulis, dengan alasan dari appraisal.

Rujukan cepat rumus dan cara membaca: `references/stat-cheatsheet.md`. Contoh jawaban gaya konsulen: `references/bank-pertanyaan-konsulen.md`.
