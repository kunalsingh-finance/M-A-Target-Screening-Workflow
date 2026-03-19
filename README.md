# M&A Target Screening Workflow

Built a Python-based workflow to validate target-company records, standardize fields, flag exceptions, and improve data quality for downstream deal-sourcing and reporting processes.

## What it does

- validates target-company records from a spreadsheet
- standardizes key fields
- flags incomplete or inconsistent records
- detects likely duplicates
- tracks processing progress
- produces clean output and exception reports

## Project scope

This is a sanitized portfolio project built to demonstrate data-quality and workflow design in a finance-relevant context.

It does not include:

- client data
- credentials
- proprietary source systems
- internal business rules

## Files

- `src/main.py`
- `src/pipeline.py`
- `src/config.py`
- `src/progress.py`
- `sample_data/company_records.csv`

## Run

```bash
python -m src.main
```

## Output

The workflow generates:

- clean records
- exception records
- processing summary
- progress tracking

## Resume description

Built a Python workflow to validate target-company records, standardize fields, flag exceptions, and support cleaner downstream deal-sourcing and reporting processes.
