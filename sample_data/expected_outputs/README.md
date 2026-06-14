# Sample Expected Outputs

This directory contains example output structures for the verification workflow.

## Output categories

- `standard_validation_pass.json` — Example output for a healthy backup.
- `standard_validation_fail.json` — Example output for a corrupted or incomplete backup.
- `ai_dynamic_validation_success.json` — Example output when AI-generated anomaly checks pass.
- `ai_dynamic_validation_fail.json` — Example output when AI-generated anomaly checks detect issues.
- `sample_report.txt` — Example narrative report text.

## How to use

Compare runtime results from `app.verifier.verify_backup()` or `run_ai_dynamic_validation()` against these examples.

If the actual outputs diverge, use the examples here as a baseline for expected field names and structure.
