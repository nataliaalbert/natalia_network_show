import sys
sys.path.insert(0, r"C:\natalia_network_show")
import config
import pandas as pd

# -------------------------------------------------------------------
# Script 05 — Metadata Merge
# -------------------------------------------------------------------
# PURPOSE:
#   After script 04 extracts term counts from PDFs, this script
#   merges those term counts back with the document metadata
#   (title, organisation, year, document type etc.) from metadata.csv
#   The result is a single enriched CSV that links WHAT was found
#   to WHERE it was found and WHO produced it.
#
# INPUT:
#   - corpus/output/metadata.csv          (from scripts 01-02)
#   - data/processed/policy_term_counts.csv  (from script 04)
#
# OUTPUT:
#   - data/processed/merged_term_metadata.csv
# -------------------------------------------------------------------

def main():
    # ── Load inputs ────────────────────────────────────────────────
    metadata_path    = config.CORPUS_OUTPUT / "metadata.csv"
    term_counts_path = config.DATA_PROCESSED / "policy_term_counts.csv"

    if not metadata_path.exists():
        print(f"❌ metadata.csv not found at {metadata_path}")
        print("   Run scripts 01 and 02 first.")
        return

    if not term_counts_path.exists():
        print(f"❌ policy_term_counts.csv not found at {term_counts_path}")
        print("   Run script 04 first.")
        return

    metadata_df    = pd.read_csv(metadata_path)
    term_counts_df = pd.read_csv(term_counts_path)

    print(f"📋 Metadata rows:     {len(metadata_df)}")
    print(f"📊 Term count rows:   {len(term_counts_df)}")

    # ── Build document filename column in metadata for joining ─────
    # The term counts use filenames like artifact-XXXXX-file-YYYYY.pdf
    # We recreate that same filename from the metadata columns
    metadata_df["document"] = (
        "artifact-" + metadata_df["Artifact ID"].astype(str) +
        "-file-"    + metadata_df["File ID"].astype(str) + ".pdf"
    )

    # ── Merge ──────────────────────────────────────────────────────
    merged_df = term_counts_df.merge(
        metadata_df,
        on="document",
        how="left"
    )

    # ── Check for unmatched rows ───────────────────────────────────
    unmatched = merged_df[merged_df["Artifact ID"].isna()]
    if len(unmatched) > 0:
        print(f"⚠️  {len(unmatched)} term count rows could not be matched to metadata.")
        print("   This usually means those PDFs were filtered out in script 02.")
        unmatched.to_csv(config.DATA_PROCESSED / "unmatched_terms.csv", index=False)
        print(f"   Saved unmatched rows to: data/processed/unmatched_terms.csv")

    # ── Save output ────────────────────────────────────────────────
    output_path = config.DATA_PROCESSED / "merged_term_metadata.csv"
    merged_df.to_csv(output_path, index=False)

    print(f"\n✅ Merged dataset saved to: {output_path}")
    print(f"   Total rows:     {len(merged_df)}")
    print(f"   Matched rows:   {len(merged_df) - len(unmatched)}")
    print(f"   Columns:        {list(merged_df.columns)}")
    print(f"\nPreview:")
    print(merged_df[["document", "category", "term", "count"]].head(10))

if __name__ == "__main__":
    main()
