import json
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from . import config
from .progress import save_progress


@dataclass
class RunStats:
    total_rows: int = 0
    clean_rows: int = 0
    exception_rows: int = 0
    duplicate_flags: int = 0


def normalize_text(value: object) -> str:
    if pd.isna(value):
        return ""
    return " ".join(str(value).strip().split())


def load_input(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = [col for col in config.REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")
    return df


def normalize_frame(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in config.TEXT_COLUMNS:
        if col in out.columns:
            out[col] = out[col].map(normalize_text)
    if "company_name" in out.columns:
        out["company_name_key"] = out["company_name"].str.lower()
    return out


def apply_quality_checks(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["missing_company_name"] = out["company_name"].eq("")
    out["missing_state"] = out["state"].eq("")
    addresses = out.get("address", pd.Series("", index=out.index, dtype=str))
    out["short_address"] = addresses.fillna("").str.len().lt(8)
    out["possible_duplicate"] = out["company_name_key"].ne("") & out["company_name_key"].duplicated(keep=False)
    out["has_exception"] = (
        out["missing_company_name"] | out["missing_state"] | out["short_address"] | out["possible_duplicate"]
    )
    return out


def write_outputs(df: pd.DataFrame, output_dir: Path, stats: RunStats) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    clean_df = df.loc[~df["has_exception"]].copy()
    exception_df = df.loc[df["has_exception"]].copy()

    clean_df.to_csv(output_dir / config.CLEAN_FILE.name, index=False)
    exception_df.to_csv(output_dir / config.EXCEPTION_FILE.name, index=False)
    (output_dir / config.SUMMARY_FILE.name).write_text(json.dumps(stats.__dict__, indent=2), encoding="utf-8")


def run_pipeline(input_file: Path | None = None, output_dir: Path | None = None) -> RunStats:
    destination = config.OUTPUT_DIR if output_dir is None else Path(output_dir)
    df = load_input(config.INPUT_FILE if input_file is None else Path(input_file))
    df = normalize_frame(df)
    df = apply_quality_checks(df)

    stats = RunStats(
        total_rows=len(df),
        clean_rows=int((~df["has_exception"]).sum()),
        exception_rows=int(df["has_exception"].sum()),
        duplicate_flags=int(df["possible_duplicate"].sum()),
    )

    write_outputs(df, destination, stats)
    save_progress(destination / config.PROGRESS_FILE.name, stats.total_rows)
    return stats
