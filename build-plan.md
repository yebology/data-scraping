# AI Farm Risk Simulator — Build Plan

## Dataset yang Tersedia

| File | Isi | Coverage |
|------|-----|----------|
| `IDN_RTFP_mkt_2007_2026-07-06 2.csv` | Harga komoditas (beras, cabai, bawang, dll) per market per bulan | 223 pasar, 35 provinsi, 2007-2026 |
| `weather-all-provinces-2010-2024.csv` | Cuaca (curah hujan, suhu, kelembapan) per provinsi per bulan | 34 provinsi, 2010-2024 |

---

## Apa yang Perlu Di-build

### 1. Data Preprocessing Pipeline

**Kenapa:** Kedua dataset punya format berbeda dan perlu digabung sebelum bisa di-train.

**Yang dilakukan:**
- Rename `"DAERAH ISTIMEWA YOGYAKARTA"` → `"DI YOGYAKARTA"` di RTFP (supaya nama provinsi match)
- Hapus row dengan `adm1_name = "MARKET AVERAGE"` (bukan provinsi)
- Filter RTFP ke 2010-2024 saja (supaya align dengan weather data)
- Aggregate harga beras RTFP dari level market → level provinsi (rata-rata per provinsi per bulan)
- Pivot weather data dari long format (1 row per parameter) → wide format (kolom: curah_hujan, suhu, kelembapan)
- Join kedua dataset via key: `province + year + month`
- Buat kolom target: `harga_beras_bulan_X+4` (harga 4 bulan ke depan = saat panen)

**Output:** 1 CSV gabungan siap di-train.

---

### 2. ML Model — Price Prediction

**Kenapa:** Ini core value dari app. Petani input lokasi + waktu tanam → dapat prediksi harga beras saat panen.

**Logic:**
```
Cuaca bulan tanam (curah hujan, suhu, kelembapan)
    + Harga beras bulan ini (baseline)
    + Provinsi (one-hot atau label encode)
    + Bulan (seasonality)
    → Prediksi harga beras 3-4 bulan kemudian (Rp/kg)
```

**Model options (dari simple ke complex):**
1. **Linear Regression** — baseline, cepat, explainable
2. **Random Forest** — lebih akurat, handle non-linear
3. **XGBoost** — best accuracy untuk tabular data

**Kenapa bukan deep learning:** Data tabular kecil (15 tahun × 12 bulan × 34 provinsi = ~6.000 rows). Tree-based models lebih cocok daripada neural nets untuk dataset size ini.

**Features (input):**
| Feature | Source | Kenapa |
|---------|--------|--------|
| `precipitation` (mm/day) | Weather | Curah hujan = faktor #1 produksi padi |
| `temperature` (°C) | Weather | Suhu tinggi = stress tanaman |
| `humidity` (%) | Weather | Kelembapan tinggi = risiko hama |
| `current_rice_price` (Rp/kg) | RTFP | Baseline harga sekarang |
| `province` (encoded) | Both | Setiap daerah punya pola berbeda |
| `month` (1-12) | Both | Seasonality (musim panen = harga turun) |
| `price_lag_1` | RTFP | Harga bulan lalu (momentum) |
| `price_lag_3` | RTFP | Harga 3 bulan lalu (trend) |

**Target (output):**
- `rice_price_future` = harga beras 4 bulan ke depan (Rp/kg)

**Metric:** MAE (Mean Absolute Error) — "rata-rata model meleset berapa Rp/kg"

---

### 3. Weather Risk Scoring

**Kenapa:** Selain harga, petani perlu tahu apakah cuaca bulan ini aman untuk mulai tanam atau tidak.

**Logic:**
```
Ambil cuaca historis provinsi X di bulan Y (15 tahun data)
    → Hitung rata-rata & standar deviasi curah hujan
    → Bandingkan dengan cuaca tahun ini / prediksi
    → Score 0-100:
        0-30  = LOW RISK (cuaca normal, aman tanam)
        31-60 = MEDIUM RISK (agak kering/basah, hati-hati)
        61-100 = HIGH RISK (anomali besar, pertimbangkan tunda)
```

**Contoh:**
- Curah hujan rata-rata Jawa Barat di Juli = 3.5 mm/day
- Tahun ini: 1.2 mm/day (jauh di bawah rata-rata)
- → Risk score: 75 (HIGH) — kemungkinan kekeringan

---

### 4. Backend API

**Kenapa:** Frontend perlu endpoint untuk kirim input dan terima prediksi.

**Endpoints:**
```
POST /api/predict
  Input:  { province: "JAWA BARAT", plant_month: 7, year: 2026 }
  Output: {
    predicted_price: 13450,      // Rp/kg
    price_range: [12800, 14100], // confidence interval
    weather_risk: 65,            // score 0-100
    risk_level: "MEDIUM",
    recommendation: "Curah hujan di bawah rata-rata. Siapkan irigasi cadangan.",
    current_price: 12900,        // harga sekarang sebagai referensi
    price_change: "+4.3%"        // prediksi perubahan
  }

GET /api/provinces
  Output: list of 34 provinces

GET /api/history?province=JAWA_BARAT&commodity=rice
  Output: harga & cuaca historis untuk chart
```

**Tech stack:**
- Python (FastAPI) — karena model ML di Python
- Atau Node.js + Python model di-serve via pickle/ONNX

---

### 5. Frontend UI

**Kenapa:** Demo ke judges harus visual dan impactful.

**Flow:**
```
[Pilih Provinsi] → [Pilih Bulan Tanam] → [Klik "Simulasi"]
                                              ↓
                            ┌─────────────────────────────┐
                            │  HASIL SIMULASI             │
                            │                             │
                            │  🌾 Prediksi Harga Panen:   │
                            │     Rp 13.450/kg            │
                            │     (+4.3% dari sekarang)   │
                            │                             │
                            │  ⚠️ Weather Risk: MEDIUM    │
                            │     Score: 65/100           │
                            │                             │
                            │  💡 Rekomendasi:            │
                            │  "Curah hujan rendah.       │
                            │   Siapkan irigasi."         │
                            │                             │
                            │  📊 [Chart harga historis]  │
                            └─────────────────────────────┘
```

**Tech options:**
- Next.js / React (standard hackathon choice)
- Atau Streamlit (Python, faster to build, less pretty)

---

## Build Order (Prioritas Hackathon 48 Jam)

| Order | Task | Waktu | Kenapa duluan |
|-------|------|-------|---------------|
| 1 | Data preprocessing + join | 2-3 jam | Foundation — semua depend ke ini |
| 2 | ML model training | 3-4 jam | Core logic harus jalan dulu |
| 3 | Backend API | 2-3 jam | Expose model ke frontend |
| 4 | Frontend UI | 4-6 jam | Demo harus visual |
| 5 | Polish + slides | 2-3 jam | Presentasi ke judges |

**Total: ~15-18 jam kerja** (feasible dalam 48 jam hackathon)

---

## Risiko Teknis

| Risk | Mitigation |
|------|-----------|
| Model accuracy rendah | Fallback ke simple moving average + seasonal pattern. Judges lebih nilai approach daripada akurasi sempurna. |
| Data terlalu sedikit (6K rows) | Feature engineering (lag, rolling avg) bisa multiply effective sample size. |
| Join mismatch | Sudah di-validate: 33/34 provinsi match, 15 tahun overlap. |
| API lambat | Pre-compute predictions, cache results. |

---

## Output Final ke Petani

> 📍 **Lokasi:** Karawang, Jawa Barat  
> 🌾 **Komoditas:** Beras  
> 📅 **Rencana tanam:** Juli 2026  
>
> ### Prediksi Harga Saat Panen (November 2026)
> **Rp 13.200 - Rp 14.800/kg** (sekarang: Rp 12.900/kg)
>
> ### Weather Risk Score: 65/100 (MEDIUM)
> Curah hujan bulan ini 35% di bawah rata-rata historis.
>
> ### Rekomendasi
> ✅ Harga diprediksi naik 4% — potensi profit bagus  
> ⚠️ Risiko kekeringan menengah — siapkan irigasi cadangan  
> 💡 Alternatif: tunda 2 minggu sampai curah hujan naik
