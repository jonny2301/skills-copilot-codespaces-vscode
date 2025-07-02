"""Sync GitHub issues with Linear.

This module is a placeholder. It **does not** talk to the Linear API or make
any network requests. Running it merely echoes progress messages so we can wire
up real API calls later once approved.
"""

import sys
from pathlib import Path


def sync_issues(repo_path: Path) -> None:
    """Placeholder for future integration with the Linear API."""

    print(f"Syncing issues for repository at {repo_path}")
    # TODO: integrate with the Linear API once approved. No network calls yet.


def main() -> int:
    """CLI entry point."""

    if len(sys.argv) != 2:
        print("Usage: sync_linear_issues.py <repo_path>")
        return 1
    repo_path = Path(sys.argv[1])
    if not repo_path.is_dir():
        print(f"Repository path {repo_path} not found", file=sys.stderr)
        return 1
    sync_issues(repo_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
