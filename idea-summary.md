# AI Farm Risk Simulator — Idea Summary

## One-Liner

> "Petani Indonesia kehilangan 1.2 juta ton beras karena salah waktu tanam. Kita kasih mereka crystal ball — prediksi cuaca + harga sebelum benih masuk tanah."

---

## Problem

### Petani kecil mengambil keputusan tanam secara buta — tanpa data.

Mereka tidak tahu apakah cuaca bulan depan aman, apakah harga saat panen nanti naik atau jatuh, atau apakah ada risiko hama. Hasilnya: salah waktu tanam → gagal panen atau panen saat harga jatuh → rugi.

### Data yang Buktikan Problem Ini

| Fakta | Data | Sumber |
|-------|------|--------|
| Kehilangan beras akibat El Niño 2023 | **1.2 juta ton** | [Tempo — Mentan, Aug 2023](https://en.tempo.co/read/1766490/indonesia-loses-1-2m-tonnes-of-rice-over-el-nino-agriculture-minister-says) |
| Prediksi penurunan produksi beras 2023-2024 | **-3.16% dan -3.75%** | [BioConf ICANARD 2024](https://www.bio-conferences.org/articles/bioconf/abs/2024/38/bioconf_icanard2024_01012/bioconf_icanard2024_01012.html) |
| Dampak per 1°C kenaikan suhu | **-4.500 ton/provinsi/tahun** | [Kompas.id, Oct 2023](https://www.kompas.id/baca/english/2023/10/12/en-faktor-iklim-tekan-produksi-padi) |
| Petani terdampak banjir | **46%** | [PLOS ONE — Kalimantan, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296262) |
| Petani terdampak kekeringan | **30%** | [PLOS ONE — Kalimantan, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296262) |
| Petani terdampak hama | **24%** | [PLOS ONE — Kalimantan, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296262) |
| Dampak signifikan ke pendapatan | **49%** petani | [PLOS ONE — Kalimantan, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296262) |
| Cabai — volatilitas harga harian | Turun **-13.69%** dalam sehari | [TVRI/PIHPSN, Jun 2026](https://ekonomi.tvrinews.com/berita/t6nogk2-pihps-harga-bawang-merah-dan-cabai-kompak-turun) |
| Petani buat keputusan tanam pakai pengalaman pribadi, tanpa data iklim global | Confirmed by survey | [MDPI Sustainability, 2021](https://mdpi.com/2071-1050/13/11/6495/htm) |
| Pertanian = sektor paling tidak terdigitalisasi di Indonesia | Confirmed | [Brookings, 2022](https://www.brookings.edu/articles/the-digital-transformation-of-agriculture-in-indonesia/) |
| Petani yang pakai internet → pendapatan lebih tinggi | **+29.6%** | [World Scientific, 2024](https://www.worldscientific.com/doi/full/10.1142/S0116110525500027) |
| AUTP (asuransi pertanian) cuma cover 8-10% lahan | 300-400K ha dari 4 juta ha | [IDN Financials, 2025](https://www.idnfinancials.com/news/65050/jasindo-syariahs-at-yaltha-ris-agriinsurance-potential-is-big) |

### Root Cause

Petani **gak punya akses ke tool prediktif yang sederhana**. Data cuaca dan harga sebenarnya ada (BMKG, BPS, World Bank) — tapi gak pernah sampai ke petani dalam bentuk yang actionable.

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

## Rekomendasi Solusi yang Diberikan App

App gak cuma kasih data — tapi kasih **actionable advice** berdasarkan kombinasi risk + price prediction:

### Tipe Rekomendasi

| Kondisi | Rekomendasi | Contoh |
|---------|-------------|--------|
| Weather risk LOW + harga naik | ✅ **Tanam sekarang** | "Cuaca aman, harga diprediksi naik 4% saat panen. Waktu ideal." |
| Weather risk MEDIUM + harga naik | ⚠️ **Tanam dengan mitigasi** | "Harga bagus, tapi curah hujan rendah. Siapkan irigasi cadangan." |
| Weather risk HIGH + harga turun | 🔴 **Tunda tanam** | "Risiko kekeringan tinggi + oversupply predicted. Tunda 2-4 minggu." |
| Pest risk HIGH | 🐛 **Siapkan preventif** | "Kelembapan 86% + suhu 27°C → risiko blast & wereng. Siapkan pestisida." |
| Harga komoditas A turun, B naik | 🔄 **Pertimbangkan switch** | "Harga beras flat, tapi cabai predicted naik 20%. Pertimbangkan diversifikasi." |

### Contoh Output Lengkap

```
📍 Lokasi: Karawang, Jawa Barat
🌾 Komoditas: Beras
📅 Rencana tanam: Juli 2026

━━━ HASIL SIMULASI ━━━

💰 Prediksi harga panen (Nov 2026): Rp 13.200 - Rp 14.800/kg
   Sekarang: Rp 12.900/kg → Potensi profit: +4.3%

⛅ Weather Risk: 65/100 (MEDIUM)
   Curah hujan 35% di bawah rata-rata historis bulan ini

🐛 Pest Risk: 72/100 (HIGH)
   Kelembapan 86% + suhu 27°C → risiko blast & wereng

━━━ REKOMENDASI ━━━

✅ TANAM — tapi dengan mitigasi:
  1. Siapkan irigasi cadangan (curah hujan rendah)
  2. Aplikasi fungisida preventif minggu ke-3 (risiko blast tinggi)
  3. Monitoring wereng intensif di fase vegetatif

💡 Alternatif: Tunda 2 minggu — curah hujan diprediksi naik di akhir Juli.
   Risk score akan turun ke ~45 (LOW).
```

### Logic di Balik Rekomendasi

```
IF weather_risk < 30 AND price_trend > 0:
    → "Tanam sekarang, kondisi ideal"
    
IF weather_risk 30-60 AND price_trend > 0:
    → "Tanam dengan mitigasi" + specific tips berdasarkan risk type
    
IF weather_risk > 60 OR price_trend < -5%:
    → "Tunda tanam" + suggest kapan risk turun (what-if slider data)
    
IF pest_risk > 70:
    → Tambah warning pestisida preventif
    
IF harga_komoditas_lain naik signifikan:
    → "Pertimbangkan diversifikasi ke [komoditas]"
```

Rekomendasi ini **rule-based** (gak perlu ML tambahan) — derived dari output model yang udah ada.

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

### 3. Pest Risk Score (Bonus — dari data yang sudah ada)

Kelembapan + suhu dari weather dataset bisa dipakai prediksi risiko hama tanpa dataset tambahan:

```
Kelembapan >80% + suhu 25-30°C = risiko hama TINGGI

Hama utama padi dan trigger cuaca:
- Wereng coklat: kelembapan tinggi, suhu hangat
- Blast (jamur): humidity >85% + suhu 25-28°C
- Penggerek batang: musim hujan berkepanjangan (curah hujan tinggi berturut-turut)
```

**Logic (rule-based, gak perlu ML):**
```
IF humidity > 85% AND temp 25-28°C → Pest Risk: HIGH (blast + wereng)
IF humidity > 80% AND temp 28-32°C → Pest Risk: MEDIUM (wereng)
IF humidity < 70% AND temp < 25°C  → Pest Risk: LOW
```

**Contoh output:**
```
📍 Jawa Barat, Juli 2026

🌾 Harga panen: Rp 13.400/kg (+4%)
⚠️ Weather risk: 65/100 (MEDIUM) — curah hujan rendah
🐛 Pest risk: 72/100 (HIGH) — kelembapan 86%, suhu 27°C
   → Risiko tinggi: blast (jamur) & wereng coklat
💡 "Siapkan pestisida preventif dan monitor tanaman minggu ke-3"
```

**Kenapa ini nambah value:**
- Gak perlu dataset tambahan (pakai humidity + temp yang udah ada)
- 24% petani surveyed terdampak hama (data PLOS ONE)
- Bedain kita dari app yang cuma prediksi harga doang
- Simple rule-based — gak nambah complexity ke ML model

---

## Summary Fitur Lengkap

| Fitur | Fungsi | Wow Level |
|-------|--------|-----------|
| Prediksi harga panen | Kasih angka Rp/kg | Core |
| Weather risk score | 0-100, level LOW/MED/HIGH | Core |
| **Pest risk score** | 0-100, rule-based dari humidity + suhu | Core |
| Rekomendasi aksi | Tanam / tunda / switch komoditas | Core |
| **What-if slider** | Explore berbagai bulan tanam interaktif | **Pembeda** |
| **Historical playback** | Buktikan value app dengan data masa lalu | **Pembeda** |

---

## Jawaban untuk "Petani Gaptek?"

### User app ini bukan petani langsung — tapi penyuluh pertanian (PPL) yang mendampingi mereka.

**Apa itu Penyuluh Pertanian (PPL):**
- Pegawai pemerintah yang tugasnya datang ke sawah, dampingi petani
- Ada di setiap kecamatan di Indonesia (sistem nasional sejak 1911)
- Peran: fasilitator, edukator, motivator, penghubung pemerintah-petani
- Mereka **sudah punya smartphone dan melek digital**

**Sumber:**
- World Bank National Agricultural Extension Project — mendokumentasikan struktur PPL sebagai jaringan nasional ([World Bank](https://documents1.worldbank.org/curated/en/713361468285353858/txt/multi-page.txt))
- IRRI (International Rice Research Institute) — **Juli 2026** melatih penyuluh untuk pakai digital nutrient management advisory tools buat petani padi di Indonesia ([IRRI, Jul 2026](https://www.irri.org/news-and-events/news/training-masters-brings-lkp-20-agricultural-trainers-extension-workers-and))
- Permentan No. 67/2016 — mengatur peran PPL sebagai pembina kelompok tani

**Flow distribusi:**
```
Penyuluh buka app → cek prediksi → sampaikan ke petani secara lisan
"Pak, bulan ini cuaca kering, mending tunda dulu 2 minggu"
```

**Kenapa ini works:**
1. Petani percaya penyuluh lebih dari app — bukan masalah, ini advantage
2. Gak perlu petani install apa-apa — penyuluh jadi "human interface"
3. 1 penyuluh cover ratusan petani — scalable
4. IRRI + Kementan juga baru digitalisasi penyuluh (Juli 2026) — kita aligned dengan arah industri

**Roadmap distribusi:**
```
Phase 1: Penyuluh pertanian (sudah digital, sudah ada di lapangan)
Phase 2: Petani muda / millennial farmer (growing segment, punya smartphone)
Phase 3: WhatsApp bot — petani kirim pesan, dapat jawaban tanpa install app
```

**Kalau judges bilang "tapi target user-nya petani, kok yang pakai penyuluh?"**

> "Petani tetap yang diuntungkan — penyuluh itu delivery channel, bukan end user.
> Sama kayak dokter pakai sistem diagnosis AI — pasien yang terbantu, tapi
> dokter yang operate tool-nya. Kita gak perlu petani jadi tech-savvy.
> Kita perlu keputusan tanam mereka jadi data-driven."
