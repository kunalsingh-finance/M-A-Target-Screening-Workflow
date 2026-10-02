import argparse
from pathlib import Path

from .pipeline import run_pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate and review synthetic target-company records.")
    parser.add_argument("--input", type=Path, default=None, help="Input CSV; defaults to the bundled synthetic sample.")
    parser.add_argument("--output-dir", type=Path, default=None, help="Output directory; defaults to output/.")
    args = parser.parse_args()
    stats = run_pipeline(args.input, args.output_dir)
    print("Run complete")
    print(f"Total rows: {stats.total_rows}")
    print(f"Clean rows: {stats.clean_rows}")
    print(f"Exception rows: {stats.exception_rows}")
    print(f"Duplicate flags: {stats.duplicate_flags}")


if __name__ == "__main__":
    main()
