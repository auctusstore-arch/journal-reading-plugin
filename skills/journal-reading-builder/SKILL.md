---
name: journal-reading-builder
description: Tim internal Auctus. Membuat paket journal reading lengkap untuk PPDS dari paper + kebutuhan mereka. Hasilnya slide Canva yang benar-benar siap presentasi (dari template journal reading Auctus navy/maroon/hijau) plus Brief & Checklist Persiapan dalam DOCX dan HTML (konteks/dasar ilmu, appraisal, apa yang dipresentasikan, mockup pertanyaan konsulen, checklist H-7 sampai H-0). Pakai skill ini setiap kali ada permintaan journal reading, telaah jurnal, critical appraisal untuk presentasi, "buatkan slide JR", "bikin PPT journal reading", "brief journal reading", order jasa journal reading dari residen/PPDS, atau ada PDF paper yang harus dijadikan presentasi ilmiah (studi primer, SR-MA, guideline/konsensus/PNPK, maupun review article), walaupun user tidak menyebut kata "skill" atau "template".
---

# Journal Reading Builder

Tujuan: dari 1 paper + kebutuhan 1 PPDS, hasilkan 5 deliverable yang bisa langsung dipakai tanpa diedit lagi:

1. **Desain Canva** berisi slide journal reading terisi penuh. Tautan Canva itulah yang diserahkan; tidak ada ekspor PPTX atau PDF.
2. **Brief & Checklist Persiapan** dalam `.docx`.
3. **Brief & Checklist Persiapan** dalam `.html` mandiri (checklist bisa dicentang, jawaban mockup bisa dibuka-tutup).
4. **Skrip presentasi** dalam `.txt`, siap dibacakan TTS, untuk didengarkan PPDS sebagai latihan (dibuat setelah slide final).
5. **Audio latihan** per slide (`.mp3`, Edge TTS) dari skrip itu, dibacakan kata demi kata.

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
| Paper (PDF, DOI, atau tautan full text) | Wajib | Minta. Untuk guideline, PDF wajib. |
| Penyaji | Wajib | Minta. |
| Departemen | Wajib | Minta. |
| Prodi & semester | Wajib | Minta. Bila hanya prodi tanpa semester, pakai apa adanya dan jangan mengarang semester. |
| Presentasi (WIB) | Wajib | Minta. |
| Durasi (menit) | Wajib | Minta; jangan mengasumsikan 30 menit. |
| Bahasa Slide | Wajib | Minta. Menentukan bahasa slide, notes, skrip, dan suara audio. |
| Warna template | Wajib | Minta (navy / maroon / hijau). |
| Status slide | Wajib | Minta. "belum" = buat dari awal; status lain = tanyakan desain yang sudah ada sebelum membuat baru. |
| Disetujui pembimbing | Wajib | Minta. Bila "Tidak" atau "belum", sampaikan risikonya (paper bisa diganti) dan tanyakan apakah tetap dikerjakan. |
| Judul paper | Opsional | Ambil dari paper. |
| Pembimbing | Opsional | Baris pembimbing dihilangkan dari cover. Jangan mengarang nama. |
| Alasan / kasus pemicu | Opsional | Kotak kasus pemicu dihapus atau diisi "[perlu diisi]" merah. Jangan mengarang kasus atau identitas pasien. |
| Fokus konsulen | Opsional | Pakai sebaran pertanyaan standar di brief. |
| Jadwal Zoom | Opsional | Tidak dipakai di slide; catat di brief bila ada. |

Aturan gerbang:

- Butir wajib yang kosong atau bertanda "." ditanyakan **sekaligus dalam satu pesan**, lalu tunggu jawabannya. Jangan mengisi sendiri dengan default.
- Butir opsional yang kosong tidak perlu ditanyakan; kerjakan sesuai kolom kanan dan sebutkan di laporan serah terima.
- Setelah formulir lengkap, ulangi ringkas dalam satu baris apa yang akan dikerjakan (paper, penyaji, bahasa, warna, durasi), baru mulai Langkah 2.
- Bila user secara eksplisit meminta mulai tanpa formulir ("kerjakan dulu, datanya menyusul"), boleh mulai dari ekstraksi saja (Langkah 2 dan 3), tetapi jangan membuat desain Canva sampai butir wajib lengkap.

Tentukan jenis paper sejak intake, karena menentukan jalur kerja:

- Studi primer atau SR-MA (termasuk systematic review tanpa meta-analisis): ikuti Langkah 2 sampai 6 di bawah.
- **Guideline, konsensus, atau PNPK**: baca `references/jalur-guideline.md` dan ikuti jalur itu. Bedanya yang paling penting: setelah ekstraksi, buat peta semua rekomendasi lalu **berhenti dan minta user menyetujui rekomendasi mana yang masuk slide**. Jangan memilih sendiri.
- **Review article yang bukan systematic review (narrative review, scoping review)**: baca `references/jalur-review.md`. Klasifikasikan dulu jenis review-nya dari bagian Metode (R0). Polanya sama dengan guideline: peta isi berisi semua klaim kunci, lalu **user menyetujui klaim mana yang masuk slide**.

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
2. Nilai validity dengan tool yang sesuai desain. Untuk setiap domain, sebut penilaian dan bukti halaman/tabel. Ikuti aturan overall resmi tool (mis. RoB 2: satu domain High membuat overall High; AMSTAR 2: satu kelemahan kritis membuat overall Low).
3. Tentukan importance (besar efek vs MCID, presisi CI), applicability (populasi, ketersediaan, Fornas/JKN, PNPK), dan GRADE untuk outcome primer.
4. Tulis kesimpulan penyaji yang boleh berbeda dari penulis, dengan alasan dari appraisal.

Rujukan cepat rumus dan cara membaca: `references/stat-cheatsheet.md`. Contoh jawaban gaya konsulen: `references/bank-pertanyaan-konsulen.md`.

## Langkah 4. Buat slide di Canva

Baca `references/template-map.md` dan `references/desain-visual.md` dulu. Yang kedua memuat aturan tampilan yang wajib dipenuhi semua deck: tidak text wall, ada penekanan dan ikon, kode warna kelas rekomendasi, tabel dan algoritma dibuat ulang (bukan tangkapan layar), serta pustaka ikon beserta `asset_id`-nya.

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
- `notes`: speaker notes untuk setiap page_id (lihat 4e).
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

**4e. Speaker notes.** Setiap slide berisi:

- 2-4 poin bicara dalam bahasa lisan.
- Angka penting beserta lokasinya di paper.
- 1-3 pertanyaan konsulen yang paling mungkin muncul di slide itu, beserta jawaban singkatnya.

Slide Diskusi: tulis jawaban penyaji untuk ketiga pertanyaan diskusi. Notes ditulis untuk dibaca PPDS saat latihan, jadi gunakan sapaan orang pertama ("Saya menilai ...").

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
- **Tidak memuat** jawaban pertanyaan konsulen (itu di brief dan speaker notes), penanda cek ulang, atau catatan untuk penyaji. Slide yang masih berisi data sementara harus dibereskan dulu, bukan dinarasikan.
- Untuk deck induk (semua rekomendasi masuk), skrip dibuat hanya untuk slide yang lolos pemilahan.
- **Audio latihan (standar): Edge TTS, satu file per slide.** Setelah skrip final:
  ```
  uv run --with edge-tts --with mutagen python3 scripts/build_audio.py skrip-presentasi.txt audio/ --gabung
  ```
  Hasilnya `audio/slide-NNN.mp3`, `latihan-lengkap.mp3`, dan `daftar-audio.txt` (durasi per slide dan total). Dibacakan kata demi kata, gratis, tanpa kuota AI. Suara default `id-ID-ArdiNeural`; `--voice id-ID-GadisNeural` untuk suara perempuan, `--rate -5%` bila terlalu cepat. Slide yang teksnya tidak berubah tidak dibuat ulang, jadi revisi satu slide cukup menjalankan perintah yang sama. Teks skrip terkirim ke layanan Microsoft, jadi skrip tidak boleh memuat identitas pasien. Suara Indonesia mengeja kata Inggris huruf demi huruf ("guideline" terdengar "gui-de-li-ni"), jadi script menulis ulang kata Inggris umum secara fonetik khusus untuk audio (daftar `LAFAL` di script; skrip tidak berubah). Jalankan `--cek-lafal` untuk melihat kata yang dieja ulang; kata salah lafal lain ditambahkan lewat `--lafal lafal.json`, dan bila berlaku umum, ke daftar `LAFAL`. Hasil audio tidak bisa didengarkan dari sesi ini: minta tim mendengarkan satu slide yang padat istilah sebelum diserahkan ke klien.
- NotebookLM hanya bila klien meminta suara yang lebih alami dan menerima kalimat yang tidak persis; pakai prompt dari `references/prompt-notebooklm-audio.md` (sumber notebook hanya file skrip tanpa penanda). ElevenLabs adalah opsi berbayar bila diminta suara premium.

**Aturan bahasa untuk semua keluaran (slide, notes, skrip, brief):** hindari kata "kita", jangan menulis rujukan halaman di subjudul, dan jangan mengisi data yang belum ada dengan asumsi (pakai `[perlu diisi]` merah atau hapus kotaknya). Rincian dan contoh di `references/desain-visual.md` bagian "Gaya bahasa dan isi".

## Langkah 6. Serahkan

Folder output order (mis. `JR-<nama>-<penulis><tahun>/`) berisi:
- `tautan-canva.txt` berisi tautan desain (slide tidak diekspor; tim mengekspor PPTX atau PDF sendiri dari Canva)
- `brief-....docx`
- `brief-....html`
- `skrip-presentasi.txt` dan `skrip-presentasi-tanpa-penanda.txt`
- `audio/` berisi audio latihan per slide dan `latihan-lengkap.mp3`
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

## Kesalahan yang sering terjadi

- **Langsung mengerjakan begitu menerima PDF.** Tunggu formulir intake lengkap (Langkah 1); tanpa itu hanya boleh meminta formulir.
- **Memakai angka dari abstrak.** Abstrak kadang berbeda dari tabel. Ambil dari Results/tabel.
- **Hanya menampilkan RRR.** Selalu tampilkan angka absolut (n/N, %) dan ARR/NNT.
- **Appraisal generik.** Contoh yang salah: "sampel kecil" tanpa angka. Setiap kelemahan harus spesifik dan disertai dampaknya (membesarkan atau mengecilkan efek).
- **Slide validity yang salah.** Template punya 6 halaman validity (RoB 2, NOS, QUADAS-2, AMSTAR 2, AGREE II, SANRA). Hanya 1 yang boleh tersisa.
- **Isi melebihi kotak.** Lebih baik ringkas lalu taruh detail di notes daripada mengecilkan font di bawah 16 pt.
- **Memilih rekomendasi guideline sendiri.** Pilihan isi slide guideline adalah keputusan user lewat peta rekomendasi, bukan keputusan penyusun.
- **Memaksa guideline atau review ke halaman studi.** PICO, hasil utama, RoB/NOS/QUADAS/AMSTAR tidak dipakai untuk guideline dan narrative/scoping review.
- **Menilai narrative review dengan AMSTAR 2**, atau menjumlah PRISMA-ScR menjadi skor kualitas.
- **Mengutip klaim review tanpa membuka sumber primernya.**
- **Text wall.** Paragraf atau kalimat panjang di slide, tanpa kartu, ikon, atau penekanan. Lihat `references/desain-visual.md`.
- **Tangkapan layar tabel atau algoritma.** Keduanya dibuat ulang di halaman 37 dan 38.
- **Edit master.** Master dipakai publik lewat link view; jangan pernah mengubahnya.
