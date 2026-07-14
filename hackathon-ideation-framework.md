# Framework Ideation Hackathon yang Manjur
## Berdasarkan Riset dari Pemenang 20+ Hackathon & Judges

---

## PRINSIP UTAMA

> "Winners are typically decided in the FIRST TWO HOURS, not the last two — they pick a tractable problem, agree on what 'done' looks like, read the judging rubric before coding, build a working skeleton early, and design the demo before writing meaningful code."
> — HackerEarth (dari 500+ events)

> "Technical sophistication without human relevance is just expensive showing off."
> — Medium, "How to Win an AI Hackathon"

> "A strong project with a confusing demo loses to a simpler project that the judges understand."
> — JetBrains, "Notes From the Judging Table" (Jun 2026)

> "The biggest mistake I see in hackathons is people jumping too quickly to solutions. They don't give themselves enough time to truly explore the problem."
> — Facilitator's Corner

> "You need to get your audience of judges sharing your frustration with the problem."
> — JetBrains

---

## FRAMEWORK: 5 Langkah Ideation

### STEP 1: Start with PERSONAL FRUSTRATION (bukan teknologi)

**Jangan mulai dari:** "Apa yang bisa AI/ML/blockchain solve?"

**Mulai dari:** "Apa yang bikin GUE SENDIRI atau ORANG TERDEKAT gue frustrasi minggu ini?"

**Pertanyaan pemandu:**
- Apa yang kamu keluhkan ke teman dalam 7 hari terakhir?
- Apa yang bikin kamu buang waktu/uang yang harusnya gak perlu?
- Apa yang kamu lihat orang struggle lakukan di sekitar kamu?
- Apa yang kamu wish "kenapa gak ada yang bikin ini"?
- Apa yang broken tapi semua orang sudah "terima" karena terbiasa?

**Why this works:** Juri harus MERASAKAN frustrasi yang sama. Kalau kamu frustrasi genuine, itu terlihat di pitch. Kalau kamu ngada-ngada problem yang gak kamu rasakan, juri juga bisa detect.

---

### STEP 2: Validate — Apakah Ini Problem BANYAK Orang atau Cuma Gue?

**Metode:**
1. **Cek social media** — search keyword di Twitter/Reddit/Threads. Orang ngeluh soal ini? Berapa banyak?
2. **Tanya 5 orang** — bukan "apakah ini masalah?" (leading question) tapi "ceritain pengalaman terakhir kamu soal [topic]?"
3. **Data publik** — ada statistik yang back up? (News, BPS, riset, laporan pemerintah)
4. **Existing solutions** — kalau sudah ada solusi tapi orang masih ngeluh = solusinya jelek = peluang

**Red flags:**
- ❌ Kamu harus "menjelaskan" kenapa ini masalah (kalau perlu dijelasin, bukan masalah real)
- ❌ Problem cuma relevan untuk 100 orang di niche super kecil
- ❌ Problem yang semua orang "tahu" tapi gak "rasakan" secara personal

**Green flags:**
- ✅ Orang langsung bilang "IYA! Gue juga!"
- ✅ Ada data/berita yang confirm
- ✅ Solusi existing ada tapi orang masih frustrasi (= gap)

---

### STEP 3: Define the "Smallest Meaningful Scope"

**Bukan:** "Platform end-to-end yang solve semua aspek masalah ini"

**Tapi:** "Satu fitur yang solve satu momen spesifik dalam journey user"

**Framework "One User, One Moment, One Action":**
- **Siapa 1 user spesifik** yang paling merasakan masalah ini?
- **Di momen apa** mereka paling frustrasi?
- **Apa 1 action** yang kalau mereka bisa lakukan, masalah ini berkurang significantly?

**Contoh bagus dari winners:**
- JalanKami: bukan "fix semua infrastruktur kota" tapi "kasih walkability score per rute" → 1 user (pejalan kaki), 1 momen (mau jalan kaki ke suatu tempat), 1 action (pilih rute yang paling walkable)
- Jendela: bukan "rehabilitasi semua napi" tapi "connect ex-convict dengan training center terdekat" → 1 user (ex-convict), 1 momen (baru keluar penjara), 1 action (daftar pelatihan)

---

### STEP 4: Design the Demo BEFORE Coding

> "Design the demo before writing meaningful code."
> — HackerEarth

**Pitch format yang work (dari Reskilll, 5000+ events):**
```
60 detik — Problem (bikin juri FEEL the pain)
30 detik — Approach (1-2 kalimat solusi)
90 detik — LIVE DEMO (ini yang bikin menang)
30 detik — Impact/next steps
```

**Pertanyaan sebelum coding:**
- Apa yang juri LIHAT saat demo? (screen recording? live app? hardware?)
- Apa "magic moment"-nya? (momen dimana juri bilang "wow")
- Bisa kamu demo ini dalam 90 detik?
- Kalau internet mati saat demo, masih bisa jalan?

**Rule:** Kalau kamu gak bisa describe demo-nya dalam 1 kalimat, scope terlalu besar.

---

### STEP 5: Sanity Check — "Apakah Ini Bodoh?"

Sebelum commit, tanya:

| Pertanyaan | Jawaban Harus "Ya" |
|-----------|-------------------|
| Apakah user TARGET beneran akan PAKAI ini? | Bukan "harusnya mereka pakai" tapi "mereka AKAN pakai" |
| Apakah behaviour ini sudah ada (kamu cuma mempermudah)? | Jangan create new behaviour — reduce friction di yang existing |
| Apakah ada revenue yang make sense? | Siapa yang bayar dan kenapa? |
| Apakah bisa demo dalam 90 detik dan juri langsung paham? | Kalau perlu 5 menit explain = terlalu complex |
| Apakah berbeda dari yang sudah ada? | Apa twist-nya? Constraint unik apa yang bikin ini fresh? |
| Apakah gue sendiri excited build ini? | Kalau gak excited, 30 jam akan terasa hell |

---

## COMMON MISTAKES (dari judges & veterans)

### ❌ Mistake 1: Start with Technology
"Kita pakai AI/blockchain/IoT!" → lalu cari masalah yang cocok.
**Fix:** Start with pain. Tech is just the tool.

### ❌ Mistake 2: Too Broad
"Platform yang solve semua X" — impossible di 30 jam, demo jadi shallow.
**Fix:** 1 user, 1 moment, 1 action.

### ❌ Mistake 3: Solution Looking for Problem
"Kita bisa build X" tapi user gak butuh X.
**Fix:** Validate dengan 5 orang dulu. Kalau mereka gak antusias, pivot.

### ❌ Mistake 4: Information = Behaviour Change
"Kalau orang TAHU, mereka akan berubah" — almost never true.
**Fix:** Help people who ALREADY WANT to act but are BLOCKED.

### ❌ Mistake 5: Perfect Code, Broken Demo
30 jam habis ngoding backend perfect tapi frontend jelek dan demo gagap.
**Fix:** Build demo-first. Working skeleton > clean architecture.

### ❌ Mistake 6: Ignore Judging Criteria
Setiap hackathon punya rubrik. Banyak tim gak baca.
**Fix:** Baca rubrik sebelum mulai. Align solution ke criteria yang di-value.

---

## TEMPLATE IDEATION (isi ini sebelum coding)

```markdown
## PROJECT: [Nama Catchy]

### Problem (1-2 kalimat)
[Siapa] mengalami [masalah apa] saat [momen kapan] karena [kenapa].

### Evidence
- Data: [statistik/berita yang confirm problem ini real]
- Personal: [pengalaman pribadi / orang terdekat]
- Existing gap: [solusi yang ada sekarang dan kenapa masih gagal]

### Solution (1 kalimat)
[Tool/platform] yang membantu [user] untuk [action] dengan cara [how — ini twist-nya].

### One User, One Moment, One Action
- User: [siapa specifically]
- Moment: [kapan exactly mereka frustrasi]
- Action: [apa 1 hal yang mereka bisa lakukan berkat kamu]

### Demo Script (90 detik)
1. [Apa yang juri lihat di detik 0-30]
2. [Magic moment di detik 30-60]
3. [Result/impact di detik 60-90]

### Revenue
- Siapa yang bayar: [customer]
- Kenapa mereka bayar: [value prop]
- Model: [subscription / per-use / freemium / B2B / B2G]

### Twist / Why This is Different
[Apa yang bikin juri bilang "kenapa gak ada yang kepikiran ini sebelumnya?"]

### Track Fit
[Mana track GarudaHacks yang cocok dan kenapa — quote deskripsi track]

### Sanity Check
- [ ] User beneran akan pakai? (bukan harusnya pakai)
- [ ] Behaviour sudah exist? (reduce friction, bukan create new)
- [ ] Revenue make sense?
- [ ] Demo 90 detik, juri langsung paham?
- [ ] Beda dari yang sudah ada?
- [ ] Tim excited build ini?
```

---

## NEXT STEP: Mulai dari Personal Frustration

Daripada brainstorm abstrak, coba:
1. **Isi list:** 10 hal yang bikin kamu/teman/keluarga frustrasi dalam 7 hari terakhir
2. **Filter:** mana yang intersect dengan Health / Safety / Agriculture track
3. **Validate:** tanya 3-5 orang — mereka relate?
4. **Scope:** 1 user, 1 moment, 1 action
5. **Demo-first:** gambar/describe apa yang juri lihat

---

## SUMBER

1. [HackerEarth — 10 Tips from 500+ Events](https://citi.hackerearth.com/blog/10-tips-win-hackathon)
2. [JetBrains — How to Win a Hackathon: Notes From the Judging Table (Jun 2026)](https://blog.jetbrains.com/ai/2026/06/how-to-win-a-hackathon-notes-from-the-judging-table/)
3. [Medium — How to Win an AI Hackathon: Build a Solution that Actually Matters](https://tanya-fesenko.medium.com/how-to-win-an-ai-hackathon-build-a-solution-that-actually-matters-0270a3983419)
4. [Medium — Ultimate 8 Step Guide to Winning Hackathons (won 20+)](https://medium.com/@garyyauchan/ultimate-8-step-guide-to-winning-hackathons-84c9dacbe8e)
5. [Medium — Hack the Hackathon: A Proven Formula for Winning](https://medium.com/@eyal.shechtman/hack-the-hackathon-a-proven-formula-for-winning-231663ff00cc)
6. [Hashnode — How to Win Hackathons: A Deep, Practical, and Honest Roadmap](https://hackathon-playbook.hashnode.dev/how-to-win-hackathons-a-deep-practical-and-honest-roadmap-for-student-builders)
7. [Medium — Ideation For Hackathons: Design Tools For Engineers](https://medium.com/design-bootcamp/ideation-for-hackathons-design-tools-for-engineers-d15f4d10b043)
8. [Facilitator's Corner — How to Effectively Facilitate a Hackathon](https://facilitatorscorner.substack.com/p/how-to-effectively-facilitate-a-hackathon)
9. [Reskilll — How to Win a Hackathon in 2026 (from 5000+ events)](https://blogs.reskilll.com/how-to-win-a-hackathon-in-2026-reskillls-guide-from-5000-events/)
10. [Medium — How to Win at Hackathons (Alex Tandy)](https://medium.com/@alex.tandy/how-to-win-at-hackathons-3d34df3a0cd2)

---

*Prepared for GarudaHacks 7.0 ideation process*
