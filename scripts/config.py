from pathlib import Path

# ── Root ──────────────────────────────────────────────────────────────────────
BASE_DIR = Path(r"C:\natalia_network_show")

# ── Corpus ────────────────────────────────────────────────────────────────────
CORPUS_RAW        = BASE_DIR / "corpus" / "raw"
CORPUS_METADATA   = CORPUS_RAW
CORPUS_OUTPUT     = BASE_DIR / "corpus" / "output"

SAMPLE_A          = BASE_DIR / "corpus" / "samples" / "sample_A"
SAMPLE_B          = BASE_DIR / "corpus" / "samples" / "sample_B"
SAMPLE_C          = BASE_DIR / "corpus" / "samples" / "sample_C"

# ── Dictionaries ──────────────────────────────────────────────────────────────
DICT_DIR          = BASE_DIR / "dictionaries"
DICT_1_HUMAN      = DICT_DIR / "dict1_human_built.xlsx"
DICT_2_LLM        = DICT_DIR / "dict2_llm_generated.xlsx"
DICT_3_CORPUS     = DICT_DIR / "dict3_corpus_derived.xlsx"
DICT_4_IMBALANCED = DICT_DIR / "dict4_imbalanced.xlsx"

# ── Data outputs ──────────────────────────────────────────────────────────────
DATA_PROCESSED    = BASE_DIR / "data" / "processed"
DATA_RUNS         = BASE_DIR / "data" / "runs"
DATA_GROUND_TRUTH = BASE_DIR / "data" / "ground_truth"
DATA_EVALUATION   = BASE_DIR / "data" / "evaluation"
DATA_NETWORK      = BASE_DIR / "data" / "network"

# ── Auto-create all folders ───────────────────────────────────────────────────
for folder in [
    CORPUS_OUTPUT, SAMPLE_A, SAMPLE_B, SAMPLE_C,
    DICT_DIR, DATA_PROCESSED, DATA_RUNS,
    DATA_GROUND_TRUTH, DATA_EVALUATION, DATA_NETWORK
]:
    folder.mkdir(parents=True, exist_ok=True)

print("✅ Config loaded. All folders ready.")