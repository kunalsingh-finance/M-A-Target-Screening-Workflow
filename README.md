# M&A Target Screening Workflow

This project simulates a data-quality workflow for M&A target screening. It validates target-company records, standardizes fields, flags exceptions, detects likely duplicates, and produces clean output files for downstream deal-sourcing review.

The project is sanitized and educational. It does not include client data, credentials, proprietary source systems, or confidential investment-banking workflows.

## What This Project Does

- Loads target-company records from a spreadsheet-style input file
- Standardizes key company fields
- Flags incomplete or inconsistent records
- Detects likely duplicate companies
- Tracks processing progress
- Produces clean records and exception reports
- Creates a repeatable workflow for reviewing target-company data quality

## Business Context

M&A and corporate development teams often rely on target lists assembled from multiple sources. Before those lists can support screening, outreach, or reporting, the data needs to be standardized and reviewed for missing fields, inconsistent naming, and duplicate records.

This project demonstrates the workflow design behind that data-quality layer.

## Project Scope

This is a sanitized portfolio project. It intentionally excludes:

- Client data
- Credentials
- Proprietary source systems
- Confidential scoring models
- Internal business rules

## Files

- `src/main.py`: command-line entry point
- `src/pipeline.py`: core validation and processing workflow
- `src/config.py`: configuration values
- `src/progress.py`: progress tracking helpers
- `sample_data/company_records.csv`: sample input file

## How to Run

Use Python 3.11 or newer and install the runtime dependencies:

```bash
python -m pip install -r requirements.txt
```

```bash
python -m src.main
```

To choose an input and output directory:

```bash
python -m src.main --input sample_data/company_records.csv --output-dir output/demo
```

The bundled six synthetic records produce **3 clean records, 3 exceptions and 2 duplicate-candidate flags**. All records are retained: possible duplicates go to the exception report for human review rather than being silently accepted or deleted. Duplicate detection compares case-insensitive, whitespace-normalized company names; it does not establish that two legal entities are identical.

Install the development dependencies and run the schema, normalization, duplicate, custom-output and rerun checks with:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

## Outputs

The workflow generates:

- Clean standardized records
- Exception records requiring review
- Duplicate or possible-duplicate flags
- Processing summary
- Progress tracking output

## Skills Demonstrated

- Finance workflow automation
- Data validation and standardization
- Exception reporting
- Duplicate detection
- Python pipeline structure
- Sanitized portfolio-project design

## Limitations

- The project uses sample data and simplified validation rules.
- It does not model a full deal-screening scorecard.
- It is meant to demonstrate workflow and data-quality thinking, not proprietary M&A diligence.

## Resume Summary

Built a Python workflow to validate target-company records, standardize fields, flag exceptions, detect likely duplicates, and support cleaner downstream deal-sourcing and reporting processes.
