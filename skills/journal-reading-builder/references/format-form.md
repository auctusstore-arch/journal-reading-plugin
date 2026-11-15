# Format form Zoom (kontrak v1)

Kontrak antara skill dan portal Journal Reading di website. Skill menghasilkan **blok form**; admin menempelnya di panel order (admin, Produk, Journal Reading, Form Zoom), lalu form muncul di portal klien. Setelah klien mengisi, admin menekan "Salin jawaban untuk Claude" dan menempelkan **blok jawaban** ke Claude.

Skema yang sama divalidasi dua kali: oleh `scripts/build_form.py` (skill) dan oleh `src/modules/products/journal-reading-forms.ts` (website). Bila salah satu diubah, ubah keduanya dan naikkan versi.

## Blok form

```
=== AUCTUS-FORM v1 ===
{ ...JSON di bawah... }
=== AKHIR AUCTUS-FORM ===
```

Teks di luar penanda diabaikan, jadi blok boleh ditempel bersama kalimat pengantar.

```
versi        1
jenis        "pre_zoom" | "post_zoom"
judul        maks 120 karakter
pengantar    maks 800 karakter; jelaskan tujuan form dengan nada diagnostik, bukan ujian
bagian       1 sampai 8 bagian:
  judul        maks 120 karakter
  deskripsi    opsional, maks 500 karakter
  pertanyaan   minimal 1
    id         unik di seluruh form, pola ^[a-z0-9_]{1,40}$
    tipe       "pilihan" | "pilihan_banyak" | "skala" | "teks_pendek" | "teks_panjang"
    teks       maks 500 karakter
    bantuan    opsional, maks 300 karakter (teks kecil di bawah pertanyaan)
    wajib      boolean, default true
    opsi       wajib untuk pilihan/pilihan_banyak: 2 sampai 8 string, masing-masing maks 200 karakter, tidak boleh dobel
    skala      wajib untuk tipe skala: {min: 0 atau 1, max: 2 sampai 10, label_min, label_max (maks 40 karakter)}
    inti       opsional, ID baku (daftar di bawah) untuk metrik lintas order
    tutor      opsional, HANYA untuk tutor:
      kunci      string atau daftar string, harus persis salah satu opsi
      catatan    maks 500 karakter, mis. "salah di sini berarti belum paham NNT"
```

Batas lain: total pertanyaan 1 sampai 30, tidak boleh ada em dash di mana pun.

**Field `tutor` tidak pernah sampai ke browser klien.** Website memisahkannya ke kolom `spec_tutor` saat menyimpan. Karena itu kunci jawaban hanya boleh ditulis di `tutor`, jangan di `teks`, `bantuan`, atau `opsi`.

## ID baku (`inti`)

Pertanyaan baku disisipkan otomatis oleh `build_form.py`, jadi teksnya sama di semua order. Jangan menulis ulang pertanyaan ini secara manual.

| ID | Form | Tipe | Isi |
|---|---|---|---|
| `tujuan_sesi` | pre | teks_panjang | Yang paling ingin didapat dari sesi |
| `kekhawatiran` | pre | teks_panjang | Kekhawatiran terbesar saat presentasi |
| `pengalaman_jr` | pre | pilihan | Berapa kali pernah membawakan journal reading |
| `status_slide` | pre | pilihan | Kondisi slide saat ini |
| `gaya_konsulen` | pre | pilihan_banyak | Jenis pertanyaan yang biasa diajukan konsulen |
| `self_pico` | pre, post | skala 1-5 | Percaya diri menjelaskan PICO dan pertanyaan penelitian |
| `self_desain` | pre, post | skala 1-5 | Desain studi dan alur partisipan |
| `self_statistik` | pre, post | skala 1-5 | Membaca ukuran efek (RR, OR, HR, NNT, CI, p) |
| `self_appraisal` | pre, post | skala 1-5 | Menjelaskan tool appraisal item per item |
| `self_applicability` | pre, post | skala 1-5 | Menilai penerapan di RS sendiri |
| `self_spontan` | pre, post | skala 1-5 | Menjawab pertanyaan spontan konsulen |
| `kebutuhan_terpenuhi` | post | skala 1-5 | Kebutuhan yang ditulis sebelum sesi terpenuhi |
| `kejelasan_umpan_balik` | post | skala 1-5 | Umpan balik tutor jelas dan bisa langsung dipakai |
| `rating_tutor` | post | skala 1-5 | Penilaian keseluruhan terhadap tutor |
| `kesiapan_maju` | post | skala 1-5 | Kesiapan maju presentasi sekarang |
| `masih_kurang` | post | teks_panjang | Yang masih terasa kurang |
| `nps` | post | skala 0-10 | Kemungkinan merekomendasikan ke teman sejawat |

Form post-presentasi (H+1) tidak dibuat skill. Pertanyaannya baku dan tersimpan di kode website: pelaksanaan, kelancaran, pertanyaan konsulen yang muncul, bagian layanan yang paling membantu, rating keseluruhan, NPS, testimoni, dan izin pakai testimoni (nama lengkap, inisial dan departemen, anonim, tidak boleh dipakai).

## Blok jawaban (ekspor dari admin)

```
=== AUCTUS-JAWABAN v1 ===
Jenis: pre_zoom
Order: 1a2b3c4d
Penyaji: dr. Nama
Layanan: Complete Bundle
Paper: Judul paper dari intake
Jadwal presentasi: 20 November 2026 13:00 WIB
Jadwal Zoom: 18 November 2026 19:30 WIB
Dikirim: 17 November 2026 21:04 WIB

[Kebutuhan sesi]
[tujuan_sesi] (teks_panjang, inti) Apa yang paling ingin dokter dapatkan dari sesi ini?
Jawaban: ...

[Cek pemahaman paper]
[cek_outcome] (pilihan) Outcome primer studi ini adalah ...
Jawaban: Persalinan sesar
Kunci tutor: Persalinan sesar (BENAR)
Catatan tutor: ...
=== AKHIR AUCTUS-JAWABAN ===
```

Pertanyaan yang tidak dijawab ditulis `Jawaban: (kosong)`. Untuk pertanyaan berkunci, baris `Kunci tutor` memuat status `BENAR` atau `SALAH`. Blok ini memuat kunci jawaban, jadi hanya untuk tim, jangan diteruskan ke klien.
