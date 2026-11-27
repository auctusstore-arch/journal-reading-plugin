# Jalur case report

Dipakai bila paper adalah laporan kasus: 1 sampai 3 pasien yang diceritakan satu per satu, dengan atau tanpa tinjauan pustaka. Tool: **JBI Critical Appraisal Checklist for Case Reports** (CASP tidak punya checklist case report). Langkah 2 dan 3 di `/jr:ekstrak` serta susunan slide studi diganti jalur ini (aturan anti-halusinasi dan penanda `[CEK]` tetap berlaku); Langkah 4b sampai 6 tetap berlaku.

## C0. Klasifikasi (wajib, di intake)

| Jenis | Tanda | Jalur |
|---|---|---|
| Case report | 1 sampai 3 pasien, narasi individual, tidak ada analisis kelompok | jalur ini |
| Case series | lebih dari 3 pasien (walau diceritakan satu per satu), atau pasien dikumpulkan sebagai kelompok dengan kriteria inklusi atau ringkasan statistik | **belum ada jalur**; sampaikan ke user dan berhenti. Jangan dialihkan ke CASP Cross-Sectional atau JBI Case Reports |
| Case report + systematic review | ada penelusuran sistematis terdokumentasi | tanyakan user bagian mana yang menjadi fokus; kasus lewat jalur ini, SR lewat CASP Systematic Review |

Tentukan dari isi, bukan judul. Pasien kontrol, insidens, atau perbandingan kelompok berarti desainnya bukan case report.

## C1. Ekstraksi

Tulis ke `extract.md`, tiap butir dengan halaman. Yang tidak ada ditulis "tidak dilaporkan".

- Identitas: judul, penulis, jurnal, tahun;vol(no):hal, DOI, persetujuan pasien (consent), etik, pendanaan, COI.
- Alasan kasus dilaporkan menurut penulis (jarang, presentasi atipikal, efek samping baru, terapi baru, jebakan diagnosis).
- Pasien: usia, jenis kelamin, riwayat medis, keluarga, psikososial, obat, intervensi sebelumnya.
- **Linimasa**: tiap kejadian dengan waktu relatif persis seperti di paper (hari ke-, minggu ke-).
- Presentasi: gejala, tanda vital, pemeriksaan fisik.
- Pemeriksaan penunjang dengan angka, satuan, dan nilai rujukan bila ditulis; diagnosis banding dan cara menyingkirkannya.
- Diagnosis akhir dan dasarnya.
- Tata laksana: obat, dosis, rute, durasi, tindakan.
- Luaran dan follow-up: kondisi sesudah intervensi, lama pengamatan, efek samping atau kejadian tak terduga.
- Pelajaran yang diklaim penulis.

Privasi: jangan menambah identitas apa pun di luar yang tercetak, dan jangan menyalin nama, nomor rekam medis, atau foto wajah yang dapat dikenali.

## C2. Konteks dan pembanding

- Cari di PubMed (jangan dari ingatan) kasus serupa, SR, dan guideline atau PNPK yang berlaku. Catat hanya yang benar-benar dibaca; sisanya masuk `cek_ulang`.
- Bandingkan diagnosis dan tata laksana kasus dengan standar: sesuai, menyimpang dengan alasan, atau menyimpang tanpa alasan.
- Tidak ada `effect_calc.py`, ARR, NNT, atau GRADE: satu kasus tidak punya ukuran efek.
- Tidak ada gerbang persetujuan peta isi; seluruh kasus muat dalam satu presentasi.

## C3. Appraisal: JBI Case Reports

Pertanyaan diparafrase dari dokumen resmi (jbi.global/critical-appraisal-tools, © JBI 2020, dibaca 26 November 2026). Dokumen itu menyatakan tool diberikan **untuk keperluan riset**; pemakaian lain ditanyakan ke jbisynthesis@adelaide.edu.au. Jangan menempel teks resmi utuh. Bila JBI sudah menerbitkan versi baru, ikuti versi baru. Karena order JR berbayar, sebut batasan riset ini di laporan akhir tiap order case report sampai tim memastikan izinnya.

| No | Pertanyaan (parafrase) | Yang dicari |
|---|---|---|
| 1 | Demografi pasien dijelaskan jelas? | usia, jenis kelamin, riwayat, diagnosis, terapi dan obat sebelumnya, konteks |
| 2 | Riwayat jelas dan disajikan sebagai linimasa? | riwayat medis, keluarga, psikososial, intervensi lalu beserta hasilnya, urutan waktu |
| 3 | Kondisi klinis saat datang dijelaskan jelas? | gejala, frekuensi, keparahan, diagnosis banding |
| 4 | Tes atau metode diagnostik dan hasilnya jelas? | pemeriksaan yang cukup untuk menegakkan diagnosis, hasil, gambar bila relevan |
| 5 | Intervensi atau prosedur terapi jelas? | bisa diulang klinisi lain: jenis, dosis, rute, frekuensi |
| 6 | Kondisi sesudah intervensi jelas? | ada atau hilangnya gejala, hasil follow-up |
| 7 | Efek samping atau kejadian tak terduga diidentifikasi dan dijelaskan? | harm dinyatakan, termasuk pernyataan bahwa tidak ada |
| 8 | Ada pelajaran yang bisa dibawa pulang? | pesan kunci dan panduan untuk kasus serupa |

- Jawaban: **Ya, Tidak, Tidak jelas, Tidak berlaku** (Yes, No, Unclear, Not applicable). Tiap jawaban disertai bukti berlokasi dan alasan.
- **Tidak ada skor total atau ambang.** Pilihan Include / Exclude / Seek further info di formulir resmi dibuat untuk seleksi studi dalam systematic review; pada journal reading ganti dengan kesimpulan penyaji: kekuatan pelaporan, item terlemah, dan apa yang boleh dipelajari.
- JBI menilai kejelasan dan mutu laporan, bukan membuktikan terapi menyebabkan luaran. Hubungan sebab-akibat dari satu kasus dinyatakan sebagai dugaan, dengan penjelasan lain yang mungkin (perjalanan alami, terapi bersamaan, regresi ke rerata).
- CARE adalah pedoman pelaporan, bukan tool appraisal. Pakai hanya bila klien memintanya, dari dokumen CARE yang benar-benar dibuka.
- Bila klien atau departemen meminta tool lain yang memang untuk case report, tool itu yang dipakai. CASP tidak punya checklist case report dan ditolak `build_brief.py`.

## C4. Di brief.json

Lihat `brief-schema.md`, "Varian case report". Adanya `paper.linimasa` mengaktifkan mode case report di `build_brief.py`. `appraisal.validity` berisi 8 baris JBI; `appraisal.importance` berisi nilai pelajaran klinis dan kebaruan; `appraisal.applicability` berisi penerapan di RS sendiri; `appraisal.grade` dikosongkan.

## C5. Susunan slide

Halaman template jalur studi dipakai ulang: ganti kicker, judul, dan label sesuai isi kolom ketiga. Satu slide boleh digandakan bila isi tidak muat; jangan mengecilkan font.

| Urutan | Halaman master | Isi untuk case report |
|---|---|---|
| 1 | 2 Cover | sama |
| 2 | 3 Identitas | desain: "Case report"; slot registrasi diganti consent dan etik; hapus tempat tangkapan layar bila kosong |
| 3 | 4 Alasan memilih | kartu: kasus pemicu, alasan kasus dilaporkan, relevansi; tanpa kasus pemicu hapus kotak bawah |
| 4 | 5 Latar belakang | penyakit dan mengapa jarang atau sulit; kotak bawah (bawaan hipotesis) diisi alasan kasus dilaporkan |
| 5 | 7 (lima baris, boleh digandakan) | Informasi pasien: satu baris pendek per butir (identitas klinis, keluhan, riwayat, obat, pemeriksaan fisik) |
| 6 | 38 Tabel bebas | Linimasa: kolom Waktu, Kejadian, Temuan / tindakan; 5 baris per slide, gandakan |
| 7 | 38 (salinan) | Pemeriksaan: kolom Tes, Hasil (dengan nilai rujukan), Arti; gandakan per 5 tes |
| 8 | 32 (dua kartu) | Diagnosis banding (maks 3 per kartu) dan diagnosis akhir |
| 9 | 32 (salinan) | Tata laksana |
| 10 | 32 (salinan) | Luaran, follow-up, efek samping |
| 11 | 33 Figur & pembahasan | figur asli + sumber, satu per slide; hapus bila tidak ada |
| 12 | 27 Perbandingan | kasus ini dibanding satu pembanding per slide; kepala kolom "Kasus ini"; gandakan untuk guideline dan literatur; hapus bila tidak ada pembanding yang dibaca |
| 13 | 4 (3 salinan) | kartu JBI Q1 sampai Q3, Q4 sampai Q6, Q7 sampai Q8 + kartu ketiga catatan penyaji; kicker CRITICAL APPRAISAL |
| 14 | 4 (salinan) | Ringkasan appraisal: jumlah tiap jawaban, item terlemah, batas kesimpulan |
| 15 | 29 Penerapan di RS setempat | yang sudah sesuai, hambatan, langkah realistis |
| 16 | 18 Kekuatan & kelemahan | sama |
| 17 | 20 Kesimpulan | slot besar efek dan kepastian bukti diganti pelajaran kunci dan batas satu kasus |
| 18 | 21, 22, 23 | diskusi; referensi (cantumkan JBI, gandakan halaman 22 bila lebih dari 4); penutup |

Halaman 6, 8 sampai 17, 19, 25, 26, 28, 30, dan 31 tidak dipakai. Susunan ini belum pernah dicoba di Canva: periksa thumbnail tiap slide yang dipakai ulang.

Semua label bawaan studi (mis. "Randomisasi:", "Posisi paper ini", teks tetap halaman 4) wajib diganti dengan tangan: `make_ops.py` hanya menandai `[kurung siku]` yang belum terisi.

Contoh `page_numbers`: `[2,3,4,5,7,38,38,32,32,32,33,27,4,4,4,4,29,18,20,21,22,23]`. Sesudah insert, cocokkan urutan lewat teks di slide, bukan judul internal (halaman kembar berjudul sama).

## C6. Pertanyaan konsulen khas case report

Minimal 6 masuk mockup, dengan jawaban spesifik kasus.

1. Apa yang baru atau penting dari kasus ini?
2. Apa diagnosis bandingnya, dan bagaimana masing-masing disingkirkan?
3. Kenapa memilih terapi itu? Apa alternatif dan standar di guideline atau PNPK?
4. Apakah perbaikan pasien benar akibat terapi? Penjelasan lain apa yang mungkin?
5. Level of evidence case report di mana? Bolehkah mengubah praktik?
6. Anda menilai dengan apa? Kenapa bukan CASP atau CARE?
7. Follow-up-nya cukup lama? Apa yang belum diketahui?
8. Apakah ada consent pasien?
9. Kalau pasien ini datang ke RS kita, apa yang Anda lakukan pertama kali?

## C7. Zoom

Di `form-pre.json` tambahkan `"jenis_paper": "case_report"` supaya label penilaian diri memakai kasus (linimasa, diagnosis banding) dan bukan PICO atau ukuran efek. Lakukan hal sama di `form-post.json`. Soal cek pemahaman: diagnosis banding, arti hasil tes kunci, alasan terapi, batas kesimpulan dari satu kasus.
