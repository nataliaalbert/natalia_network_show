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

1. config.py — folders created, paths ready
2. 2. 01_data_integration — master metadata.csv + all PDFs in one place
   3. 3. 02_filter_nz_only — NZ-only corpus
      4. 4. 03_fix_discrepancy — quality check
         5. 5. 04_extract_terms — term counts per document
            6. 6. 05_metadata_merge — enriched feature table
               7. 7. explore_data — see what you've got
                 
                  8. ---
                 
                  9. ## First results
                 
                  10. Scripts 01–05 run against the full NZ corpus: 70,257 term match rows, 6,922 of 7,080 unique documents matched (97.8%), 105 unique terms, 863,913 total mentions, 158 unmatched documents (likely scanned PDFs).
                 
                  11. By Four Pillars category: Groups 462,489 (53.6%), Institutions 218,748 (25.3%), Social Cohesion Dimensions 165,272 (19.1%), Housing Policy Instruments 17,404 (2.0%).
                 
                  12. Maori (206,175 mentions) is the single most frequent term.
                 
                  13. ---
                 
                  14. ## Dependencies
                 
                  15. pip install pandas pymupdf openpyxl
                 
                  16. ---
                 
                  17. ## Acknowledgements
                 
                  18. Pipeline design: Natalia Albert Llorente, with supervision from Markus Luczak-Roesch and support from Hassan Mustafa.
                  19. Dictionary framework: Four Pillars, grounded in Chan et al. (2006).
                  20. Benchmarking approach: Wang et al. (2025).
                  21. Coding support: Claude (Anthropic).
