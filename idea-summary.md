# AI Farm Risk Simulator — Idea Summary

## One-Liner

> "Petani Indonesia kehilangan 1.2 juta ton beras karena salah waktu tanam. Kita kasih mereka crystal ball — prediksi cuaca + harga sebelum benih masuk tanah."

---

## Apa Ini

AI-powered decision support tool yang membantu petani kecil-menengah **mempertimbangkan risiko sebelum mulai menanam.**

Sekarang petani ambil keputusan tanam pakai feeling + pengalaman pribadi. App ini kasih mereka data — kayak financial advisor tapi buat pertanian.

---

## Yang App Lakukan

Petani buka app → pilih lokasi, komoditas, bulan tanam → app kasih:

1. **Prediksi harga saat panen** — "Kalau lo tanam sekarang, November nanti beras di daerah lo kemungkinan Rp 13.400/kg"
2. **Weather risk score** — "Cuaca bulan ini 65/100 (MEDIUM) — curah hujan di bawah normal, ada risiko kekeringan"
3. **Rekomendasi** — "Tanam sekarang (profit +4%)" atau "Tunda 2 minggu" atau "Pertimbangkan komoditas lain"

---

## Intinya

Simulasi yang kasi tau petani: **kalau dia tanam di bulan ini, di lokasi ini, pertimbangannya gimana** — dari sisi cuaca dan harga.

Bukan suruh mereka ngapain. Tapi kasih informasi supaya keputusan mereka lebih informed, bukan pure gambling.

---

## Kenapa Ini Penting

- Petani sekarang: tanam → berdoa → panen → baru tau harga jatuh
- Dengan app: cek dulu → tau risikonya → decide → tanam dengan percaya diri

Dari "reactive" (tau setelah rugi) ke "proactive" (tau sebelum mulai).

---

## Fitur Wow (Pembeda di Demo)

### 1. What-If Slider

Petani geser slider bulan tanam — grafik dan angka berubah real-time:

```
Tanam Juli:      Harga panen Rp 13.400 | Risk: 65 (MEDIUM) ⚠️
Tanam Agustus:   Harga panen Rp 14.100 | Risk: 45 (LOW) ✅  ← sweet spot
Tanam September: Harga panen Rp 12.800 | Risk: 70 (HIGH) 🔴
```

Petani bisa "main-main" explore sendiri — cari waktu tanam terbaik. Bukan cuma 1 jawaban statis, tapi simulasi interaktif.

**Kenapa ini wow:** Judges bisa langsung coba sendiri. Interactive > static.

---

### 2. Historical Playback — "Proof of Value"

Tunjukin ke judges: "Kalau app ini udah ada di 2023 sebelum El Niño, ini yang bakal petani lihat:"

```
📅 Mei 2023 — App bilang:
⚠️ WARNING: Curah hujan 60% di bawah normal.
   Risk score: 85/100 (HIGH)
💡 "Tunda tanam sampai curah hujan naik, atau siapkan irigasi."

📅 Realita (Agustus 2023):
❌ El Niño → Indonesia kehilangan 1.2 juta ton beras
❌ Harga beras naik signifikan
❌ Petani yang sudah terlanjur tanam → rugi besar

→ Petani yang dengar warning ini bisa:
  ✅ Tunda tanam
  ✅ Siapkan irigasi
  ✅ Switch ke komoditas yang lebih drought-resistant
```

**Kenapa ini wow:** Bukan janji masa depan — ini proof pakai data yang UDAH terjadi. Judges bisa verify sendiri. Storytelling kuat.

---

## Summary Fitur Lengkap

| Fitur | Fungsi | Wow Level |
|-------|--------|-----------|
| Prediksi harga panen | Kasih angka Rp/kg | Core |
| Weather risk score | 0-100, level LOW/MED/HIGH | Core |
| Rekomendasi aksi | Tanam / tunda / switch komoditas | Core |
| **What-if slider** | Explore berbagai bulan tanam interaktif | **Pembeda** |
| **Historical playback** | Buktikan value app dengan data masa lalu | **Pembeda** |
