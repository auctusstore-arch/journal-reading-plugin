# Jalur Zoom (add-on sesi 1-on-1)

Dipakai untuk order yang memuat sesi Zoom (Complete Bundle atau Zoom Only). Tujuannya: sesi 60 menit fokus ke celah pemahaman klien yang nyata, bukan latihan generik. Tiga keluaran skill: form pre-zoom, panduan tutor, dan form post-zoom. Form post-presentasi (H+1, testimoni) baku di website dan tidak dibuat di sini.

Format blok form dan blok jawaban: `references/format-form.md`. Baca dulu sebelum menulis form.

```
Z1 sumber  ->  Z2 form pre-zoom  ->  [admin tempel, klien isi, admin salin jawaban]
           ->  Z3 baca jawaban   ->  Z4 panduan tutor + Z5 form post-zoom  ->  sesi  ->  Z6 serah terima
```

Pemetaan gap ke slide adalah inti sesi: tiap area prioritas harus punya nomor slide klien yang dibuka dan dibahas (Z3 dan Z4). Panduan tutor menolak prioritas tanpa slide.

Waktu ideal: form pre-zoom dipublish H-3 sebelum Zoom dan diisi paling lambat H-1; panduan tutor siap malam sebelum Zoom.

## Z1. Sumber

- **Order Complete Bundle (slide dan brief sudah dibuat):** pakai `extract.md`, `brief.json`, dan slide final di folder order. Jangan mengekstrak ulang.
- **Order Zoom saja:** minta PDF paper dan slide klien (PPTX, PDF, atau tautan) bila belum ada di portal. Buat ekstraksi ringan ke `extract.md`: identitas, desain studi dan tool appraisal, PICO, alur partisipan, outcome primer dengan angka dan lokasinya, 3 kelemahan utama. Aturan anti-halusinasi Langkah 2 tetap berlaku. Hitung ulang ukuran efek utama dengan `effect_calc.py`. Tidak perlu brief, skrip, atau audio.
- **Case report:** ekstraksi ringan memakai butir C1 dan JBI (`jalur-case-report.md`), bukan PICO, alur partisipan, atau `effect_calc.py`; `form-pre.json` dan `form-post.json` memuat `"jenis_paper": "case_report"`; soal cek mengikuti C7; prioritas default: diagnosis banding, alasan terapi, batas kesimpulan satu kasus.
- **Ekstrak slide klien per nomor** (PPTX): `uv run --with python-pptx python3 -I` membaca tiap slide (teks bentuk dan tabel) ke `slides.txt` dengan penanda `--- S<n>`. Pakai ini untuk Z3 dan Z4; tabel dan gambar yang hanya berupa gambar perlu dibuka manual di PPTX atau paper.

## Z2. Form pre-zoom

Tulis `form-pre.json` (hanya bagian personal), lalu:

```
uv run python3 scripts/build_form.py form-pre.json <outdir>/
```

Script menyisipkan bagian baku "Kebutuhan sesi" dan "Penilaian diri" (6 area self-rating) di depan, memvalidasi kontrak, dan menulis `form-pre-zoom.txt` yang siap ditempel admin.

Bagian personal (1 bagian, judul "Cek pemahaman paper", 5 sampai 7 pertanyaan):

- 4 sampai 6 pilihan ganda dari paper ini, masing-masing menguji satu konsep yang hampir pasti ditanya konsulen. Sebaran yang disarankan: outcome primer atau PICO, arti ukuran efek utama (mis. "HR 0,78 (0,65 sampai 0,94) berarti ..."), desain atau alur partisipan (mis. analisis ITT vs per protokol), satu item appraisal yang kontroversial, dan applicability. Untuk guideline: kelas dan level satu rekomendasi kunci. Untuk review: jenis review dan kekuatan klaim utama.
- Opsi 3 sampai 4, pengecoh masuk akal (kesalahan umum PPDS, bukan jawaban konyol). Kunci dan makna salahnya ditulis di `tutor.kunci` dan `tutor.catatan`.
- 1 soal terbuka `teks_panjang`: "Tuliskan take-home message paper ini dalam satu kalimat."
- Angka di soal harus identik dengan `extract.md`. Jangan membuat soal dari angka yang tidak ada di paper.
- Tidak menyebut kunci di teks soal, dan soal harus bisa dijawab tanpa membuka paper bila klien sudah membacanya sekali.

## Z3. Baca blok jawaban

User menempelkan blok `AUCTUS-JAWABAN v1`. Dari blok itu, tentukan:

- Kebutuhan: salin `tujuan_sesi`, `kekhawatiran`, `pengalaman_jr`, `status_slide`, `gaya_konsulen` (ringkas, tanpa mengubah maknanya).
- Gap: area dengan self-rating 1 sampai 2, soal cek pemahaman yang `SALAH` atau kosong, dan ketidaksesuaian (self-rating statistik 4 tetapi salah membaca HR berarti percaya diri berlebih; ini prioritas tinggi).
- 2 sampai 3 area prioritas, masing-masing dengan alasan yang merujuk ke jawaban klien.
- **Petakan tiap prioritas ke nomor slide klien** (dan tiap soal cek yang salah ke slide terkait). Contoh: gap membaca Bland-Altman memetakan ke slide tabel Bland-Altman, slide plot, dan slide metode ICC; gap sensitivitas vs PPV memetakan ke slide tabel akurasi dan slide telaah kritis; gap rekomendasi memetakan ke slide diskusi, kesimpulan, dan saran. Bila klien meminta membahas gambar atau tabel tertentu, slide itu masuk. Jangan memetakan ke nomor gambar paper saja.

Bila klien belum mengisi form, tetap buat panduan dari sumber Z1 dengan prioritas default (statistik, kelemahan terbesar, applicability) dan tulis di `meta.sumber` bahwa pre-zoom belum diisi.

Blok jawaban memuat kunci jawaban, jadi tidak disimpan di folder yang dikirim ke klien.

## Z4. Panduan tutor

Tulis `tutor.json`, lalu:

```
uv run python3 scripts/build_tutor_guide.py tutor.json <outdir>/
```

Skema:

```
meta:
  penyaji, prodi, departemen, judul_paper
  paper              sitasi singkat (penulis, jurnal, tahun)
  jadwal_presentasi  mis. "20 November 2026 13:00 WIB"
  durasi_menit       durasi presentasi klien
  jadwal_zoom        mis. "18 November 2026 19:30 WIB"
  layanan            "Complete Bundle" | "Zoom Only"
  sumber             mis. "extract + brief + pre-zoom diisi 17/11" atau "paper + slide klien, pre-zoom belum diisi"
  warna, nama_file   nama_file mis. "panduan-tutor-dr-nama"
kebutuhan:           {tujuan, kekhawatiran, pengalaman, status_slide, gaya_konsulen}
self_rating:         [{area, skor}]  6 area baku; skor 1 sampai 5 atau null
cek_pemahaman:       [{soal, jawaban, status: benar|salah|terbuka|kosong, makna, slide?}]  makna = artinya untuk sesi; slide = slide terkait (opsional, dianjurkan untuk soal salah)
prioritas:           2 sampai 3 [{area, alasan, slide}]  slide = daftar nomor/rentang slide klien yang dibahas untuk gap ini (wajib, tidak boleh kosong)
agenda:              [{menit, blok, fokus, slide?}]  slide = slide yang dibuka pada blok itu (opsional)  total 55 sampai 60 menit, mengikuti SOP 5:
                       5 tujuan dan kekhawatiran, 20 presentasi singkat, 25 simulasi tanya-jawab, 10 perbaikan dan H-0
                     boleh digeser sesuai kebutuhan (mis. slide belum mulai: presentasi 10, review struktur slide 15)
review_slide:        5 sampai 8 [{slide, cek, gap?}]  gap = nomor prioritas (1 sampai 3) atau daftar nomor yang dilayani titik ini; tiap prioritas sebaiknya punya minimal satu titik. angka yang harus dicocokkan ke paper, klaim berlebihan, slide rawan ditanya
simulasi:            6 sampai 8 [{kategori, pertanyaan, jawaban_model, tanda_lemah, lanjutan}]
perbaikan_kandidat:  tepat 3 butir
checklist_h0:        4 sampai 6 butir untuk klien di hari presentasi
visual:              opsional, id visual yang SUDAH disetujui tutor/user (lihat references/visual-katalog.md). Jangan mengisi tanpa bertanya lebih dulu.
```

Usulan visual (Z4a, sebelum menulis `tutor.json`): petakan gap klien ke katalog `references/visual-katalog.md`, usulkan paling banyak 3 kandidat dengan alasannya, **tanyakan dulu ke tutor/user mana yang dibuat atau apakah perlu** (AskUserQuestion, sertakan "Tidak perlu visual"), baru eksekusi yang dipilih.

Aturan isi:

- **Simulasi** diurutkan dari area prioritas. Ambil dari `brief.json` bagian `pertanyaan` bila ada (pilih yang paling dekat dengan gap, perdalam bila perlu); bila tidak ada brief, buat dari `extract.md` dan `references/bank-pertanyaan-konsulen.md`. `jawaban_model` 2 sampai 4 kalimat mengikuti teknik jawab 5 langkah (`references/bank-pertanyaan-konsulen.md`: klarifikasi bila perlu, jawab inti, bukti berlokasi, akui batasan, dan "belum menemukan datanya, akan dicek" bila tidak tahu). `tanda_lemah` menyebut kesalahan spesifik yang harus ditangkap tutor (mis. "menyebut HR sebagai risiko absolut"). `lanjutan` adalah pertanyaan susulan konsulen bila jawaban pertama benar.
- **Peta gap ke slide**: panduan menampilkan tabel Gap, Area, Slide; tiap prioritas wajib punya `slide`, dan `review_slide.gap` menautkan titik review ke prioritas (skrip memberi peringatan bila ada prioritas tanpa titik review). Cek bahwa nomor slide cocok dengan isi slide di `slides.txt`, bukan dari ingatan.
- **Review slide** merujuk nomor atau judul slide klien. Untuk order Complete Bundle, fokus ke bagian yang disentuh klien setelah serah terima dan ke item `cek_ulang`.
- **Perbaikan kandidat** spesifik dan bisa dikerjakan sebelum hari H, bukan nasihat umum.
- Panduan memuat penilaian kesiapan klien dan kunci jawaban. Hanya untuk tutor.

## Z5. Form post-zoom

Dibuat bersamaan dengan panduan tutor (sebelum sesi), supaya admin bisa langsung publish begitu sesi selesai. Tulis `form-post.json` (hanya bagian personal), lalu jalankan `build_form.py` yang sama. Script menyisipkan bagian baku "Sesi Zoom", "Penilaian diri setelah sesi" (6 area yang sama dengan pre, untuk delta), dan "Penutup" (kesiapan maju, yang masih kurang, NPS).

Bagian personal (1 bagian, judul "Kebutuhan dokter", 2 sampai 5 pertanyaan):

- 1 pertanyaan `pilihan` per kebutuhan atau kekhawatiran yang ditulis klien di pre-zoom, opsi tetap: "Sudah terjawab", "Sebagian", "Belum". Teks memuat kebutuhannya dalam kata-kata klien, diringkas.
- 1 sampai 2 soal cek ulang (pilihan ganda berkunci) dari konsep yang salah di pre-zoom, dengan angka atau sudut yang sedikit berbeda supaya bukan hafalan.

Bila tutor mencatat hal baru selama sesi, form post-zoom boleh dibuat ulang setelah sesi sebelum dipublish.

## Z6. Serah terima

Simpan di folder order: `form-pre-zoom.txt`, `form-post-zoom.txt`, `panduan-tutor-....html`, dan blok jawaban pre-zoom (`jawaban-pre-zoom.txt`, arsip internal). Laporkan ke user:

- Langkah admin berikutnya (tempel dan publish form mana, kapan).
- 2 sampai 3 area prioritas sesi dalam satu baris masing-masing.
- Hal yang diasumsikan (mis. pre-zoom belum diisi, slide klien belum diterima).

Setelah sesi, tutor mengirim 3 perbaikan prioritas lewat WhatsApp dan admin mempublish form post-zoom. Form post-presentasi muncul sendiri di portal klien sehari setelah tanggal presentasi.
