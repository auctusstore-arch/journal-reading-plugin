# Checklist CASP dan menyesuaikan deck dengan pakem klien

**CASP adalah tool appraisal default** untuk semua studi dan systematic review (keputusan pemesan, 26 November 2026). Bagian 4 dan 6 berlaku untuk setiap order tersebut. Bagian 1, 2, 3, dan 5 dipakai bila klien memberi format departemen atau contoh slide (PPTX, PDF, Canva). Bagian pakem dibuat dari kasus dr. Putri Nabila (15 November 2026), yang memberi contoh deck 38 slide ("Jurding Contoh.pptx", RCT besi intravena). Prinsipnya: **pakem klien adalah kelengkapan minimal.** Urutan, nama bagian, dan jenis slide klien harus ada dan berurutan sama. Isi tambahan penyusun (GRADE, applicability Indonesia, strategi RS daerah, pertanyaan diskusi, referensi) boleh ditambahkan, tetapi tidak boleh menggeser atau menghapus bagian klien.

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
| Validity, Importance, Applicability | salinan halaman 4 (ringkasan), 17, 29 | |

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

CASP (Critical Appraisal Skills Programme, casp-uk.net/casp-tools-checklists) adalah checklist per desain studi, lisensi CC BY-NC-SA: parafrase pertanyaannya, jangan menempel teks resmi utuh. Jawaban selalu salah satu dari **Ya, Tidak, Belum pasti** (can't tell). Sebut satu penilai (penyaji) di notes, dan setiap jawaban wajib disertai bukti satu kalimat dari paper (angka atau lokasi), bukan jawaban kosong. CASP tidak memberi skor total: jangan menjumlah jawaban Ya menjadi nilai atau ambang "layak".

Pilih checklist menurut desain, bukan menurut selera. Kolom "Baris validity" adalah pertanyaan yang masuk `appraisal.validity` (sub-pertanyaan dihitung satu baris bila dipisah).

| Desain paper | Nama di `meta.tool_appraisal` | Pertanyaan | Baris validity |
|---|---|---|---|
| RCT | CASP RCT Checklist | 11 | Q1 sampai Q6 (minimum 6) |
| Kohort (termasuk retrospektif, pre-post dua kelompok waktu, intervensi non-acak) | CASP Cohort Study Checklist | 12 | Q1 sampai Q6b (8) |
| Kasus-kontrol | CASP Case Control Study Checklist | 11 | Q1 sampai Q6b (7) |
| Cross-sectional / deskriptif | CASP Cross-Sectional Study Checklist | 11 | Q1 sampai Q6 (6) |
| Akurasi diagnostik | CASP Diagnostic Test Study Checklist | 12 | Q1 sampai Q6 (6) |
| Systematic review (dengan atau tanpa meta-analisis) | CASP Systematic Review Checklist | 10 | Q1 sampai Q5 (5) |
| Kualitatif | CASP Qualitative Checklist | 10 | Q1 sampai Q6 (6) |
| Evaluasi ekonomi | CASP Economic Evaluation Checklist | 12 | Q1 sampai Q4 (4) |
| Clinical prediction rule | CASP Clinical Prediction Rule Checklist | 11 | Q1 sampai Q6 (6) |

**Pengecualian:** guideline/konsensus memakai AGREE II (`jalur-guideline.md`), narrative review SANRA dan scoping review PRISMA-ScR (`jalur-review.md`). case report memakai JBI Case Reports (`jalur-case-report.md`) karena CASP tidak punya checklistnya.

**RoB 2, NOS, QUADAS-2, AMSTAR 2** dipakai hanya bila klien atau departemen memintanya. Saat itu tool yang diminta menjadi tool utama.

Urutan pertanyaan di bawah diparafrase dari checklist versi 2024 (kasus-kontrol: Oktober 2026), dibaca 26 November 2026. Bila situs CASP sudah menerbitkan versi baru, ikuti versi baru dan catat tahunnya di notes. Referensi slide dan brief: "Critical Appraisal Skills Programme. CASP [nama] Checklist. [tahun]. casp-uk.net".

### RCT (11)

- Validitas desain dan metode: 1 pertanyaan penelitian terfokus; 2 alokasi acak (dan tersembunyi); 3 semua peserta diperhitungkan di akhir; 4 penyamaran: (a) peserta, (b) investigator, (c) penilai atau analis luaran; 5 kelompok serupa di awal; 6 perlakuan setara selain intervensi.
- Hasil: 7 efek dilaporkan lengkap; 8 presisi dilaporkan; 9 manfaat melebihi bahaya dan biaya.
- Lokal: 10 dapat diterapkan pada populasi lokal; 11 nilai tambah dibanding intervensi yang sudah ada.

### Kohort (12)

- Validitas: 1 isu terfokus; 2 kohort direkrut dengan baik; 3 paparan diukur akurat; 4 luaran diukur akurat; 5a confounder penting teridentifikasi; 5b confounder diperhitungkan di desain atau analisis; 6a follow-up cukup lengkap; 6b follow-up cukup lama.
- Hasil: 7 apa hasilnya; 8 seberapa presisi; 9 apakah hasil dapat dipercaya.
- Lokal: 10 dapat diterapkan pada populasi lokal; 11 sesuai bukti lain; 12 implikasi untuk praktik.

### Kasus-kontrol (11)

- Validitas: 1 isu terfokus; 2 metode tepat untuk pertanyaannya; 3 kasus direkrut dengan baik; 4 kontrol dipilih dengan baik; 5 paparan diukur akurat; 6a confounder penting teridentifikasi; 6b confounder diperhitungkan di desain atau analisis.
- Hasil: 7 besar efek paparan; 8 presisi; 9 apakah hasil dapat dipercaya.
- Lokal: 10 dapat diterapkan pada populasi lokal; 11 sesuai bukti lain.

### Cross-sectional (11)

PDF resmi hanya memberi judul bagian pertama; pembagian di bawah adalah pengelompokan skill ini.

- Validitas: 1 isu terfokus; 2 metode tepat; 3 subjek direkrut dengan baik; 4 pengukuran akurat; 5 data dikumpulkan sesuai pertanyaan; 6 jumlah subjek cukup.
- Hasil: 7 penyajian dan hasil utama; 8 analisis cukup ketat; 9 temuan dinyatakan jelas.
- Lokal: 10 dapat diterapkan pada populasi lokal; 11 nilai penelitian.

### Diagnostik (12)

- Validitas: 1 pertanyaan terfokus; 2 pembanding baku emas tepat; 3 semua pasien menjalani tes dan baku emas; 4 hasil tes tidak terpengaruh hasil baku emas; 5 status penyakit populasi dijelaskan; 6 cara pemeriksaan dijelaskan rinci.
- Hasil: 7 apa hasilnya; 8 seberapa yakin (presisi).
- Lokal: 9 dapat diterapkan pada pasien kita; 10 tesnya dapat dikerjakan pada populasi kita; 11 semua luaran penting dipertimbangkan; 12 dampak pemakaian tes.

### Systematic review (10)

- Validitas: 1 pertanyaan terfokus; 2 jenis studi yang dicari tepat; 3 semua studi penting terjangkau; 4 kualitas studi dinilai; 5 penggabungan hasil wajar.
- Hasil: 6 hasil keseluruhan; 7 presisi hasil.
- Lokal: 8 dapat diterapkan lokal; 9 semua luaran penting dipertimbangkan; 10 manfaat sebanding bahaya dan biaya.

### Kualitatif (10)

- Validitas: 1 tujuan jelas; 2 metode kualitatif tepat; 3 desain sesuai tujuan; 4 strategi rekrutmen tepat; 5 pengumpulan data sesuai isu; 6 hubungan peneliti dan partisipan dipertimbangkan.
- Hasil: 7 etik dipertimbangkan; 8 analisis cukup ketat; 9 temuan dinyatakan jelas.
- Lokal: 10 nilai penelitian.

### Evaluasi ekonomi (12)

- Validitas: 1 pertanyaan terdefinisi baik; 2 alternatif yang dibandingkan diuraikan; 3 bukti efektivitas ada; 4 efek diidentifikasi, diukur, dan dinilai tepat.
- Biaya dan konsekuensi: 5 sumber daya dan biaya diidentifikasi, diukur, dan dinilai; 6 discounting; 7 hasil evaluasi; 8 analisis inkremental; 9 analisis sensitivitas.
- Lokal: 10 efektivitas setara di konteks kita; 11 biaya dapat diterjemahkan ke konteks kita; 12 layak dikerjakan di tempat kita.

### Clinical prediction rule (11)

- Validitas: 1 aturan prediksi terdefinisi jelas; 2 populasi derivasi mewakili; 3 divalidasi pada kelompok pasien berbeda; 4 prediktor dan luaran dinilai tersamar; 5 prediktor dan luaran dievaluasi pada seluruh sampel awal; 6 metode statistik derivasi dan validasi dijelaskan.
- Hasil: 7 performa aturan dapat dihitung; 8 presisi estimasi.
- Lokal: 9 andal dan dapat ditafsirkan untuk pasien kita; 10 dapat diterima di tempat kita; 11 mengubah keputusan atau informasi ke pasien.

### Bentuk slide

- **Kartu tiga per slide** (halaman template tiga kartu): judul kartu `Q1. Fokus masalah`; isi kartu diawali jawaban huruf kapital (`YA.`, `TIDAK.`, `BELUM PASTI.`) lalu bukti satu sampai dua kalimat; kotak bawah: ringkasan bagian. **Ini bentuk default.** Salin halaman 4 sebanyak yang dibutuhkan (tiga pertanyaan per slide; mis. kohort: tiga slide untuk 8 baris validitas, satu hasil, satu lokal). Pengelompokan slide mengikuti bagian checklist di atas.
- **Tabel empat kolom** (pakem klien): `Pertanyaan dan penilaian | Ya | Tidak | Belum pasti` dengan centang di kolom jawaban; tiga baris per slide, pertanyaan tebal diikuti kalimat bukti. Dipakai bila klien memberi contoh berbentuk tabel; ukuran font tabel minimal sekitar 22,5 sampai 24.
- Tulis pengelompokan klien apa adanya bila beda dari urutan resmi CASP (mis. klien memecah pertanyaan penyamaran tiga baris). Jangan menghapus pertanyaan resmi; di tabel slide boleh menggabung dua pertanyaan sub (5a dan 5b) dalam satu baris; di `brief.json` tetap satu baris per sub-pertanyaan.
- Setelah slide CASP, buat **satu slide Validity** (ringkasan jawaban pertanyaan validitas: berapa Ya, Belum pasti, Tidak, dan ancaman terbesar), lalu **Importance** (besar efek, presisi, MCID, NNT atau NNH) dan **Applicability** (populasi, ketersediaan, Fornas atau JKN, PNPK). Halaman validity bawaan template (RoB 2, NOS, QUADAS-2, AMSTAR 2) dihapus dari salinan order; tool lain tidak ditampilkan kecuali diminta klien.

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

- Isi `meta.tool_appraisal` dengan nama di tabel bagian 4 ditambah "(satu penilai)", mis. "CASP Cohort Study Checklist (satu penilai)". Jangan menyebut tool lain di kolom itu.
- Isi `appraisal.validity` dengan pertanyaan validitas (kolom "Baris validity"). Tiap baris: `domain` = nomor dan parafrase pertanyaan, `penilaian` = "Ya" / "Tidak" / "Belum pasti", `bukti` bermuatan lokasi paper, `alasan` minimal 8 kata. `kelas` terisi otomatis (Ya ok, Tidak bad, Belum pasti mid); timpa bila arah pertanyaannya lain. Pertanyaan hasil dan lokal dijawab di `importance` dan `applicability`, tiap poin diawali nomor pertanyaan dan jawabannya.
- Bila klien meminta perbandingan dengan tool lain, tulis di `validity_overall` saja.
- Ubah `rencana_presentasi` dan angka "slide N" di checklist mengikuti nomor slide akhir deck (termasuk pembatas bagian).
