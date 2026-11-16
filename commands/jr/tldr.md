---
description: JR tahap 5c-6: rangkuman TLDR dan serah terima folder order
---

Semua path `scripts/`, `references/`, `assets/` di bawah relatif ke `.claude/skills/journal-reading-builder/`. Jalankan script dari folder itu atau pakai path lengkapnya. Aturan umum (bahasa Indonesia akademik, tanpa em dash, desimal koma, anti-halusinasi) dan daftar kesalahan umum ada di `/jr:salah`.

## Langkah 5c. Rangkuman TLDR (TXT)

Dikerjakan paling akhir, setelah slide, brief, skrip, dan audio final, karena TLDR merangkum semuanya dan harus memakai angka yang identik. Satu berkas teks biasa (`tldr-jurnal-reading.txt`, bukan `.md`), tanpa format markdown (tanpa `#`, `**`, atau tabel), supaya bisa ditempel ke WhatsApp, email, atau dibacakan.

Isi, dalam bahasa Indonesia tanpa em dash, **maksimal 2 menit** dibaca atau didengar (sekitar 250 kata pada 130 kata per menit; hitung dengan `wc -w`, jangan melebihi 260), urutan tetap. Bila terlalu panjang, ringkas butir 3, 4, dan 8 dulu, bukan membuang butir 5 (take-home message):

1. Judul: penyaji, judul paper, jurnal dan tahun, DOI, tanggal presentasi.
2. Pertanyaan penelitian dan desain studi (1 sampai 2 kalimat).
3. Hasil utama: 3 sampai 5 butir berangka (n/N, persen, ukuran efek dengan 95% CI, p), angka yang sama dengan slide.
4. Appraisal: tool yang dipakai, skor atau penilaian, dan GRADE atau level evidence; 3 kelemahan utama termasuk temuan penyaji.
5. Kesimpulan penyaji dan take-home message (satu kalimat).
6. Applicability dan, bila diminta fokus konsulen, jawaban singkatnya (mis. penerapan di Indonesia, strategi daerah).
7. Audio: jumlah file, durasi total (dari `audio/daftar-audio.txt`), suara yang dipakai, dan bahasa audio; satu kalimat bahwa audio dibacakan dari `skrip-presentasi.txt` dan belum didengarkan oleh pembuat.
8. Hal yang harus dicek PPDS (isi `cek_ulang`, versi ringkas).
9. Tautan: Canva (edit dan view) serta daftar nama file di folder.

Aturan: jangan menambah angka atau klaim yang tidak ada di `extract.md`, skrip, atau brief; salin dari sumber yang sama. Jangan memuat identitas pasien. Jangan membuat berkas TLDR terpisah untuk audio; rangkuman audio cukup butir 7.

## Langkah 6. Serahkan

Folder output order (mis. `JR-<nama>-<penulis><tahun>/`) berisi:
- `tautan-canva.txt` berisi tautan desain (slide tidak diekspor; tim mengekspor PPTX atau PDF sendiri dari Canva)
- `brief-....docx`
- `brief-....html`
- `skrip-presentasi.txt` dan `skrip-presentasi-tanpa-penanda.txt`
- `audio/` berisi audio latihan per slide dan `latihan-lengkap.mp3`
- `tldr-jurnal-reading.txt` (rangkuman TLDR, Langkah 5c)
- `extract.md` (arsip internal)

Laporkan ke user secara singkat:

- Link edit desain Canva. Untuk dibagikan ke PPDS, pakai link view publik dan minta PPDS memakai File, lalu Make a copy.
- Daftar file.
- Desain studi dan tool yang dipakai.
- Kesimpulan appraisal 1 kalimat.
- Semua item `cek_ulang`. Ini wajib disampaikan, karena PPDS yang harus memverifikasinya.
- Hal yang diasumsikan, misalnya kasus pemicu atau risiko dasar lokal.
- Untuk guideline: siapa yang menyetujui pilihan rekomendasi, berapa yang masuk dari total, dan bahwa skor AGREE II berasal dari satu penilai. Sertakan `peta-rekomendasi.md` di folder output.
- Untuk review article: jenis review dan dasarnya, siapa yang menyetujui pilihan klaim, hasil cek sitasi (berapa sesuai, dilebihkan, tidak bisa diakses), dan `peta-isi.md` di folder output.
