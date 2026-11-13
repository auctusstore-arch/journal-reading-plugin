# Jalur review article (narrative review dan scoping review)

Dipakai bila paper adalah artikel review yang **bukan** systematic review. Polanya sama dengan jalur guideline (`jalur-guideline.md`): isi terlalu luas untuk satu presentasi, sehingga ada peta isi yang harus disetujui user sebelum slide dibuat.

## R0. Klasifikasi (wajib, di intake)

"Review" ada tiga macam dan jalurnya berbeda. Tentukan dari bagian Metode, bukan dari judul.

| Jenis | Tanda | Jalur | Tool |
|---|---|---|---|
| Systematic review (dengan atau tanpa meta-analisis) | pertanyaan terfokus, penelusuran sistematis terdokumentasi, kriteria inklusi, penilaian risiko bias, biasanya PRISMA dan registrasi | jalur SR-MA di SKILL.md | AMSTAR 2 |
| Scoping review | memetakan luas bukti, penelusuran sistematis, tanpa penilaian risiko bias wajib, biasanya PRISMA-ScR atau kerangka JBI/Arksey-O'Malley | jalur ini | kelengkapan pelaporan PRISMA-ScR (bukan skor kualitas) |
| Narrative review (termasuk state-of-the-art, clinical review, seminar, update) | topik luas, penulis ahli, metode penelusuran tidak ada atau ringkas | jalur ini | SANRA |

Bila paper menyebut dirinya "systematic" tetapi tidak punya penelusuran terdokumentasi dan kriteria inklusi, perlakukan sebagai narrative review dan jadikan ketidaksesuaian label itu temuan appraisal. Umbrella review dan review of reviews: di luar cakupan jalur ini, sampaikan ke user.

## R1. Ekstraksi

Tulis ke `extract.md`:

- Identitas: judul, penulis dan afiliasi, jurnal, tahun;vol(no):hal, DOI, jenis artikel menurut jurnal (invited/commissioned?), pendanaan dan COI.
- Tujuan atau pertanyaan review persis seperti ditulis. Bila tidak dinyatakan, tulis "tidak dinyatakan".
- Metode: basis data, kata kunci, rentang tanggal, kriteria pemilihan, jumlah sumber. Bila tidak ada bagian metode, tulis "tidak dilaporkan" (ini bahan appraisal, bukan untuk ditebak).
- Jumlah referensi dan gambaran jenisnya (RCT, observasional, guideline, review lain, opini), bila bisa dihitung dari daftar pustaka.
- Figur/tabel ringkasan kunci dan lokasinya.

## R2. Peta isi (wajib, sebelum appraisal dan slide)

Buat `peta-isi.md` yang memuat **semua** bagian review dengan klaim kuncinya.

```
## Ringkasan
Total: 9 bagian, 31 klaim kunci, 142 referensi.
| Bagian | Judul | Jumlah klaim | Usulan masuk |

## Bagian 3 <judul bagian persis>
| ID | Klaim kunci (ringkas, maks 25 kata) | Bukti yang dikutip penulis | Jenis bukti | Hal. | Usulan | Alasan usulan |
| 3-1 | ... | ref 12, 13 | 2 RCT | 4 | masuk | menjawab kasus pemicu |
| 3-2 | ... | tanpa sitasi | opini penulis | 5 | lewati | di luar fokus |
```

Aturan pengisian:

- **Klaim kunci** = pernyataan yang bisa benar atau salah dan relevan secara klinis (angka epidemiologi, efek terapi, rekomendasi praktis, mekanisme yang dipakai untuk membenarkan terapi). Bukan kalimat pengantar.
- **Jenis bukti** dibaca dari daftar pustaka (judul dan jurnal referensi). Bila tidak bisa ditentukan dari situ, tulis "belum dicek". Klaim tanpa sitasi ditulis "tanpa sitasi".
- Bahasa kekuatan ("terbukti", "mungkin", "diduga") harus setia pada penulis.
- **Usulan** hanyalah saran awal. Dasarnya: fokus dan kasus pemicu dari intake, klaim yang mengubah praktik, dan klaim yang buktinya tampak lemah (bagus untuk appraisal).
- Peta juga memuat **tema** (ID `T-<nomor bagian>`: bagian yang layak dibahas naratif) dan **figur/tabel** penting. Review article umumnya lebih cocok dibawakan tematik: tema yang disetujui memakai halaman 32 (Pembahasan tematik), figur memakai halaman 33 (Figur & pembahasan), lalu klaim yang perlu ditelaah buktinya dirangkum di halaman 30. Tiap poin di slide tematik tetap harus punya halaman/sumber, dan klaim klinis di dalamnya tetap melewati cek sitasi (R3).
- Muatan realistis presentasi 30 menit: 6 sampai 10 klaim, sekitar 3 sampai 4 per slide.

### Gerbang persetujuan

Sama dengan guideline: **berhenti dan serahkan peta ke user**. User menjawab per bagian, per ID, atau "pakai usulan"; boleh menolak usulan atau menambah. Tanyakan siapa yang menyetujui (idealnya PPDS atau konsulennya). Catat di kolom Keputusan pada `peta-isi.md` dan di `brief.json` pada `meta.poin_disetujui`, mis. "dr. Ani (PPDS), 12 November 2026, 8 dari 31 klaim". `build_brief.py` menolak mode review tanpa field ini. Hanya klaim berstatus "masuk" yang boleh muncul di slide; bagian lain diringkas 1 baris di `paper.tidak_dipresentasikan`.

## R3. Cek sitasi klaim terpilih

Ini pengganti "hitung ulang" dan biasanya menghasilkan temuan appraisal terkuat.

Untuk tiap klaim yang disetujui, buka 1 sampai 2 sumber primer yang dikutip (minimal abstrak di PubMed; full text bila angka dipakai di slide) dan catat di `extract.md`:

- Desain, n, populasi, dan hasil sumber itu dengan angka.
- Vonis: **sesuai** / **dilebihkan** (klaim lebih kuat dari sumber) / **tidak sesuai** / **sumber sekunder** (yang dikutip review lain, bukan studi asli) / **tidak bisa diakses** (tandai `[CEK]`).
- Kekuatan bukti menurut penyaji: kuat (SR/RCT konsisten), sedang (RCT tunggal atau observasional besar), lemah (seri kasus, mekanistik, opini).

Selain itu:

- Kemutakhiran: tahun referensi termuda, dan apakah ada studi besar atau guideline baru setelah review terbit. Cari di PubMed, jangan dari ingatan; yang belum terverifikasi masuk `cek_ulang`.
- Pembanding: guideline atau PNPK yang berlaku untuk klaim terpilih. Hanya yang benar-benar dibaca.

`effect_calc.py` hanya dipakai bila angka mentah diambil dari sumber primer yang sudah dibuka.

## R4. Appraisal

### Narrative review: SANRA

6 item, tiap item 0 sampai 2, total 0 sampai 12 (Baethge C, Goldbeck-Wood S, Mertens S. Res Integr Peer Rev. 2019;4:5).

| Item | Yang dinilai |
|---|---|
| 1. Justifikasi pentingnya artikel bagi pembaca | alasan topik ini perlu direview dinyatakan jelas |
| 2. Tujuan atau pertanyaan konkret | tujuan/pertanyaan dirumuskan |
| 3. Deskripsi penelusuran literatur | basis data, kata kunci, rentang waktu, kriteria |
| 4. Referensi | pernyataan kunci didukung sitasi |
| 5. Penalaran ilmiah | jenis bukti disebut dan ditimbang (mis. RCT vs observasional) |
| 6. Penyajian data yang tepat | data hasil disajikan dengan ukuran efek dan CI, bukan hanya "signifikan" |

- SANRA tidak punya ambang resmi. Laporkan skor per item dan total, sebut item terlemah.
- SANRA menilai kualitas penulisan review, bukan kebenaran tiap klaim. Kebenaran isi dinilai lewat R3.
- Skor dari satu penilai: tulis sebagai keterbatasan.

### Scoping review: PRISMA-ScR

PRISMA-ScR (Tricco AC, et al. Ann Intern Med. 2018;169:467-73) adalah pedoman **pelaporan** dengan 20 item wajib dan 2 opsional, bukan alat ukur kualitas. Jangan dijumlah menjadi skor kualitas. Sajikan 6 aspek berikut dengan penilaian dilaporkan / sebagian / tidak dilaporkan + bukti halaman:

1. Protokol dan registrasi.
2. Kriteria kelayakan dan sumber informasi.
3. Strategi penelusuran lengkap (minimal 1 basis data).
4. Seleksi sumber dan proses charting data (berapa penelaah).
5. Hasil: alur seleksi dan karakteristik sumber.
6. Keterbatasan dan pendanaan.

Sebutkan kepada audiens bahwa scoping review memetakan bukti dan tidak dirancang untuk menjawab efektivitas, sehingga tidak boleh dipakai sebagai dasar tunggal mengubah terapi.

### Di brief.json

`appraisal.validity` berisi baris per item SANRA (`penilaian`: "2/2", "1/2", "0/2") atau per aspek PRISMA-ScR ("dilaporkan", "sebagian", "tidak dilaporkan"), dengan `kelas` ("ok" / "mid" / "bad"). `appraisal.grade` dikosongkan. `appraisal.importance` berisi dampak klinis klaim terpilih; `appraisal.applicability` berisi penerapan di RS Indonesia.

## R5. Susunan slide

| Urutan | Halaman master | Isi untuk review |
|---|---|---|
| 1 | 2 Cover | sama |
| 2 | 3 Identitas | desain: "Narrative review" / "Scoping review"; registrasi: sesuai paper atau "tidak ada" |
| 3 | 4 Alasan memilih | sama |
| 4 | 5 Latar belakang | masalah klinis, apa yang belum jelas, tujuan review persis |
| 5 | 25 Ruang lingkup & metodologi | cakupan topik, penulis, penelusuran literatur, jumlah dan jenis sumber, pendanaan dan COI |
| 5b | 32 Pembahasan tematik, 33 Figur & pembahasan (digandakan) | isi utama untuk review yang naratif: satu tema atau bagian per slide 32, satu figur/tabel per slide 33 |
| 6 | 30 Poin kunci review (digandakan) | tabel: klaim, bukti pendukung, kekuatan bukti, cek sitasi; 3 sampai 4 baris per slide, per bagian |
| 7 | 12 Figur kunci | figur/tabel ringkasan dari review + sumber |
| 8 | 27 Perbandingan | guideline, PNPK, review lain |
| 9 | 31 Validity review | SANRA (6 item) atau PRISMA-ScR (6 aspek) |
| 10 | 29 Penerapan di RS setempat | yang sudah sesuai praktik, yang belum beserta hambatannya, dan langkah realistis |
| 11 | 18 Kekuatan & kelemahan | kelemahan mencakup item terlemah dan hasil cek sitasi |
| 12 | 20, 21, 22, 23 | sama |

Halaman 6 sampai 11, 13 sampai 17, 19, 26, dan 28 tidak dipakai. Rincian placeholder halaman 25 sampai 33 ada di `template-map.md`.

## R6. Pertanyaan konsulen khas review

Minimal 6 masuk ke mockup, dengan jawaban spesifik paper.

1. Ini narrative review, scoping review, atau systematic review? Bagaimana Anda tahu?
2. Kenapa memilih narrative review, bukan systematic review atau RCT-nya langsung?
3. Bagaimana penulis memilih literaturnya? Ada kemungkinan memilih yang mendukung pendapatnya saja?
4. Klaim X dasarnya studi apa? Anda sudah baca studi aslinya? Hasilnya berapa?
5. Klaim mana yang hanya opini ahli?
6. Level of evidence artikel ini berapa? Bisa dipakai mengubah praktik?
7. Anda menilai dengan apa? Kenapa bukan AMSTAR 2?
8. Penulisnya siapa, ahli di bidang ini? Ada hubungan dengan industri?
9. Referensinya sampai tahun berapa? Ada studi baru sesudahnya?
10. Sesuai dengan guideline atau PNPK kita? Bila berbeda, ikut yang mana?
11. Kenapa hanya membahas bagian ini? (jawab: pilihan disepakati bersama pembimbing, lalu ringkas bagian lain)
12. (Scoping) Kenapa tidak ada penilaian risiko bias dan tidak ada meta-analisis?

Jebakan yang harus dijawab jujur: klaim tanpa sitasi, sumber yang belum sempat dibuka, dan angka yang hanya ada di review tanpa sumber primer.

## Checklist tambahan (masuk ke brief)

- Buka sumber primer tiap klaim terpilih dan cocokkan angkanya.
- Siapkan penjelasan beda narrative, scoping, dan systematic review dalam 30 detik.
- Cek profil penulis utama dan pernyataan COI.
- Cari 1 systematic review atau guideline terbaru untuk topik yang sama sebagai pembanding.
- Baca ringkasan 1 baris bagian yang tidak dipresentasikan.
