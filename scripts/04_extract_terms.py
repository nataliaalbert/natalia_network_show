import sys
sys.path.insert(0, r"C:\natalia_network_show")
import config
import re
import pandas as pd
import fitz  # PyMuPDF

# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def load_terms_from_excel(path):
    df = pd.read_excel(path)
    records = []
    for col in df.columns:
        for value in df[col].dropna().unique():
            term = str(value).strip()
            if term:
                records.append({"category": col, "term": term})
    return pd.DataFrame(records).drop_duplicates().reset_index(drop=True)

def pdf_to_text(path):
    doc  = fitz.open(str(path))
    text = ''.join(page.get_text() + '\n' for page in doc)
    doc.close()
    return text

def count_term(text, term):
    return len(re.findall(re.escape(term), text, flags=re.IGNORECASE))

# -------------------------------------------------------------------
# Main pipeline
# -------------------------------------------------------------------
def main():
    # Load terms from dictionary
    terms_df = load_terms_from_excel(config.DICT_1_HUMAN)
    print(f"📖 Loaded {len(terms_df)} terms from dictionary.")

    # Find PDFs
    pdf_files = list(config.CORPUS_RAW.glob("*.pdf"))
    if not pdf_files:
        print(f"❌ No PDFs found in {config.CORPUS_RAW}")
        return

    print(f"📄 Found {len(pdf_files)} PDFs")
    results = []

    for pdf_path in pdf_files:
        print(f"   Reading {pdf_path.name}...")
        text = pdf_to_text(pdf_path)
        for _, row in terms_df.iterrows():
            c = count_term(text, row["term"])
            if c > 0:
                results.append({
                    "document": pdf_path.name,
                    "category": row["category"],
                    "term":     row["term"],
                    "count":    c
                })

    if not results:
        print("⚠️  No matches found. Check your dictionary or PDFs.")
        return

    results_df  = pd.DataFrame(results)
    output_path = config.DATA_PROCESSED / "policy_term_counts.csv"
    results_df.to_csv(output_path, index=False)
    print(f"\n✅ Saved to: {output_path}")
    print(results_df.head())

if __name__ == "__main__":
    main()
