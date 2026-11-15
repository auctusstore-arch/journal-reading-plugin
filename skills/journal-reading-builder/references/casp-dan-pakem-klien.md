# Checklist CASP dan menyesuaikan deck dengan pakem klien

Dipakai bila klien memberi format departemen, contoh slide (PPTX, PDF, Canva), atau meminta appraisal dengan CASP. Dibuat dari kasus dr. Putri Nabila (15 November 2026), yang memberi contoh deck 38 slide ("Jurding Contoh.pptx", RCT besi intravena) sebagai pakem. Prinsipnya: **pakem klien adalah kelengkapan minimal.** Urutan, nama bagian, dan jenis slide klien harus ada dan berurutan sama. Isi tambahan penyusun (GRADE, applicability Indonesia, strategi RS daerah, pertanyaan diskusi, referensi) boleh ditambahkan, tetapi tidak boleh menggeser atau menghapus bagian klien.

## 1. Membaca pakem klien

1. PPTX: `uv run --with python-pptx python3 scripts/baca_draf.py contoh.pptx pakem-inventaris.md`. Tautan Canva: `read-design`. Baca seluruh slide, termasuk tabel dan teks kecil di bawah.
2. Tulis `pakem-klien.md` di folder kerja: daftar slide berurutan dengan (a) nama slide, (b) komponen isi (mis. "Metode Penelitian: desain dan lokasi, periode dan peserta, randomisasi, analisis"), (c) bentuk (kartu, tabel, figur, pembatas), (d) catatan format (footer, kode centang). Tandai slide yang hanya dekoratif (mis. "Artikel" berisi sampul jurnal).
3. Contoh klien adalah paper lain. Jangan menyalin isi, angka, atau kesimpulannya. Ambil hanya struktur dan gaya.
4. Daftar komponen format departemen (teks yang ditempel klien) dan contoh slide harus disatukan: bila keduanya berbeda, ikuti contoh slide dan sebut selisihnya di laporan.

### Pakem dr. Putri Nabila (referensi, 38 slide)

| Bagian | Slide klien | Bentuk |
|---|---|---|
| Pembuka | Cover; Artikel (sampul jurnal); Identitas Artikel | tabel: judul, penulis, jurnal, tahun dan halaman, DOI, registrasi |
| PENDAHULUAN (pembatas) | Latar Belakang; Kesenjangan Penelitian | 3 poin; 2 poin dan satu kalimat pertanyaan |
| TUJUAN (pembatas) | Tujuan Penelitian | satu paragraf pendek |
| METODE (pembatas) | Metode Penelitian; Intervensi dan Luaran; Kriteria Partisipan; Alur Penelitian | 4 blok (desain dan lokasi, periode dan peserta, randomisasi, analisis); tabel; inklusi dan eksklusi dua kolom; figur CONSORT |
| HASIL (pembatas) | Karakteristik Dasar; Luaran Primer; Luaran Bayi (sekunder); Analisis Subkelompok; Respons terhadap Terapi; Keamanan | tabel dengan 1 kalimat pesan; figur forest plot |
| DISKUSI (pembatas) | Interpretasi hasil utama; Kekuatan dan Keterbatasan | 2 poin; dua kolom |
| KESIMPULAN (pembatas) | Kesimpulan | 4 poin |
| CRITICAL APPRAISAL (pembatas) | Analisis PICO; CASP Section A, B, kesebandingan, C, D; Validity (3 slide); Importance; Applicability | tabel PICO; tabel Ya, Tidak, Belum pasti dengan centang; tanya jawab |
| Penutup | TERIMA KASIH | |

Ciri gaya klien yang ikut dipertahankan:

- **Pembatas bagian** untuk tiap bagian utama, huruf kapital.
- **Footer sumber** di tiap slide isi: `Penulis et al. Jurnal Tahun · halaman paper`. Halaman diambil dari lokasi angka di `extract.md`.
- **Satu pesan di bawah tabel** (kalimat interpretasi) dan catatan kaki singkatan.
- Bahasa slide Indonesia dengan koma desimal dan titik ribuan; istilah baku (CASP, PICO, Validity, Importance, Applicability) tetap Inggris.

## 2. Memetakan pakem ke template Auctus

| Slide klien | Halaman template (master hijau/navy/maroon) | Catatan |
|---|---|---|
| Cover, Identitas Artikel | 2, 3 | tabel Identitas diisi: judul, penulis, jurnal, tahun, penerbit, DOI; desain, registrasi, etika di kotak bawah |
| Pembatas bagian | 24 | salin 7 kali (duplikasi halaman yang sama dalam satu `insert_pages`); angka besar 01 sampai 07; teks nama bagian huruf kapital; teks kecil satu baris deskripsi |
| Latar Belakang | 4 (tiga kartu) | satu kartu satu poin; kotak bawah: pertanyaan klinis |
| Kesenjangan Penelitian, Tujuan | 5 (dua kartu dan kotak bawah) | Tujuan memakai salinan halaman 5: kartu kiri tujuan, kartu kanan luaran, kotak bawah tujuan resmi |
| Metode Penelitian | 7 (lima baris bernomor) | desain dan lokasi, periode dan sampel, sampling dan pembagian kelompok, intervensi vs kontrol, randomisasi dan penyamaran |
| Kriteria Partisipan | 32 atau 18 (dua kartu dan kotak bawah) | inklusi kiri, eksklusi kanan |
| Intervensi dan Luaran | 8 (tabel tiga kolom) | |
| Alur Penelitian | 9 | diagram dibuat ulang bila paper tidak punya; tulis "dibuat ulang" di footer |
| Karakteristik Dasar, Luaran Primer, Luaran Sekunder, Subkelompok | 10, 11, 12 dan 38 | |
| Diskusi: interpretasi, perbandingan, kekuatan dan keterbatasan | 32 (kartu tematik), 27, 18 | |
| Kesimpulan | 20 | |
| Analisis PICO | 6 | dipindah ke bagian Critical Appraisal |
| CASP | halaman kartu tiga (halaman 4) atau tabel empat kolom | lihat bagian 4 |
| Validity, Importance, Applicability | 14 (ringkasan), 17, 29 | |

Urutan akhir selalu mengikuti klien: PICO pindah dari bagian Metode ke Critical Appraisal bila klien menaruhnya di sana.

## 3. Prosedur Canva untuk menyusun ulang deck yang sudah ada

Pelajaran dari kasus ini (deck 27 slide disusun ulang menjadi 40 slide):

1. **Satu slide, satu halaman, satu berkas operasi.** Bangun operasi lewat skrip Python: indeks lokator dari hasil `read-design` per halaman (simpan ke file; hasil besar otomatis tersimpan), isi kamus `{lokator_terakhir: teks baru}`, hasilkan `ops/NN_<page_id>.json` berisi `page_index`, `ops`, dan nomor final. Subagen hanya menyalin isi berkas ke `edit-design` pada transaksi yang sama; hasilkan satu subagen per sekitar 10 berkas.
2. **Duplikasi halaman dari desain itu sendiri** lewat `merge-designs` (`modify_existing_design`, `insert_pages` dengan `design_id` sama dan `page_numbers` berulang, mis. `[3,3,3,3,4,15]`). Salinan mendapat id halaman dan elemen baru; baca ulang untuk mendapat lokatornya. Pemetaan lokator dari halaman sumber ke salinan dilakukan menurut urutan sortir (top, left), bukan menurut id.
3. **Hapus halaman** salinan yang tidak dipakai dengan `delete_pages` (butuh persetujuan). Jangan pernah menghapus halaman yang diedit user.
4. **Urutan akhir** diatur terakhir dengan deretan `reorder_page` (page_id, anchor_page_id, before/after) dalam satu panggilan `edit-design`. Hitung deretan operasi dengan simulasi daftar, bukan menebak. Nomor slide diisi sesuai posisi akhir, bukan posisi saat diedit.
5. **Elemen multi-region** (satu teks berisi judul tebal dan isi biasa) jangan diganti dengan `replace_text`: pakai `find_and_replace_text` per region lama ke baru. Skrip membaca `textRegions` dan memastikan jumlah region baru sama dengan lama.
6. **Bentuk (shape) yang memuat teks** (kotak diagram alur) memakai `textContents`, bukan `type: text`; masukkan juga ke indeks.
7. **Footer sumber tanpa elemen baru:** ubah elemen nomor slide yang sudah ada: `position_element` (left 100, top 1028), `resize_element` (width 1720), lalu `replace_text` menjadi `Penulis et al., Jurnal Tahun · hal. X   |   NN`. Rata kanan bawaan tetap dipakai.
8. Teks hasil terjemah lebih panjang dari aslinya (bahasa Indonesia sekitar 10 sampai 25 persen lebih panjang). Periksa thumbnail untuk meluber, terutama sel tabel dan judul kartu.
9. Catatan pembicara berisi naskah skrip slide itu, berbahasa skrip (Inggris bila skrip Inggris). Bila isi slide berubah, ubah naskah di skrip dan notes sekaligus.

## 4. Checklist CASP

CASP (Critical Appraisal Skills Programme, casp-uk.net) adalah checklist per desain studi, lisensi CC BY-NC-SA: parafrase pertanyaannya, jangan menempel teks resmi utuh. Jawaban selalu salah satu dari **Ya, Tidak, Belum pasti** (can't tell). Sebut satu penilai (penyaji) di notes, dan setiap jawaban wajib disertai bukti satu kalimat dari paper (angka atau lokasi), bukan jawaban kosong.

Pilih checklist menurut desain, bukan menurut selera:

| Desain paper | Checklist CASP | Jumlah pertanyaan |
|---|---|---|
| RCT | Randomised Controlled Trial | 11 |
| Kohort (termasuk retrospektif dan pre-post dua kelompok waktu) | Cohort Study | 12 |
| Kasus-kontrol | Case Control Study | 11 |
| Systematic review (dengan atau tanpa meta-analisis) | Systematic Review | 10 |
| Akurasi diagnostik | Diagnostic Test Study | 12 |
| Kualitatif, ekonomi, prediksi klinis | Qualitative, Economic Evaluation, Clinical Prediction Rule | 10, 12, 12 |

Guideline dan narrative review tidak memakai CASP (lihat `jalur-guideline.md` dan `jalur-review.md`).

### RCT (11 pertanyaan)

- Bagian A, apakah hasil valid: 1 isu terfokus; 2 randomisasi tepat; 3 semua peserta diperhitungkan di akhir; 4 peserta, tenaga, dan penilai luaran disamarkan; 5 kelompok serupa di awal; 6 perlakuan setara selain intervensi.
- Bagian B, apa hasilnya: 7 besar efek; 8 presisi (IK).
- Bagian C, berguna secara lokal: 9 semua luaran penting dipertimbangkan; 10 manfaat sebanding dengan bahaya dan biaya; 11 dapat diterapkan pada populasi lokal.

### Kohort (12 pertanyaan)

- Bagian A, valid: 1 isu terfokus; 2 kohort direkrut dengan baik; 3 paparan diukur akurat; 4 luaran diukur akurat; 5a confounder penting teridentifikasi; 5b confounder diperhitungkan di desain atau analisis; 6a follow-up cukup lengkap; 6b follow-up cukup lama.
- Bagian B, hasil: 7 apa hasilnya; 8 seberapa presisi; 9 apakah hasil dapat dipercaya.
- Bagian C, lokal: 10 dapat diterapkan pada populasi lokal; 11 sesuai bukti lain; 12 implikasi untuk praktik.

### Systematic review (10 pertanyaan)

1 isu terfokus; 2 jenis studi yang dicari tepat; 3 semua studi penting terjangkau; 4 kualitas studi dinilai; 5 penggabungan hasil wajar; 6 hasil keseluruhan; 7 presisi hasil; 8 dapat diterapkan lokal; 9 semua luaran penting dipertimbangkan; 10 manfaat sebanding bahaya dan biaya.

### Bentuk slide

- **Kartu tiga per slide** (halaman template tiga kartu): judul kartu `Q1. Fokus masalah`; isi kartu diawali jawaban huruf kapital (`YA.`, `TIDAK.`, `BELUM PASTI.`) lalu bukti satu sampai dua kalimat; kotak bawah: ringkasan bagian. Cocok untuk kohort (empat slide: A satu, A dua, B, C) dan SR.
- **Tabel empat kolom** (pakem klien): `Pertanyaan dan penilaian | Ya | Tidak | Belum pasti` dengan centang di kolom jawaban; tiga baris per slide, pertanyaan tebal diikuti kalimat bukti. Dipakai bila klien memberi contoh berbentuk tabel; ukuran font tabel minimal sekitar 22,5 sampai 24.
- Tulis pengelompokan klien apa adanya bila beda dari urutan resmi CASP (mis. klien memecah pertanyaan penyamaran tiga baris). Jangan menghapus pertanyaan resmi; boleh menggabung dua pertanyaan sub (5a dan 5b) dalam satu baris.
- Setelah slide CASP, buat **satu slide Validity** (ringkasan jawaban bagian A: berapa Ya, Belum pasti, Tidak, dan ancaman terbesar), lalu **Importance** (besar efek, presisi, MCID, NNT atau NNH) dan **Applicability** (populasi, ketersediaan, Fornas atau JKN, PNPK). NOS, RoB 2, atau tool lain boleh ditampilkan sebagai pembanding di slide Validity, tetapi CASP adalah tool utama bila klien memintanya.

### Aturan jawaban

- Studi observasional pre-post: komponen "perlakuan setara" dan "kelompok serupa di awal" hampir selalu **Belum pasti** atau **Tidak**; jangan memberi Ya hanya karena tabel dasar terlihat mirip.
- Bila penulis menyatakan "tidak ada confounder" tanpa analisis, jawab **Tidak** pada pertanyaan confounder dan jelaskan.
- Jangan menjawab pertanyaan penerapan lokal dengan opini; sebut data yang ada (populasi, IMT, sumber daya) dan tandai `cek_ulang` bila butuh Fornas, JKN, atau PNPK.

## 5. Bahasa slide dan skrip

Pakem klien dapat meminta slide Indonesia sementara skrip dan audio Inggris. Aturan:

- Slide: Indonesia (angka koma desimal), kecuali istilah baku.
- Skrip dan audio: Inggris di folder utama (`skrip-presentasi.txt`, `skrip-presentasi-tanpa-penanda.txt`, `audio/`); ditulis sendiri karena `build_script.py` memakai aturan ejaan Indonesia. Audio: salin `build_audio.py` dengan `LAFAL = []` dan suara `en-US-AriaNeural`, jalankan dengan `--gabung`.
- Skrip mengikuti urutan akhir deck dengan satu entri per slide, termasuk pembatas (satu kalimat pembuka bagian) dan setiap slide CASP. Slide referensi tidak dibacakan.
- Notes pembicara = naskah skrip per slide, berbahasa skrip (Inggris bila skrip Inggris).
- Bila ada folder versi bahasa lain dari urutan lama, pindahkan ke `arsip-urutan-lama/` dan beri tahu user bahwa urutannya sudah tidak sama dengan deck.

## 6. Brief untuk appraisal CASP

- Isi `meta.tool_appraisal` dengan "CASP Cohort Study Checklist (satu penilai)" (atau checklist lain). Jangan menyebut NOS di kolom itu: `build_brief.py` lalu menuntut pemecahan NOS per item dan menolak ringkasan.
- Isi `appraisal.validity` dengan pertanyaan CASP bagian A (Q1 sampai Q6 untuk kohort), tiap baris punya `penilaian` (Ya, Tidak, Belum pasti), `bukti` bermuatan lokasi paper, dan `alasan` minimal 8 kata. Pertanyaan bagian B dan C masuk ke `importance` dan `applicability`.
- Tulis NOS atau tool lain sebagai pembanding di `validity_overall` saja.
- Ubah `rencana_presentasi` dan angka "slide N" di checklist mengikuti nomor slide akhir deck (termasuk pembatas bagian).
