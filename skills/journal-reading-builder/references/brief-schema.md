# Skema brief.json

Satu file JSON menghasilkan DOCX dan HTML lewat `scripts/build_brief.py`. Contoh lengkap yang lolos cek: `brief-example.json` (paper latihan fiktif probiotik). Salin strukturnya, ganti isinya.

## Target ukuran ("sedang")

| Bagian | Target |
|---|---|
| Total | 2.200 sampai 4.000 kata (script memberi peringatan di luar rentang) |
| ringkasan | 1 paragraf, 90 sampai 150 kata |
| konteks | 3 sampai 4 poin per sub-bagian + 5 sampai 8 istilah |
| validity | semua domain tool appraisal, tiap domain ada bukti halaman/tabel |
| pertanyaan | 12 sampai 16, jawaban 2 sampai 4 kalimat |
| checklist | 16 sampai 24 item dalam 4 kelompok waktu |

Semua teks berbahasa Indonesia, tanpa em dash. Desimal pakai koma (8,0%) supaya sama dengan slide.

## Field

```
meta:
  judul_paper      judul lengkap persis seperti di jurnal
  sitasi           Vancouver singkat + doi
  penyaji, prodi, departemen, pembimbing, tanggal   dari intake; kosongkan bila tidak diketahui
  durasi_menit     angka
  desain_studi     mis. "RCT paralel, double-blind, 3 RS"
  tool_appraisal   "Cochrane RoB 2" | "Newcastle-Ottawa Scale" | "QUADAS-2" | "AMSTAR 2" | lainnya
  warna            "navy" | "maroon" | "hijau" (samakan dengan slide)
  nama_file        nama file output tanpa ekstensi, mis. "brief-jr-dr-ani-probiotik"
ringkasan          paragraf: pertanyaan penelitian, desain, hasil utama dengan angka, masalah appraisal utama, kesimpulan penyaji
bottom_line        take-home message 1 kalimat, maks 30 kata (sama dengan slide Kesimpulan)
konteks:
  penyakit         [poin] definisi, epidemiologi, beban, faktor risiko
  standar_terapi   [poin] tata laksana saat ini, posisi guideline / PNPK, gap
  mekanisme        [poin] patofisiologi / farmakologi / dasar tes yang perlu dikuasai untuk menjawab konsulen
  istilah          [{istilah, arti}] istilah metodologi & klinis yang pasti muncul
paper:
  pico             {P, I, C, O}  (diagnostik: P, I = index test, C = reference standard, O = target condition)
  desain           [poin] desain, setting, randomisasi/sampling, sampel, analisis, registrasi, pendanaan
  hasil            [{outcome, intervensi, kontrol, efek, catatan}] angka persis dari paper
  angka_kunci      [poin] hasil hitung ulang effect_calc.py + NNT lokal
appraisal:
  validity         [{kelompok, domain, penilaian, kelas, bukti, alasan}] SATU BARIS PER ITEM instrumen, bukan per domain (lihat "Appraisal berbasis instrumen" di bawah).
                   domain = nama item; kelompok = domain induknya (opsional, mis. "Selection"); penilaian memakai istilah tool (Low/Some concerns/High, bintang NOS, Yes/Partial/No);
                   kelas ok|mid|bad; bukti = apa yang tertulis di paper + lokasi; alasan = MENGAPA dinilai demikian
  validity_overall kalimat kesimpulan + arah bias
  importance       [poin]
  applicability    [poin] pasien, sumber daya RS, Fornas/JKN, preferensi pasien
  grade            {outcome, rating, alasan}
kekuatan           [3 poin spesifik paper]
kelemahan          [3 poin; minimal 1 temuan penyaji yang tidak diakui penulis]
rencana_presentasi [{slide, pesan, menit}] mengikuti urutan slide yang benar-benar dibuat
pertanyaan         [{kategori, pertanyaan, jawaban}] kategori: Pemilihan, PICO, Metode, Statistik, Appraisal, Applicability, Kesimpulan, Dasar ilmu, Jebakan
checklist          [{waktu, items[]}] kelompok: H-7 sampai H-5, H-4 sampai H-3, H-2 sampai H-1, H-0 (sesuaikan bila jadwal lebih dekat)
cek_ulang          [poin] semua hal bertanda [CEK] di slide atau brief
referensi          [string] paper yang ditelaah nomor 1, lalu guideline & tool appraisal
```

## Varian guideline

Bila paper adalah guideline (lihat `jalur-guideline.md`), `paper.pico` dan `paper.hasil` diganti field di bawah. Adanya `paper.rekomendasi` mengaktifkan mode guideline di `build_brief.py`.

```
meta:
  desain_studi            "Clinical practice guideline (AHA/ASA)" atau sejenis
  tool_appraisal          "AGREE II (satu penilai)"
  rekomendasi_disetujui   WAJIB. Siapa yang menyetujui pilihan rekomendasi, kapan, berapa dari total.
                          mis. "dr. Ani (PPDS), 12 November 2026, 8 dari 137 rekomendasi"
paper:
  ruang_lingkup           [poin] populasi/kondisi yang dicakup dan dikecualikan, pengguna sasaran
  desain                  [poin] metodologi penyusunan: panel, penelusuran bukti + batas tanggal, sistem kelas/level, konsensus, telaah eksternal, pendanaan, COI
  rekomendasi             [{no, bagian, teks, cor, loe, bukti, status, catatan}]
                          hanya yang disetujui di peta rekomendasi. no = ID di peta; cor/loe persis sistem guideline;
                          bukti = studi dasar + angka + halaman; status = baru / berubah / tetap / tidak ditandai
  perbandingan_edisi      [{topik, jenis, lama, baru}] WAJIB. Perbandingan dengan edisi sebelumnya dari organisasi yang sama.
                          jenis: baru / diubah / dihapus. lama dan baru memuat bunyi rekomendasi + kelas, level, halaman.
                          Boleh kosong hanya bila meta.sumber_perbandingan diawali "edisi pertama".
  perbandingan            [{topik, guideline_ini, pembanding, catatan}] PNPK dan guideline organisasi lain (opsional; hanya sumber yang benar-benar dibaca)
  meta.sumber_perbandingan  WAJIB. Dari mana perbandingan edisi diambil: "Tabel What is New, hal. e12-e14" atau
                          "PDF edisi 2015 dilampirkan pemesan (Hemphill et al., Stroke 2015)" atau "edisi pertama, tidak ada edisi sebelumnya".
  tidak_dipresentasikan   [poin] 1 baris per bagian guideline yang tidak masuk slide
  angka_kunci             [poin] angka studi pendukung yang sudah dicek ke paper aslinya (opsional)
appraisal:
  validity                6 baris domain AGREE II: {domain, penilaian: "78%", kelas: "ok"|"mid"|"bad", bukti}
  validity_overall        penilaian keseluruhan (_/7), rekomendasi pemakaian, domain terlemah, catatan satu penilai
  grade                   dikosongkan
```

Field lain sama. `pertanyaan` memakai daftar G6 di `jalur-guideline.md` (kategori tambahan: Metodologi guideline, Bukti dasar, Perbandingan).

## Varian review article

Untuk narrative review dan scoping review (lihat `jalur-review.md`). Adanya `paper.poin_kunci` mengaktifkan mode review.

```
meta:
  desain_studi      "Narrative review" | "Scoping review"
  tool_appraisal    "SANRA (satu penilai)" | "PRISMA-ScR (kelengkapan pelaporan)"
  poin_disetujui    WAJIB. Siapa yang menyetujui pilihan klaim, kapan, berapa dari total.
paper:
  ruang_lingkup           [poin] tujuan/pertanyaan review persis, cakupan topik
  desain                  [poin] metode penelusuran (atau "tidak dilaporkan"), jumlah dan jenis sumber, penulis, pendanaan, COI
  poin_kunci              [{no, bagian, klaim, bukti, kekuatan, cek_sitasi, catatan}]
                          hanya yang disetujui di peta isi. bukti = sumber yang dikutip + angka dari sumber primer;
                          kekuatan = kuat / sedang / lemah; cek_sitasi = sesuai / dilebihkan / tidak sesuai / sumber sekunder / tidak bisa diakses
  perbandingan            [{topik, review_ini, pembanding, catatan}] guideline, PNPK, review lain
  tidak_dipresentasikan   [poin] 1 baris per bagian yang tidak masuk slide
  angka_kunci             [poin] angka dari sumber primer yang sudah dibuka (opsional)
appraisal:
  validity                SANRA: 6 baris {domain, penilaian: "1/2", kelas, bukti}; PRISMA-ScR: 6 aspek {domain, penilaian: "sebagian", kelas, bukti}
  validity_overall        total SANRA (_/12) atau ringkasan pelaporan, item terlemah, catatan satu penilai
  grade                   dikosongkan
```

`pertanyaan` memakai daftar R6 di `jalur-review.md` (kategori tambahan: Jenis review, Bukti dasar, Perbandingan).

Penanda `[CEK ...]` boleh muncul di dalam teks brief untuk data yang tidak pasti, tetapi setiap penanda wajib juga tercantum di `cek_ulang`, supaya PPDS tahu apa yang harus diverifikasi.


## Appraisal berbasis instrumen (NOS, AGREE II, AMSTAR 2, QUADAS-2, RoB 2, SANRA, PRISMA-ScR)

Wajib dan dicek `build_brief.py` (exit dengan MASALAH bila dilanggar):

- **Satu baris per item**, bukan ringkasan per domain. Contoh NOS: Selection punya 4 item, Comparability 1, Outcome 3, masing-masing satu baris dengan `kelompok` = nama domainnya. Minimum baris: NOS 7, AMSTAR 2 16, AGREE II 23 (boleh ditambah baris skor domain), SANRA 6, PRISMA-ScR 6. QUADAS-2 (11 signalling question) dan RoB 2 (sekitar 20 pertanyaan penuntun) memberi peringatan bila kurang. Baris penilaian domain boleh ditambah di akhir tiap kelompok dengan `"rangkuman": true` (tidak perlu lokasi, tetap perlu `alasan`).
- `bukti`: apa yang tertulis di paper, dengan lokasi (hal./Tabel/Figure/Metode), atau "tidak dilaporkan". Itu bukti, bukan alasan.
- `alasan` (min 8 kata): MENGAPA bukti itu menghasilkan penilaian tersebut. Hubungkan bukti dengan kriteria item di instrumen (mis. "NOS item Representativeness memberi bintang bila sampel mewakili populasi sasaran; sampel hanya dari satu RS rujukan, jadi tidak diberi bintang"). Untuk item yang kena batasan aturan resmi, sebut aturannya. Jangan mengulang bukti, jangan "sesuai kriteria".
- Penilaian "tidak ada informasi" atau tidak diberi bintang karena paper diam harus dinyatakan begitu di `alasan`, bukan ditulis seolah paper salah.
