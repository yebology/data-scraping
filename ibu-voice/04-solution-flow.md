# Solusi + Flow

## Solusi

Ibu TKI rekam suaranya sekali (5-10 menit) → AI clone voice-nya → setiap malam, app bacakan cerita/dongeng/pesan pengantar tidur ke anak pakai suara ibu mereka sendiri.

AI voice clone = fallback untuk malam-malam dimana ibu gak sempat rekam sendiri. Anak tetap dengar "suara ibu" walau ibu sedang gak available.

## Flow

### Sisi Ibu (di luar negeri):

```
1. Download app → rekam suara 5-10 menit (baca teks panduan)
2. AI clone voice → selesai (hanya perlu dilakukan SEKALI)
3. Kapanpun sempat: rekam pesan personal pendek
   ("Ibu sayang kamu, belajar yang rajin ya")
   ("Hari ini ibu masak rendang, inget masakan ibu kan?")
```

### Sisi Anak (di kampung, dengan nenek/wali):

```
1. Setiap malam sebelum tidur → wali tekan play (atau timer otomatis)
2. Anak dengar:
   - Pesan personal dari ibu (kalau ibu sempat rekam hari itu)
   - ATAU dongeng/cerita yang di-generate AI pakai suara ibu
   - ATAU doa/nyanyian pengantar tidur pakai suara ibu
3. Anak tidur dengan suara ibu sebagai hal terakhir yang mereka dengar
```

### Kalau Ibu Gak Sempat Rekam (yang terjadi kebanyakan hari):

```
AI generate cerita anak → convert ke suara pakai voice clone ibu → play otomatis sesuai jadwal

Anak tetap dengar "suara ibu" setiap malam — regardless apakah ibu sempat atau tidak.
```

## Tech Stack

| Component | Tool |
|-----------|------|
| Voice cloning | ElevenLabs Voice Clone (5 menit sample cukup) |
| Story generation | LLM (GPT-4o / Gemini) — generate cerita anak sesuai usia |
| Text-to-Speech (cloned voice) | ElevenLabs TTS with cloned voice |
| App frontend | React Native / Flutter (cross-platform) |
| Backend | Python FastAPI |
| Storage | Cloud storage untuk voice samples + generated audio |
| Scheduling | Cron job atau local alarm untuk play otomatis |

## Kenapa Bukan Video Call / Voice Note Biasa?

| Existing (Video call / Voice note) | IbuVoice |
|------------------------------------|----------|
| Butuh ibu available SAAT ITU | Ibu rekam sekali, AI extend selamanya |
| Timezone clash (ibu kerja saat anak tidur) | Auto-play sesuai jadwal anak |
| Anak kecil gak bisa operate HP | Wali tekan 1 tombol / timer otomatis |
| Kalau ibu gak sempat = anak gak dengar apa-apa | Kalau ibu gak sempat = AI generate pakai suara ibu |
| Inconsistent (kadang nelpon kadang tidak) | Konsisten setiap malam (yang proven penting) |
