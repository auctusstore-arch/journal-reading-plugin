# Jalur guideline (clinical practice guideline, konsensus, PNPK)

Dipakai bila paper adalah guideline atau pernyataan konsensus, bukan studi primer atau SR-MA. Tanda: judul memuat "Guideline", "Consensus", "Scientific Statement", "Recommendations"; PubMed publication type "Practice Guideline"; isi berupa daftar rekomendasi berkelas.

Bedanya dengan jalur studi: tidak ada PICO tunggal, tidak ada hasil untuk dihitung ulang, dan isinya terlalu banyak untuk satu presentasi. Karena itu jalur ini punya satu langkah tambahan yang wajib: **peta rekomendasi yang disetujui user** sebelum slide dibuat.

## G1. Ekstraksi

PDF guideline wajib ada di intake. Situs penerbit (mis. ahajournals.org) sering menolak pengambilan otomatis dengan verifikasi anti-bot, dan banyak guideline tidak tersedia di PubMed Central. Verifikasi itu tidak boleh diakali: minta user menaruh PDF di folder kerja. PDF juga dibutuhkan untuk me-render figur.

Tabel rekomendasi diekstrak dengan script, bukan dibaca dari teks biasa:

```
uv run --with pymupdf python3 scripts/extract_recs.py paper.pdf work/recs.json
```

Pada PDF dua kolom, `pdftotext` mengeluarkan kolom kelas, level, dan teks rekomendasi dalam urutan yang tidak sejajar, sehingga pasangan COR/LOE mudah tertukar (pada uji guideline ICH 2022, rekomendasi berkelas 1 terbaca sebagai 2b). `extract_recs.py` memasangkan berdasarkan posisi di halaman dan berhenti dengan exit 1 bila ada baris yang kelas atau levelnya tidak tepat satu nilai valid, atau penomoran tabel tidak berurutan. Setelah itu tetap cek acak 2 sampai 3 tabel ke PDF, dan baca ulang angka ambang di teks rekomendasi (volume, tekanan darah, dosis) karena teks bisa terpecah tata letak. Untuk sistem selain AHA, pakai opsi `--class-header`, `--level-header`, `--class-values`, `--level-values`.

Tulis ke `extract.md`:

- Identitas: judul, organisasi penerbit, ketua penulis, jurnal, tahun;vol(no):hal, DOI, edisi yang digantikan (tahun dan sitasi).
- Ruang lingkup: populasi/kondisi yang dicakup dan yang dikecualikan, pengguna sasaran.
- Metodologi penyusunan: komposisi panel (spesialisasi, wakil pasien), metode penelusuran bukti dan tanggal batas penelusuran, cara mencapai konsensus (voting, ambang), telaah eksternal, rencana pembaruan, pendanaan, kebijakan dan pengungkapan COI.
- Sistem kelas rekomendasi dan level bukti **persis seperti dipakai guideline itu**. Jangan dikonversi ke sistem lain. Contoh yang sering muncul:
  - AHA/ACC: COR 1, 2a, 2b, 3: No Benefit, 3: Harm; LOE A, B-R, B-NR, C-LD, C-EO.
  - ESC: Class I, IIa, IIb, III; Level A, B, C.
  - GRADE: strong / conditional (weak); certainty high, moderate, low, very low.
  Salin definisi tiap kelas dari tabel di guideline, dengan nomor halaman.
- Figur/algoritma kunci dan lokasinya.

## G2. Peta rekomendasi (wajib, sebelum appraisal dan slide)

Buat `peta-rekomendasi.md` yang memuat **semua** rekomendasi di guideline, tanpa menyaring. Tujuannya agar user melihat seluruh isi lalu memutuskan sendiri apa yang masuk slide.

Format: satu tabel per bagian guideline, dengan ringkasan di atas.

```
## Ringkasan
Total: 12 bagian, 137 rekomendasi. Sistem: AHA COR/LOE.
| Bagian | Judul | Jumlah | COR 1 | COR 3 | Baru/berubah |

## Bagian 5.1 <judul bagian persis>
| ID | COR | LOE | Rekomendasi (ringkas, maks 25 kata) | Hal. | Status | Usulan | Alasan usulan |
| 5.1-1 | 1 | B-R | ... | e298 | baru | masuk | menjawab kasus pemicu |
| 5.1-2 | 2b | C-LD | ... | e298 | tetap | lewati | di luar fokus departemen |
```

Aturan pengisian:

- **ID** mengikuti penomoran guideline (nomor bagian + nomor rekomendasi). Bila guideline tidak menomori, buat ID `bagian-urutan` dan sebutkan itu di ringkasan.
- **Rekomendasi** diparafrase ringkas dalam bahasa Indonesia. Kata kerja kekuatan ("direkomendasikan", "dapat dipertimbangkan", "tidak bermanfaat", "berbahaya") harus setia pada aslinya.
- **Status** hanya diisi "baru" atau "berubah" bila guideline sendiri menyatakannya (tabel "What's new", penanda di teks) atau sudah dicek ke edisi sebelumnya. Selain itu tulis "tidak ditandai". Jangan menebak. Bila guideline tidak menandai satu pun (umum pada guideline AHA; yang ada hanya ringkasan "Top 10 Take-Home Messages"), sebut butir yang disorot ringkasan itu di kolom alasan, dan di slide ganti kepala kolom "Status" menjadi "Hal." berisi halaman rekomendasi.
- **Usulan** adalah saran awal ("masuk" atau "lewati") plus alasannya. Dasar usulan: fokus dan kasus pemicu dari intake, rekomendasi baru/berubah, COR 3 (jangan dilakukan), dan yang berdampak ke praktik RS Indonesia. Usulan hanyalah saran: keputusan ada di user.
- Bagian guideline yang bersifat naratif tanpa rekomendasi berkelas (mis. mekanisme cedera, epidemiologi, definisi) dan figur/tabel penting juga dimasukkan ke peta sebagai baris **tema** (ID `T-<nomor bagian>`, kolom COR/LOE diisi "tema" atau "figur"). Bila disetujui, tema dibawakan dengan halaman 32 (Pembahasan tematik) dan figur dengan halaman 33 (Figur & pembahasan). Sekelompok rekomendasi yang saling terkait juga boleh diusulkan dibahas tematik di halaman 32 sebelum tabel rekomendasinya.
- Sertakan perkiraan muatan: tabel rekomendasi memuat sekitar 4 rekomendasi per slide, dan presentasi 30 menit realistis untuk 6 sampai 10 rekomendasi. Bila user menyetujui lebih banyak, sampaikan konsekuensinya (jumlah slide, menit) dan biarkan user memilih: menambah durasi, memindahkan sebagian ke brief, atau tetap.

### Gerbang persetujuan

Setelah peta selesai, **berhenti dan serahkan ke user**. Jangan memilih sendiri lalu lanjut.

1. Kirim `peta-rekomendasi.md` (untuk guideline besar, tampilkan ringkasan per bagian di chat dan lampirkan filenya).
2. Minta keputusan. User boleh menjawab per bagian ("semua 5.1 dan 5.2"), per ID ("5.1-1, 5.1-3, 6.2-4"), atau "pakai usulan". User juga boleh menolak sebagian usulan atau menambah yang tidak diusulkan.
3. Bila yang memesan adalah tim Auctus atas nama PPDS, keputusan idealnya dari PPDS (atau konsulennya). Tanyakan siapa yang menyetujui.
4. Catat hasilnya di `peta-rekomendasi.md` (kolom Keputusan: masuk / tidak) dan di `brief.json` pada `meta.rekomendasi_disetujui`, mis. "dr. Ani (PPDS), 12 November 2026, 8 dari 137 rekomendasi". `build_brief.py` menolak mode guideline tanpa field ini.
5. Hanya rekomendasi berstatus "masuk" yang boleh muncul di slide. Bagian yang tidak dipilih diringkas 1 baris per bagian di brief (`paper.tidak_dipresentasikan`) supaya PPDS tidak kosong bila ditanya.

Bila user mengubah pilihan setelah slide dibuat, perbarui peta dulu, baru slide dan brief.

### Mode deck induk

User boleh memutuskan **semua** rekomendasi, tema, dan figur masuk, untuk dipilah sendiri atau oleh klien setelah PPT jadi. Itu keputusan yang sah; catat persis begitu di `meta.rekomendasi_disetujui`. Sebelum mengerjakan, sampaikan konsekuensinya dengan angka: jumlah slide (jumlah slide tabel = jumlah dari pembulatan ke atas rekomendasi per bagian dibagi 4) dan bahwa deck tidak bisa dibawakan utuh dalam durasi yang diminta. Pada mode ini:

- Satu bagian guideline per kelompok slide: judul slide = nomor dan judul bagian (font 40 supaya muat satu baris), baris pesan = pesan utama Synopsis bagian itu (maks 25 kata).
- Tema dan figur disisipkan di dekat bagian yang berkaitan, bukan dikumpulkan di depan.
- Slide cover dan notes menyebut bahwa ini deck induk yang harus dipilah.
- Brief memuat tabel semua rekomendasi, sehingga jumlah kata jauh di atas target; peringatan panjang dari `build_brief.py` boleh diabaikan dan disebut di laporan.
- `rencana_presentasi` tetap menganjurkan 6 sampai 10 rekomendasi untuk dibawakan.

## G3. Pendalaman rekomendasi terpilih

Untuk guideline besar (puluhan rekomendasi), bagi pendalaman ke subagen per kelompok bagian (sekitar 15 sampai 25 rekomendasi per subagen) dan minta hasil terstruktur per rekomendasi: `bukti_slide` (maks 90 karakter: nama studi, desain, n), `bukti_detail` (1 sampai 3 kalimat dengan angka persis dan nomor rujukan), `catatan_kritis` (keterbatasan yang disebut guideline sendiri), dan `cek` (apa pun yang tidak terbaca pasti). Instruksikan: hanya dari teks guideline, tanpa pengetahuan luar, tanpa menebak. Teks pendukung pada PDF dua kolom sering berpindah tempat, jadi beri rentang baca yang tumpang tindih. Setelah hasil masuk, uji petik beberapa angka ke teks sumber, dan masukkan semua `cek` ke `cek_ulang`.

Untuk tiap rekomendasi yang disetujui, tambahkan ke `extract.md`:

- Teks rekomendasi persis (bahasa asli) + COR + LOE + halaman.
- Bukti dasar dari teks pendukung guideline: nama studi, desain, n, hasil utama dengan angka, dan nomor referensinya. Bila angka penting untuk presentasi, cek ke paper aslinya; bila tidak sempat, tandai `[CEK]`.
- Ketidaksesuaian kekuatan dan bukti (mis. COR 1 dengan LOE C-EO): catat alasan yang diberikan panel.
- Perubahan dari edisi sebelumnya, bila terverifikasi.
- Posisi pembanding: PNPK/pedoman Indonesia yang berlaku dan 1 guideline internasional lain (mis. ESO untuk stroke). Hanya yang benar-benar dibaca; sisanya `[CEK]`.
- Kemutakhiran: studi besar yang terbit setelah tanggal batas penelusuran dan bisa mengubah rekomendasi. Boleh dicari di PubMed; jangan mengandalkan ingatan. Yang belum terverifikasi masuk `cek_ulang`.

`effect_calc.py` tidak dipakai untuk guideline, kecuali untuk menghitung ARR/NNT dari studi pendukung yang angkanya diambil dari paper aslinya.

## G4. Appraisal: AGREE II

23 item dalam 6 domain, tiap item diberi skor 1 (sangat tidak setuju) sampai 7 (sangat setuju), dengan bukti halaman.

| Domain | Item | Yang dinilai |
|---|---|---|
| 1. Ruang lingkup & tujuan | 1-3 | tujuan, pertanyaan kesehatan, populasi sasaran |
| 2. Keterlibatan pemangku kepentingan | 4-6 | komposisi panel, pandangan pasien, pengguna sasaran |
| 3. Kekakuan penyusunan (rigour) | 7-14 | penelusuran sistematis, kriteria seleksi bukti, kekuatan dan keterbatasan bukti, metode perumusan, pertimbangan manfaat-risiko, kaitan rekomendasi dengan bukti, telaah eksternal, prosedur pembaruan |
| 4. Kejelasan penyajian | 15-17 | rekomendasi spesifik, opsi tata laksana, rekomendasi kunci mudah dikenali |
| 5. Aplikabilitas | 18-21 | fasilitator dan hambatan, alat bantu penerapan, implikasi sumber daya, kriteria audit |
| 6. Independensi editorial | 22-23 | pengaruh pendana, pencatatan dan pengelolaan COI |

- Skor domain (%) = (jumlah skor − skor minimum) / (skor maksimum − skor minimum) x 100. Untuk satu penilai: minimum = jumlah item x 1, maksimum = jumlah item x 7.
- Penilaian keseluruhan: kualitas keseluruhan (1 sampai 7) dan "direkomendasikan / direkomendasikan dengan modifikasi / tidak direkomendasikan".
- AGREE II **tidak menetapkan ambang** skor baik atau buruk. Jangan menulis "lolos" atau "berkualitas tinggi karena di atas X%" seolah aturan resmi. Bandingkan antar domain dan sebut domain terlemah.
- AGREE II menganjurkan minimal 2 penilai (lebih baik 4). Skor di sini dari satu penilai: tulis itu sebagai keterbatasan di slide validity dan di brief.
- AGREE II menilai proses penyusunan dan pelaporan, bukan kebenaran klinis tiap rekomendasi. Kebenaran isi dinilai lewat G3 (bukti dasar, kemutakhiran, pembanding).

Di `brief.json`, `appraisal.validity` berisi 6 baris domain dengan `penilaian` berupa persen (mis. "78%") dan `kelas` ("ok" / "mid" / "bad") untuk warna relatif antar domain. `appraisal.grade` dikosongkan. `appraisal.importance` berisi besar manfaat rekomendasi terpilih; `appraisal.applicability` berisi penerapan per rekomendasi di RS Indonesia (ketersediaan obat/alat, Fornas/JKN, SDM, waktu respons).

## G5. Susunan slide

Baca `desain-visual.md` dulu. Urutan untuk guideline:

| Urutan | Halaman master | Isi untuk guideline |
|---|---|---|
| 1 | 2 Cover | sama |
| 2 | 3 Identitas | desain: "Clinical practice guideline"; registrasi: "tidak berlaku"; pendanaan + COI panel |
| 3 | 4 Alasan memilih | sama |
| 4 | 5 Latar belakang | beban penyakit, apa yang berubah sejak edisi lalu, tujuan guideline |
| 5 | 25 Ruang lingkup & metodologi | ruang lingkup, panel, penelusuran bukti, sistem kelas dan level, konsensus, COI |
| 6 | 34 Daftar isi | satu baris per bagian utama guideline: nomor, judul, jumlah rekomendasi, halaman, ikon |
| 7 | 35 Peta topik | mindmap: simpul pusat = topik guideline, tiap kartu = satu bagian dengan subtopiknya |
| 8 | 12 Figur kunci (opsional) | hanya figur yang memang gambar (infografik, grafik); selalu dengan sumber |
| 9 | 32 Pembahasan tematik (digandakan) | tema naratif yang disetujui; judul slide = judul tema, tanpa kicker |
| 10 | per bagian: 36 Rangkuman, lalu 26 Tabel rekomendasi (digandakan) | lihat "Slide per bagian" di bawah |
| 11 | 37 Algoritma (digandakan) | algoritma guideline disusun ulang sendiri, kotak diwarnai menurut kelas |
| 12 | 38 Tabel bebas (digandakan) | tabel guideline yang diketik ulang ringkas, dengan sumber |
| 13 | 27 Perbandingan | edisi sebelumnya, PNPK, guideline lain |
| 14 | 28 Validity AGREE II | skor 6 domain + bukti + penilaian keseluruhan + catatan satu penilai |
| 15 | 29 Penerapan di RS setempat | yang sudah sesuai praktik, yang belum beserta hambatannya, langkah realistis |
| 16 | 18 Kekuatan & kelemahan | kelemahan mencakup domain AGREE terlemah dan rekomendasi kuat berbukti lemah |
| 17 | 20 Kesimpulan & implikasi | "kesimpulan penulis" diisi pesan utama guideline |
| 18 | 21 Diskusi, 22 Referensi, 23 Penutup | sama |

Halaman 6 sampai 11, 13 sampai 17, dan 19 tidak dipakai. Halaman 33 (Figur & pembahasan) dipakai hanya untuk figur yang memang gambar; tabel dan algoritma memakai 38 dan 37.

### Slide per bagian

Tiap bagian rekomendasi yang disetujui mendapat **dua jenis slide**:

1. **Rangkuman (halaman 36), satu per bagian.** Judul = nomor dan judul bagian; kicker memuat jumlah rekomendasi dan halaman. Tiga kartu: Do (kelas 1 dan 2a), Consider (2b), Don't (kelas 3). Tiap rekomendasi ditulis sebagai frasa inti maks 6 kata (frasa yang sama dengan kolom Inti di tabel) dan diakhiri kelasnya, mis. "Notifikasi dini ke RS penerima (1)". Judul memakai titik setelah nomor bagian ("3. Organization of ..."). Semua rekomendasi bagian itu masuk ke kartunya; ukuran huruf turun bertahap 26 sampai 18 px menurut jumlah baris (kartu memuat sekitar 262 px tinggi teks). Bila pada 18 px pun tidak muat, baru pilih yang paling mengubah tindakan dan sebut sisanya ada di tabel. Kartu tanpa isi ditulis miring abu-abu "Tidak ada rekomendasi kelas ... di bagian ini", jangan dihapus. Batang "Pesan utama" berisi 2 sampai 3 poin, tiap poin maks sekitar 95 karakter (bukan satu kalimat panjang bertitik koma).
2. **Tabel lengkap (halaman 26), digandakan per 4 rekomendasi.** Kolom: Kelas · Level, Inti rekomendasi (ID + frasa tebal maks 6 kata), Rincian (populasi, syarat, tujuan), Bukti dasar, Hal. Sel pertama tiap baris dan strip di tepi kiri diwarnai menurut kelas (`recolor_element`; kode warna di `desain-visual.md`). Baris tidak terpakai dihapus beserta kotak selnya dan stripnya. Slide tabel tidak memuat baris legenda warna (dihapus 12 November 2026); arti warna disebut sekali di slide Ruang Lingkup & Metodologi dan di speaker notes. Tambahkan lencana kecil di pojok kanan atas sel pertama (centang untuk kelas 1 dan 2a, tanda tanya untuk 2b, silang untuk kelas 3) supaya arti warna terbaca tanpa legenda. Rincian lebih dari 200 karakter diturunkan ke 18 px; lebih panjang dari itu, ringkas.

Saat presentasi, slide rangkuman yang dibawakan; tabel menjadi cadangan saat ditanya. Speaker notes slide tabel memuat teks asli rekomendasi, bukti detail, catatan kritis, dan tanda cek ulang.

### Daftar isi, peta topik, algoritma, tabel

- **Daftar isi (34)** dan **peta topik (35)** dibuat dari struktur guideline (judul bagian dan subbagian), bukan dari pilihan rekomendasi, supaya audiens melihat cakupan utuh. Maksimal 8 baris atau kartu; baris, kartu, dan garis yang tidak terpakai dihapus. Ikon diganti dengan `update_fill`.
- **Algoritma (37)**: susun dari figur alur guideline dan rekomendasi terkait. Tiap kotak tindakan diakhiri kelasnya dan diwarnai menurut kelas; baris sumber di bawah judul menyebut figur dan halaman asal. Bila algoritma asli lebih besar dari kerangka (4 cabang x 3 tindakan), pecah menjadi dua slide; jangan mengecilkan teks.
- Judul kartu peta topik maks sekitar 24 karakter (satu baris); judul yang turun ke baris kedua menimpa subjudulnya.
- Kotak tindakan algoritma maks 2 baris (sekitar 70 karakter); kotak, garis penghubung, dan teks yang tidak terpakai dihapus bertiga. Kotak yang bukan rekomendasi (syarat, langkah penilaian) dibiarkan putih.
- **Tabel bebas (38)**: ketik ulang isi tabel secara ringkas (maks 5 baris per slide), dengan baris sumber "Disarikan dan dibuat ulang dari ...". Jangan menempel tangkapan layar.

## G6. Pertanyaan konsulen khas guideline

Pakai untuk speaker notes dan mockup pertanyaan (minimal 6 dari daftar ini, dengan jawaban spesifik guideline yang ditelaah). Soal statistik wajib diganti soal tentang studi pendukung rekomendasi terpilih.

1. Apa beda kelas rekomendasi dan level bukti? Bisa kelas kuat dengan bukti lemah?
2. Rekomendasi X berkelas kuat tetapi LOE-nya rendah. Kenapa panel berani?
3. Rekomendasi X didasarkan pada studi apa? Desainnya apa, hasilnya berapa?
4. Apa yang berubah dari edisi sebelumnya, dan studi apa yang mengubahnya?
5. Bedanya dengan PNPK kita atau guideline lain (mis. Eropa) di mana? Kalau berbeda, kita ikut yang mana?
6. Guideline ini disusun bagaimana? Siapa panelnya? Ada wakil pasien?
7. Berapa penulis yang punya hubungan dengan industri, dan bagaimana dikelola?
8. Penelusuran buktinya sampai kapan? Ada studi baru setelah itu yang mengubah rekomendasi?
9. Anda menilai guideline ini dengan apa? Kenapa bukan AMSTAR atau RoB?
10. Domain AGREE mana yang paling lemah dan apa dampaknya?
11. Guideline ini dari negara maju. Rekomendasi mana yang tidak bisa diterapkan di RS kita, dan apa alternatifnya?
12. Kenapa Anda hanya membahas rekomendasi ini? Bagian lain bagaimana? (jawab: pilihan disepakati bersama pembimbing, lalu ringkas bagian lain dari brief)
13. Guideline itu wajib diikuti? Apa bedanya guideline, PNPK, PPK, dan clinical pathway?
14. Kalau pasien tidak masuk kriteria studi pendukungnya, rekomendasi masih berlaku?

Jebakan yang harus dijawab jujur: rekomendasi yang tidak dibahas guideline, data biaya yang tidak ada, dan pembanding yang belum sempat dibaca.

## Checklist tambahan (masuk ke brief)

- Baca teks pendukung tiap rekomendasi terpilih, bukan hanya tabelnya.
- Buka minimal 2 studi pendukung utama dan cocokkan angkanya.
- Hafalkan definisi tiap kelas dan level yang dipakai guideline.
- Bandingkan dengan PNPK terbaru dan catat tahun terbitnya.
- Cek ketersediaan obat/alat rekomendasi terpilih di RS sendiri dan status Fornas.
- Baca ringkasan 1 baris bagian yang tidak dipresentasikan.
