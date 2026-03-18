from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "sample_data"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_FILE = DATA_DIR / "company_records.csv"
CLEAN_FILE = OUTPUT_DIR / "clean_records.csv"
EXCEPTION_FILE = OUTPUT_DIR / "exception_records.csv"
SUMMARY_FILE = OUTPUT_DIR / "run_summary.json"
PROGRESS_FILE = OUTPUT_DIR / "progress.json"

REQUIRED_COLUMNS = [
    "company_name",
    "state",
]

TEXT_COLUMNS = [
    "company_name",
    "state",
    "city",
    "address",
    "industry",
]
