import os
import pandas as pd
import shutil
from pathlib import Path

# Define paths
base_dir = Path('C:\\Users\\albertna\\OneDrive - Victoria University of Wellington - STAFF\\Documents\\Natalia\'s Second Brain\\01. Projects\\PhD\\Data Collection\\Policy Corpus\\2025-12-29')  # Adjust to your base directory
metadata_dir = base_dir / "Metadata"
output_dir = base_dir / "output"
output_dir.mkdir(exist_ok=True)

all_metadata = []
processed_files = set()  # Track already processed files

for metadata_file in metadata_dir.glob("metadata-search-*.csv"):
    identifier = metadata_file.stem.replace("metadata-search-", "")
    search_folder = base_dir / f"search-{identifier}"

    df = pd.read_csv(metadata_file)
    df["Source_Search"] = identifier
    all_metadata.append(df)

    for _, row in df.iterrows():
        artifact_id = row["Artifact ID"]
        file_id = row["File ID"]
        pdf_name = f"artifact-{artifact_id}-file-{file_id}.pdf"

        # Skip if already processed
        if pdf_name in processed_files:
            continue

        source_path = search_folder / pdf_name
        if source_path.exists():
            shutil.copy2(source_path, output_dir / pdf_name)
            processed_files.add(pdf_name)

# Combine and remove duplicate metadata rows
combined_df = pd.concat(all_metadata, ignore_index=True)
combined_df = combined_df.drop_duplicates(subset=["Artifact ID", "File ID"])
combined_df.to_csv(output_dir / "metadata.csv", index=False)

print(f"Done! {len(processed_files)} unique files copied.")