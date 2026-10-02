from __future__ import annotations

import json

import pandas as pd
import pytest

from src import config
from src.pipeline import apply_quality_checks, load_input, normalize_frame, run_pipeline


def test_bundled_sample_routes_duplicate_candidates_to_review(tmp_path):
    stats = run_pipeline(config.INPUT_FILE, tmp_path)
    assert (stats.total_rows, stats.clean_rows, stats.exception_rows, stats.duplicate_flags) == (6, 3, 3, 2)
    clean = pd.read_csv(tmp_path / "clean_records.csv")
    exceptions = pd.read_csv(tmp_path / "exception_records.csv")
    assert not clean.possible_duplicate.any()
    assert len(clean) + len(exceptions) == stats.total_rows
    assert exceptions.possible_duplicate.sum() == 2
    assert json.loads((tmp_path / "run_summary.json").read_text())["exception_rows"] == 3
    assert json.loads((tmp_path / "progress.json").read_text())["last_processed_row"] == 6


def test_optional_address_keeps_original_row_index():
    frame = pd.DataFrame(dict(company_name=["Acme", "Beta"], state=["NY", "CA"]), index=[10, 20])
    result = apply_quality_checks(normalize_frame(frame))
    assert result.short_address.tolist() == [True, True]
    assert result.has_exception.all()


def test_whitespace_and_case_duplicate_candidates_preserved():
    frame = pd.DataFrame(dict(company_name=["  Acme  Holdings ", "acme holdings"],
                              state=["NY", "NY"], address=["100 Main Street", "100 Main Street"]))
    result = apply_quality_checks(normalize_frame(frame))
    assert result.possible_duplicate.all()
    assert result.has_exception.all()
    assert len(result) == 2


def test_missing_names_are_exceptions_not_duplicate_companies():
    frame = pd.DataFrame(dict(company_name=[None, ""], state=["NY", "NY"], address=["100 Main Street"] * 2))
    result = apply_quality_checks(normalize_frame(frame))
    assert result.missing_company_name.all()
    assert not result.possible_duplicate.any()


def test_missing_required_schema_rejected(tmp_path):
    path = tmp_path / "bad.csv"
    pd.DataFrame(dict(company_name=["Acme"])).to_csv(path, index=False)
    with pytest.raises(ValueError, match="state"):
        load_input(path)


def test_empty_valid_input_produces_readable_outputs(tmp_path):
    source = tmp_path / "input.csv"
    pd.DataFrame(columns=config.REQUIRED_COLUMNS).to_csv(source, index=False)
    stats = run_pipeline(source, tmp_path / "nested")
    assert stats.total_rows == 0
    assert pd.read_csv(tmp_path / "nested" / "clean_records.csv").empty


def test_rerun_replaces_prior_records(tmp_path):
    source = tmp_path / "input.csv"
    destination = tmp_path / "exports"
    run_pipeline(config.INPUT_FILE, destination)
    pd.DataFrame([dict(company_name="Unique Company", state="NY", address="100 Main Street")]).to_csv(source, index=False)
    stats = run_pipeline(source, destination)
    assert stats.clean_rows == 1
    assert pd.read_csv(destination / "exception_records.csv").empty
