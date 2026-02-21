"""Helpers for invoking ReFrame runs."""

from pathlib import Path
from typing import Sequence


def build_reframe_command(config_file: Path, extra_args: Sequence[str] = ()) -> list[str]:
    return ["reframe", "-C", str(config_file), *extra_args]
