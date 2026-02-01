import pandas as pd
from pathlib import Path
import os

# Define paths
base_dir = Path('C:\\Users\\albertna\\OneDrive - Victoria University of Wellington - STAFF\\Documents\\Natalia\'s Second Brain\\01. Projects\\PhD\\Data Collection\\Policy Corpus\\2025-12-29')  # Adjust to your base directory
output_dir = base_dir / "output"
metadata_file = output_dir / "metadata.csv"

# Read metadata
df = pd.read_csv(metadata_file)

# Filter for Zealand publications
zealand_df = df[df["Org. Country of Publication"] == "NZ:New Zealand"]
non_zealand_df = df[df["Org. Country of Publication"] != "NZ:New Zealand"]

# Remove non-Zealand PDF files
removed_count = 0
for _, row in non_zealand_df.iterrows():
    artifact_id = row["Artifact ID"]
    file_id = row["File ID"]
    pdf_name = f"artifact-{artifact_id}-file-{file_id}.pdf"
    pdf_path = output_dir / pdf_name

    if pdf_path.exists():
        os.remove(pdf_path)
        removed_count += 1

# Save filtered metadata (overwrite original)
zealand_df.to_csv(metadata_file, index=False)

# Summary
print(f"Removed {removed_count} non-Zealand PDF files")
print(f"Retained {len(zealand_df)} Zealand entries in metadata")
print(f"Filtered out {len(non_zealand_df)} metadata entries")