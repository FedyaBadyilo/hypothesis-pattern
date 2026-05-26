# Datasets

- `build/` — scripts that turn raw customer inputs into dev-friendly artifacts
- `processed/` — small versioned JSON/SQLite/reference artifacts safe to commit
- `access.py` — loading helpers for processed artifacts

Raw customer files must not be committed. Keep them outside Git or in a gitignored location.
