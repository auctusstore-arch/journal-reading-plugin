---
description: JR router: baca paket order dan jalankan urutan tahap yang sesuai
argument-hint: paket-lengkap | asistensi-slide | zoom-1on1 | kelas
---

Paket yang dijual (slug di `src/modules/products/journal-reading-intake.ts`) dan tahap kerjanya. Paket dari argumen: $ARGUMENTS (bila kosong, tanyakan paket order).

| Paket | Urutan tahap | Pintu masuk |
|---|---|---|
| `paket-lengkap` | intake, ekstrak, slide, brief, skrip, tldr, zoom | `/jr:lengkap` |
| `asistensi-slide` | intake, ekstrak, slide, brief, skrip, tldr | `/jr:asistensi` |
| `zoom-1on1` | intake ringan, ekstrak ringan (Z1 di jalur-zoom), zoom | `/jr:zoom-saja` |
| `kelas` | tidak ada kerja skill (akses kelas saja) | - |

Tahap: `/jr:intake`, `/jr:ekstrak`, `/jr:slide`, `/jr:brief`, `/jr:skrip`, `/jr:tldr`, `/jr:zoom`. Aturan umum dan kesalahan umum: `/jr:salah`.

Untuk `kelas`, sampaikan bahwa tidak ada deliverable yang dikerjakan skill. Untuk paket lain, jalankan pintu masuknya.
