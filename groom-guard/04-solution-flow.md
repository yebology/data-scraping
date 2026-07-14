# Solusi + Flow

## Solusi

App Android yang monitor pola komunikasi anak via NotificationListenerService → AI detect grooming pattern per-contact over time → classify stage → alert orang tua dengan context + action plan spesifik.

## Flow

```
[Install di HP anak — orang tua setup permission]
         |
         v
[NotificationListenerService capture: sender, preview pesan, timestamp, app source]
         |
         v
[Data di-batch per contact per hari → kirim ke backend]
         |
         v
[Backend: LLM analyze batch per contact]
  - Frekuensi komunikasi (naik/turun/stable?)
  - Jam komunikasi (pattern malam hari?)
  - Bahasa (flattery? secret-keeping? escalating intimacy?)
  - Contact baru vs lama?
  - Age indicators (apakah contact ini kemungkinan dewasa?)
         |
         v
[Output per contact: Risk Level]
  - SAFE (normal friendship pattern)
  - WATCH (beberapa indicator, belum conclusive)
  - CONCERNING (multiple indicators, Stage 2-3)
  - DANGER (clear grooming pattern, Stage 4+)
         |
         v
[Kalau CONCERNING/DANGER → Push notification ke HP orang tua]
         |
         v
[Orang tua buka dashboard → lihat:]
  - Contact mana yang flagged
  - Timeline pattern (grafik frekuensi + jam)
  - Grooming stage assessment (Stage 1-6)
  - SPECIFIC action plan:
    1. "Jangan langsung konfrontasi anak (mereka akan defensive)"
    2. "Screenshot bukti ini: [guidance]"
    3. "Report ke KPAI: [link + cara]"
    4. "Ini script cara bicara ke anak: [template]"
    5. "Kapan harus ke polisi: [threshold]"
```

## Contoh Alert ke Orang Tua

```
⚠️ CONCERNING — Contact: "Kak Rio" (baru dikenal 12 hari)

PATTERN:
- Hari 1-3: 5 pesan/hari (normal)
- Hari 4-7: 20 pesan/hari (naik 4x)
- Hari 8-12: 35 pesan/hari, 70% antara 22.00-01.00
- Language indicators: flattery tinggi, "ini rahasia kita ya", "kamu beda dari yang lain"

ASSESSMENT: Grooming Stage 3 (Isolation)
Contact ini kemungkinan sedang membangun dependensi emosional dan mulai mengisolasi anak dari support system.

APA YANG HARUS KAMU LAKUKAN:
1. JANGAN langsung ambil HP atau marah — anak akan tutup diri
2. Screenshot percakapan sebagai bukti (panduan: ...)
3. Ajak anak ngobrol santai soal teman-teman online mereka (script: ...)
4. Kalau ada request foto/ketemu → segera report ke KPAI (link: ...)
5. Konsultasi: hubungi hotline 129 (KPAI)
```

## Tech Stack

| Component | Tool |
|-----------|------|
| Notification capture | Android NotificationListenerService |
| Local storage | SQLite (cache before batch send) |
| Backend | Python FastAPI |
| Pattern analysis | GPT-4o / Gemini (prompt with grooming stage framework) |
| Parent dashboard | Next.js (web) |
| Alert | Firebase Cloud Messaging (push notif) |
| Parent app | Web app (bisa dibuka di HP orang tua) |

## Token Cost per User per Hari

- Batch pesan per contact per hari: ~200-500 token input
- LLM analysis + output: ~300-500 token
- Total per contact per day: ~500-1000 token
- Kalau anak punya 10 active contacts: ~5000-10000 token/hari
- Cost: ~$0.01-0.03/hari per anak
- Monthly: ~$0.30-1.00 per anak = Rp 5000-15000

Sangat affordable.
