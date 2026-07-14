# AI Farm Risk Simulator — Validated Research

**Ide:** AI-powered pre-planting risk simulator untuk petani kecil-menengah Indonesia  
**Input:** Lokasi, komoditas, waktu tanam  
**Output:** Simulasi risiko cuaca, prediksi harga saat panen, rekomendasi waktu tanam optimal  
**Last validated:** 14 Juli 2026

---

## 1. PROBLEM VALIDATION

### 1.1 Kerugian Akibat Cuaca (Data Resmi)

| Fakta | Data | Sumber |
|-------|------|--------|
| Kehilangan beras akibat El Niño 2023 | **1.2 juta ton** | [Tempo — Mentan Syahrul, Aug 2023](https://en.tempo.co/read/1766490/indonesia-loses-1-2m-tonnes-of-rice-over-el-nino-agriculture-minister-says) |
| Penurunan produksi beras akibat kekeringan Jan 2023 | **530.000 ton** (Jan-Sep vs tahun sebelumnya) | [Kompas.id, Aug 2023](https://www.kompas.id/baca/english/2023/08/02/en-duh-produksi-beras-ri-diproyeksikan-turun-530000-ton-gara-gara-el-nino) |
| Prediksi penurunan produksi beras 2023-2024 | **3.16% dan 3.75%** dibanding 2022 | [BioConf ICANARD 2024](https://www.bio-conferences.org/articles/bioconf/abs/2024/38/bioconf_icanard2024_01012/bioconf_icanard2024_01012.html) |
| Dampak per 1°C kenaikan suhu | **-4.500 ton/provinsi/tahun** | [Kompas.id, Oct 2023](https://www.kompas.id/baca/english/2023/10/12/en-faktor-iklim-tekan-produksi-padi) |
| Prediksi penurunan yield musim kering 2050s (RCP 8.5) | Hingga **-11.77%** | [MDPI Environments, 2021](https://www.mdpi.com/2076-3298/8/11/117/html) |
| El Niño → import beras naik | "Imports remain above average in 2024" | [Reuters, Feb 2024](https://www.reuters.com/markets/asia/indonesias-january-drought-points-lower-rice-harvest-higher-imports-2024-02-01/) |
| OECD: El Niño + food inflation | "5% decline in rice production" → pemerintah tingkatkan cadangan | [OECD Agriculture Policy 2024](https://www.oecd.org/en/publications/agricultural-policy-monitoring-and-evaluation-2024_74da57ed-en/full-report/component-19) |

### 1.2 Bencana Iklim yang Menimpa Petani

| Jenis Bencana | % Petani Terdampak | Sumber |
|---------------|-------------------|--------|
| Banjir | **46%** | [PLOS ONE — Kalimantan study, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296262) |
| Kekeringan | **30%** | [PLOS ONE — Kalimantan study, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296262) |
| Serangan hama | **24%** | [PLOS ONE — Kalimantan study, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296262) |
| Dampak signifikan terhadap pendapatan | **49%** petani surveyed | [PLOS ONE — Kalimantan study, 2024](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296262) |

### 1.3 Fluktuasi Harga Komoditas

| Fakta | Data | Sumber |
|-------|------|--------|
| Cabai rawit merah — penurunan harian | -8.58% dalam sehari (ke Rp69.750/kg) | [TVRI News/PIHPSN, Jun 2026](https://ekonomi.tvrinews.com/berita/t0ybqe0-harga-cabai-dan-bawang-merah-turun) |
| Cabai merah keriting — koreksi tajam | -13.69% (ke Rp42.800/kg) | [TVRI News/PIHPSN, Jun 2026](https://ekonomi.tvrinews.com/berita/t6nogk2-pihps-harga-bawang-merah-dan-cabai-kompak-turun) |
| Beras kualitas bawah — kenaikan | +0.69% (ke Rp14.600/kg) | [TVRI News/PIHPSN, Jun 2026](https://ekonomi.tvrinews.com/berita/tgydbm2-fluktuasi-pangan-harga-beras-naik-cabai-melandai) |
| Gula pasir lokal — lonjakan | +3.4% dalam sehari (ke Rp19.750/kg) | [TVRI News/PIHPSN, Jun 2026](https://ekonomi.tvrinews.com/berita/tgydbm2-fluktuasi-pangan-harga-beras-naik-cabai-melandai) |
| Cabai = penyumbang utama inflasi pangan | Confirmed by PIHPSN | [TVRI News, Jun 2026](https://ekonomi.tvrinews.com/berita/t9mbiml-harga-cabai-anjlok-inflasi-pangan-melandai) |

**Insight:** Petani yang menanam cabai menghadapi volatilitas ekstrem — harga bisa jatuh >13% dalam hitungan hari. Tanpa prediksi, petani menanam "buta" dan baru tahu harga jatuh saat sudah panen.

### 1.4 Persepsi Petani Sendiri

| Fakta | Sumber |
|-------|--------|
| Mayoritas petani setuju ada perubahan variabel klimatologi yang mempengaruhi aktivitas mereka, terutama presipitasi dan suhu | [MDPI Sustainability — Kebumen study, 2021](https://www.mdpi.com/2071-1050/13/13/7069) |
| Petani Indonesia umumnya membuat kalender pertanian berdasarkan **pengalaman pribadi** tanpa mempertimbangkan fenomena iklim global (La Niña/El Niño) | [MDPI Sustainability — Coping Mechanism, 2021](https://mdpi.com/2071-1050/13/11/6495/htm) |
| Climate change meningkatkan frekuensi banjir dan kekeringan, menjadi ancaman signifikan bagi petani padi kecil | [IntechOpen — Rice sector climate policy, 2020](https://www.intechopen.com/chapters/73617) |

---

## 2. TARGET USER

### 2.1 Ukuran Pasar

| Data | Angka | Sumber |
|------|-------|--------|
| Penduduk bekerja di sektor pertanian | **28.21%** dari 139.85 juta pekerja (~39.5 juta orang) | [Kompas.id / BPS Aug 2023](https://www.kompas.id/baca/english/2024/03/06/en-menahan-pertambahan-petani-gurem) |
| Rumah tangga miskin yang bergantung pada pertanian | **48.86%** | [Kompas.id, Oct 2024](https://www.kompas.id/artikel/en-mendengar-dari-petani) |
| Petani gurem (<0.5 hektar) — peningkatan | **+2 juta petani** dalam dekade terakhir | [Jakarta Post / BPS Dec 2023](https://www.thejakartapost.com/business/2024/10/18/smallholders-must-organize-to-succeed-eu-commissioner) |
| Produktivitas petani kecil | Lemah — "access to technology remains weak" | [FAO — Small Family Farming in Indonesia](https://www.fao.org/family-farming/detail/en/c/1111082/) |

### 2.2 Digital Access & Literacy

| Data | Angka | Sumber |
|------|-------|--------|
| Pertanian = sektor **paling tidak terdigitalisasi** di Indonesia | Confirmed | [Brookings Institution, 2022](https://www.brookings.edu/articles/the-digital-transformation-of-agriculture-in-indonesia/) |
| Petani internet vs non-internet: selisih pendapatan | Internet user = **+29.6% farm earnings** | [World Scientific / Indonesia Labor Force Survey, 2024](https://www.worldscientific.com/doi/full/10.1142/S0116110525500027) |
| Digital access perempuan Indonesia 2022 | 64% (naik dari 51% di 2020), gap 6pp vs laki-laki | [OECD Economic Survey Indonesia 2024](https://www.oecd.org/en/publications/2024/11/oecd-economic-surveys-indonesia-2024_e3ab8960/full-report/making-the-digital-transformation-work-for-all_3eaf6d8c.html) |
| Gap digital literacy urban vs rural | "Significant gap remains in digital literacy and utilization capacity" | [ResearchGate — Urban-Rural Divide, 2025](https://www.researchgate.net/publication/394752633_Bridging_the_Urban-Rural_Divide_Leveraging_Technology_for_Development_and_Connectivity_in_Small_Village_Indonesia) |
| Digital hotspots | Masih terkonsentrasi di Jawa; eastern Indonesia = low spots | [MDPI Sustainability — Digital Society Index, 2024](https://www.mdpi.com/2071-1050/16/24/11258) |

**Implikasi untuk MVP:** Solusi harus sederhana (WhatsApp-based atau low-data app), bukan complex web app. Target awal bisa petani di Jawa yang sudah punya smartphone.

### 2.3 Asuransi Pertanian (Safety Net Gap)

| Data | Angka | Sumber |
|------|-------|--------|
| Program AUTP (Asuransi Usaha Tani Padi) | Launched 2015 oleh Kementan | [BioConf 2024](https://www.bio-conferences.org/articles/bioconf/abs/2024/38/bioconf_icanard2024_04004/bioconf_icanard2024_04004.html) |
| Coverage AUTP vs total lahan | **300-400K ha** dari **4 juta ha** (hanya ~8-10%) | [IDN Financials / Jasindo Syariah, 2025](https://www.idnfinancials.com/news/65050/jasindo-syariahs-at-yaltha-ris-agriinsurance-potential-is-big) |
| Subsidi pemerintah untuk premi AUTP | **80%** dari annual fee | [OECD Agriculture Policy 2023](https://www.oecd.org/en/publications/2023/10/agricultural-policy-monitoring-and-evaluation-2023_7cc05c6a/full-report/indonesia_4ff13b00.html) |
| Hambatan adopsi AUTP | Low awareness, procedural complexity, **digital literacy barriers** | [Atlantis Press — Multi-Hazard Prone Area study](https://www.atlantis-press.com/article/126025374.pdf) |
| AXA Climate — parametric insurance | Promoting rapid funding untuk smallholders (drought/excessive rainfall) | [AXA Climate, 2024](https://climate.axa/publications/natural-disasters-smallholder-farmers-indonesia/) |
| Pemerintah aktifkan AUTP untuk banjir | "Negara tidak boleh membiarkan petani menanggung kerugian sendiri" | [RRI, 2025](https://rri.co.id/en/national/2215015/govt-activates-rice-farm-insurance-for-flood-affected-farmers) |

**Insight:** 90%+ petani padi TIDAK punya asuransi. Risk simulation tool bisa jadi "pre-insurance decision support" — membantu petani assess risk SEBELUM menanam, bukan claim SETELAH gagal panen.

---

## 3. DATASET AVAILABILITY (Confirmed Accessible)

### 3.1 Harga Komoditas

| Dataset | Coverage | Format | URL |
|---------|----------|--------|-----|
| **World Bank RTFP** (Real-Time Food Prices) | 222 markets di Indonesia, 2007-2026, updated weekly | CSV | [microdata.worldbank.org/catalog/6166](https://microdata.worldbank.org/catalog/6166) |
| PIHPSN (Pusat Informasi Harga Pangan Strategis Nasional) | Harian, seluruh Indonesia | Web/API | [hargapangan.id](https://hargapangan.id) |
| BPS — Statistik Harga Komoditas Pertanian | Bulanan & tahunan, per provinsi | PDF/API | [webapi.bps.go.id](https://webapi.bps.go.id/developer/) |

> **Note:** User sudah punya file `IDN_RTFP_mkt_2007_2026-07-06 2.csv` di project folder — ini World Bank RTFP dataset.

### 3.2 Cuaca & Iklim

| Dataset | Coverage | Format | URL |
|---------|----------|--------|-----|
| **BMKG Open Data** — Prakiraan Cuaca | Seluruh Indonesia, 3-harian | JSON API | [data.bmkg.go.id/prakiraan-cuaca](https://data.bmkg.go.id/prakiraan-cuaca) |
| BMKG Data Online — Historical | Curah hujan, suhu, kelembapan historis per stasiun | CSV downloadable | [dataonline.bmkg.go.id](https://dataonline.bmkg.go.id/) |
| BMKG REST API (community) | Weather forecast + earthquake data | JSON | [bmkg-restapi.vercel.app](https://bmkg-restapi.vercel.app/) |
| BMKG API Scraper → CSV | Scraping BMKG ke CSV | Python/CSV | [github.com/ahmadzakiakmal/BMKG-API-Scraper](https://github.com/ahmadzakiakmal/BMKG-API-Scraper) |
| GitHub infoBMKG/data-cuaca | Official open data BMKG | JSON | [github.com/infoBMKG/data-cuaca](https://github.com/infoBMKG/data-cuaca) |

### 3.3 Produksi Pertanian

| Dataset | Coverage | Format | URL |
|---------|----------|--------|-----|
| **BPS WebAPI** — Produksi Padi & Komoditas | Per provinsi, per tahun | JSON API | [webapi.bps.go.id](https://webapi.bps.go.id/developer/) |
| BPS Python Package (stadata) | Akses programmatic ke semua data BPS | Python | [github.com/bps-statistics/stadata](https://github.com/bps-statistics/stadata) |
| Kementan — epublikasi.pertanian.go.id | Data produksi per komoditas | PDF/Reports | [epublikasi.pertanian.go.id](https://epublikasi.pertanian.go.id) |

### 3.4 Comprehensive Reference

| Resource | Deskripsi | URL |
|----------|-----------|-----|
| **Indonesia Government APIs** (57 APIs) | Referensi lengkap semua API pemerintah Indonesia + Python examples | [github.com/suryast/indonesia-gov-apis](https://github.com/suryast/indonesia-gov-apis) |

---

## 4. FEASIBILITY — ML/AI PREDICTION ACCURACY

### 4.1 Crop Yield Prediction

| Method | Accuracy | Context | Sumber |
|--------|----------|---------|--------|
| Random Forest | **R² = 0.99** | Crop yield prediction | [ResearchGate, 2024](https://www.researchgate.net/publication/384404644_Sowing_Intelligence_Advancements_in_Crop_Yield_Prediction_Through_Machine_Learning_and_Deep_Learning_Approaches) |
| Deep Learning (general) | **93% accuracy**, error -65% | Crop yield | [Preprints.org, 2025](https://www.preprints.org/manuscript/202505.0814) |
| Extra Trees Classifier | **99.15% accuracy** | Crop yield with weather + soil data | [ResearchGate — Ensemble ML, 2024](https://www.researchgate.net/publication/386875003_Crop_Yield_Prediction_Using_Ensemble_Machine_Learning_Techniques) |
| MODIS + Meteorological + ML | Strong R² | Paddy prediction — solar radiation, soil moisture, NDVI, ET | [Springer, 2026](https://link.springer.com/10.1007/s10333-026-01077-4) |
| Causal Learning + Clustering (Indonesia) | Silhouette 0.35 | Meteorological → crop yield dependency graphs | [Nature Scientific Reports, 2026](https://www.nature.com/articles/s41598-026-40418-5) |

### 4.2 Food Price Prediction (Indonesia-specific)

| Method | Accuracy/Error | Context | Sumber |
|--------|---------------|---------|--------|
| Ridge Regression | MSE 43.045 | Food commodity prices Aceh 2025-2028 | [ISTP Press JAIT, 2025](https://ojs.istp-press.com/jait/article/view/912) |
| LSTM Multivariate | Proven approach | Forecasting with external factors | [AIP Conference Proceedings, 2024](https://pubs.aip.org/aip/acp/article/3098/1/040044/3318030/Multivariate-forecasting-prices-of-basic-food) |
| Extreme Learning Machine (ELM) | Validated | Predicting food prices in East Java | [ResearchGate, 2020](https://www.researchgate.net/publication/346423292_Food_Commodity_Price_Prediction_in_East_Java_Using_Extreme_Learning_Machine_ELM_Method/) |
| Twitter Nowcasting | Proven | Daily price fluctuation: beef, chicken, onion, chili (Indonesia) | [PeerJ Computer Science, 2017](https://peerj.com/articles/cs-126/) |
| Palm oil price forecast (Indonesia) | **91-92% accuracy** | Most reliable environment | [Vespertool, 2025](https://vespertool.com/knowledge-hub/oils-and-fats/palm-oil/indonesia-crude-palm-oil-price-forecasts/) |
| Satellite + Cellular Automata | Predicted 2%↓ production, 3%↑ demand → 57%↓ surplus | Rice status forecasting Malang | [MDPI Sustainability, 2022](https://www.mdpi.com/2071-1050/14/15/8972) |

**Kesimpulan feasibility:** Prediksi harga komoditas dan yield dengan ML sudah terbukti di konteks Indonesia. Bukan riset baru — tinggal implementasi.

---

## 5. COMPETITIVE LANDSCAPE

### 5.1 Existing AgriTech Indonesia

| App/Platform | What It Does | What It DOESN'T Do |
|--------------|-------------|---------------------|
| **Neurafarm (Dr. Tania)** | AI crop disease identification, treatment recs | Tidak prediksi harga, tidak simulasi risiko pre-planting |
| **Agrimate** (Microsoft Imagine Cup 2024) | Multiplatform farming solution (Azure-based) | Tidak spesifik pre-planting risk decision |
| **LISA** (Mercy Corps) | Agricultural advisory tips, financial literacy | Tidak AI-based, tidak real-time prediction |
| **Sayurbox** | Supply chain farm-to-consumer | Marketplace, bukan decision support |
| **RegoPantes** | Farm-to-home, cut middlemen | Marketplace, bukan prediction tool |
| **TaniHub Group** | B2B agri e-commerce | Logistics, bukan risk analytics |

### 5.2 AgriTech Ecosystem Model (Brookings/IFC)

Indonesia's AgriTech berkembang di 5 model bisnis utama ([Brookings, 2022](https://www.brookings.edu/articles/the-digital-transformation-of-agriculture-in-indonesia/)):
1. **Farmers advisory** ← closest to our idea, tapi existing apps fokus pada disease/treatment
2. Peer-to-peer lending
3. Traceability
4. Digital marketplaces
5. Mechanization

**Gap yang kita isi:** Tidak ada "farmers advisory" yang fokus pada **pre-planting risk simulation** (cuaca × harga × waktu tanam). Semua advisory existing = reactive (setelah menanam), bukan predictive (sebelum menanam).

---

## 6. ADDITIONAL SUPPORTING DATA

### 6.1 Economic Impact of Agriculture

| Data | Angka | Sumber |
|------|-------|--------|
| USDA: El Niño historically = significant climate problems for Indonesia | Deficient rainfall/drought pattern | [USDA IPAD](https://www.fas.usda.gov/data/southeast-asia-historical-el-ni-o-related-crop-yield-impact) |
| Agriculture sector vulnerable to climate change | "implications for food and nutrient security" | [World Bank — Indonesia CCDR](http://knowledge4policy.ec.europa.eu/publication/indonesia-country-climate-development-report_en) |
| Hidden costs of Indonesia's food system | Deforestation, peat fires, biodiversity loss | [WRI Indonesia, 2025](https://wri-indonesia.org/en/publications/hidden-costs-indonesias-food-system) |
| Indonesia can end hunger by 2030 | Dengan investment di agricultural R&D, irrigation, rural infra | [ADB, 2020](https://www.adb.org/publications/indonesia-food-agriculture-development-2020-2045) |

### 6.2 Government Direction (Peluang Alignment)

| Signal | Detail | Sumber |
|--------|--------|--------|
| DBS Foundation program | Meningkatkan produktivitas **80.000 petani kecil** di NTT, 2025-2028 | [DBS Indonesia](https://www.dbs.com/indonesia/bh/foundation/default.page) |
| SPI (Serikat Petani Indonesia) | Renewed call for food sovereignty + agrarian reform, Jul 2025 | [Via Campesina, 2025](https://viacampesina.org/en/2025/07/indonesia-spi-closes-5th-congress-with-renewed-call-for-agrarian-reform-and-food-sovereignty/) |
| Pemerintah subsidize 80% premi AUTP | Government already investing in risk protection | [OECD, 2023](https://www.oecd.org/en/publications/2023/10/agricultural-policy-monitoring-and-evaluation-2023_7cc05c6a/full-report/indonesia_4ff13b00.html) |
| AXA Climate parametric insurance | International players entering Indonesian agri-risk market | [AXA Climate, 2024](https://climate.axa/publications/natural-disasters-smallholder-farmers-indonesia/) |
| ArXiv 2025: Stuttering-Aware ASR for Indonesian | Research community actively working on Indonesian-specific AI solutions | [ArXiv 2601.03727](https://arxiv.org/abs/2601.03727) |

### 6.3 Relevant Academic Work (Indonesia-specific)

| Paper | Key Finding | Sumber |
|-------|-------------|--------|
| "Assessing risks of climate variability for Indonesian rice agriculture" | Quantified climate risk for rice across Indonesia | [PMC, 2007](https://pmc.ncbi.nlm.nih.gov/articles/PMC1876519/) |
| "What Drives Climate Change Adaptation in Smallholder Potato Farmers" | Multivariate probit analysis of adaptation determinants in East Java | [MDPI Atmosphere, 2022](https://www.mdpi.com/2073-4433/13/1/113/htm) |
| "Integrated analysis of meteorological conditions and agricultural yields in Indonesia" | Causal learning reveals dependency between weather and yields | [Nature Sci Reports, 2026](https://www.nature.com/articles/s41598-026-40418-5) |
| Spatial Heterogeneity of Rice Production vs ENSO | Tangerang = β=-33,371 t/year significant vulnerability | [FAO AGRIS, 2025](https://agris.fao.org/search/es/records/69b96ccdce5e0ae4f878e23f) |

---

## 7. RISKS & CHALLENGES

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Digital literacy petani rendah | **High** | Target petani muda / kelompok tani yang sudah punya smartphone. Atau integrasi via penyuluh pertanian. |
| Data BMKG historis mungkin perlu scraping manual | Medium | Gunakan BMKG API Scraper (GitHub) + World Bank RTFP yang sudah jadi CSV. |
| Akurasi prediksi di level hyperlocal (desa) | Medium | Mulai di level kabupaten/kota dulu, bukan desa. 222 markets di RTFP sudah cukup granular. |
| User acquisition untuk petani | **High** | Partnership dengan penyuluh pertanian, kelompok tani, atau embed di AUTP flow. |
| Kompetitor besar (Google, Microsoft) bisa masuk | Low-Medium | First mover advantage di Indonesia-specific context. Data lokal = moat. |
| Hackathon scope (48 jam) | Medium | Fokus 1 komoditas (beras/cabai), 1 region, demo prediction + risk score. |

---

## 8. MVP SCOPE (Recommended for Hackathon)

### Input
- Lokasi (kabupaten/kota)
- Komoditas (beras ATAU cabai)
- Rencana waktu tanam (bulan)

### Output
- **Weather Risk Score** (0-100): berdasarkan historical curah hujan + ENSO forecast di lokasi tersebut untuk periode tanam
- **Price Forecast**: prediksi harga komoditas di waktu panen (3-4 bulan ke depan) berdasarkan RTFP historical data
- **Recommendation**: "Tanam sekarang (risk rendah)" vs "Tunda 2 minggu (curah hujan tinggi)" vs "Pertimbangkan komoditas lain"

### Data yang Sudah Ada
- `IDN_RTFP_mkt_2007_2026-07-06 2.csv` — World Bank food price data ✓

### Data yang Perlu Di-fetch
- BMKG historical rainfall per lokasi (via API/scraper)
- BPS produksi padi per wilayah (via stadata Python package)

---

## 9. KEY QUOTES FOR PITCH

> "Agriculture is the **least digitized sector** in Indonesia, and as a result, productivity gains and development opportunities are left untapped."
> — Brookings Institution, 2022

> "Self-employed farmers who use the internet have **29.6% more farm earnings** than those who do not."
> — World Scientific / Indonesia Labor Force Survey, 2024

> "Indonesia lost **1.2 million tonnes** of rice over El Niño."
> — Agriculture Minister Syahrul Yasin Limpo, Aug 2023

> "Out of 4 million hectares of agricultural land, AUTP coverage only reaches **300,000-400,000 hectares** per year."
> — Jasindo Syariah / IDN Financials, 2025

> "The state must not allow farmers to bear the losses alone due to flooding and the impacts of climate change."
> — Indonesian Government via RRI, 2025

> "Climate change increases the frequency of flood and drought and is a significant threat to smallholder rice farming in Indonesia."
> — IntechOpen / Rice Climate Policy, 2020

---

*Document compiled for GarudaHacks 7.0 Agriculture Track research validation*  
*Sources cross-referenced and verified 14 Juli 2026*
