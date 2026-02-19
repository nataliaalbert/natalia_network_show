# natalia_network_show

## PhD Research — Natalia Albert Llorente

**Victoria University of Wellington · School of Information Management**

Supervisors: Markus Luczak-Roesch · Alex Beattie

---

## What this is

This is the computational pipeline for my PhD research on housing policy and social cohesion in Aotearoa New Zealand. It processes a corpus of ~7,080 NZ government policy PDFs sourced from Policy Commons, extracts terms using a theoretically-grounded dictionary (the Four Pillars framework), and will eventually build a multipartite network connecting policy documents, actors, institutions, and social cohesion concepts.

The local project on my machine is called `natalia_network_show`. This repo holds the scripts.

---

## Run order

| Step | Script | What it does |
|------|--------|--------------|
| 1 | config.py | Folders created, paths ready |
| 2 | 01_data_integration.py | Master metadata.csv and all PDFs in one place |
| 3 | 02_filter_nz_only.py | NZ-only corpus |
| 4 | 03_fix_discrepancy.py | Quality check |
| 5 | 04_extract_terms.py | Term counts per document |
| 6 | 05_metadata_merge.py | Enriched feature table |
| 7 | explore_data.py | See what you have got |

---

## First results

Scripts 01 through 05 run against the full NZ corpus: 70,257 term match rows, 6,922 of 7,080 unique documents matched (97.8%), 105 unique terms, 863,913 total mentions, 158 unmatched documents (likely scanned PDFs).

By Four Pillars category: Groups 462,489 (53.6%), Institutions 218,748 (25.3%), Social Cohesion Dimensions 165,272 (19.1%), Housing Policy Instruments 17,404 (2.0%).

Maori (206,175 mentions) is the single most frequent term — nearly 2.5x the next term (Communities, 83,280).

---

## Dependencies

```
pip install pandas pymupdf openpyxl
```

---

## Acknowledgements

Pipeline design: Natalia Albert Llorente, with supervision from Markus Luczak-Roesch and support from Hassan Mustafa.

Dictionary framework: Four Pillars (Social Cohesion Dimensions, Groups, Institutions, Housing Policy Instruments), grounded in Chan et al. (2006).

Benchmarking approach: Wang et al. (2025).

Coding support: Claude (Anthropic).
