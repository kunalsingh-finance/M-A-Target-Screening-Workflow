import json
from pathlib import Path


def load_progress(path: Path) -> dict:
    if not path.exists():
        return {"last_processed_row": 0}
    return json.loads(path.read_text(encoding="utf-8"))


def save_progress(path: Path, last_processed_row: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"last_processed_row": last_processed_row}, indent=2),
        encoding="utf-8",
    )
