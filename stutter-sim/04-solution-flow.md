# Solusi + Flow

## Solusi

AI simulator dimana HR/recruiter berlatih interview dengan "kandidat gagap virtual" (AI yang roleplay gagap). AI analyze bagaimana mereka merespons — lalu kasih scorecard: apa yang supportive, apa yang diskriminatif, dan cara improve.

## Flow

```
[HR buka app] → [Pilih skenario: "Interview kandidat gagap untuk posisi X"]
         |
         v
[AI roleplay sebagai kandidat gagap — bicara via voice (ElevenLabs) dengan stuttering pattern]
  Contoh: "Se-se-selamat pagi... nama s-s-saya Andi... saya m-melamar posisi..."
         |
         v
[HR respond via suara — percakapan natural 3-5 menit seperti interview biasa]
         |
         v
[Percakapan selesai]
         |
         v
[AI analyze transcript + audio HR:]
  - Apakah memotong kalimat kandidat? (diskriminatif)
  - Apakah menyelesaikan kata mereka? (patronizing)
  - Apakah memberi waktu/jeda cukup? (supportive)
  - Apakah tone terburu-buru / impatient? (harmful)
  - Apakah skip pertanyaan karena assume kandidat gak bisa? (bias)
  - Apakah tetap assess skill, bukan speech? (fair)
         |
         v
[Output: Scorecard + Tips]
```

## Contoh Output Scorecard

```
SCORE: 65/100 — "Ada beberapa bias yang perlu diperbaiki"

WHAT YOU DID WELL:
✅ Kamu memberi jeda di menit 1:00 saat kandidat blocking — bagus
✅ Pertanyaan kamu fokus ke skill, bukan communication ability

WHAT NEEDS IMPROVEMENT:
❌ Menit 2:30 — kamu menyelesaikan kalimat kandidat ("...jadi kamu maksudnya X?")
❌ Menit 3:00 — kamu skip pertanyaan presentasi (bias: assume mereka gak bisa)
⚠️ Tone kamu terdengar terburu-buru di menit 4

TIPS:
- Tunggu 5 detik setelah blocking sebelum respond
- Jangan finish their sentences — biarkan mereka selesaikan sendiri
- Assess skill dan pengalaman, bukan fluency bicara
- "Pelan-pelan aja" = patronizing. Jangan bilang itu.
```

## Tech Stack

| Component | Tool |
|-----------|------|
| AI roleplay voice (gagap) | LLM generate text with stutter markers → ElevenLabs TTS |
| STT (HR response) | Whisper API |
| Conversation logic | LLM (GPT-4o / Gemini) — roleplay as stuttering candidate |
| Behavior analysis | LLM analyze transcript: detect interruptions, pacing, bias |
| Frontend | React/Next.js — minimal UI, voice-first |
| Backend | Python FastAPI |
