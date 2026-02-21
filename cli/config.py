"""Application configuration and default paths."""

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class AppConfig:
    repo_root: Path = Path(__file__).resolve().parents[1]
    data_dir: Path = repo_root / "data"
    runs_db: Path = data_dir / "runs.db"
    artifacts_dir: Path = data_dir / "artifacts"
