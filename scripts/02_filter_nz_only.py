import sys
sys.path.insert(0, r"C:\natalia_network_show")
import config
import pandas as pd
import os

metadata_file = config.CORPUS_OUTPUT / "metadata.csv"
df = pd.read_csv(metadata_file)

zealand_df     = df[df["Org. Country of Publication"] == "NZ:New Zealand"]
non_zealand_df = df[df["Org. Country of Publication"] != "NZ:New Zealand"]

removed_count = 0
for _, row in non_zealand_df.iterrows():
    pdf_name = f"artifact-{row['Artifact ID']}-file-{row['File ID']}.pdf"
    pdf_path = config.CORPUS_OUTPUT / pdf_name
    if pdf_path.exists():
        os.remove(pdf_path)
        removed_count += 1

zealand_df.to_csv(metadata_file, index=False)

print(f"🗑️  Removed {removed_count} non-NZ PDFs")
print(f"✅ Retained {len(zealand_df)} NZ entries")
print(f"   Filtered out {len(non_zealand_df)} non-NZ metadata entries")
