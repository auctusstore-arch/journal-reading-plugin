# Katalog visual untuk panduan tutor Zoom

Visual hanya dibuat bila tutor atau user menyetujuinya. Skill memetakan kandidat dari gap klien, mengusulkannya, menunggu jawaban, baru mengeksekusi.

## Alur (Z4a, sebelum menulis `tutor.json`)

1. Baca prioritas, soal cek yang salah, kebutuhan klien (mis. "jelaskan kurva plot"), dan jenis paper.
2. Cocokkan dengan kolom "Pemicu" di bawah. Ambil paling banyak 3 kandidat; buang yang tidak relevan dengan paper atau gap.
3. **Tanyakan dulu** dengan AskUserQuestion (multiSelect). Tiap opsi memuat nama visual dan alasan satu kalimat yang merujuk ke gap klien. Selalu sertakan opsi "Tidak perlu visual". Jangan membuat visual sebelum ada jawaban.
4. Eksekusi hanya yang dipilih:
   - Status `tersedia`: isi `visual` di `tutor.json` dengan id-nya; `build_tutor_guide.py` menyisipkan lampiran.
   - Status `kandidat`: buat dengan data sintetis atau angka paper, mandiri tanpa CDN (SVG dan JavaScript biasa), lalu daftarkan sebagai id baru di `VISUALS` pada `build_tutor_guide.py` dan di tabel ini bila akan dipakai ulang. Bila hanya sekali pakai, tawarkan menyimpannya sebagai file terpisah di folder order.
5. Catat di `meta.sumber` visual apa yang diminta dan disetujui oleh siapa.

Aturan isi: data sintetis harus diberi label sintetis; angka dari paper harus identik dengan `extract.md`; tanpa em dash; satu visual satu konsep.

## Katalog

| id | Status | Pemicu (gap atau permintaan) | Isi |
|---|---|---|---|
| `korelasi_icc_ba` | tersedia | Soal Bland-Altman, ICC, atau korelasi salah; klien meminta menjelaskan plot atau tabel kesepakatan; paper perbandingan metode atau akurasi diagnostik kuantitatif | Empat skenario (sepakat, bias konstan, bias proporsional, banyak error) dengan scatterplot, Bland-Altman, r, ICC, beda rerata, LoA |
| `prevalensi_ppv_npv` | kandidat | Soal PPV, NPV, atau prevalensi salah; klien menyebut PPV/NPV sebagai sifat alat; paper akurasi diagnostik | Slider prevalensi dan tabel 2x2 untuk 1000 orang; sensitivitas dan spesifisitas tetap, PPV dan NPV berubah |
| `roc_cutoff` | kandidat | Sensitivitas dan spesifisitas tertukar; klien lemah membaca AUC atau cut-off; paper dengan ambang diagnostik | Slider cut-off pada dua distribusi (sehat dan sakit), kurva ROC ikut bergerak |
| `rr_or_nnt` | kandidat | Soal RR, OR, ARR, atau NNT salah; paper RCT atau kohort | Ikon 100 orang dua kelompok; RR, ARR, NNT dihitung dari kejadian |
| `forest_plot_i2` | kandidat | Klien lemah membaca forest plot atau heterogenitas; paper SR-MA | Forest plot sintetis dengan tombol heterogenitas rendah dan tinggi, I2 dan model efek |
| `km_hr` | kandidat | Soal HR atau median survival salah; paper survival | Dua kurva Kaplan-Meier dengan HR; beda HR vs risiko absolut |
| `alur_itt_pp` | kandidat | self_desain rendah atau soal ITT vs per protokol salah; paper RCT | Diagram alur CONSORT dengan toggle ITT dan per protokol |

Kandidat yang pernah dibuat dan dipakai ulang naik menjadi `tersedia` setelah didaftarkan di `VISUALS`.
