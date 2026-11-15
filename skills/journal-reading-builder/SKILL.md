---
name: journal-reading-builder
description: Tim internal Auctus. Membuat paket journal reading lengkap untuk PPDS dari paper + kebutuhan mereka. Hasilnya slide Canva yang benar-benar siap presentasi (dari template journal reading Auctus navy/maroon/hijau) plus Brief & Checklist Persiapan dalam DOCX dan HTML (konteks/dasar ilmu, appraisal, apa yang dipresentasikan, mockup pertanyaan konsulen, checklist H-7 sampai H-0), serta perangkat sesi Zoom 1-on-1 (form pre-zoom, panduan tutor, form post-zoom). Pakai skill ini setiap kali ada permintaan journal reading, telaah jurnal, critical appraisal untuk presentasi, "buatkan slide JR", "bikin PPT journal reading", "brief journal reading", order jasa journal reading dari residen/PPDS, persiapan sesi Zoom journal reading, "form pre-zoom", "panduan tutor", jawaban form AUCTUS-JAWABAN yang ditempel, atau ada PDF paper yang harus dijadikan presentasi ilmiah (studi primer, SR-MA, guideline/konsensus/PNPK, maupun review article), walaupun user tidak menyebut kata "skill" atau "template".
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

Script ada di `scripts/` (termasuk `extract_recs.py` untuk tabel rekomendasi guideline, lihat `references/jalur-guideline.md`). Contoh perintah di bawah memakai `uv run python3` (wajib di mesin tim Auctus karena python3 polos diblokir hook). Di lingkungan tanpa `uv` (mis. claude.ai), jalankan `python3` biasa dan pasang dependensi dengan `pip install python-docx pillow` bila belum ada. Simpan semua file kerja di scratchpad atau folder kerja order, jangan di repo.

Contoh hasil akhir brief (paper latihan fiktif) ada di `assets/contoh-output/`. Buka untuk melihat standar kualitas dan tampilan yang dituju.

Langkah slide butuh connector Canva yang terhubung ke akun Canva Auctus (pemilik template master). Bila connector tidak tersedia, tetap kerjakan brief, lalu buat `fill.json` sebagai teks isian per slide dan beri tahu user bahwa slide harus diisi manual dari template.

---

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
| Bahasa Slide | Wajib | Minta. Menentukan bahasa slide, notes, skrip, dan suara audio. |
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

- **Klien sudah punya draf slide** (berlaku untuk semua jenis paper di atas): baca `references/jalur-draf-klien.md`. Ekstraksi tetap dari paper dulu; draf diaudit terhadap paper (angka salah, klaim berlebihan, bagian kosong), dipetakan ke struktur JR, lalu **user memilih** perbaiki di tempat atau pindah ke template Auctus. File klien tidak pernah diubah langsung. Brief, skrip, audio, dan TLDR tetap dibuat seperti biasa dari slide final.

User story/kebutuhan PPDS adalah input utama: alasan memilih paper, kasus pemicu, dan fokus konsulen masuk ke slide 4, ke mockup pertanyaan, dan ke bagian applicability. Bila PPDS tidak memberi kasus pemicu, hapus kotaknya atau isi "[perlu diisi]" merah dan tandai di laporan akhir. Jangan mengarang kasus atau identitas pasien.

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

## Langkah 4. Buat slide di Canva

Baca `references/template-map.md` dan `references/desain-visual.md` dulu (wajib, termasuk pustaka ikon dan pemetaan ikon per slide; jalur studi juga harus memakai ikon, minimal 2 sampai 3 per slide isi). Yang kedua memuat aturan tampilan yang wajib dipenuhi semua deck: tidak text wall, ada penekanan dan ikon, kode warna kelas rekomendasi, tabel dan algoritma dibuat ulang (bukan tangkapan layar), serta pustaka ikon beserta `asset_id`-nya.

Baca `references/template-map.md` dulu. File itu berisi ID master, daftar halaman, halaman mana dipakai untuk tiap desain studi, dan placeholder tiap halaman.

**4a. Buat desain baru dari master (jangan edit master).** Panggil `merge-designs` dengan `type: "create_new_design"`, title `JR - <nama penyaji> - <penulis pertama> <tahun>`, dan **satu** operasi `insert_pages` dari master warna pilihan dengan `page_numbers` sesuai desain studi. Contoh RCT: `[2,3,4,5,6,7,8,9,10,11,12,13,17,18,19,20,21,22,23]`.

Hal yang perlu diketahui tentang `merge-designs`:

- Tool ini butuh persetujuan eksplisit user per panggilan. Sebutkan judul dan halaman yang akan diambil.
- Tool ini hanya menerima satu operasi per panggilan.
- Urutan halaman hasil insert ke desain yang sudah ada tidak bisa diandalkan (pernah terbalik, pernah tidak). Jangan menebak: selalu baca judul halaman sesudahnya dan cocokkan dengan rencana. Langkah 4b memverifikasinya. Bila seluruh blok terbalik, satu operasi `move_pages` dengan daftar halaman ditulis mundur (mis. `from_page_numbers: [9,8,...,1]`, `to_after_page_number: 0`) membalikkannya dalam satu panggilan.
- Untuk menggandakan halaman (mis. 26, 30, 32, 33 pada jalur guideline/review), tulis nomornya berulang di `page_numbers`.
- Halaman 1 master adalah "Cara Pakai Template", bukan cover. Cover = halaman 2. Jangan ikutkan halaman 1 ke deck.
- Satu permintaan `merge-designs` dibatasi ukuran (sekitar 6 MB): menyalin 100 halaman sekaligus gagal dengan `RequestTooLargeException`. Buat desain dengan sekitar 50 halaman pertama, lalu sisipkan sisanya dengan panggilan kedua.
- Batas keras: desain di atas 100 halaman tidak bisa dibuka untuk diedit (`Editing a Canva Design with a size of 101 pages is not currently supported`). Rencanakan deck maksimal 100 slide; bila deck induk guideline melebihi itu, padatkan (gabungkan tabel pendukung, kurangi slide figur) atau pecah menjadi dua desain per bab.

**4b. Inventaris desain baru.**

1. Buka transaksi dengan `read-design` open_transaction pada design_id baru.
2. Hasil besar otomatis tersimpan ke file tool-results. Pakai file itu sebagai `design.json`.
3. Jalankan:
   ```
   uv run python3 scripts/list_placeholders.py design.json --json inv.json > inv.txt
   ```
4. Cek urutan judul halaman di `inv.txt`. Bila tidak sesuai urutan template, perbaiki dengan operasi `reorder_page` di edit-design (page_id, anchor_page_id, position before/after).
5. Jalankan ulang `list_placeholders.py` setelah reorder, karena nomor halaman dipakai untuk penomoran slide.

Transaksi kedaluwarsa bila lama menganggur. Kerjakan langkah 4c-4e tanpa jeda panjang. Bila kedaluwarsa, buka transaksi baru dan ulangi inventaris, karena locator bisa berubah.

**4c. Tulis `fill.json`.** Formatnya ada di docstring `scripts/make_ops.py`. Isi:

- Tidak ada `footer`. Template tidak lagi memuat teks nama penyaji di kiri bawah slide (dihapus 12 November 2026 atas permintaan pemesan); nama penyaji hanya di cover dan slide penutup. Jangan menambahkannya kembali.
- `texts`: setiap locator berflag `B` diisi teks final. Sel tabel `[ ]` dipetakan lewat posisi y,x dan label `T` di sekitarnya. Baris tabel yang tidak terpakai dimasukkan ke `delete` atau diisi "tidak dilaporkan".
- `notes`: penanda singkat saja; isi akhirnya adalah naskah skrip per slide (lihat 4e dan Langkah 5b).
- Pertahankan gaya template: judul tetap singkat dan netral. Pesan utama diletakkan di baris kesimpulan slide Hasil Utama dan slide Kesimpulan.
- Isi harus ringkas agar muat di kotak. Patokan: tidak lebih dari kurang lebih 1,5x panjang placeholder. Satu sel tabel berisi 1 frasa, dan setiap kolom poin maksimal 3 poin.

Lalu jalankan:
```
uv run python3 scripts/make_ops.py inv.json fill.json ops/
```
Script menghapus PETUNJUK (dan sisa footer bila deck dibuat dari salinan lama), menomori ulang slide, dan berhenti dengan exit 1 bila masih ada placeholder kosong, `[` tersisa, atau em dash. Perbaiki sampai `MASALAH` hilang. `PERINGATAN` panjang teks dicek di thumbnail.

**4d. Terapkan dan tempel figur.**

1. Kirim tiap `ops/ops_NN.json` ke `edit-design` (satu file per panggilan) dalam transaksi yang sama.
2. Figur kunci (slide Figur Kunci, dan figur alur partisipan bila lebih jelas dari diagram):
   - Render halaman PDF yang memuat figur: `pdftoppm -r 200 -png -f <hal> -l <hal> paper.pdf fig`.
   - Crop ke area figur dengan PIL (`uv run --with pillow`).
   - Upload: `create-upload-url`, lalu `curl -X POST -H "Content-Type: application/octet-stream" --data-binary @fig.png "<url>"`.
   - Masukkan ke slide dengan `insert_fill` (asset_type image, asset_id dari respons upload) pada posisi kotak placeholder figur. Hapus teks placeholder figur.
   - Elemen baru selalu berada di lapisan paling depan. Bila menutupi elemen lain, atur dengan `layer_element`.
   - Teks sumber "Sumber: Penulis et al., Jurnal Tahun, Figure X" wajib ada.

**4e. Speaker notes = naskah skrip per slide (WAJIB).** Catatan pembicara Canva setiap slide berisi **naskah yang akan diucapkan di slide itu**, kata demi kata sama dengan `skrip-presentasi.txt`, dalam bahasa skrip yang dipilih klien (mis. slide Indonesia, skrip dan notes Inggris). Bukan poin bicara, bukan angka beserta lokasinya, dan bukan pertanyaan konsulen: itu semua ada di brief. Pemesan memutuskan ini pada 15 November 2026 karena notes dipakai penyaji membaca langsung saat presentasi.

- Selama Langkah 4 isi notes seperlunya (satu kalimat penanda), karena naskah baru ada setelah slide final.
- Setelah skrip final (Langkah 5b), tulis naskah ke notes: satu operasi `replace_speaker_notes` per `page_id` dengan isi persis paragraf skrip slide itu, tanpa baris "Slide N. Judul." Pembatas bagian dan slide penutup ikut diberi naskah pendeknya.
- Slide yang tidak dibacakan (Referensi) boleh berisi satu kalimat "Slide ini tidak dibacakan" dan catatan cek rujukan.
- Pemetaan memakai urutan deck terkini, bukan nomor lama: baca `page_metadata` dari `read-design` dalam transaksi terbuka, karena pemesan bisa menyisipkan atau memecah slide (Identitas Artikel pernah dipecah dua, sehingga satu entri skrip dibagi ke dua halaman). Bila ada slide yang ditambah, tulis dulu naskahnya di skrip, baru ke notes.
- Hasilkan satu file operasi per halaman dari skrip dengan skrip Python kecil, lalu serahkan ke beberapa subagen (sekitar 10 halaman per subagen) pada transaksi yang sama, lalu commit setelah persetujuan.
- Setiap revisi slide yang mengubah isi wajib mengubah naskah di skrip dan notes sekaligus, supaya slide, notes, skrip, dan audio tidak berbeda.

**4f. QA visual, lalu commit.**

1. Ambil thumbnail semua halaman (`read-design` dengan thumbnails) dan periksa satu per satu:
   - teks meluber atau terpotong;
   - kotak kosong;
   - `[` tersisa;
   - figur buram;
   - nomor slide berurutan.
2. Perbaiki dengan `resize_element`, `format_text` (font_size), atau ringkas teksnya.
3. Ringkas hasil ke user dengan 2-3 thumbnail kunci, lalu minta persetujuan dan commit transaksi.
4. Setelah commit, selesai. **Jangan mengekspor ke PPTX atau PDF** (`export-design`) dan jangan mengunduh file slide: keputusan pemesan 12 November 2026, karena boros waktu dan pemakaian AI. Tim mengekspor sendiri dari Canva bila perlu. Serahkan tautan desain Canva. QA visual cukup lewat thumbnail `read-design`, bukan lembar kontak dari PDF.

**4g. Deck besar (lebih dari sekitar 25 slide).**

- Satu panggilan `edit-design` hanya untuk satu halaman dan mengembalikan seluruh isi halaman (sangat besar). Susun operasi per halaman (satu file per halaman) dan serahkan penerapannya ke subagen supaya konteks utama tidak penuh; beberapa subagen boleh mengerjakan halaman berbeda pada transaksi yang sama.
- Simpan (commit) per kelompok halaman, jangan menunggu semuanya selesai: pekerjaan panjang bisa terputus batas pemakaian atau transaksi kedaluwarsa.
- Untuk melanjutkan setelah terputus: baca desain, tandai halaman yang masih memuat teks "PETUNJUK" atau "[", lalu terapkan ulang hanya file operasi halaman itu. ID halaman dan locator tidak berubah antar transaksi pada desain yang sama.
- `make_ops.py` menghasilkan satu daftar operasi; untuk deck besar, kelompokkan ulang per halaman berdasarkan awalan locator (page_id) sebelum dikirim.

## Langkah 5. Brief & Checklist (DOCX + HTML)

Tulis `brief.json` mengikuti `references/brief-schema.md`. Contoh lengkap dan bagus ada di `references/brief-example.json`. Isinya diambil dari `extract.md` dan hasil appraisal yang sama dengan slide, jadi angka di brief, slide, dan notes harus identik.

Tujuan tiap bagian:

- **Critical appraisal berbasis instrumen (WAJIB breakdown per item).** Tabel validity di brief berisi satu baris per item instrumen (NOS 7 sampai 8, AMSTAR 2 16, AGREE II 23, SANRA 6, dan seterusnya), tiap baris memuat penilaian, bukti berlokasi, dan **alasan mengapa dinilai demikian**. Domain boleh dirangkum di baris tambahan (`rangkuman: true`), tetapi tidak boleh menggantikan item. `build_brief.py` menolak brief yang alasannya kosong atau jumlah barisnya kurang dari item instrumen. Di slide validity, penyajian juga per item: bila tabel template tidak memuat semua item, gandakan halaman validity dan bagi itemnya (alasan singkat di slide, alasan lengkap di speaker notes dan brief). Pertanyaan mockup bagian Appraisal harus mencakup item yang kontroversial atau tidak diberi bintang.

- **Konteks & dasar ilmu.** Hal yang PPDS harus kuasai di luar paper agar tidak gugup saat ditanya, misalnya patofisiologi, mekanisme obat atau tes, posisi guideline atau PNPK, dan istilah metodologi. Ini sering jadi titik lemah PPDS, jadi tulis cukup dalam tetapi padat.
- **Apa yang dipresentasikan.** Satu baris per slide atau kelompok slide: pesan kunci dan alokasi menit. Total menit sedikit di bawah durasi, untuk menyisakan waktu diskusi.
- **Mockup pertanyaan.** Isi 12-16 pertanyaan yang realistis untuk paper ini, bukan generik:
  - minimal 2 soal statistik dengan angka paper;
  - 2 soal tentang kelemahan terbesar;
  - 1 soal dasar ilmu atau patofisiologi;
  - 1 soal applicability di RS Indonesia;
  - 1-2 soal jebakan, yaitu data yang tidak dilaporkan, yang harus dijawab jujur.
  Sesuaikan dengan fokus konsulen dari intake. Jawaban model ditulis 2-4 kalimat dengan pola: jawab inti, tunjukkan bukti (halaman/tabel), lalu akui batasan.
- **Checklist.** Isi 16-24 item yang bisa dicentang dan spesifik paper, misalnya "bandingkan outcome primer dengan NCT0xxxx", bukan hanya "baca paper". Bila tanggal presentasi kurang dari 7 hari lagi, padatkan kelompok waktunya.

Jalankan:
```
uv run --with python-docx python3 scripts/build_brief.py brief.json <outdir>/
```
Script mengecek field wajib, em dash, jumlah kata (target 2.200-4.000), jumlah pertanyaan, dan penanda [CEK]. Buka HTML di browser untuk cek sekilas tampilan dan fungsi centang.

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

## Langkah 5c. Rangkuman TLDR (TXT)

Dikerjakan paling akhir, setelah slide, brief, skrip, dan audio final, karena TLDR merangkum semuanya dan harus memakai angka yang identik. Satu berkas teks biasa (`tldr-jurnal-reading.txt`, bukan `.md`), tanpa format markdown (tanpa `#`, `**`, atau tabel), supaya bisa ditempel ke WhatsApp, email, atau dibacakan.

Isi, dalam bahasa Indonesia tanpa em dash, **maksimal 2 menit** dibaca atau didengar (sekitar 250 kata pada 130 kata per menit; hitung dengan `wc -w`, jangan melebihi 260), urutan tetap. Bila terlalu panjang, ringkas butir 3, 4, dan 8 dulu, bukan membuang butir 5 (take-home message):

1. Judul: penyaji, judul paper, jurnal dan tahun, DOI, tanggal presentasi.
2. Pertanyaan penelitian dan desain studi (1 sampai 2 kalimat).
3. Hasil utama: 3 sampai 5 butir berangka (n/N, persen, ukuran efek dengan 95% CI, p), angka yang sama dengan slide.
4. Appraisal: tool yang dipakai, skor atau penilaian, dan GRADE atau level evidence; 3 kelemahan utama termasuk temuan penyaji.
5. Kesimpulan penyaji dan take-home message (satu kalimat).
6. Applicability dan, bila diminta fokus konsulen, jawaban singkatnya (mis. penerapan di Indonesia, strategi daerah).
7. Audio: jumlah file, durasi total (dari `audio/daftar-audio.txt`), suara yang dipakai, dan bahasa audio; satu kalimat bahwa audio dibacakan dari `skrip-presentasi.txt` dan belum didengarkan oleh pembuat.
8. Hal yang harus dicek PPDS (isi `cek_ulang`, versi ringkas).
9. Tautan: Canva (edit dan view) serta daftar nama file di folder.

Aturan: jangan menambah angka atau klaim yang tidak ada di `extract.md`, skrip, atau brief; salin dari sumber yang sama. Jangan memuat identitas pasien. Jangan membuat berkas TLDR terpisah untuk audio; rangkuman audio cukup butir 7.

## Langkah 6. Serahkan

Folder output order (mis. `JR-<nama>-<penulis><tahun>/`) berisi:
- `tautan-canva.txt` berisi tautan desain (slide tidak diekspor; tim mengekspor PPTX atau PDF sendiri dari Canva)
- `brief-....docx`
- `brief-....html`
- `skrip-presentasi.txt` dan `skrip-presentasi-tanpa-penanda.txt`
- `audio/` berisi audio latihan per slide dan `latihan-lengkap.mp3`
- `tldr-jurnal-reading.txt` (rangkuman TLDR, Langkah 5c)
- `extract.md` (arsip internal)

Laporkan ke user secara singkat:

- Link edit desain Canva. Untuk dibagikan ke PPDS, pakai link view publik dan minta PPDS memakai File, lalu Make a copy.
- Daftar file.
- Desain studi dan tool yang dipakai.
- Kesimpulan appraisal 1 kalimat.
- Semua item `cek_ulang`. Ini wajib disampaikan, karena PPDS yang harus memverifikasinya.
- Hal yang diasumsikan, misalnya kasus pemicu atau risiko dasar lokal.
- Untuk guideline: siapa yang menyetujui pilihan rekomendasi, berapa yang masuk dari total, dan bahwa skor AGREE II berasal dari satu penilai. Sertakan `peta-rekomendasi.md` di folder output.
- Untuk review article: jenis review dan dasarnya, siapa yang menyetujui pilihan klaim, hasil cek sitasi (berapa sesuai, dilebihkan, tidak bisa diakses), dan `peta-isi.md` di folder output.

## Langkah 7. Fase Zoom (sesi 1-on-1)

Dikerjakan untuk order yang memuat Zoom, termasuk Zoom Only yang dibeli tanpa slide. Ikuti `references/jalur-zoom.md`; format form dan blok jawaban di `references/format-form.md`.

1. **Form pre-zoom (Z2).** Tulis bagian personal "Cek pemahaman paper" (4 sampai 6 pilihan ganda berkunci dan 1 soal take-home message) dari `extract.md`, lalu `uv run python3 scripts/build_form.py form-pre.json <outdir>/`. Script menambahkan pertanyaan baku kebutuhan sesi dan penilaian diri. Serahkan `form-pre-zoom.txt` ke admin untuk ditempel di portal (H-3 sebelum Zoom).
2. **Baca jawaban (Z3).** User menempelkan blok `AUCTUS-JAWABAN v1` dari admin. Petakan kebutuhan, gap (self-rating rendah, soal salah, percaya diri berlebih), dan 2 sampai 3 area prioritas.
3. **Panduan tutor (Z4).** Tulis `tutor.json`, lalu `uv run python3 scripts/build_tutor_guide.py tutor.json <outdir>/`. Isinya kebutuhan klien, peta gap, agenda 60 menit, titik review slide, 6 sampai 8 simulasi tanya-jawab berurutan prioritas, dan kandidat 3 perbaikan. Hanya untuk tutor.
4. **Form post-zoom (Z5).** Bagian personal "Kebutuhan dokter" (apakah tiap kebutuhan terjawab, 1 sampai 2 soal cek ulang), lalu `build_form.py`. Script menambahkan kepuasan sesi, penilaian diri ulang, dan NPS.

Form post-presentasi (H+1, testimoni dan izin pakai) baku di website; skill tidak membuatnya.

## Kesalahan yang sering terjadi

- **Mengisi perbandingan edisi dari ingatan.** Pada guideline, perubahan dari edisi sebelumnya hanya diambil dari bagian perubahan di guideline baru atau dari PDF edisi lama; bila tidak ada, minta PDF-nya.
- **Langsung mengerjakan begitu menerima PDF.** Tunggu formulir intake lengkap (Langkah 1); tanpa itu hanya boleh meminta formulir.
- **Menyalin angka dari draf klien.** Draf diaudit terhadap paper, bukan dijadikan sumber `extract.md` (lihat `references/jalur-draf-klien.md`).
- **Memakai angka dari abstrak.** Abstrak kadang berbeda dari tabel. Ambil dari Results/tabel.
- **Hanya menampilkan RRR.** Selalu tampilkan angka absolut (n/N, %) dan ARR/NNT.
- **Appraisal generik.** Contoh yang salah: "sampel kecil" tanpa angka. Setiap kelemahan harus spesifik dan disertai dampaknya (membesarkan atau mengecilkan efek).
- **Appraisal diringkas per domain.** NOS "Selection: 3/4 bintang" tanpa menjelaskan item mana yang kehilangan bintang dan kenapa. Wajib per item dengan bukti dan alasan.
- **Slide validity yang salah.** Template punya 6 halaman validity (RoB 2, NOS, QUADAS-2, AMSTAR 2, AGREE II, SANRA). Hanya 1 yang boleh tersisa.
- **Isi melebihi kotak.** Lebih baik ringkas lalu taruh detail di notes daripada mengecilkan font di bawah 16 pt.
- **Memilih rekomendasi guideline sendiri.** Pilihan isi slide guideline adalah keputusan user lewat peta rekomendasi, bukan keputusan penyusun.
- **Memaksa guideline atau review ke halaman studi.** PICO, hasil utama, RoB/NOS/QUADAS/AMSTAR tidak dipakai untuk guideline dan narrative/scoping review.
- **Menilai narrative review dengan AMSTAR 2**, atau menjumlah PRISMA-ScR menjadi skor kualitas.
- **Mengutip klaim review tanpa membuka sumber primernya.**
- **Text wall.** Paragraf atau kalimat panjang di slide, tanpa kartu, ikon, atau penekanan. Lihat `references/desain-visual.md`.
- **Tangkapan layar tabel atau algoritma.** Keduanya dibuat ulang di halaman 37 dan 38.
- **Edit master.** Master dipakai publik lewat link view; jangan pernah mengubahnya.
- **Menambah keterangan program studi di baris penyaji.** Pada cover dan slide penutup, tulis cukup "dr. Nama" dan departemen. Jangan menambahkan ", Resident in Obstetrics and Gynecology" (atau padanan program studi lain) di belakang nama penyaji; keputusan pemesan, tim mengedit slide sendiri. Ini hanya berlaku untuk teks slide, brief tetap memuat prodi di meta.
- **Label kolom dan kartu memakai "Presenter's ...".** Pada slide berbahasa Inggris, tulis kepala kolom "Note" (bukan "Presenter's note") dan kartu "Assessment" (bukan "Presenter's assessment"). Padanan Indonesia: "Catatan" dan "Penilaian". Keputusan pemesan, tim mengedit slide sendiri.
- **Judul kartu "How to read it".** Pada slide Figur Kunci berbahasa Inggris, tulis judul kartu kanan "Interpretation" (bukan "How to read it"). Padanan Indonesia: "Interpretasi" (bukan "Cara membaca"). Keputusan pemesan, tim mengedit slide sendiri.
- **Judul kartu panjang untuk data yang tidak dilaporkan.** Pada slide luaran sekunder/maternal/neonatal berbahasa Inggris, judul kartu penjelasan cukup "Reporting Gap" (bukan "What the paper does not show"). Keputusan pemesan, tim mengedit slide sendiri.
- **Font tabel terlalu kecil.** Teks sel tabel minimal sekitar 22,5 sampai 24 (ukuran yang tampil di Canva) untuk volume teks seperti slide Subgroup dan Statistical Interpretation (3 kolom x 5 baris, satu frasa per sel). Di API `edit-design` angka yang sama terbaca sekitar 30 sampai 32 px (isi sel 31,3 px, kepala kolom 34,3 px, label baris 33,3 px; 1 pt Canva = 1,33 px). Bila isi tidak muat, ringkas kalimatnya atau kurangi jumlah baris/kolom; jangan kecilkan font di bawah batas itu. Setelah mengisi tabel, cek `fontSize` sel hasilnya (mis. lewat `read-design` dengan `open_transaction` pada satu halaman) dan jangan membiarkan sel berukuran lebih kecil dari halaman acuan tadi. Keputusan pemesan, tim mengedit slide sendiri.
- **PENTING: isi kartu berupa paragraf (wall of text).** Setiap kartu atau kotak yang berisi lebih dari satu klausa (mis. "Authors' conclusion", "Presenter's conclusion", "Clinical practice" di slide Kesimpulan & implikasi) wajib ditulis sebagai butir pendek, satu gagasan per butir, bukan satu paragraf. Pola yang benar: kalimat pembuka pendek bila perlu, lalu 2 sampai 3 butir (mis. "Results are mixed versus ARRIVE:" lalu butir "induction and pre-delivery stay rose", "cesarean did not fall (19.8% to 24.9%, p=0.224)", "the labor ward was strained"). Berlaku untuk semua slide berkartu: Latar belakang, Alasan memilih, Importance & applicability, Kekuatan & kelemahan, Penerapan, Pembahasan tematik, Kesimpulan. Di Canva gunakan `format_text` dengan `list_level: 1` dan `list_marker: "disc"` (atau tulis "• " per baris seperti di template) setelah `replace_text`; pastikan butir yang membungkus baris tetap rapi. Cek thumbnail: tidak boleh ada kartu dengan teks paragraf utuh. Keputusan pemesan, tim mengedit slide sendiri.
- **Kotak atas menimpa kotak bawah.** Pada slide berpola 2 sampai 3 kartu di atas dan 1 kotak lebar di bawah (Alasan memilih, Latar belakang, PICO, Importance & applicability, Penerapan, Pembahasan tematik, Kesimpulan), kartu atas tidak boleh bertabrakan dengan kotak bawah. Acuan dari slide Alasan memilih yang sudah dirapikan pemesan: kartu atas top 225 tinggi 437 (berakhir 662), kotak bawah top 700 tinggi 209, jadi jarak sekitar 25 sampai 40 px, dan tiap lapis kartu (termasuk bayangan tipis di belakangnya) diberi tinggi yang sama. Untuk tata letak 3 baris (Kesimpulan): baris 1 top 240 tinggi 250, baris 2 top 515 tinggi 230, kotak bawah top 775. Bila teks lebih tinggi dari kartu, turunkan kotak bawah atau perpendek teks; jangan biarkan kartu menembus kotak bawah. Cek thumbnail setiap slide berpola ini. Di master hijau, halaman 4, 5, 6, 17, 20, 29, dan 32 dalam keadaan kosong tidak bertabrakan; tabrakan muncul ketika teks terisi lebih panjang dan kartu ikut membesar (pernah kartu PICO tumbuh dari 420 ke 500 sampai 620 px). Karena itu cek thumbnail setelah mengisi, lalu perkecil teks atau atur ulang tinggi kartu dan posisi kotak bawah seperti acuan di atas. Halaman variasi berbutir 40 sampai 42 di master hijau sudah memakai jarak aman (lihat `template-map.md`); master navy dan maroon juga sudah punya halaman variasi 40 sampai 42.
- **Tinggi kartu berubah sendiri saat teks diganti.** Di Canva, kartu (grup) menyesuaikan tinggi dengan teks di dalamnya: setelah `replace_text` kartu bisa membesar (mis. kartu PICO 420 menjadi 620 px) atau menyusut (kartu Outcome 465 menjadi 345 px saat teks dipendekkan) sementara kotak di bawahnya tetap. Setelah mengisi slide berkartu, baca ulang tinggi bentuk kartu dan kembalikan ke tinggi seragam dengan `resize_element` pada bentuk kartu di dalam grup (bukan pada grupnya), termasuk bayangan tipis di belakangnya; lalu cek thumbnail.
- **Ikon di samping judul utama slide.** Judul utama slide (54 px) tidak diberi ikon atau lencana. Ikon hanya untuk kartu, baris tabel (tinggi baris 100 px atau lebih), daftar bernomor, atau kotak isi (lihat `references/desain-visual.md`). Keputusan pemesan, 15 November 2026; deck dr. Putri sempat memasang lencana judul lalu dihapus.
- **Deck berbahasa Inggris tetap diberi versi Indonesia untuk skrip dan audio.** Bila Bahasa Slide Inggris, buat skrip dan audio Inggris di folder utama (tulis sendiri `skrip-presentasi.txt`, jalankan `build_audio.py` dengan suara Inggris dan tanpa daftar `LAFAL`), lalu buat juga versi Indonesia di subfolder `versi-indonesia/` (`skrip.json` Indonesia, `build_script.py`, lalu `build_audio.py --voice id-ID-GadisNeural --lafal lafal.json --gabung`). Angka dan urutan slide harus identik dengan versi Inggris; nama asing (Shamoun, Bishop, Foley, Newcastle-Ottawa) dan singkatan khusus paper ditambahkan di `ejaan` atau `lafal.json`. Singkatan huruf besar seperti ARRIVE, GRADE, NICU, dan BMI wajib dieja di `ejaan` atau script berhenti. Tulis desimal dengan koma dan ribuan dengan huruf ("seribu sembilan ratus tujuh puluh"), bukan "1.970". Catat durasi total kedua versi di TLDR (butir 7). Permintaan pemesan, 15 November 2026.
- **Bayangan kotak bawah terlalu tinggi.** Bayangan tipis (bentuk hijau tua opasitas 0,1) di belakang kotak lebar bawah sering tertinggal lebih tinggi dari kotaknya, sehingga garis abu-abu menjulur di bawah kotak (pernah 180 dan 224 px di belakang kotak 166 px, slide CASP 30 sampai 32). Penyebabnya: bayangan bukan bagian grup kotak, jadi tidak ikut menyusut saat teks dipendekkan atau kotak diubah ukurannya. Aturannya: bayangan harus selalu sama lebar dan sama tinggi dengan kotak putihnya, digeser top +10 dan left +6 (kartu atas: top 245, left 106, kartu putih top 235, left 100). Setelah mengisi atau meresize slide berpola kartu atas + kotak bawah, baca tinggi kotak putih (anak grup), lalu `resize_element` bayangan ke lebar dan tinggi yang sama dan `position_element` ke top kotak +10, left kotak +6. Cek thumbnail: tidak boleh ada pita abu-abu di bawah atau di sisi kanan kotak lebih dari sekitar 10 px. Berlaku untuk semua slide berbayangan (Alasan memilih, Latar belakang, PICO, CASP, Applicability, Strategi).
- **Mengabaikan pakem klien.** Bila klien memberi format atau contoh deck, urutan dan nama bagiannya adalah kelengkapan minimal (pembatas bagian, Identitas, Kriteria Partisipan, Alur, empat slide CASP, Validity, Importance, Applicability, footer sumber halaman). Tambahan penyusun boleh, tetapi tidak boleh menggeser atau menghapus bagian klien. Lihat `references/casp-dan-pakem-klien.md`.
- **Menilai dengan NOS atau RoB padahal klien meminta CASP.** Pakai CASP sesuai desain dan jawab per pertanyaan (Ya, Tidak, Belum pasti) dengan bukti; tool lain hanya pembanding.
- **Slide Indonesia, skrip dan audio Inggris** bila klien meminta begitu: skrip mengikuti urutan akhir deck termasuk pembatas bagian dan slide CASP; folder bahasa lain dari urutan lama dipindah ke `arsip-urutan-lama/`.
- **Kunci jawaban bocor ke klien.** Kunci dan catatan soal cek pemahaman hanya di field `tutor` blok form; jangan menulisnya di teks soal, dan jangan mengirim `panduan-tutor` atau blok jawaban ke klien.
- **Form pre-zoom generik.** Soal cek pemahaman harus dari angka dan konsep paper ini (mis. arti HR 0,78 di paper itu), bukan "apa itu RCT". Pertanyaan baku sudah disisipkan script; jangan menulis ulang.
