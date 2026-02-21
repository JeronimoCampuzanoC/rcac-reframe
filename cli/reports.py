"""Report parsing utilities for ReFrame JSON output."""

import json
from pathlib import Path
from typing import Any


def load_report(report_path: Path) -> dict[str, Any]:
    with report_path.open("r", encoding="utf-8") as handle:
        return json.load(handle)
