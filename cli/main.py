"""Command-line entrypoint for rcac-reframe."""

from .config import AppConfig


def main() -> int:
    config = AppConfig()
    print(f"rcac-reframe ready (root={config.repo_root})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
