# GarudaHacks 7.0 — SafePlate
## AI Food Safety Monitoring untuk Program MBG

**Track:** Health + Safety  
**Tanggal:** 16-18 Juli 2026, UMN  
**Last updated:** 7 Juli 2026

---

## 1. PROBLEM

### Inti Masalah

Program Makan Bergizi Gratis (MBG) — program unggulan Presiden Prabowo senilai **$10.2 miliar** — telah meracuni **9.000+ anak sekolah** dalam tahun pertama pelaksanaannya (2025). BPOM mengakui: "Kesalahan terbesar kami adalah kurangnya pengawasan."

### Data Problem

| Fakta | Data | Sumber |
|-------|------|--------|
| Anak keracunan dari MBG | 9.000+ (Jan-Okt 2025) | [Reuters](https://www.reuters.com/business/healthcare-pharmaceuticals/more-than-9000-children-indonesia-got-food-poisoning-school-meals-2025-2025-10-01/) |
| Kasus terdokumentasi detail | 5.626+ siswa (Jan-Sep 2025) | [Kompas.id](https://www.kompas.id/artikel/en-kemanan-pangan-mbg-lemah-bagaimana-mengatasinya) |
| Insiden tercatat | 70 insiden di 10 provinsi | [Food Safety News](https://www.foodsafetynews.com/2025/10/thousands-sickened-by-school-food-in-indonesia/) |
| Termasuk 2026 | 10.000+ total korban | [ABC News Australia](https://www.abc.net.au/news/2025-11-16/indonesia-free-school-meals-program-for-kids-in-schools-problems/106009984) |
| Budget MBG | $10.2 miliar/tahun | [AviNews](https://avinews.com/en/feeding-indonesias-future-or-poisoning-its-promise/) |
| Target penerima | 82.9 juta orang/hari | [AviNews](https://avinews.com/en/feeding-indonesias-future-or-poisoning-its-promise/) |
| Pemerintah butuh AI | Rencana embed AI untuk monitoring | [CryptoBriefing Jun 2026](https://cryptobriefing.com/indonesia-ai-free-meal-program/) |
| Program sempat dihentikan | Awal Jan 2026, untuk perkuat food safety | [SEAsia.co](https://seasia.co/2025/12/27/indonesia-to-halt-the-mbg-program-in-early-2026) |
| Bakteri ditemukan di makanan | E. coli & Salmonella confirmed | [Tempo](https://en.tempo.co/read/2006994/5-cases-of-mbg-food-poisoning-since-january-2025) |

---

## 2. ROOT CAUSE (Based on Data)

Root cause berikut **bukan kesimpulan sendiri**, melainkan langsung dari pernyataan resmi investigator/pejabat:

---

### Root Cause #1: Makanan Didistribusikan Terlalu Lama Setelah Dimasak (Time-Temperature Abuse)

**Siapa yang bilang:** Kepala BPOM Ikrar

> "Food poisoning stemmed from **distribution of meals four hours after cooking**"

**Sumber:** [Reuters, Oct 2025](https://www.reuters.com/business/healthcare-pharmaceuticals/more-than-9000-children-indonesia-got-food-poisoning-school-meals-2025-2025-10-01/)

**Diperkuat oleh pakar Tjandra:**
> "Bacillus cereus often appears due to **improper rice storage**"

**Sumber:** [Tempo, Sep 2025](https://en.tempo.co/read/2052598/todays-top-3-news-experts-identify-salmonella-and-bacillus-cereus-in-free-nutritious-meal-poisoning-probe)

---

### Root Cause #2: Penyimpanan Bahan Baku yang Tidak Tepat (Improper Storage)

**Siapa yang bilang:** Kepala BPOM Ikrar

> "...improper storage of ingredients..."

**Sumber:** [Reuters, Oct 2025](https://www.reuters.com/business/healthcare-pharmaceuticals/more-than-9000-children-indonesia-got-food-poisoning-school-meals-2025-2025-10-01/)

**Diperkuat oleh BPOM (via Jakarta Globe):**
> "BPOM has identified **contaminated raw ingredients** and poor hygiene as key causes"

**Sumber:** [Jakarta Globe, Feb 2025](https://jakartaglobe.id/news/food-poisoning-in-10-provinces-tied-to-poor-hygiene-bpom-says)

**Kasus spesifik:** Keracunan di Mamuju disebabkan **expired sauce**.

**Sumber:** [ABC News, Oct 2025](https://www.abc.net.au/news/2025-10-05/indonesia-free-meal-program-poisons-thousands-of-kids/105836302)

---

### Root Cause #3: Kelalaian dalam Proses Pengolahan (Processing Negligence)

**Siapa yang bilang:** Kepala BGN Dadan Hindayana

> "Our initial suspicion is **negligence in processing** [of food ingredients]"

**Sumber:** [Jakarta Globe, Apr 2025](https://jakartaglobe.id/news/police-investigate-mass-food-poisoning-tied-to-govt-free-meal-program)

**Diperkuat oleh Kantor Staf Presiden — Qodari (4 faktor):**
> 1. Food hygiene issues
> 2. **Improper food temperature and processing**
> 3. Cross-contamination by staff
> 4. Allergic reactions

**Sumber:** [Tempo, Sep 2025](https://en.tempo.co/read/2051106/presidential-staff-office-5000-people-poisoned-by-free-nutritious-meals)

---

### Root Cause #4: Kurangnya Pengetahuan tentang Keamanan Pangan

**Siapa yang bilang:** Kepala BPOM Ikrar

> "...and **lack of knowledge of food security**"

**Sumber:** [Reuters, Oct 2025](https://www.reuters.com/business/healthcare-pharmaceuticals/more-than-9000-children-indonesia-got-food-poisoning-school-meals-2025-2025-10-01/)

---

### Root Cause #5: Kurangnya Pengawasan (Lack of Oversight)

**Siapa yang bilang:** BPOM sendiri

> "Our biggest mistake is... **our lack of oversight**"

**Sumber:** [Reuters, Sep 2025](https://www.reuters.com/world/asia-pacific/indonesia-agency-says-lack-oversight-free-meal-programme-led-food-poisoning-2025-09-26/)

---

### Bukti Lab — Apa yang Ditemukan di Makanan:

| Kontaminan | Ditemukan di | Sumber |
|------------|-------------|--------|
| E. coli | Makanan MBG | [Tempo, May 2025](https://en.tempo.co/read/2006994/5-cases-of-mbg-food-poisoning-since-january-2025) |
| Salmonella | Daging, unggas, telur yang tidak diproses benar | [Tempo, Sep 2025](https://en.tempo.co/read/2052598/todays-top-3-news-experts-identify-salmonella-and-bacillus-cereus-in-free-nutritious-meal-poisoning-probe) |
| Bacillus cereus | Nasi yang disimpan tidak tepat | [Tempo, Sep 2025](https://en.tempo.co/read/2052598/todays-top-3-news-experts-identify-salmonella-and-bacillus-cereus-in-free-nutritious-meal-poisoning-probe) |
| Nitrite (kimia) | Melon dan salad sayur | [Tempo, Oct 2025](https://en.tempo.co/read/2054740/bgn-urged-to-pinpoint-cause-of-nitrite-contamination-in-free-meal-poisoning) |

---

### Ringkasan Root Cause (Ranked by Data Frequency):

| # | Root Cause | Berapa Kali Disebut | Oleh Siapa |
|---|-----------|-------------------|-----------|
| 1 | **Time-temperature abuse** (makanan >4 jam di suhu ruang, penyimpanan suhu tidak tepat) | 5x | BPOM, Menkes, Pakar Tjandra, Kantor Staf Presiden, ABC News |
| 2 | **Bahan baku terkontaminasi/expired** | 4x | BPOM, BGN, ABC News, Tempo |
| 3 | **Kelalaian proses pengolahan** | 3x | BGN, Kantor Staf Presiden, Food Safety News |
| 4 | **Kurangnya pengawasan/oversight** | 2x | BPOM |
| 5 | **Hygiene pekerja (cross-contamination)** | 2x | Kantor Staf Presiden, BPOM |
| 6 | **Kurangnya pengetahuan food safety** | 1x | BPOM |

**Insight kunci:** Root cause #1 (time-temperature) dan #2 (bahan baku) secara konsisten disebut sebagai penyebab utama oleh BPOM dan investigator. Hygiene pekerja (sarung tangan, hairnet) disebut tapi **bukan sebagai penyebab dominan**.

---

## 3. SOLUSI

*[TO BE DETERMINED — solusi harus menjawab root cause #1 dan #2 yang dominan berdasarkan data]*

**Yang harus dijawab solusi:**
- Bagaimana memastikan makanan tidak didistribusikan >4 jam setelah dimasak?
- Bagaimana memastikan bahan baku disimpan pada suhu yang tepat?
- Bagaimana memastikan bahan baku yang expired/terkontaminasi tidak terpakai?
- Bagaimana meng-scale pengawasan ke ribuan dapur tanpa menambah inspektur fisik?

---

## 4. SUMBER LENGKAP

### Berita Utama:
1. [Reuters — 9,000+ children food poisoning (Oct 2025)](https://www.reuters.com/business/healthcare-pharmaceuticals/more-than-9000-children-indonesia-got-food-poisoning-school-meals-2025-2025-10-01/)
2. [Reuters — BPOM admits lack of oversight (Sep 2025)](https://www.reuters.com/world/asia-pacific/indonesia-agency-says-lack-oversight-free-meal-programme-led-food-poisoning-2025-09-26/)
3. [ABC News — How free school meals gave thousands food poisoning (Nov 2025)](https://www.abc.net.au/news/2025-11-16/indonesia-free-school-meals-program-for-kids-in-schools-problems/106009984)
4. [ABC News — Fried shark and maggots (Oct 2025)](https://www.abc.net.au/news/2025-10-05/indonesia-free-meal-program-poisons-thousands-of-kids/105836302)
5. [CNA — MBG under fire (Oct 2025)](https://www.channelnewsasia.com/asia/indonesia-free-nutritious-meals-programme-prabowo-food-poisioning-outbreaks-5379411)
6. [CNA — 1,000+ sick West Java (Jan 2026)](https://www.channelnewsasia.com/asia/indonesia-free-school-meal-mass-food-poisoning-5368136)
7. [The Diplomat — Safety Failures & Governance Breakdown (Oct 2025)](https://thediplomat.com/2025/10/indonesias-free-meals-program-under-fire-for-safety-failures-and-governance-breakdown/)
8. [AviNews — Feeding Indonesia's future or poisoning its promise? (Dec 2025)](https://avinews.com/en/feeding-indonesias-future-or-poisoning-its-promise/)

### Investigasi & Penyebab:
9. [Jakarta Globe — BPOM: contaminated raw ingredients & poor hygiene (Feb 2025)](https://jakartaglobe.id/news/food-poisoning-in-10-provinces-tied-to-poor-hygiene-bpom-says)
10. [Jakarta Globe — BGN: negligence in processing (Apr 2025)](https://jakartaglobe.id/news/police-investigate-mass-food-poisoning-tied-to-govt-free-meal-program)
11. [Tempo — Lab test: E. coli & Salmonella confirmed (May 2025)](https://en.tempo.co/read/2006994/5-cases-of-mbg-food-poisoning-since-january-2025)
12. [Tempo — Experts: Salmonella & Bacillus cereus (Sep 2025)](https://en.tempo.co/read/2052598/todays-top-3-news-experts-identify-salmonella-and-bacillus-cereus-in-free-nutritious-meal-poisoning-probe)
13. [Tempo — Health Minister: bacterial, viral, chemical causes (Oct 2025)](https://en.tempo.co/read/2053415/indonesian-health-minister-identifies-cause-of-free-meal-poisoning)
14. [Tempo — Presidential Staff: 4 contributing factors (Sep 2025)](https://en.tempo.co/read/2051106/presidential-staff-office-5000-people-poisoned-by-free-nutritious-meals)
15. [Tempo — Nitrite contamination in melon & salad (Oct 2025)](https://en.tempo.co/read/2054740/bgn-urged-to-pinpoint-cause-of-nitrite-contamination-in-free-meal-poisoning)
16. [Tempo — List of cases Jan-Sep 2025 (Sep 2025)](https://en.tempo.co/read/2052072/list-of-mbg-food-poisoning-cases-across-indonesia-january-september-2025)
17. [Food Safety News — Call for stricter controls (May 2025)](https://www.foodsafetynews.com/2025/05/call-for-stricter-controls-after-indonesian-meal-program-poisonings/)
18. [Food Safety News — Thousands sickened (Oct 2025)](https://www.foodsafetynews.com/2025/10/thousands-sickened-by-school-food-in-indonesia/)
19. [Kompas.id — MBG's weak food security (Sep 2025)](https://www.kompas.id/artikel/en-kemanan-pangan-mbg-lemah-bagaimana-mengatasinya)

### Kebijakan & Rencana Pemerintah:
20. [CryptoBriefing — Indonesia plans to embed AI in MBG (Jun 2026)](https://cryptobriefing.com/indonesia-ai-free-meal-program/)
21. [SEAsia.co — MBG halted early 2026 to strengthen food safety (Dec 2025)](https://seasia.co/2025/12/27/indonesia-to-halt-the-mbg-program-in-early-2026)
22. [RRI — BPOM & BGN strengthen oversight (Jun 2026)](https://rri.co.id/en/national/2397767/bpom-bgn-strengthen-oversight-of-free-nutritional-meal-program)
23. [SUCOFINDO — Large-scale kitchens need large-scale systems (Jun 2026)](https://www.sucofindo.co.id/en/articles/large-scale-kitchens-need-large-scale-systems/)

### Existing Solutions:
24. [King MBG by Clasnet — IoT Kitchen Monitoring](https://demombg.clasnet.co.id/)
25. [WHO Indonesia — Risk-Based Food Inspection pilot (2023)](https://www.who.int/indonesia/news-room/item/02-11-2023-breaking-new-ground--piloting-risk-based-food-inspection-in-five-districts-for-better-food-safety)
26. [Kompas.id — UNJ Pathogenic Bacteria Detection Kit (Jun 2026)](https://www.kompas.id/artikel/en-kit-pendeteksi-bakteri-patogen-untuk-mencegah-keracunan-pangan)

### Data Stunting & Nutrisi:
27. [WFP — Indonesia Country Strategic Plan 2026-2030 (stunting 21.5%)](https://www.wfp.org/operations/id03-indonesia-country-strategic-plan-2026-2030)
28. [Nutrition International — Stunting progress 30.8% → 19.8% (Jun 2026)](https://nutritionintl.org/news/all-blog-posts/why-indonesia-must-guard-its-hard-won-progress-against-stunting/)

---

*Document prepared for GarudaHacks 7.0 (16-18 Juli 2026)*  
*Track: Health + Safety*
