# Prompt NotebookLM: audio pembacaan skrip presentasi

Dipakai setelah skrip final (Langkah 5b). Catatan: cara standar membuat audio latihan adalah `scripts/build_audio.py` (Edge TTS, kata demi kata, per slide). NotebookLM hanya alternatif. Tujuannya audio latihan: skrip dibacakan apa adanya, bukan dibahas.

## Cara pakai

1. Buat notebook baru. Unggah **hanya** `skrip-presentasi-tanpa-penanda.txt` sebagai sumber (jangan unggah paper atau brief, supaya isi audio tidak melebar).
2. Studio > Audio Overview > Customize. Pilih bahasa Indonesia dan panjang terpanjang yang tersedia.
3. Tempel prompt di bawah, ganti bagian dalam kurung kurawal, lalu Generate.
4. Dengarkan sambil membuka skrip. Bila ada bagian yang dilewati, diringkas, atau diubah angkanya, buat ulang atau pecah skrip menjadi beberapa notebook per bab.

## Prompt utama

```
Bacakan sumber ini apa adanya sebagai latihan presentasi ilmiah. Ini bukan diskusi dan bukan ringkasan.

Aturan:
- Satu narator saja, sebagai penyaji. Tidak ada pembawa acara kedua, tidak ada tanya jawab, tidak ada komentar.
- Bacakan kata demi kata dari awal sampai akhir, urut, tanpa melewatkan, meringkas, menambah, atau mengubah susunan kalimat.
- Jangan menambah pembuka, penutup, sapaan kepada pendengar, atau kalimat seperti "mari kita bahas".
- Angka, dosis, persentase, kelas rekomendasi, dan level bukti dibacakan persis seperti tertulis.
- Bahasa Indonesia baku. Istilah medis dan nama obat dilafalkan jelas. Singkatan yang sudah dieja dalam teks dibaca seperti tertulis.
- Tempo tenang, sekitar 130 kata per menit, dengan jeda singkat di tiap pergantian paragraf.
- Nada: {dokter residen yang presentasi di depan konsulen: jelas, percaya diri, tidak terburu-buru}.
```

## Versi pendek (bila kolom kustomisasi membatasi panjang)

```
Bacakan sumber ini kata demi kata dari awal sampai akhir sebagai satu narator (penyaji presentasi ilmiah). Bukan diskusi, bukan ringkasan, tanpa pembawa acara kedua, tanpa pembuka, penutup, atau komentar tambahan. Jangan melewatkan atau mengubah kalimat. Angka dan istilah medis dibaca persis seperti tertulis. Bahasa Indonesia baku, tempo tenang, jeda di tiap paragraf.
```

## Batasan yang perlu diketahui

- Audio Overview dirancang sebagai percakapan dua pembawa acara yang merangkum sumber. Prompt di atas mengarahkannya menjadi pembacaan, tetapi NotebookLM **tidak menjamin** pembacaan kata demi kata: ia bisa tetap memakai dua suara, memadatkan, atau mengubah kalimat. Selalu cek hasilnya terhadap skrip.
- Skrip panjang (deck induk, puluhan menit) lebih berisiko dipadatkan. Pecah per bab (satu notebook per file) dan gabungkan audionya.
- Pakai file tanpa penanda. Bila ingin penanda pindah slide ikut terdengar, pakai `skrip-presentasi.txt` dan tambahkan ke prompt: "Baris 'Slide N. Judul.' dibacakan sebagai penanda, diikuti jeda dua detik."
- Bila yang dibutuhkan pembacaan yang benar-benar persis, pakai mesin TTS biasa (teks ke suara) dengan file yang sama; NotebookLM lebih cocok bila penyaji menginginkan suara yang lebih alami dan menerima sedikit perbedaan kalimat.
