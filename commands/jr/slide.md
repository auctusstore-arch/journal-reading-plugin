---
description: JR tahap 4: buat slide di Canva dari template, fill.json, notes, QA visual
---

Semua path `scripts/`, `references/`, `assets/` di bawah relatif ke `.claude/skills/journal-reading-builder/`. Jalankan script dari folder itu atau pakai path lengkapnya. Aturan umum (bahasa Indonesia akademik, tanpa em dash, desimal koma, anti-halusinasi) dan daftar kesalahan umum ada di `/jr:salah`.

## Langkah 4. Buat slide di Canva

**Sebelum mulai:** connector Canva wajib login ke akun journal reading Auctus. Baca metadata master warna pilihan dengan `read-design`; bila tidak bisa diakses, berhenti dan minta user menghubungkan connector ke akun itu.

Baca `references/template-map.md` dan `references/desain-visual.md` dulu (wajib, termasuk pustaka ikon dan pemetaan ikon per slide; jalur studi juga harus memakai ikon, minimal 2 sampai 3 per slide isi). Yang kedua memuat aturan tampilan yang wajib dipenuhi semua deck: tidak text wall, ada penekanan dan ikon, kode warna kelas rekomendasi, tabel dan algoritma dibuat ulang (bukan tangkapan layar), serta pustaka ikon beserta `asset_id`-nya.

Baca `references/template-map.md` dulu. File itu berisi ID master, daftar halaman, halaman mana dipakai untuk tiap desain studi, dan placeholder tiap halaman.

**4a. Buat desain baru dari master (jangan edit master).** Panggil `merge-designs` dengan `type: "create_new_design"`, title `JR - <nama penyaji> - <penulis pertama> <tahun>`, dan **satu** operasi `insert_pages` dari master warna pilihan dengan `page_numbers` sesuai desain studi. Contoh RCT jalur default CASP (3 slide validitas, hasil, lokal, lalu Validity ringkasan = 6 salinan halaman 4): `[2,3,4,5,6,7,8,9,10,11,12,4,4,4,4,4,4,17,18,19,20,21,22,23]`. Jumlah salinan mengikuti jumlah pertanyaan checklist (`references/casp-dan-pakem-klien.md`, "Bentuk slide").

**Case report:** abaikan daftar halaman jalur studi; ikuti `references/jalur-case-report.md` C5.

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

0. **Cek tata letak otomatis (wajib, sebelum thumbnail).** Baca desain dengan `read-design` (`open_transaction`, field `design_content`; hasil besar tersimpan ke file) lalu jalankan:
   ```
   uv run python3 scripts/cek_tabrakan.py design.json --fix ops_tabrakan/
   ```
   Script melaporkan kartu atas yang berakhir kurang dari 30 px di atas kotak lebar di bawahnya, bayangan yang tidak sama ukuran atau posisi dengan kartunya, teks yang keluar kartu, dan kartu yang keluar slide, lalu menulis operasi perbaikan per halaman (kecilkan kartu ke batas aman, samakan bayangan). Jalankan untuk **semua halaman**, termasuk halaman yang tidak diedit pada revisi deck lama: tabrakan di deck klien B (slide 4, 10-12) berasal dari deck yang dibuat sebelum aturan jarak ada, dan lolos karena revisi hanya memeriksa halaman yang diubah. Kartu yang tidak bisa dikecilkan karena teksnya panjang ditandai "tidak bisa diperbaiki": ringkas teksnya atau turunkan kotak bawah. Samakan juga tinggi kartu dalam satu baris (Alasan memilih, Kekuatan & kelemahan) dan pangkas ruang kosong besar di bawah teks. Temuan QA dari subagen tentang tabrakan atau bayangan tidak boleh dilewati dengan alasan "slide buatan pemesan"; perbaiki atau tanyakan.
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
