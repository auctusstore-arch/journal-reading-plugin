# Desain visual slide (berlaku untuk semua jalur)

Masukan pemilik Auctus setelah uji deck guideline: deck pertama terasa "text wall", tanpa penekanan, tanpa ikon, dan tabelnya tangkapan layar. Aturan di bawah memperbaikinya. Arah gaya: lencana bulat berisi ikon garis, kartu berwarna, daftar bernomor berbentuk pil, diagram buatan sendiri.

## Prinsip

1. **Satu slide, satu pesan.** Bila isi tidak muat sebagai 3 sampai 5 butir pendek, pecah menjadi slide rangkuman dan slide rincian.
2. **Rangkuman dulu, rincian kemudian.** Tiap bagian yang berisi banyak butir (bagian rekomendasi guideline, kelompok klaim review) punya slide rangkuman visual sebelum tabel lengkapnya.
3. **Penekanan lewat struktur, bukan paragraf.** Connector Canva hanya bisa menebalkan satu kotak teks utuh, tidak sebagian kalimat. Karena itu frasa inti ditaruh di kotak teks tersendiri yang tebal (kolom "Inti", judul kartu), dan rinciannya di kotak lain yang tidak tebal.
4. **Poin, bukan kalimat panjang.** Jangan menggabungkan beberapa pesan dengan titik koma dalam satu kalimat. Pesan utama ditulis sebagai 2 sampai 3 poin di dalam kotak berwarna dengan ikon.
5. **Minimal 2 sampai 3 ikon per slide isi**, tidak perlu satu per butir.
6. **Tabel dan algoritma dibuat ulang**, bukan tangkapan layar. Tangkapan layar hanya untuk figur yang memang gambar (grafik, foto, infografik asli) dan selalu dengan sumber.
7. **Judul slide adalah isi**, bukan label generik. Slide tematik tidak memakai kicker "PEMBAHASAN TEMATIK"; cukup judul temanya.

## Kode warna kelas rekomendasi

Dipakai konsisten di tabel, algoritma, dan kartu. Warna ini sama di ketiga tema (navy, maroon, hijau).

| Kelas | Isi kotak | Garis dan teks | Arti |
|---|---|---|---|
| 1 (atau I) | #dff3e4 | #1e7a3c | hijau: direkomendasikan |
| 2a (IIa) | #fff4c7 | #8a6d00 | kuning: wajar dilakukan |
| 2b (IIb) | #ffe3c2 | #b25a00 | jingga: dapat dipertimbangkan |
| 3 (III) | #fbdada | #b3261e | merah: tidak bermanfaat atau berbahaya |
| netral | #ffffff | #5b6b7f | belum diisi atau tanpa kelas |

Untuk sistem GRADE: strong for = hijau, conditional for = kuning, conditional against = jingga, strong against = merah. Tulis pemetaan itu di slide metodologi dan speaker notes, bukan sebagai baris legenda di tiap slide tabel.

Kartu **Do / Consider / Don't**: Do memuat kelas 1 dan 2a, Consider memuat 2b, Don't memuat kelas 3. Tiap poin diakhiri kelasnya dalam kurung, mis. "(2a)". Kartu tanpa isi ditulis "Tidak ada rekomendasi kelas ini".

## Pustaka ikon

42 ikon garis buatan Auctus (berkas SVG di `assets/ikon/`; pratinjau `_lembar-ikon.png` untuk 24 ikon pertama dan `_lembar-ikon-2.png` untuk 18 ikon tambahan 15 November 2026). Yang sudah diunggah ke akun Canva Auctus sebagai gambar putih transparan:

| Nama | asset_id Canva | Dipakai untuk |
|---|---|---|
| `buku` | MAHasOHW8EU | referensi, guideline, teori |
| `centang` | MAHar-jk8Qo | lakukan, benar, Do |
| `daftar` | MAHasBycids | daftar isi, checklist, kriteria |
| `denyut` | MAHar7aTzFY | tanda vital, tekanan darah, perawatan intensif |
| `jam` | MAHar2p3Ku4 | waktu, onset, prahospital, kecepatan |
| `jantung` | MAHasF-YCyU | kardiovaskular |
| `labu` | MAHasJ9y3e4 | laboratorium, penelitian |
| `lampu` | MAHar6mR16Y | pesan utama, ide, pendahuluan |
| `naik` | MAHar7Z5gqc | pemulihan, rehabilitasi, perbaikan |
| `panah` | MAHasHEZfXs | langkah berikut, alur |
| `peringatan` | MAHasD1gdDI | waspada, bahaya, efek samping |
| `perisai` | MAHar-w31Hc | pencegahan, keamanan |
| `peta` | MAHar825iMg | struktur, alur, mindmap |
| `pil` | MAHasA5eGQ0 | obat oral, farmakoterapi |
| `pindai` | MAHar-LT6fY | pencitraan, CT, MRI, diagnosis |
| `pisau` | MAHar1qDDgA | bedah, intervensi |
| `ranjang` | MAHasDe-43M | rawat inap, bangsal |
| `sasaran` | MAHar0wxfGo | target, tujuan perawatan, luaran |
| `silang` | MAHary3hUjs | jangan, Don't |
| `suntik` | MAHasKeJtQU | injeksi, reversal, obat intravena |
| `tanya` | MAHar-tKQxc | pertimbangkan, belum pasti, Consider |
| `tetes` | MAHasGKGADw | darah, perdarahan, cairan |
| `tim` | MAHasF3JJhk | tim multidisiplin, pasien dan keluarga |

| `bandingkan` | MAHa9i6A4k8 | perbandingan, pre vs post, edisi lama vs baru |
| `bayi` | MAHa9l-OOPo | neonatus, luaran perinatal, pediatrik |
| `bendera` | MAHa9iLhl6c | kesimpulan, take-home message, tonggak |
| `biaya` | MAHa9uBJo5k | biaya, pembiayaan, JKN, tarif |
| `bintang` | MAHa9lCJCHQ | kualitas, skor NOS, kekuatan |
| `dokumen` | MAHa9izALHE | identitas artikel, naskah, PNPK |
| `gelembung` | MAHa9umLbxk | diskusi, pertanyaan konsulen, pendapat |
| `gerigi` | MAHa9kJ6Rk4 | implementasi, proses, metode |
| `grafik` | MAHa9m-HtAI | hasil, data, statistik |
| `kacapembesar` | MAHa9lCNR_k | appraisal, penelusuran, telaah kritis |
| `kalender` | MAHa9tthygo | periode studi, jadwal, tahun |
| `klipboard` | MAHa9sInS3o | kriteria inklusi, checklist metode |
| `kurva` | MAHa9r8k9u8 | distribusi, p-value, interval kepercayaan |
| `lokasi` | MAHa9sWlJkY | setting, negara, daerah, rujukan |
| `orang` | MAHa9tTiUUs | populasi, pasien, penyaji |
| `rahim` | MAHa9pQCpC0 | obstetri, persalinan, kehamilan |
| `rumahsakit` | MAHa9vCgg98 | RS, fasilitas, kapasitas ruang |
| `timbangan` | MAHa9qPHcRk | risiko vs manfaat, keseimbangan, etika |

Ikon `tambah` belum diunggah (unggah dari `assets/ikon/tambah.svg` bila perlu, setelah diubah ke PNG).

Cara pakai:

- Ikon putih selalu di atas **lencana bulat berwarna**. Lencana: `insert_shape` dengan path lingkaran `M32 0A32 32 0 1 1 32 64A32 32 0 1 1 32 0Z` (view box 64 x 64), warna aksen tema atau warna gelap kelas. Ikon: `insert_fill` dengan `asset_type: "image"`, ukuran 1,2 x jari-jari lencana, dipusatkan.
- Pada halaman template yang sudah punya ikon (34, 35, 36), ganti gambarnya dengan `update_fill` pada elemen gambar itu, jangan menambah elemen baru.
- Bila perlu ikon baru: tulis SVG 24 x 24 bergaya sama (garis putih 1,9, ujung membulat, tanpa isi), render ke PNG 256 px (`uv run --with cairosvg`), unggah lewat `create-upload-url`, dan catat `asset_id`-nya di tabel ini.
- Connector Canva tidak bisa mengambil ikon dari pustaka elemen Canva; jangan menjanjikannya.

## Teknik Canva yang perlu diketahui

- **Bentuk baru menutupi teks lama.** `insert_shape` dan `insert_fill` selalu masuk ke lapisan paling depan. Teks bawaan template berada di dalam grup, dan `layer_element` pada teks hanya mengurutkan di dalam grupnya. Setelah menyisipkan bentuk, naikkan **grupnya** ke depan (`layer_element` pada locator grup), baru sisipkan lencana dan ikon.
- **Teks baru (`add_text`) memakai font bawaan Canva**, bukan font template. Pakai seperlunya (baris sumber, baris ringkasan) dan atur ukuran serta warnanya dengan `format_text`.
- **Membangun tata letak baru dari halaman tabel**: sel tabel template adalah kotak teks terpisah yang bisa dipindah, diubah ukurannya, dan diformat. Kotak selnya dihapus, lalu bentuk baru disisipkan. Ini cara membuat halaman 34, 35, dan 37.
- **Garis penghubung** dibuat sebagai bentuk tipis (jajaran genjang setebal 4 px) dengan `insert_shape`; connector tidak bisa membuat elemen garis.
- **Ukuran teks minimum** untuk dibaca di proyektor: 21 px untuk isi tabel, 24 px untuk poin. Bila teks tidak muat, ringkas teksnya, jangan mengecilkan lagi.
- **Lencana ikon di atas halaman yang tidak diubah tata letaknya** (mis. slide tema, latar belakang, penerapan) cukup disisipkan langsung: lingkaran `insert_shape` lalu ikon `insert_fill` berukuran 1,2 x jari-jari, diletakkan di pojok kanan atas panel supaya tidak menimpa teks. Tidak perlu menaikkan grup karena tidak ada teks di bawahnya.
- **Jangan menerapkan operasi dari sesi utama.** Satu panggilan `edit-design` mengembalikan seluruh isi halaman (puluhan ribu token), termasuk untuk perbaikan satu teks. Serahkan ke subagen; sesi utama hanya melihat thumbnail lewat `read-design` dengan `transaction_id` dan `fields: ["thumbnails"]`.
- Untuk menemukan locator bentuk, gambar, dan grup (tidak tampil di `list_placeholders.py`), jalankan `scripts/page_elements.py design.json <no halaman>`.

## Pemeriksaan sebelum menyerahkan

- Tiap slide isi punya judul yang menyebut isinya dan minimal satu elemen visual (ikon, kartu berwarna, diagram, atau figur).
- Tidak ada kalimat lebih dari sekitar 20 kata di dalam slide (rincian pindah ke speaker notes).
- Warna kelas konsisten antara slide rangkuman, tabel, dan algoritma.
- Tidak ada tangkapan layar tabel.

## Gaya bahasa dan isi: pelajaran dari revisi manual pemesan (12 November 2026)

Pemesan menyunting sendiri deck guideline ICH setelah diserahkan. Perubahannya dicatat di sini sebagai aturan untuk order berikutnya.

**Hindari kata "kita"** di slide, speaker notes, skrip presentasi, dan brief (kalimat yang diucapkan atau ditulis atas nama penyaji). Ganti dengan kalimat pasif atau rujukan netral:

| Jangan | Pakai |
|---|---|
| Mengapa penting bagi kita | Relevansi ke lokal |
| Rekomendasi mana yang paling layak langsung kita adopsi? | Rekomendasi mana yang paling layak langsung diadopsi? |
| Seberapa jauh kita percaya ... | Seberapa jauh ... dapat dipercayai? |
| pasien kita, RS kita, praktik kita | pasien lokal, RS setempat, praktik setempat |

`make_ops.py` dan `build_script.py` berhenti dengan MASALAH bila masih ada kata "kita". Placeholder dan notes bawaan di tiga master sudah diganti pada 13 November 2026 (mis. "Mirip pasien lokal?", "Intervensi tersedia di RS setempat?"), jadi kata itu tidak lagi terbawa dari template. Pengecualian: kutipan pertanyaan konsulen di brief boleh memakai "kita" karena itu ucapan konsulen, bukan penyaji.

**Pola lain yang dipakai pemesan:**

- **Tanpa rujukan halaman di subjudul dan kesimpulan.** "Dua patologi utama (e287)" menjadi "Dua patologi utama"; "(Top 10, e282-e283)" dibuang. Halaman sumber cukup di kolom Hal. tabel, baris sumber tabel atau figur, dan speaker notes.
- **Data yang belum ada tidak diisi asumsi.** Isi dengan `[perlu diisi]` berwarna merah (#b3261e), bukan kalimat perkiraan atau "data uji". Kotak yang seluruhnya belum ada datanya (mis. Kasus pemicu) dihapus bersama kotaknya. Ini satu-satunya kurung siku yang boleh tersisa, dan harus dilaporkan saat serah terima.
- **Slide yang tidak lengkap dibuang**, kecuali slide yang wajib. Slide Perbandingan dengan sumber lain (halaman 27) dihapus bila pembandingnya belum dibaca. Slide Perbandingan dengan Edisi Sebelumnya (halaman 39) wajib pada jalur guideline: sumbernya diminta dulu (lihat `jalur-guideline.md` G2b), dan bila tetap tidak tersedia diisi `[perlu diisi]` merah, bukan dihapus.
- **Kesimpulan diringkas.** Cukup kesimpulan penulis dan take-home message. Kotak "Kesimpulan penyaji" dan tiga kotak implikasi (praktik klinis, sistem, penelitian) dihapus pada deck guideline; isinya pindah ke speaker notes.
- **Slide figur tanpa label berlapis.** Label "Yang ditunjukkan", "Poin penting", "Catatan kritis" dibuang; cukup 2 kalimat pendek, dengan kata kunci tebal. Catatan kritis pindah ke notes.
- **Baris pertama kartu ditebalkan** (mis. "Relevansi klinis", "Kebaruan & dampak") dan kata kunci di poin ditebalkan. API Canva tidak bisa menebalkan sebagian teks; sebutkan di laporan serah terima kata mana yang perlu ditebalkan manual, atau pisahkan judul kartu ke elemen teks sendiri.
- **Identitas ringkas.** Penulis ditulis "Greenberg SM (Chair); AHA/ASA", bukan daftar panjang. Kalimat tambahan di baris sumber ("Tabel asli memuat lebih banyak dokumen") dibuang.
- **Nomor bagian memakai titik**: "3. Organization of ..." bukan "3 Organization of ...".
- **Ukuran huruf rincian tabel jangan di bawah 19 px**; bila tidak muat, ringkas teksnya.

### Pemetaan ikon untuk jalur studi (RCT, kohort, diagnostik, SR-MA)

Aturan 5 di atas (minimal 2 sampai 3 ikon per slide isi) berlaku untuk **semua** deck, termasuk jalur studi, bukan hanya guideline. Pada deck JR dr. Putri Nabila (15 November 2026) ikon belum dipakai karena `desain-visual.md` tidak dibaca sebelum mengisi slide; jangan diulang. Pola yang dipakai pada deck acuan pemesan: lencana bulat berwarna aksen berisi ikon putih di pojok kanan atas kartu atau di sel pertama tabel.

| Slide | Ikon yang disarankan |
|---|---|
| Identitas artikel | `dokumen`, `kalender`, `buku` |
| Alasan memilih | `lampu` (relevansi), `sasaran` (kebaruan), `bintang` (kualitas) |
| Latar belakang | `buku` (yang diketahui), `tanya` (knowledge gap), `sasaran` (tujuan) |
| PICO | `orang` (P), `pil` atau `gerigi` (I), `bandingkan` (C), `sasaran` (O) |
| Metode | `klipboard` (kriteria), `kalender` (periode), `gerigi` (analisis) |
| Alur partisipan dan karakteristik dasar | `orang`, `tim` |
| Hasil utama dan tabel | `grafik`, `kurva`, `naik`, `peringatan` (harm) |
| Validity | `kacapembesar`, `bintang` |
| Importance & applicability | `timbangan`, `rumahsakit`, `biaya`, `lokasi` |
| Kekuatan & kelemahan | `centang` (kekuatan), `peringatan` (kelemahan) |
| Level of evidence | `bintang`, `perisai` |
| Perbandingan | `bandingkan`, `buku` |
| Strategi daerah | `peta`, `lokasi`, `rumahsakit`, `jam` |
| Kesimpulan | `bendera`, `lampu` |
| Diskusi | `gelembung`, `tanya` |
| Obstetri (isi klinis) | `rahim`, `bayi` |

Cara memasang tetap seperti catatan di bawah (lencana `insert_shape`, ikon `insert_fill`, naikkan grup ke depan bila perlu). Tinggi kartu ikut berubah saat teks diganti, jadi pasang ikon setelah teks final.

### Aturan: judul utama slide tidak diberi ikon

Keputusan pemesan (15 November 2026): **heading utama slide (judul besar 54 px di kiri atas) tidak boleh diberi ikon atau lencana**, baik di kiri maupun di samping judul. Ikon hanya untuk kartu, baris tabel, daftar bernomor, atau kotak isi. Untuk slide yang isinya hanya satu tabel berbaris pendek (mis. Methods: Outcomes & Statistics, NOS, dua slide Comparison), cukup tanpa ikon atau beri ikon pada baris tabel bila tinggi barisnya 100 px atau lebih. Kolom "Slide" dengan "lencana judul" di pemetaan di atas tidak berlaku lagi.
