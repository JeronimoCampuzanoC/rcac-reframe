"""State tracking helpers for run metadata."""

from pathlib import Path


def ensure_state_db(db_path: Path) -> Path:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    db_path.touch(exist_ok=True)
    return db_path
