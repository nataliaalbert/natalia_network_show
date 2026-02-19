import sys
sys.path.insert(0, r"C:\natalia_network_show")
import config
import pandas as pd
import shutil

all_metadata = []
processed_files = set()

for metadata_file in config.CORPUS_METADATA.glob("metadata-search-*.csv"):
    identifier = metadata_file.stem.replace("metadata-search-", "")
    search_folder = config.CORPUS_RAW / f"search-{identifier}"

    df = pd.read_csv(metadata_file)
    df["Source_Search"] = identifier
    all_metadata.append(df)

    for _, row in df.iterrows():
        pdf_name = f"artifact-{row['Artifact ID']}-file-{row['File ID']}.pdf"
        if pdf_name in processed_files:
            continue
        source_path = search_folder / pdf_name
        if source_path.exists():
            shutil.copy2(source_path, config.CORPUS_OUTPUT / pdf_name)
            processed_files.add(pdf_name)

combined_df = pd.concat(all_metadata, ignore_index=True)
combined_df = combined_df.drop_duplicates(subset=["Artifact ID", "File ID"])
combined_df.to_csv(config.CORPUS_OUTPUT / "metadata.csv", index=False)

print(f"✅ Done! {len(processed_files)} unique files copied to {config.CORPUS_OUTPUT}")
