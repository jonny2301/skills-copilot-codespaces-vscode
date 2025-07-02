"""Stub for syncing GitHub issues with Linear.

This script prints progress messages but never contacts the Linear API or makes
any network requests. It is a placeholder for future integration once approved.
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
