# Kartu Ringkas Statistik untuk Journal Reading
**Kit Jurus Jitu Siap Maju Journal Reading** · Auctus Academy · dr. Muhammad Yusuf

> Semua angka di kartu ini berasal dari **paper latihan FIKTIF** (RCT probiotik untuk mencegah diare terkait antibiotik pada pasien dewasa rawat inap). Angka contoh, bukan data penelitian nyata.
>
> Semua hitungan di kartu ini bisa dikerjakan otomatis di `journal-reading-helper.html` (nomor tab disebut di tiap bagian).

**Daftar isi:** 1 Jenis data · 2 Proporsi · 3 Mean ± SD vs median (IQR) · 4 Mean difference · 5 Tabel 2×2 · 6 Ukuran efek biner · 7 Confidence interval & p-value · 8 Memilih uji statistik · 9 Uji diagnostik · 10 Forest plot · 11 Level of evidence & GRADE · 12 Ringkasan nilai nol-efek · 13 Lima pertanyaan untuk setiap angka

---

## 1. Kenali jenis data dulu

| Jenis data | Contoh | Disajikan sebagai | Ukuran efek antar kelompok |
|---|---|---|---|
| **Kategorik / biner** | diare ya/tidak, meninggal ya/tidak | n/N (%) | RR, OR, ARR, NNT |
| **Numerik, distribusi normal** | tekanan darah, Hb | mean ± SD | mean difference (MD) |
| **Numerik, distribusi miring** | lama rawat, lama diare, biaya | median (IQR) | selisih median, Hodges-Lehmann, atau cukup p dari uji non-parametrik |
| **Waktu sampai kejadian** | waktu sampai meninggal/kambuh | kurva Kaplan-Meier, median survival | HR |

Jenis data outcome menentukan cara penyajian, ukuran efek, **dan** uji statistik (bagian 8).

---

## 2. Proporsi (widget tab 2)

**Proporsi = x / n** (jumlah yang mengalami kejadian ÷ jumlah total di kelompok itu)

| Kelompok | Hitung | Proporsi | 95% CI (Wilson) |
|---|---|---|---|
| Probiotik | 12 / 150 | **8,0%** | 4,6% sampai 13,5% |
| Plasebo | 27 / 150 | **18,0%** | 12,7% sampai 24,9% |

- Di slide, selalu tulis **n/N (%)**, misalnya 12/150 (8%). Persen saja menyembunyikan besar sampel: 8% dari 25 orang jauh kurang pasti dibanding 8% dari 1.000 orang.
- CI proporsi melebar bila n kecil atau proporsi mendekati 0% atau 100%. Metode Wilson lebih tepat daripada rumus Wald (p ± 1,96 × √[p(1-p)/n]) untuk n kecil.
- Prevalensi = proporsi kasus pada satu waktu; insidens kumulatif (risiko) = proporsi kasus baru selama periode follow-up.

---

## 3. Mean ± SD vs median (IQR) (widget tab 3, bagian "Data mentah")

| | **Mean ± SD** | **Median (IQR)** |
|---|---|---|
| Dipakai bila | distribusi simetris / normal | distribusi miring, ada outlier, skala ordinal |
| Pusat data | rata-rata | nilai tengah (persentil 50) |
| Sebaran | SD: rata-rata jarak data dari mean | IQR: Q1 sampai Q3, berisi **50% data di tengah** |
| Uji yang cocok | parametrik (t-test, ANOVA) | non-parametrik (Mann-Whitney, Kruskal-Wallis) |

**Cara menghitung IQR (manual):**
1. Urutkan data dari kecil ke besar.
2. Median (Q2) = nilai tengah. Q1 = median dari separuh bawah (persentil 25). Q3 = median dari separuh atas (persentil 75).
3. IQR ditulis "median (Q1 sampai Q3)" atau "median (IQR Q1-Q3)". Secara teknis IQR = Q3 - Q1, tetapi di paper klinis yang dilaporkan biasanya kedua batasnya.

**Contoh (ANGKA CONTOH):** lama diare (hari) pada 11 pasien yang mengalami diare
`1, 2, 2, 2, 3, 3, 3, 5, 5, 6, 9`
- Median = **3 hari**, Q1 = 2, Q3 = 5 → ditulis **3 (IQR 2 sampai 5) hari**.
- Mean = 3,7 ± 2,3 hari: tertarik ke atas oleh satu pasien 9 hari. Median lebih jujur menggambarkan pasien "tipikal".
- Cara membaca: "setengah pasien diare ≤ 3 hari; separuh pasien di bagian tengah diare antara 2 sampai 5 hari."

**Tanda data kemungkinan miring:**
- SD lebih dari setengah mean pada variabel yang tidak mungkin negatif (lama rawat, biaya, kadar).
- Mean dan median berbeda jauh.
- Penulis melaporkan median (IQR) atau memakai uji non-parametrik.

> Pertanyaan konsulen yang sering: "Kenapa dilaporkan median, bukan mean?" Jawab: distribusinya miring, jadi median dan IQR lebih mewakili; ujinya pun harus non-parametrik.

---

## 4. Mean difference (MD) (widget tab 3, bagian "Dua kelompok")

**MD = mean intervensi - mean kontrol** · nilai nol-efek = **0**

**Contoh (ANGKA CONTOH):** lama rawat inap
| | n | mean ± SD |
|---|---|---|
| Probiotik | 150 | 5,2 ± 1,8 hari |
| Plasebo | 150 | 6,0 ± 2,1 hari |

| Langkah | Rumus | Hasil |
|---|---|---|
| MD | 5,2 - 6,0 | **-0,8 hari** |
| SE | √(SD₁²/n₁ + SD₂²/n₂) = √(1,8²/150 + 2,1²/150) | 0,226 |
| 95% CI | MD ± 1,96 × SE | **-1,24 sampai -0,36 hari** |
| t (Welch) | MD / SE | 3,54 → p < 0,001 |

**Cara membaca:**
- Tanda minus = kelompok intervensi lebih rendah (di sini: rawat inap lebih singkat). Selalu cek arah pengurangan yang dipakai penulis.
- CI tidak memotong 0 → bermakna statistik.
- **Bermakna klinis?** Bandingkan dengan MCID (minimal clinically important difference) atau dampak praktis: 0,8 hari per pasien berarti apa untuk bed occupancy dan biaya RS kita?
- **SMD** (standardized mean difference, mis. Cohen d / Hedges g) dipakai di meta-analisis bila studi memakai skala ukur berbeda. Patokan kasar: 0,2 kecil, 0,5 sedang, 0,8 besar.
- Jangan pakai MD dan t-test untuk data yang jelas miring; lihat bagian 3 dan 8.

---

## 5. Tabel 2×2 (dasar semua hitungan biner) (widget tab 4)

**Untuk studi terapi/etiologi (RCT, kohort, case-control):**

|                          | Outcome (+) | Outcome (-) | Total |
|--------------------------|:-----------:|:-----------:|:-----:|
| Intervensi / Terpapar    | **a**       | **b**       | a + b |
| Kontrol / Tidak terpapar | **c**       | **d**       | c + d |

- **EER** (experimental event rate) = a / (a + b)
- **CER** (control event rate) = c / (c + d)

**Paper latihan:** a = 12, b = 138, c = 27, d = 123.

> Selalu susun tabel dari **jumlah pasien** per kelompok, bukan dari persen. Kalau paper hanya memberi persen, kalikan dengan n kelompok lalu bulatkan.

**Untuk studi diagnostik:**

|                 | Penyakit (+) (reference standard) | Penyakit (-) |
|-----------------|:---------------------------------:|:------------:|
| Tes (+)         | **a** (TP)                        | **b** (FP)   |
| Tes (-)         | **c** (FN)                        | **d** (TN)   |

---

## 6. Ukuran efek untuk outcome biner (widget tab 4)

| Ukuran | Rumus | Cara membaca | Nilai nol-efek |
|---|---|---|---|
| **RR** (risk ratio / relative risk) | EER / CER | Risiko kelompok intervensi = RR × risiko kontrol | 1 |
| **RRR** (relative risk reduction) | 1 - RR = (CER - EER) / CER | "Intervensi menurunkan risiko relatif sebesar ...%" | 0 |
| **ARR** (absolute risk reduction) / RD | CER - EER | Selisih risiko absolut; paling relevan untuk pasien | 0 |
| **NNT** | 1 / ARR (bulatkan **ke atas**) | Jumlah pasien yang perlu diobati agar 1 kejadian tercegah | ∞ |
| **NNH** | 1 / ARI (selisih kejadian efek samping) | Jumlah pasien diobati sampai 1 mengalami harm tambahan | ∞ |
| **OR** (odds ratio) | (a × d) / (b × c) | Rasio odds; ukuran utama case-control & regresi logistik | 1 |
| **HR** (hazard ratio) | Dari Cox regression | Rasio laju kejadian sepanjang follow-up (time-to-event) | 1 |

### Contoh hitung (ANGKA CONTOH)

| Langkah | Hasil |
|---|---|
| EER = 12/150 | 0,080 (8,0%) |
| CER = 27/150 | 0,180 (18,0%) |
| RR = 0,080 / 0,180 | **0,44** (95% CI 0,23 sampai 0,84) |
| RRR = 1 - 0,44 | **56%** |
| ARR = 0,180 - 0,080 | **0,10** (10 poin persentase; 95% CI 0,025 sampai 0,175) |
| NNT = 1 / 0,10 | **10** (95% CI sekitar 6 sampai 40) |
| OR = (12 × 123) / (138 × 27) | **0,40** (95% CI 0,19 sampai 0,82): lebih jauh dari 1 daripada RR karena outcome tidak jarang |
| Chi-square (tanpa koreksi) | χ² = 6,63, **p = 0,010** · Fisher exact p = 0,015 |

> CI NNT = kebalikan dari batas CI ARR (1/0,175 ≈ 6 dan 1/0,025 = 40). Jika CI ARR melewati 0, CI NNT mencakup "NNH ... ∞ ... NNT", jadi tulis dengan hati-hati.

**Catatan penting**
- OR ≈ RR **hanya jika** outcome jarang (aturan praktis < ~10%). Jika outcome sering, OR tampak lebih ekstrem daripada RR; jangan dibaca sebagai RR.
- Case-control **tidak bisa** menghasilkan RR/insidens langsung (jumlah kasus & kontrol ditentukan peneliti) → gunakan OR.
- HR bukan risiko kumulatif; HR 0,70 tidak sama dengan "30% lebih sedikit pasien meninggal". Baca bersama kurva Kaplan-Meier dan angka absolut.
- RRR yang besar bisa berarti ARR yang kecil bila risiko dasar rendah → selalu tampilkan **ARR dan NNT**.
- NNT untuk pasien lokal ≈ 1 / (risiko dasar lokal × RRR). Contoh: risiko dasar di RS kita 5% → ARR ≈ 0,05 × 0,56 = 2,8% → NNT ≈ 36.

---

## 7. Confidence interval (CI) & p-value (widget tab 5)

**95% CI** = rentang nilai efek yang masuk akal (kompatibel dengan data, di bawah asumsi model). Baca tiga hal:
1. **Memotong nilai nol-efek?** (1 untuk rasio; 0 untuk selisih). Jika ya → tidak bermakna statistik pada α 0,05.
2. **Seberapa lebar?** CI lebar = estimasi tidak presisi (sampel/kejadian sedikit) → GRADE: *imprecision*.
3. **Kedua ujungnya bermakna klinis?** Bandingkan ujung CI yang paling tidak menguntungkan dengan MCID. Jika ujung terburuk pun masih bermanfaat → bukti kuat.

**Rumus CI 95% (untuk dicek cepat):**
- RR: exp[ ln(RR) ± 1,96 × SE ], SE = √(1/a - 1/(a+b) + 1/c - 1/(c+d))
- OR: exp[ ln(OR) ± 1,96 × SE ], SE = √(1/a + 1/b + 1/c + 1/d)
- ARR (Wald): ARR ± 1,96 × √[EER(1-EER)/n₁ + CER(1-CER)/n₂]
- MD: MD ± 1,96 × √(SD₁²/n₁ + SD₂²/n₂)

**p-value** = probabilitas mendapatkan data seekstrem ini (atau lebih) **jika H₀ benar** (tidak ada perbedaan).
- p **bukan** probabilitas bahwa H₀ benar, dan **bukan** besar efek. "p = 0,01" tidak berarti "99% benar".
- p < 0,05 tidak sama dengan penting secara klinis; p ≥ 0,05 tidak sama dengan "terbukti tidak ada efek" (absence of evidence is not evidence of absence). Bisa jadi sampel kurang.
- Waspadai banyak outcome sekunder/subgrup tanpa koreksi multiplisitas: makin banyak uji, makin besar peluang p < 0,05 karena kebetulan.
- Utamakan: **besar efek + CI**, baru p-value.

**Mengecek p dari CI yang dilaporkan (metode Altman, widget tab 5):**
- Rasio (RR/OR/HR): SE = [ln(batas atas) - ln(batas bawah)] / (2 × 1,96); z = ln(estimasi) / SE.
- Selisih (MD/ARR): SE = (batas atas - batas bawah) / (2 × 1,96); z = estimasi / SE.
- p ≈ 2 × (1 - Φ(|z|)). Berguna kalau paper hanya melaporkan CI atau p-nya tampak janggal.

---

## 8. Memilih uji statistik (widget tab 6)

Jawab tiga pertanyaan: **(1) jenis data outcome, (2) berapa kelompok, (3) independen atau berpasangan.**

| Outcome | 2 kelompok independen | 2 kelompok berpasangan (sebelum-sesudah, matched) | > 2 kelompok independen |
|---|---|---|---|
| **Kategorik** | Chi-square; **Fisher exact** bila ada sel harapan < 5 | McNemar | Chi-square |
| **Numerik normal** | Independent t-test (Welch bila varians beda) | Paired t-test | One-way ANOVA |
| **Numerik tidak normal / ordinal** | Mann-Whitney U | Wilcoxon signed-rank | Kruskal-Wallis |
| **Waktu sampai kejadian** | Log-rank (Kaplan-Meier) | | Log-rank |

**Hubungan dua variabel:**
- Numerik normal vs numerik: korelasi **Pearson**. Tidak normal/ordinal: **Spearman**.
- Korelasi tidak sama dengan kausalitas, dan r tidak sama dengan besar efek klinis.

**Mengontrol perancu (multivariat):**
| Outcome | Model | Ukuran efek yang keluar |
|---|---|---|
| Biner | Regresi logistik | adjusted OR |
| Numerik | Regresi linear | koefisien β (selisih rata-rata) |
| Waktu sampai kejadian | Regresi Cox | adjusted HR |
| Hitungan/laju | Regresi Poisson / negative binomial | rate ratio |

**Cara mengecek uji di paper:**
1. Baca bagian "Statistical analysis" di Methods: uji apa untuk outcome primer?
2. Cocokkan dengan tabel di atas. Contoh salah kaprah: t-test untuk lama rawat yang dilaporkan median (IQR); chi-square untuk sel berisi 2 pasien; uji independen untuk data sebelum-sesudah.
3. Cek normalitas: apakah penulis menyebut Shapiro-Wilk/Kolmogorov-Smirnov atau melihat histogram?
4. Bila uji tidak sesuai: sebut di slide kelemahan, dan jelaskan dampaknya (p bisa terlalu kecil atau terlalu besar).

**Paper latihan:** outcome diare (biner, 2 kelompok independen, sel tidak kecil) → **chi-square** (p = 0,010). Lama rawat (numerik, kira-kira normal) → **t-test** (p < 0,001). Lama diare (miring, median IQR) → **Mann-Whitney**.

---

## 9. Uji diagnostik (widget tab 7)

| Ukuran | Rumus | Cara membaca |
|---|---|---|
| **Sensitivitas** | a / (a + c) | Proporsi orang sakit yang tesnya positif. Tinggi → **SnNout** (Sensitive, Negative = rule out) |
| **Spesifisitas** | d / (b + d) | Proporsi orang sehat yang tesnya negatif. Tinggi → **SpPin** (Specific, Positive = rule in) |
| **PPV** | a / (a + b) | Peluang sakit bila tes (+). **Bergantung prevalensi** |
| **NPV** | d / (c + d) | Peluang tidak sakit bila tes (-). **Bergantung prevalensi** |
| **LR+** | Sens / (1 - Spes) | Seberapa kuat tes (+) menaikkan peluang penyakit |
| **LR-** | (1 - Sens) / Spes | Seberapa kuat tes (-) menurunkan peluang penyakit |

**Dari pre-test ke post-test probability:**
1. Pre-test odds = p / (1 - p)
2. Post-test odds = pre-test odds × LR
3. Post-test probability = odds / (1 + odds) (atau pakai Fagan nomogram)

Patokan kasar: LR+ > 10 atau LR- < 0,1 → perubahan peluang besar; LR+ 5-10 / LR- 0,1-0,2 → sedang; LR mendekati 1 → tes hampir tidak mengubah peluang.

**Contoh (ANGKA CONTOH):** TP 90, FP 30, FN 10, TN 170 → Sens 90% · Spes 85% · PPV 75% · NPV 94% · LR+ 6,0 · LR- 0,12.
Pre-test 20% → odds 0,25 → × 6 = 1,5 → **post-test 60%**.

---

## 10. Membaca forest plot (meta-analisis)

1. **Satu baris = satu studi**: kotak = estimasi titik (ukuran kotak sebanding bobot), garis horizontal = 95% CI.
2. **Garis vertikal** = nilai nol-efek (1 untuk RR/OR/HR, 0 untuk MD/SMD). Cek label arah: "favours intervention" di kiri atau kanan?
3. **Diamond** = estimasi gabungan; lebar diamond = CI gabungan. Diamond menyentuh garis vertikal → tidak bermakna.
4. **Heterogenitas**: I² (patokan Cochrane Handbook: 0-40% mungkin tidak penting, 30-60% sedang, 50-90% substansial, 75-100% besar; rentangnya sengaja tumpang tindih), uji Q (p), dan tau². Lihat juga visual: apakah CI antar studi saling tumpang tindih?
5. **Model**: fixed-effect vs random-effects. Prediction interval (bila dilaporkan) menunjukkan rentang efek yang mungkin di setting baru.
6. **Cek**: studi berbobot terbesar mendominasi? Ada outlier? Subgrup/sensitivity analysis konsisten?

---

## 11. Level of evidence & GRADE (ringkas)

- **Hierarki desain** (mis. Oxford CEBM Levels of Evidence 2011): SR dari RCT > RCT > kohort > case-control/case series > mechanism-based reasoning. Level bergantung pada **jenis pertanyaan** (terapi, diagnosis, prognosis, harm).
- **GRADE** menilai kepastian bukti **per outcome**:
  - Mulai: RCT = **tinggi**; observasional = **rendah**.
  - Turunkan (-1/-2): risk of bias, inconsistency, indirectness, imprecision, publication bias.
  - Naikkan (observasional): efek besar, dose-response, confounding yang masuk akal justru akan mengecilkan efek.
  - Hasil akhir: **High · Moderate · Low · Very low**.
- **Paper latihan:** RCT (mulai tinggi) → -1 risk of bias (per-protocol, loss tidak seimbang, outcome berbeda dari registrasi) → -1 imprecision (CI lebar, 1 studi) → **low**.

---

## 12. Ringkasan nilai nol-efek (foto bagian ini)

| Nilai nol-efek = **1** | Nilai nol-efek = **0** |
|---|---|
| RR, OR, HR, rasio prevalensi, rate ratio, LR | MD, SMD, ARR / selisih risiko, RRR, koefisien β |

**95% CI memotong angka ini = tidak bermakna statistik.**

---

## 13. Lima pertanyaan cepat untuk setiap angka di slide hasil

1. Ini ukuran **relatif** atau **absolut**? Mana angka absolutnya?
2. **CI**-nya berapa, memotong nilai nol-efek, dan apakah ujungnya bermakna klinis?
3. Outcome ini **primer** atau sekunder/subgrup?
4. Analisis **ITT** atau per-protocol? Uji statistiknya sesuai jenis data?
5. Risiko dasar pasien **kita** berapa? → hitung ulang NNT lokal: NNT ≈ 1 / (risiko dasar lokal × RRR).
