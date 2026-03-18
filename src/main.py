from .pipeline import run_pipeline


def main() -> None:
    stats = run_pipeline()
    print("Run complete")
    print(f"Total rows: {stats.total_rows}")
    print(f"Clean rows: {stats.clean_rows}")
    print(f"Exception rows: {stats.exception_rows}")
    print(f"Duplicate flags: {stats.duplicate_flags}")


if __name__ == "__main__":
    main()
