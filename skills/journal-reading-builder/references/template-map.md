# Peta template journal reading (Canva)

Tiga desain master di akun Canva Auctus. Strukturnya identik (33 halaman: 24 halaman jalur studi + 9 halaman guideline/review, urutan dan placeholder sama), hanya warna berbeda. Jangan pernah mengedit master langsung: selalu buat desain baru dari master (lihat SKILL.md langkah 4).

| Warna | design_id master | Link view publik |
|---|---|---|
| navy (default) | DAHYiY7-9Ps | https://canva.link/clb266xdufq1ndt |
| maroon | DAHYiuIiRCg | https://canva.link/g2fw8osptldrzic |
| hijau tua | DAHYikOThv8 | https://canva.link/slqb1b5gynjpxrv |

Palet (dipakai juga oleh build_brief.py): navy 0b2545/13807a/e3f2f0, maroon 4a1520/a3313f/f7e8ea, hijau 1e3a2b/3f7d3a/eaf3e6.

## Halaman dan pemakaiannya

| No | Halaman | Dipakai? |
|---|---|---|
| 1 | Cara pakai | Selalu dibuang |
| 2 | Cover | Ya |
| 3 | Identitas jurnal | Ya |
| 4 | Alasan memilih | Ya |
| 5 | Latar belakang | Ya |
| 6 | PICO | Ya (untuk diagnostik: P, Index test, Reference standard, Target condition; untuk SR-MA: PICO pertanyaan review) |
| 7 | Metode 1/2 | Ya |
| 8 | Metode 2/2 | Ya |
| 9 | Alur partisipan | Ya (CONSORT / STARD / PRISMA; boleh diganti figur asli) |
| 10 | Karakteristik dasar | Ya (SR-MA: ganti jadi karakteristik studi yang diinklusi) |
| 11 | Hasil utama | Ya, baris kesimpulan di bawah judul wajib diisi |
| 12 | Figur kunci | Ya, tempel figur asli + sumber |
| 13 | Validity RCT (RoB 2) | Hanya bila klien meminta RoB 2 |
| 14 | Validity observasional (NOS) | Hanya bila klien meminta NOS |
| 15 | Validity diagnostik (QUADAS-2) | Hanya bila klien meminta QUADAS-2 |
| 16 | Validity SR-MA (AMSTAR 2) | Hanya bila klien meminta AMSTAR 2 |
| 17 | Importance & applicability | Ya |
| 18 | Kekuatan & kelemahan | Ya |
| 19 | Level of evidence & GRADE | Ya |
| 20 | Kesimpulan & implikasi | Ya |
| 21 | Diskusi | Ya |
| 22 | Referensi | Ya |
| 23 | Penutup | Ya |
| 24 | Pembatas bagian | Opsional, biasanya dibuang |

Jalur default (CASP, semua desain studi dan SR-MA; case report lihat `jalur-case-report.md` C5): 2-12, salinan halaman 4 untuk kartu CASP dan satu slide Validity (tulis nomor 4 berulang di `page_numbers`, sesudah 12), lalu 17-23. Bila klien meminta tool lain, ganti salinan itu dengan satu halaman tool: RoB 2 = 13, NOS = 14, QUADAS-2 = 15, AMSTAR 2 = 16.

### Halaman guideline dan review (25 sampai 33)

Ditambahkan ke ketiga master pada 12 November 2026, setelah halaman 24, sehingga nomor halaman 1 sampai 24 dan daftar `page_numbers` jalur studi tidak berubah. Master sekarang 33 halaman.

Kotak baris pesan di bawah judul pada halaman 11, 26, dan 30 dipersempit menjadi 1540 px (12 November 2026) supaya tidak menabrak hiasan titik di pojok kanan atas. Baris itu muat sekitar 110 karakter per baris pada font 32; untuk pesan dua baris turunkan font ke 24.

Dua hal yang perlu diketahui saat inventaris:

- **Appraisal default = CASP** (studi dan SR/MA): salin halaman 4 (tiga kartu) untuk pertanyaan CASP, tiga per slide, kicker CRITICAL APPRAISAL, lalu satu slide Validity ringkasan (lihat `casp-dan-pakem-klien.md`, "Bentuk slide"). Halaman 13 sampai 16 dihapus dari salinan order kecuali klien meminta tool-nya. Kotak PETUNJUK di halaman itu masih teks lama template.
- **Case report** tidak punya halaman khusus: pakai ulang halaman sesuai `jalur-case-report.md` C5.
- Judul halaman internal (kolom judul di `inv.txt`) masih memakai nama halaman asalnya, mis. halaman 26 dan 30 terbaca "Hasil utama", 28 dan 31 "Validity SR-MA", 32 "Latar belakang", 33 "Figur kunci". Kenali halaman dari teks kicker dan judul di slide, bukan dari judul internal.
- Pada halaman 28 dan 31, baris ringkasan di bawah tabel ("Penilaian keseluruhan ..." / "Total SANRA ...") adalah teks lepas di luar grup tabel. Label baris tabel (nama domain/item) berflag `T` dan boleh diganti lewat `texts` bila perlu (mis. scoping review memakai 6 aspek PRISMA-ScR).

| No | Halaman | Kicker | Isi dan placeholder |
|---|---|---|---|
| 25 | Ruang Lingkup & Metodologi | METODE | 5 baris bernomor: Ruang lingkup [topik, populasi, yang dikecualikan; tujuan] · Penyusun [organisasi/panel atau penulis] · Penelusuran bukti [basis data, rentang tanggal, kriteria] · Cara menilai bukti [sistem kelas dan level; konsensus; telaah eksternal] · Pendanaan & COI |
| 26 | Tabel rekomendasi | REKOMENDASI | Judul [No dan judul bagian]; tabel 4 baris x 5 kolom: [COR] + [LOE] / [ID] + [Inti rekomendasi] tebal / [Rincian] / [Studi, desain, n] / [hal.]; strip warna di kiri tiap baris. Digandakan per 4 rekomendasi; baris kosong dihapus |
| 27 | Perbandingan dengan Sumber Lain | PERBANDINGAN | Tabel 5 baris x 3 kolom: [Topik] / [Posisi paper ini] / [Posisi pembanding]; kepala kolom ketiga [Pembanding + tahun]. Satu pembanding per slide; gandakan untuk pembanding kedua |
| 28 | Validity: Guideline (AGREE II) | CRITICAL APPRAISAL | Tabel 6 domain: [skor %] / [halaman + alasan singkat], satu baris teks per sel; baris ringkasan: Penilaian keseluruhan [ ]/7 · [Direkomendasikan / dengan modifikasi / tidak] · Domain terlemah [ ] · Skor dari satu penilai |
| 29 | Penerapan di RS Setempat | CRITICAL APPRAISAL | Kartu kiri "Sudah sesuai praktik": [rekomendasi atau klaim 1 sampai 3 + dasar]; kartu kanan "Belum sesuai / hambatan": ketersediaan obat/alat, Fornas/JKN, SDM & waktu respons, beda dari PNPK/PPK; batang "Langkah realistis": [1 sampai 2 langkah konkret] |

| 30 | Poin Kunci Review | ISI REVIEW | Baris kesimpulan [bagian review + pesan utama]; tabel 4 baris x 5 kolom: [Klaim kunci] / [Bukti pendukung] / [Kekuatan: kuat, sedang, lemah] / [Cek sitasi: sesuai, dilebihkan, tidak sesuai] / [Hal.]. Digandakan sesuai jumlah klaim yang disetujui; baris kosong dihapus |
| 31 | Validity: Review (SANRA) | CRITICAL APPRAISAL | Tabel 6 item SANRA: [skor /2] / [halaman + alasan singkat]; baris ringkasan: Total SANRA [ ]/12 · Item terlemah [ ] · Penilaian satu penilai. Scoping review: ganti judul, label item jadi 6 aspek PRISMA-ScR, isi dilaporkan / sebagian / tidak, dan ubah baris ringkasan (tanpa total) |
| 32 | Pembahasan Tematik (slide bebas) | PEMBAHASAN TEMATIK | Judul [tema]; dua kartu dengan [subjudul] + 3 poin; batang "Pesan utama" [1 kalimat]. Digandakan per tema |
| 33 | Figur & Pembahasan (slide bebas) | FIGUR & PEMBAHASAN | Judul [figur atau tema]; kotak kiri untuk figur/tabel/algoritma asli + sumber; kartu kanan "Pembahasan": yang ditunjukkan, poin penting, kaitan dengan rekomendasi/praktik, catatan kritis penyaji. Digandakan per figur |

### Halaman desain visual (34 sampai 39)

Ditambahkan 12 November 2026 setelah masukan desain. Aturan pakai dan kode warna ada di `desain-visual.md`.

| No | Halaman | Kicker | Isi dan placeholder |
|---|---|---|---|
| 34 | Daftar Isi | GAMBARAN UMUM | 8 baris pil dalam 2 kolom: lencana nomor (1 sampai 8), [Judul bagian n], [jumlah rekomendasi · hal.], lencana ikon di kanan. Hapus baris tak terpakai (bayangan, pil, lencana, ikon, 3 teks) |
| 35 | Peta Topik | GAMBARAN UMUM | Simpul pusat [Topik utama] + [Sumber · jumlah rekomendasi]; 8 kartu (4 kiri, 4 kanan): [No  Judul cabang n], [Subtopik, dipisah koma], lencana ikon; tiap kartu punya garis ke pusat. Hapus kartu dan garis tak terpakai |
| 36 | Rangkuman Do / Consider / Don't | RANGKUMAN BAGIAN | Judul [No dan judul bagian]; tiga kartu hijau, jingga, merah dengan lencana ikon dan poin-poin; batang gelap "PESAN UTAMA" berisi 2 sampai 3 poin |
| 37 | Algoritma | ALGORITMA | Judul [Judul algoritma]; baris sumber; kotak [Titik masuk], kotak hijau [Langkah untuk semua pasien (kelas)], 4 cabang masing-masing kepala [Cabang n] + 3 kotak [Tindakan (kelas)], kotak [Catatan lintas cabang]. Kotak tindakan netral, diwarnai saat diisi |
| 38 | Tabel bebas | TABEL | Judul [Judul tabel]; tabel 3 kolom x 5 baris ([Kolom n], [Baris n]); baris sumber di bawah tabel |
| 39 | Perbandingan dengan Edisi Sebelumnya | PERBANDINGAN | Wajib pada jalur guideline. Tabel 5 baris x 3 kolom: [Topik · baru / diubah / dihapus] / [Rekomendasi lama + kelas, level, hal.] / [Rekomendasi baru + kelas, level, hal.]; kepala kolom "Edisi sebelumnya ([tahun])" dan "Edisi ini ([tahun])". Sumber hanya bagian perubahan di guideline baru atau PDF edisi lama (lihat `jalur-guideline.md` G2b). Salinan tata letak halaman 27. |

Halaman 26 diubah di tempat menjadi gaya baru: kolom Kelas · Level, Inti rekomendasi, Rincian, Bukti dasar, Hal.; tiap baris punya strip tipis di tepi kiri (bentuk lepas, netral) yang diwarnai menurut kelas bersama sel pertamanya. Halaman 32 tidak lagi punya kicker.

Elemen non-teks (kotak, strip, lencana, gambar ikon, grup) dicari dengan `scripts/page_elements.py`.

Halaman 32 dan 33 adalah slide serbaguna untuk guideline dan review article. Pakai untuk membahas satu tema secara naratif (mis. bagian mekanisme penyakit di guideline, atau tiap bagian utama narrative review) dan untuk menampilkan figur selain figur kunci. Pada review article, slide ini biasanya menjadi isi utama presentasi.

Halaman 25, 27, dan 29 dipakai bersama oleh guideline dan review, jadi label barisnya dibuat netral atau berupa placeholder.

Guideline = 2-5, 25, 34, 35, 12 (opsional), 32 (sesuai tema), lalu per bagian 36 + 26 (digandakan), 37 dan 38 bila ada, 39 (wajib), 27 (opsional), 28, 29, 18, 20-23. Rincian di `jalur-guideline.md` bagian G5.
Review = 2-5, 25, 32/33 (sesuai tema yang disetujui), 30 (digandakan), 27, 31, 29, 18, 20-23.

`merge-designs` menyalin tiap nomor halaman satu kali. Untuk menggandakan halaman 26, 30, 32, atau 33, tulis nomornya berulang di `page_numbers` (mis. `[..., 32, 32, 33, 26, 26, ...]`).

Setiap slide isi punya: kicker (PENDAHULUAN / METODE / HASIL / CRITICAL APPRAISAL / PENUTUP), judul singkat netral, kotak kuning PETUNJUK (shape #fff2b8 + teks "PETUNJUK ..."), dan nomor slide statis di pojok kanan bawah. make_ops.py menangani footer, PETUNJUK, dan nomor slide secara otomatis.

Sejak 12 November 2026 template tidak punya footer nama penyaji di kiri bawah dan halaman 26 tidak punya baris legenda warna (keduanya dihapus atas permintaan pemesan). Garis tipis dan nomor slide di kanan bawah tetap ada. Arti warna kelas dijelaskan lewat lencana ikon di sel pertama, slide Ruang Lingkup & Metodologi, dan speaker notes.

## Placeholder per halaman (dari master navy)

Flag: `B` = teks berisi [placeholder] yang harus diganti, `P` = teks PETUNJUK (dihapus). Sel tabel yang hanya berisi `[ ]` dipetakan lewat posisi (y,x) di output list_placeholders.py: urutannya per baris kiri ke kanan, dan label baris/kolom ada di teks `T` di sekitarnya. Notes bawaan adalah pertanyaan konsulen umum; ganti dengan notes spesifik paper.

### 1. Cara pakai

- `B` Ganti semua teks dalam [kurung siku]. Cari cepat dengan Ctrl/Cmd+F "[".
- Notes bawaan: SLIDE PANDUAN. Hapus sebelum presentasi. / Urutan deck: Cover, Identitas, Alasan memilih, Latar belakang, PICO, Metode 1/2, Metode 2/2, Alur partisipan, Karakteristik dasar, Hasil utama, Figur kunci, ...

### 2. Cover

- `B` [Judul artikel lengkap, persis seperti di jurnal]
- `B` [Penulis pertama] et al.  ·  [Nama jurnal]. [Tahun];[Vol]([No]):[Halaman]  ·  doi:[10.xxxx/xxxxx]
- `B` Penyaji      [Nama], PPDS [Program Studi] semester [X] / Pembimbing   [Nama konsulen], Sp.[X] / [Departemen / KSM]  ·  [FK / RS Pendidikan]  ·  [Hari, tanggal]
- Notes bawaan: Pembukaan (sekitar 30 detik): salam, sebut judul, jurnal, tahun, dan satu kalimat alasan memilih paper. / Contoh: "Selamat pagi dok, saya akan membawakan journal reading berjudul ... yang terbit di .....

### 3. Identitas artikel

- `B` [Penulis pertama] et al.; [negara]
- `B` [Sumber dana: pemerintah / universitas / industri] / [Hubungan penulis dengan industri, tulis apa adanya] /  / [Opsional: tempel screenshot halaman pertama artikel di sini]
- `B` [Jurnal]. [Tahun];[Vol]([No]):[Hal]
- `B` [PubMed / Scopus Q_]
- `B` [RCT / kohort / diagnostik / SR-MA]
- `B` [NCT... / PROSPERO CRD... / tidak ada]
- `P` PETUNJUK  Cek indeksasi di PubMed/Scopus dan registrasi di ClinicalTrials.gov/PROSPERO. Tulis pendanaan & COI apa adanya. Hapus kotak ini se...
- Notes bawaan: Sebutkan desain studi sejak awal agar audiens tahu tool appraisal yang akan dipakai. / Pertanyaan konsulen yang sering muncul: / - Jurnalnya terindeks di mana? Quartile berapa? / - Studinya terdaftar?...

### 4. Alasan memilih

- `B` Relevansi klinis / [Masalah yang sering ditemui di bangsal/poli; besar beban penyakit]
- `B` Kebaruan & dampak / [Apa yang baru dibanding guideline/bukti sebelumnya; potensi mengubah praktik]
- `B` Kualitas sumber / [Desain studi, ukuran sampel, jurnal terindeks & peer-reviewed]
- `B` [Ringkas 1 kasus atau pertanyaan klinis nyata yang mendorong pemilihan paper ini, tanpa identitas pasien]
- `P` PETUNJUK  Kaitkan dengan kasus nyata di bangsal/poli dan guideline/PNPK yang berlaku. Jawab dengan relevansi klinis, bukan sekadar "baru ter...
- Notes bawaan: Pertanyaan konsulen favorit: "Kenapa memilih paper ini?" / Jawab dengan relevansi klinis (masalah nyata di departemen), lalu kebaruan, lalu kualitas. Hindari jawaban "karena baru terbit". / Bila hasil...

### 5. Latar belakang

- `B` • [Fakta 1 + sumber] / • [Fakta 2 + sumber] / • [Fakta 3 + sumber]
- `B` • [Apa yang belum terjawab] / • [Keterbatasan studi sebelumnya] / • [Mengapa studi ini diperlukan]
- `B` [Tulis persis seperti di paper, termasuk superiority / non-inferiority bila ada]
- `P` PETUNJUK  Ambil dari Introduction. Maksimal 3 poin per kolom; kutip angka epidemiologi beserta sumbernya.
- Notes bawaan: Cukup 1 menit. Bedakan klaim penulis dengan fakta yang Anda cek sendiri. / Pertanyaan konsulen yang sering muncul: / - Apa bedanya dengan guideline atau meta-analisis terbaru? / - Hipotesisnya superio...

### 6. PICO

- `B` Population / [Usia, diagnosis, keparahan, setting]
- `B` Intervention / [Intervensi / paparan / index test; dosis & durasi]
- `B` Comparison / [Plasebo / terapi standar / reference standard]
- `B` Outcome / [Outcome primer + waktu ukur; outcome sekunder utama]
- `B` Desain: [ ]     Follow-up: [ ]     Setting: [negara, jenis RS, periode]
- `P` PETUNJUK  Diagnostik: P, Index test, Reference standard, Target condition. Prognosis/etiologi: ganti I dengan exposure/faktor risiko.
- Notes bawaan: PICO adalah dasar menilai applicability di akhir presentasi: simpan detail populasi (usia, keparahan, setting) untuk dibandingkan dengan pasien lokal. / Pertanyaan konsulen yang sering muncul: / - Outc...

### 7. Metode 1/2

- `B` Setting & periode:  [negara, jumlah pusat, jenis RS, periode rekrutmen]
- `B` Kriteria:  Inklusi [ ]  ·  Eksklusi [ ]
- `B` Randomisasi:  [metode random sequence, rasio, stratifikasi/blok]
- `B` Allocation concealment:  [amplop tertutup / sistem sentral / tidak dilaporkan]
- `B` Blinding:  [pasien / klinisi / penilai outcome / analis]
- `P` PETUNJUK  Detail randomisasi/concealment/blinding sering ada di supplementary; tulis ‘tidak dilaporkan’ bila tidak ada.
- Notes bawaan: Bagian ini menjadi bahan utama domain 1 dan 2 RoB 2 di slide appraisal. / Pertanyaan konsulen yang sering muncul: / - Apa bedanya randomisasi dengan allocation concealment? /   Jawab: randomisasi = ca...

### 8. Metode 2/2

- `B` [Definisi + waktu pengukuran]
- `B` [Sama dengan registrasi?]
- `B` [Daftar singkat]
- `B` [Risiko multiplisitas?]
- `B` [Power, alfa, n target vs n tercapai]
- `B` [Tercapai / tidak]
- `B` [ITT / mITT / per-protocol; uji statistik]
- `B` [Tepat untuk jenis data?]
- `B` [Imputasi?  ·  Subgrup pre-specified?]
- `B` [Seimbang?  ·  Eksploratif?]
- `P` PETUNJUK  Bandingkan outcome primer dengan registrasi/protokol. Catat apakah sample size tercapai dan analisisnya ITT atau per-protocol.
- Notes bawaan: Pertanyaan konsulen favorit: / - "ITT atau per-protocol?" Jelaskan konsekuensinya: per-protocol dengan attrition tidak seimbang bisa membesarkan efek. / - "Outcome primernya berubah tidak dari protoko...

### 9. Alur partisipan

- `B` Diskrining n=[ ]
- `B` Dieksklusi n=[ ] ([alasan utama])
- `B` Dirandomisasi n=[ ]
- `B` Dialokasikan n=[ ]
- `B` Dialokasikan n=[ ]
- `B` Loss to follow-up n=[ ] ([alasan])
- `B` Loss to follow-up n=[ ] ([alasan])
- `B` Dianalisis n=[ ] ([ITT/PP])
- `B` Dianalisis n=[ ] ([ITT/PP])
- `P` PETUNJUK  Isi angka dari diagram CONSORT (RCT), STARD (diagnostik), atau PRISMA (SR-MA), atau ganti seluruh diagram dengan figur asli + sumb...
- Notes bawaan: Soroti loss to follow-up per kelompok dan apakah seimbang. / Pertanyaan konsulen yang sering muncul: / - Berapa yang dirandomisasi dan berapa yang dianalisis? / - Loss to follow-up-nya seimbang antar ...

### 10. Karakteristik dasar

- `B` Intervensi n=[ ]
- `B` Kontrol n=[ ]
- `B` [ ]
- `B` [ ]
- `B` Seimbang? / [Ya / Tidak: sebut perbedaan penting] /  / Mirip pasien lokal? / [Usia, keparahan, komorbid, setting]
- `B` [ ]
- `B` [ ]
- `B` [Komorbid utama], n (%)
- `B` [ ]
- `B` [ ]
- `B` [Skor keparahan]
- `B` [ ]
- `B` [ ]
- `B` [Terapi penyerta], n (%)
- `B` [ ]
- `B` [ ]
- `B` [Karakteristik lain]
- `B` [ ]
- `B` [ ]
- `P` PETUNJUK  Ambil dari Table 1. Pilih 5-7 karakteristik yang paling memengaruhi outcome. Pada RCT, nilai p untuk baseline tidak diperlukan.
- Notes bawaan: Fokus pada keseimbangan prognostik dan kemiripan dengan pasien lokal; ini dipakai lagi di slide applicability. / Pertanyaan konsulen yang sering muncul: / - Kelompoknya seimbang? Kalau ada yang tidak ...

### 11. Hasil utama

- `B` [Kesimpulan hasil dalam 1 kalimat, mis. Intervensi menurunkan X dari a% ke b%]
- `B` [Outcome primer]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [Sekunder 1]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [Sekunder 2]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [Efek samping utama]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` CER = [ ]%    EER = [ ]% / ARR = CER − EER = [ ] / NNT = 1 / ARR = [ ]   (95% CI [ ] sampai [ ]) / [Kalimat interpretasi: perlu mengobati N pasien untuk mencegah 1 kejadian]
- `P` PETUNJUK  Tampilkan angka absolut (n/N, %) DAN ukuran efek dengan 95% CI. Hitung ulang ARR & NNT sendiri (widget). Harm: NNH = 1 / ARI.
- Notes bawaan: Kalimat siap baca: "Risiko [outcome] turun dari X% menjadi Y%; RR ... (95% CI ...); artinya perlu mengobati N pasien untuk mencegah 1 kejadian." / Pertanyaan konsulen yang sering muncul: / - Berapa NN...

### 12. Figur kunci

- `B` [Forest plot / kurva Kaplan-Meier / ROC dari paper] /  / Sumber: [Penulis, Jurnal, Tahun, Figure X]
- `B` Arah efek: / [favours intervensi / kontrol] /  / Estimasi: / [ ] (95% CI [ ]) /  / Menyentuh garis nol-efek? / [Ya / Tidak] /  / Heterogenitas: / I² = [ ]%
- `P` PETUNJUK  Tempel figur asli (screenshot resolusi tinggi) dan cantumkan sumber. Forest plot: cek garis nol-efek, diamond, bobot, dan I².
- Notes bawaan: Jelaskan arah "favours" dan apakah diamond atau CI menyentuh garis 1 (rasio) atau 0 (selisih). / Pertanyaan konsulen yang sering muncul: / - Cara membaca forest plot ini bagaimana? / - Kurva Kaplan-Me...

### 13. Validity RCT

- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [Low / Some concerns / High]
- `B` [Domain paling bermasalah]
- `P` PETUNJUK  Untuk RCT (Cochrane RoB 2). Tiap penilaian wajib ada bukti halaman/tabel. Hapus 3 slide validity lain yang tidak sesuai desain.
- Notes bawaan: Untuk setiap domain, sebut penilaian lalu buktinya (halaman/tabel). "Tidak jelas" = informasi tidak dilaporkan. / Aturan overall RoB 2: Low bila semua domain low; High bila ada satu domain high atau b...

### 14. Validity observasional

- `B` [ ] / 4
- `B` [ ]
- `B` [ ] / 2
- `B` [ ]
- `B` [ ] / 3
- `B` [ ]
- `B` [ ] / 9
- `B` [Baik / sedang / buruk]
- `P` PETUNJUK  Untuk kohort/case-control (Newcastle-Ottawa Scale atau CASP). Tulis item yang tidak mendapat bintang beserta alasannya di kolom Bu...
- Notes bawaan: Newcastle-Ottawa (kohort): Seleksi 4 item (representatif kohort terpapar, seleksi non-terpapar, pemastian paparan, outcome belum ada di awal); Komparabilitas 1 item (maks 2 bintang: confounder utama d...

### 15. Validity diagnostik

- `B` [L/H/U] · [L/H/U]
- `B` [ ]
- `B` [L/H/U] · [L/H/U]
- `B` [ ]
- `B` [L/H/U] · [L/H/U]
- `B` [ ]
- `B` [L/H/U] · tidak dinilai
- `B` [ ]
- `P` PETUNJUK  Untuk studi akurasi diagnostik (QUADAS-2). L/H/U = Low / High / Unclear. Hitung sens, spes, LR dengan widget dan tampilkan di slid...
- Notes bawaan: QUADAS-2 menilai 4 domain risk of bias, dan 3 domain pertama juga dinilai applicability concerns. / Pertanyaan konsulen yang sering muncul: / - Spektrum pasiennya mirip pasien lokal? Ada spectrum bias?...

### 16. Validity SR-MA

- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [ ]
- `B` [High/Mod/Low/Crit. low]
- `B` [Jumlah kelemahan kritis]
- `P` PETUNJUK  Untuk systematic review/meta-analisis (AMSTAR 2). Angka dalam kurung = nomor item domain kritis. Satu kelemahan kritis sudah membu...
- Notes bawaan: AMSTAR 2 punya 16 item, 7 di antaranya domain kritis: 2 (protokol), 4 (pencarian), 7 (daftar eksklusi), 9 (RoB studi), 11 (metode MA), 13 (RoB dalam interpretasi), 15 (publication bias). / Overall: Hi...

### 17. Importance & applicability

- `B` Besar efek relatif & absolut (ARR, NNT)?  [ ] / Presisi: seberapa lebar 95% CI?  [ ] / Melampaui MCID, bukan hanya p < 0,05?  [ ] / Harm / efek samping (NNH) sepadan?  [ ]
- `B` Pasien lokal mirip populasi studi?  [ ] / Intervensi tersedia di RS setempat?  [ ] / Masuk Fornas / ditanggung JKN?  [ ] / Sesuai preferensi pasien & PNPK?  [ ]
- `B` NNT lokal = 1 / (risiko dasar pasien lokal × RRR) = [ ]   ·   sumber risiko dasar: [data RS / registri / literatur nasional]
- `P` PETUNJUK  Importance: nilai besar & presisi efek terhadap MCID. Applicability: bandingkan pasien, sumber daya, dan biaya di RS Anda (Fornas/...
- Notes bawaan: Sebut risiko dasar pasien lokal bila ada data, lalu hitung NNT lokal kurang lebih 1 / (risiko dasar x RRR). / Pertanyaan konsulen yang sering muncul: / - Bisa diterapkan di RS setempat? Ditanggung JKN? / ...

### 18. Kekuatan & kelemahan

- `B` 1. [Kekuatan + buktinya] /  / 2. [Kekuatan + buktinya] /  / 3. [Kekuatan + buktinya]
- `B` 1. [Kelemahan + dampaknya ke hasil] /  / 2. [Kelemahan + dampaknya ke hasil] /  / 3. [Temuan penyaji, tidak diakui penulis]
- `P` PETUNJUK  Tulis yang spesifik untuk paper ini (mis. "loss to follow-up 15% di kelompok kontrol"), bukan kalimat umum.
- Notes bawaan: Kelemahan yang Anda temukan sendiri (tidak diakui penulis) biasanya paling dihargai konsulen. / Untuk setiap kelemahan, sebut dampaknya: membesarkan atau mengecilkan efek? mengurangi applicability? / ...

### 19. Level of evidence

- `B` [0/-1/-2]
- `B` [ ]
- `B` [Level _] / Oxford CEBM 2011
- `B` [0/-1/-2]
- `B` [ ]
- `B` [0/-1/-2]
- `B` [ ]
- `B` [0/-1/-2]
- `B` [ ]
- `B` [High / Moderate / Low / Very low] / Outcome: [outcome primer]
- `B` [0/-1/-2]
- `B` [ ]
- `P` PETUNJUK  Level desain: Oxford CEBM 2011 sesuai jenis pertanyaan. GRADE dinilai per outcome: RCT mulai tinggi, observasional mulai rendah.
- Notes bawaan: Jelaskan alasan setiap penurunan (downgrade). Faktor naik untuk observasional: efek besar, dose-response, confounding yang justru melemahkan efek. / Bila paper adalah SR-MA, kutip tabel Summary of Fin...

### 20. Kesimpulan & implikasi

- `B` [Kutip/parafrase kesimpulan di abstrak]
- `B` [Setelah appraisal: seberapa yakin & untuk siapa]
- `B` [Yang diubah/dipertahankan di bangsal/poli]
- `B` [Formularium, clinical pathway, JKN]
- `B` [Pertanyaan yang belum terjawab]
- `B` [Satu kalimat, maks 20 kata: arah & besar efek, keyakinan bukti, untuk pasien siapa]
- `P` PETUNJUK  Pisahkan kesimpulan penulis dan kesimpulan Anda setelah appraisal. Implikasi harus konkret dan realistis untuk RS Anda.
- Notes bawaan: Kesimpulan penyaji boleh berbeda dari penulis, asalkan alasannya dari appraisal. / Contoh take-home message: "Probiotik mungkin menurunkan diare terkait antibiotik (NNT 10), tetapi bukti berisiko bias...

### 21. Diskusi

- `B` [Pertanyaan klinis: apakah praktik perlu diubah?]
- `B` [Pertanyaan metodologi: seberapa besar bias memengaruhi hasil?]
- `B` [Pertanyaan penerapan: apa yang dibutuhkan di RS setempat?]
- `P` PETUNJUK  Siapkan 2-3 pertanyaan terbuka yang memancing diskusi klinis, lalu tulis jawaban singkat Anda sendiri di Speaker Notes.
- Notes bawaan: Tulis jawaban singkat Anda untuk tiap pertanyaan di sini, supaya diskusi tetap terarah. / 1. [Jawaban Anda] / 2. [Jawaban Anda] / 3. [Jawaban Anda] / Bila konsulen bertanya data yang tidak ada di pape...

### 22. Referensi

- `B` 1. [Artikel yang ditelaah, format Vancouver lengkap] /  / 2. [Tool appraisal, mis. Sterne JAC, et al. RoB 2: a revised tool for assessing risk of bias in randomised trials. BMJ. 2019;366:l4898] /  / 3. [Guideline / PNPK terkait] /  / 4. [Data lokal / referensi lain yang Anda cek sendiri]
- `P` PETUNJUK  Satu gaya sitasi (mis. Vancouver). Artikel yang ditelaah nomor 1. Jangan cantumkan referensi yang belum Anda cek sendiri (AI serin...
- Notes bawaan: Slide ini tidak perlu dibacakan. / Cek setiap referensi di PubMed atau situs jurnal sebelum dicantumkan. Hapus referensi yang tidak bisa Anda temukan sendiri.

### 23. Penutup

- Notes bawaan: Tutup dengan terima kasih kepada pembimbing dan audiens, lalu buka sesi diskusi. / Catat pertanyaan yang belum terjawab dan tindak lanjuti setelah sesi.

### 24. Pembatas bagian

- `B` [Nama bagian, mis. Metode]
- `B` [Opsional. Duplikat slide ini untuk tiap bagian: Pendahuluan, Metode, Hasil, Appraisal, Kesimpulan]
- Notes bawaan: SLIDE OPSIONAL. Pakai sebagai pembatas bagian bila presentasi panjang. Hapus bila tidak dipakai.
### Halaman variasi berbutir (40 sampai 42, ketiga master)

Ditambahkan 15 November 2026 dari slide hasil rapikan pemesan pada JR dr. Putri Nabila. Isinya semua berupa butir pendek (list disc), bukan paragraf. Pakai sebagai pengganti halaman asalnya, jangan menyertakan keduanya.

| No | Pengganti halaman | Isi dan placeholder |
|---|---|---|
| 40 | 4 (Alasan memilih) | 3 kartu atas (Relevansi klinis berbutir, Kebaruan & dampak, Kualitas sumber, judul kartu 40 px) + kotak bawah PERTANYAAN KLINIS. Kartu atas top 225 tinggi 437, kotak bawah top 700. |
| 41 | 6 (PICO) | Kartu P, I, C, O berbutir + kotak Desain Studi (Desain, Follow-up, Setting) berbutir. Kartu top 270 tinggi 465, kotak bawah top 760 tinggi 190. |
| 42 | 20 (Kesimpulan & implikasi) | Kartu Kesimpulan penulis dan penyaji berbutir (top 240 tinggi 250), tiga kartu Praktik klinis, Sistem/kebijakan, Penelitian (top 515 tinggi 230), kotak TAKE-HOME MESSAGE (top 775). |

Gunakan `find_and_replace_text` per butir (bukan `replace_text` pada seluruh kotak) bila ingin mempertahankan format list. Halaman 40 sampai 42 ada di master hijau, navy, dan maroon (navy dan maroon disalin dari hijau lalu diwarnai ulang dengan palet masing-masing pada 15 November 2026). Jumlah halaman ketiga master sekarang 42.

Catatan penting saat mengisi: bentuk kartu dalam grup ikut menyesuaikan tinggi teks. Setelah `replace_text` atau `find_and_replace_text`, cek tinggi kartu dan samakan lagi (halaman 41: kartu 465 px, kotak Desain Studi top 760 tinggi 205; halaman 42: lihat tabel di atas).
