# Formula Ideation Hackathon — 17 Poin

Extracted dari proses iterasi 20+ ide untuk GarudaHacks 7.0. Ini pattern yang bikin ide survive vs mati.

---

## The Formula

### Core (Ide-nya)

**1. Bantu orang yang TERDAMPAK tapi INVISIBLE.**
Bukan orang yang "punya masalah" — tapi secondary victim yang kena dampak dan selama ini gak dianggap perlu bantuan.

**2. Problem sudah banyak yang tahu exist — tapi belum ada yang solve dari ANGLE ini.**
Bukan cari masalah baru. Tapi lihat masalah lama dari sisi yang belum ada orang lihat.

**3. Ada EVIDENCE yang bilang intervensi di sisi ini lebih efektif.**
Bukan opini "harusnya gini." Tapi paper/data yang support bahwa approach kamu itu scientifically lebih impactful dari approach yang sudah ada.

**4. Problem punya URGENCY / deadline alami.**
Bukan problem yang bisa "nanti aja." Ada window yang kalau lewat = damage permanent atau opportunity hilang.

### User & Behaviour

**5. User BENAR-BENAR akan pakai — bukan "harusnya pakai."**
Test: "Kalau besok app ini ada, apakah user pakai TANPA disuruh?" Kalau jawaban = "ya kalau mereka tahu" → red flag.

**6. Behaviour user SUDAH exist — kamu enhance, bukan create new.**
Jangan fight existing habit. Ride on top of it. Masuk ke slot kehidupan yang sudah ada.

**7. Solve ACTION gap — bukan info gap.**
Produk yang baik MELAKUKAN sesuatu untuk user — bukan memberitahu user untuk melakukan sesuatu. "Kasih informasi → orang berubah" = almost never works.

**8. Jangan fight existing behaviour — ride on it.**
Kalau user harus download app baru, belajar UI baru, ingat buka tiap hari — itu friction. Masuk ke flow yang sudah ada (training schedule, bedtime routine, dll).

### Demo & Presentation

**9. Demo bikin orang FEEL, bukan cuma understand.**
Juri harus merasakan sesuatu — bukan cuma ngangguk "oh iya masuk akal." Feel > understand.

**10. Demo 90 detik — paham + feel tanpa penjelasan.**
Kalau butuh 5 menit explain, terlalu complex. Kalau juri langsung bilang "oh shit" dalam 10 detik pertama — kamu menang.

**11. Punya 1 KALIMAT yang bikin ruangan diam.**
Kalau gak bisa bikin orang diam dalam 1 kalimat, ide kurang tajam. Ini kalimat pembuka pitch kamu.

### Tech & Differentiator

**12. Tech ENABLE something previously impossible — bukan gimmick.**
"Kita pakai AI karena keren" = gimmick. "AI unlock sesuatu yang sebelumnya gak bisa dilakukan" = genuine.

**13. Differentiator JELAS dalam 1 kalimat.**
Kalau kamu perlu explain >2 kalimat kenapa ini beda dari yang ada — ide kurang beda. "Same but in Indonesian" bukan differentiator.

**14. Why NOW — kenapa ide ini baru bisa exist sekarang.**
Tech baru? Kebijakan baru? Event baru? Kalau ide ini bisa exist 5 tahun lalu tapi gak ada yang bikin — mungkin memang gak dibutuhkan.

### Revenue & Sustainability

**15. Revenue dari pihak yang PUNYA UANG + INCENTIVE.**
Jangan target orang miskin/korban sebagai paying customer. Cari siapa yang punya budget dan alasan clear untuk bayar (avoid lawsuit, comply regulasi, competitive advantage, CSR).

### Validation

**16. Problem SPESIFIK ke 1 kelompok orang — bukan "everyone."**
Kalau gak bisa bilang "Namanya X, umur Y, tinggal di Z, masalahnya ABC" — scope terlalu lebar. Specific > broad.

**17. Kritik sendiri SEBELUM juri kritik.**
Destroy ide dari segala angle: siapa pakai? udah ada? data mana? track fit? revenue? demo? gimmick? Ide yang lolos semua = defensible. Ide yang gak bisa kamu kritik sendiri = juri akan hancurkan di Q&A.

---

## Quick Checklist (Sebelum Commit ke Ide)

- [ ] Siapa secondary victim yang invisible?
- [ ] Angle baru dari masalah yang sudah dikenal?
- [ ] Ada paper/data yang support approach ini?
- [ ] Urgency — kenapa gak bisa nanti?
- [ ] User benar-benar akan pakai?
- [ ] Behaviour sudah exist yang bisa di-ride?
- [ ] Solve action, bukan info?
- [ ] Demo 90 detik — feel, bukan cuma paham?
- [ ] 1 kalimat yang bikin diam?
- [ ] Tech enable something new, bukan gimmick?
- [ ] Differentiator 1 kalimat?
- [ ] Why now?
- [ ] Revenue dari yang punya uang?
- [ ] Spesifik ke 1 kelompok?
- [ ] Sudah kritik sendiri dari semua angle?

Kalau ada yang gak bisa dijawab dengan yakin — ide perlu di-refine atau pivot.

---

## Output: Folder Struktur per Ide

Setelah ide lolos checklist, dokumentasikan dalam folder dengan struktur ini:

```
[nama-ide]/
├── README.md                   → One-liner + overview + link ke semua file
├── 01-problem.md               → Inti masalah + data statistik + skala problem
├── 02-why-[angle].md           → Kenapa approach/angle ini (bukan yang obvious) — evidence-based
├── 03-differentiator.md        → Pembeda dari existing solutions (tabel comparison)
├── 04-solution-flow.md         → Solusi + flow diagram + tech stack
├── 05-revenue.md               → Revenue model + unit economics + why they pay
├── 06-track-fit.md             → Keselarasan dengan track hackathon (quote deskripsi track)
```

### Isi tiap file:

**README.md:**
- Nama project (catchy, memorable)
- 1 one-liner yang bikin ruangan diam
- Table of contents dengan link ke setiap file

**01-problem.md:**
- Inti masalah dalam 2-3 kalimat
- Tabel data dengan angka + sumber link
- Skala (berapa orang terdampak)
- Kenapa urgent / deadline alami

**02-why-[angle].md:**
- Kenapa approach ini bukan yang obvious (evidence)
- Quotes dari paper/riset yang support
- Comparison tabel: approach A (yang biasa) vs approach B (kita) — mana yang evidence bilang lebih efektif
- Nama file sesuai angle (contoh: `02-why-hr-not-stutterer.md`, `02-why-mothers-voice.md`, `02-why-parents-cant.md`)

**03-differentiator.md:**
- Tabel: existing vs kita
- 1 kalimat differentiator
- Kenapa zero/minimal competitor di angle ini

**04-solution-flow.md:**
- Deskripsi solusi 1-2 kalimat
- Flow diagram (ASCII art)
- Contoh output/scorecard ke user
- Tech stack tabel

**05-revenue.md:**
- Tabel streams (customer, model, why they pay)
- Unit economics
- Cost-benefit argument
- Target customer awal yang realistis

**06-track-fit.md:**
- Quote deskripsi track hackathon
- Tabel kata kunci track → bagaimana ide fit
- Argue kenapa ini BUKAN track lain
- Why now / timing
