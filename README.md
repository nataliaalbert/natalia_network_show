<div align="center">

<!-- Dark header banner using shields.io -->
![natalia_network_show](https://img.shields.io/badge/natalia__network__show-PhD%20Research%20Pipeline-24292e?style=for-the-badge&logo=github&logoColor=white)

# natalia_network_show

### PhD Research — Natalia Albert Llorente

![Victoria University of Wellington](https://img.shields.io/badge/Victoria%20University%20of%20Wellington-School%20of%20Information%20Management-0366d6?style=flat-square&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-24292e?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-586069?style=flat-square)
![Branch](https://img.shields.io/badge/Branch-master-0366d6?style=flat-square&logo=git&logoColor=white)

**Supervisors:** Markus Luczak-Roesch · Alex Beattie

---

</div>

## 📋 What this is

This is the computational pipeline for my PhD research on housing policy and social cohesion in Aotearoa New Zealand. It processes a corpus of ~7,080 NZ government policy PDFs sourced from Policy Commons, extracts terms using a theoretically-grounded dictionary (the Four Pillars framework), and will eventually build a multipartite network connecting policy documents, actors, institutions, and social cohesion concepts.

The local project on my machine is called `natalia_network_show`. This repo holds the scripts.

---

## 📁 Project structure

```
natalia_network_show/
|
|-- corpus/
|   |-- raw/           <- original PDFs + metadata CSVs from Policy Commons
|   |-- output/        <- NZ-filtered PDFs + master metadata.csv
|   `-- samples/
|       |-- sample_A/  <- international housing corpus (variation testing)
|       |-- sample_B/  <- mixed corpus with NZ health docs
|       `-- sample_C/  <- micro-sample of NZ 7k corpus (baseline runs)
|
|-- dictionaries/
|   |-- dict1_human_built.xlsx   <- Four Pillars, expert built, running now
|   |-- dict2_llm_generated.xlsx <- LLM-generated (to build)
|   |-- dict3_corpus_derived.xlsx <- Corpus-derived via TF-IDF (to build)
|   `-- dict4_imbalanced.xlsx    <- Deliberately imbalanced stress test (to build)
|
|-- data/
|   |-- processed/    <- term counts + merged feature tables
|   |-- runs/         <- one subfolder per combination run
|   |-- ground_truth/ <- manually coded benchmark sample
|   |-- evaluation/   <- metrics, variable matrix
|   `-- network/      <- final graph files (future)
|
`-- scripts/
    |-- config.py          <- all paths live here, import this first
    |-- 01_data_integration.py
    |-- 02_filter_nz_only.py
    |-- 03_fix_discrepancy.py
    |-- 04_extract_terms.py
    |-- 05_metadata_merge.py
    `-- explore_data.py
```

---

## 🛠️ Scripts

### `config.py` — start here

Defines every file path in the project as a Python variable. All other scripts import this instead of hardcoding paths. Also auto-creates any missing folders on first run, so the structure above builds itself.

---

### Phase 1 — Corpus Assembly

**`01_data_integration.py`**
Loops through all the metadata CSVs (one per Policy Commons search query), combines them into a single master `metadata.csv`, and copies all unique PDFs into one `corpus/output/` folder. Handles deduplication — if the same PDF appears across multiple searches, it is only copied once.
- Input: `corpus/raw/metadata-search-*.csv` and `corpus/raw/search-{id}/artifact-*.pdf`
- - Output: `corpus/output/metadata.csv` and `corpus/output/artifact-*.pdf`
 
  - **`02_filter_nz_only.py`**
  - Reads the master metadata, keeps only rows where `Org. Country of Publication` is `NZ:New Zealand`, and deletes the non-NZ PDFs from the output folder. Overwrites `metadata.csv` in place with the NZ-only version.
  - > ⚠️ **Warning:** This script deletes files. Back up `corpus/output/` before running if unsure.
    >
    > **`03_fix_discrepancy.py`**
    > Quality check — compares every row in `metadata.csv` against the actual PDFs on disk. Any metadata row with no corresponding file gets flagged and saved.
    > - Output: `corpus/output/missing_files_metadata.csv`
    > - - Pass condition: missing file list is empty or less than 1% of corpus
    >  
    >   - ---
    >
    > ### Phase 2 — Term Extraction and Merging
    >
    > **`04_extract_terms.py`**
    > The main extraction script. Opens each PDF with PyMuPDF (`fitz`), extracts the full text, then uses regex to count how many times each term from `dict1_human_built.xlsx` appears. Only records non-zero matches. Case-insensitive.
    > - Output: `data/processed/policy_term_counts.csv` with columns: `document`, `category`, `term`, `count`
    >
    > - **`05_metadata_merge.py`**
    > - Takes the term counts from script 04 and joins them with the document metadata on artifact ID. The result is an enriched table where every term match row also carries the publisher, year, title, and document type of the source document.
    > - - Output: `data/processed/merged_term_metadata.csv` and `data/processed/unmatched_terms.csv` (if any)
    >  
    >   - ---
    >
    > ### Exploration
    >
    > **`explore_data.py`**
    > Runs summary analyses on the merged dataset and prints to terminal. Covers: corpus overview (total rows, unique documents, unique terms, total mentions), top 20 most frequent terms, term counts by Four Pillars category, top 15 publishers by document count, documents per year, and top 10 documents by total term mentions. Run after script 05.
    >
    > ---
    >
    > ## ▶️ Run order
    >
    > | Step | Script | What it does |
    > |------|--------|-------------|
    > | A | `config.py` | Folders created, paths ready |
    > | B | `01_data_integration.py` | Master `metadata.csv` and all PDFs in one place |
    > | C | `02_filter_nz_only.py` | NZ-only corpus |
    > | D | `03_fix_discrepancy.py` | Quality check |
    > | E | `04_extract_terms.py` | Term counts per document |
    > | F | `05_metadata_merge.py` | Enriched feature table |
    > | G | `explore_data.py` | See what you have got |
    >
    > ---
    >
    > ## 📊 First results
    >
    > Scripts 01 through 05 run against the full NZ corpus:
    >
    > | Metric | Value |
    > |--------|-------|
    > | Total term match rows | 70,257 |
    > | Unique documents matched | 6,922 of 7,080 (97.8%) |
    > | Unique terms matched | 105 |
    > | Total term mentions | 863,913 |
    > | Unmatched documents | 158 (likely scanned PDFs) |
    >
    > **By Four Pillars category:**
    >
    > | Category | Mentions | Share |
    > |----------|----------|-------|
    > | Groups | 462,489 | 53.6% |
    > | Institutions | 218,748 | 25.3% |
    > | Social Cohesion Dimensions | 165,272 | 19.1% |
    > | Housing Policy Instruments | 17,404 | 2.0% |
    >
    > The 26:1 ratio between Groups and Housing Policy Instruments is the headline finding from this phase. Māori (206,175 mentions) is the single most frequent term — nearly 2.5x the next term (Communities, 83,280). The corpus is deeply organised around indigenous rights and Crown-Māori relationships, which is theoretically significant.
    >
    > ---
    >
    > ## 🔭 What's next
    >
    > The testing plan uses a **3 datasets × 4 dictionaries = 12 combination runs** design, following Wang et al. (2025).
    >
    > Priority run order: `sample_C + dict1` (baseline), then `sample_C + dict2, dict3, dict4`, then repeat with `sample_A` and `sample_B`.
    >
    > Scripts still to write: `06` (LLM dict builder), `07` (corpus dict builder), `08` (imbalanced dict builder), `09` (sample corpora builder), `10` (master runner), `11` (evaluation), `12` (variable matrix), `13` (network construction — future).
    >
    > ---
    >
    > ## 📦 Dependencies
    >
    > ```bash
    > pip install pandas pymupdf openpyxl
    > ```
    >
    > ---
    >
    > ## 🙏 Acknowledgements
    >
    > - **Pipeline design:** Natalia Albert Llorente, with supervision from Markus Luczak-Roesch and support from Hassan Mustafa
    > - - **Dictionary framework:** Four Pillars (Social Cohesion Dimensions, Groups, Institutions, Housing Policy Instruments), grounded in Chan et al. (2006)
    >   - - **Benchmarking approach:** Wang et al. (2025), Rundell and Kilgarriff (2011), Guthrie et al. (1996)
    >     - - **Coding support:** Claude (Anthropic)
