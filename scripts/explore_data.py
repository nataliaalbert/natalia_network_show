import sys
sys.path.insert(0, r"C:\natalia_network_show")
import config
import pandas as pd

# ──────────────────────────────────────────────────────────────────────────────
# Script C — Explore the Merged Dataset
# What does your corpus actually look like?
# ──────────────────────────────────────────────────────────────────────────────

df = pd.read_csv(config.DATA_PROCESSED / "merged_term_metadata.csv")

print("=" * 60)
print("CORPUS OVERVIEW")
print("=" * 60)
print(f"Total term match rows:      {len(df):,}")
print(f"Unique documents:           {df['document'].nunique():,}")
print(f"Unique terms matched:       {df['term'].nunique():,}")
print(f"Total term mentions:        {df['count'].sum():,}")

print("\n" + "=" * 60)
print("TOP 20 MOST FREQUENT TERMS")
print("=" * 60)
top_terms = df.groupby("term")["count"].sum().sort_values(ascending=False).head(20)
for term, count in top_terms.items():
    print(f"  {count:>8,}  {term}")

print("\n" + "=" * 60)
print("TERM COUNTS BY FOUR PILLARS CATEGORY")
print("=" * 60)
by_category = df.groupby("category")["count"].sum().sort_values(ascending=False)
for cat, count in by_category.items():
    print(f"  {count:>8,}  {cat}")

print("\n" + "=" * 60)
print("TOP 15 MOST ACTIVE PUBLISHERS")
print("=" * 60)
top_publishers = df.groupby("Publisher")["document"].nunique().sort_values(ascending=False).head(15)
for pub, count in top_publishers.items():
    print(f"  {count:>6,} docs  {pub}")

print("\n" + "=" * 60)
print("DOCUMENTS PER YEAR")
print("=" * 60)
by_year = df.groupby("Year of publication")["document"].nunique().sort_values(ascending=False).head(20)
for year, count in by_year.items():
    print(f"  {year}:  {count:,} documents")

print("\n" + "=" * 60)
print("TOP 10 DOCUMENTS BY TOTAL TERM MENTIONS")
print("=" * 60)
top_docs = df.groupby(["document", "Title"])["count"].sum().sort_values(ascending=False).head(10)
for (doc, title), count in top_docs.items():
    short_title = str(title)[:60] + "..." if len(str(title)) > 60 else str(title)
    print(f"  {count:>6,} mentions  {short_title}")

print("\n✅ Exploration complete!")
