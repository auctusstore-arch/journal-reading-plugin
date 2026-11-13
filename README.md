# journal-reading-plugin

Plugin internal Auctus untuk membuat paket journal reading PPDS dari satu paper.

## Isi

- `skills/journal-reading-builder/`: skill beserta rujukan, script, dan aset (ikon, contoh brief).
- `TEMPLATE-CANVA.md`: tautan tiga master template Canva dan peta halamannya.
- `.claude-plugin/plugin.json`: manifest plugin.

## Keluaran skill

1. Desain Canva terisi penuh (tautan; slide tidak diekspor ke PPTX atau PDF).
2. Brief & Checklist Persiapan dalam DOCX.
3. Brief & Checklist Persiapan dalam HTML.
4. Skrip presentasi TXT siap TTS.
5. Audio latihan per slide (MP3, Edge TTS).

## Jalur

- Studi primer dan SR-MA.
- Guideline, konsensus, PNPK (PDF wajib; rekomendasi dipilih pemesan lewat peta rekomendasi).
- Review article non-sistematis (narrative, scoping).

## Pemasangan

Repo ini privat, jadi akun GitHub di mesin tersebut harus punya akses.

```
/plugin marketplace add auctusstore-arch/journal-reading-plugin
/plugin install journal-reading-plugin@auctus-journal-reading
```

Setelah terpasang, skill muncul sebagai `journal-reading-plugin:journal-reading-builder`. Untuk mencoba tanpa memasang: `claude --plugin-dir <folder repo ini>`.

## Prasyarat

- Koneksi MCP Canva dengan akses ke tiga master template.
- `uv` untuk menjalankan script Python (`uv run python3 ...`).
- Formulir intake lengkap sebelum pengerjaan dimulai (lihat Langkah 1 di `SKILL.md`).

## Catatan

- Jalur review article belum diuji dengan paper nyata.
- Audio dibuat lewat layanan Microsoft Edge TTS; skrip tidak boleh memuat identitas pasien.
