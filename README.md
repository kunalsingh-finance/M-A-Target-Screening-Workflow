# Entity Registry Workflow

This repository is a sanitized portfolio version of an internal data operations project.

It demonstrates how to:

- validate company records from a spreadsheet
- standardize key fields
- flag incomplete or inconsistent records
- detect likely duplicates
- track processing progress
- produce clean output and exception reports

This version does **not** include:

- client data
- credentials
- proprietary source systems
- internal business rules
- production automation steps from the original project

## Project Summary

The workflow is designed for company record intake and review. It reads a flat file of records, applies validation and normalization rules, identifies likely duplicates, and writes three outputs:

- cleaned records
- exception records
- processing summary

## Example Use Cases

- vendor onboarding support
- company master data review
- research pipeline QA
- reporting control checks
- record standardization before CRM import

## Files

- `src/main.py`: command-line entry point
- `src/pipeline.py`: validation, normalization, and duplicate review flow
- `src/progress.py`: run-state tracking
- `src/config.py`: field settings
- `sample_data/company_records.csv`: sample input file

## Run

```bash
python -m src.main
```

## Outputs

The workflow writes output files to `output/`:

- `clean_records.csv`
- `exception_records.csv`
- `run_summary.json`
- `progress.json`

## Resume-Safe Description

Built a Python-based data QA workflow to validate company records, standardize fields, flag exceptions, and improve reliability of downstream reporting and record management.
