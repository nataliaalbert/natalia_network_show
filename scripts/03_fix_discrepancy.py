import sys
sys.path.insert(0, r"C:\natalia_network_show")
import config
import pandas as pd

metadata_file = config.CORPUS_OUTPUT / "metadata.csv"
df = pd.read_csv(metadata_file)

missing_files = []
for _, row in df.iterrows():
    pdf_name = f"artifact-{row['Artifact ID']}-file-{row['File ID']}.pdf"
    if not (config.CORPUS_OUTPUT / pdf_name).exists():
        missing_files.append(row)

missing_df  = pd.DataFrame(missing_files)
output_path = config.CORPUS_OUTPUT / "missing_files_metadata.csv"
missing_df.to_csv(output_path, index=False)

print(f"🔍 Found {len(missing_df)} metadata entries without corresponding files")
print(f"   Saved to: {output_path}")
