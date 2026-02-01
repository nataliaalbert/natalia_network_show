import pandas as pd
from pathlib import Path

# Define paths
base_dir = Path('C:\\Users\\albertna\\OneDrive - Victoria University of Wellington - STAFF\\Documents\\Natalia\'s Second Brain\\01. Projects\\PhD\\Data Collection\\Policy Corpus\\2025-12-29')  # Adjust to your base directory
output_dir = base_dir / "output"
metadata_file = output_dir / 'metadata.csv'

# Read the integrated metadata
df = pd.read_csv(metadata_file)

# Find entries without corresponding files
missing_files = []

for _, row in df.iterrows():
    artifact_id = row['Artifact ID']
    file_id = row['File ID']
    pdf_name = f'artifact-{artifact_id}-file-{file_id}.pdf'
    pdf_path = output_dir / pdf_name

    if not pdf_path.exists():
        missing_files.append(row)

# Create DataFrame of missing entries
missing_df = pd.DataFrame(missing_files)

# Output results
print(f'Found {len(missing_df)} metadata entries without corresponding files:')
print(missing_df)

# Save to CSV for review
missing_df.to_csv(output_dir / 'missing_files_metadata.csv', index=False)
print(f'\nSaved to: {output_dir / 'missing_files_metadata.csv'}')