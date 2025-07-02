"""Offline-only stub for syncing GitHub issues with Linear.

This script merely prints progress messages; it never contacts the Linear API or
makes network requests. Once integration is approved, it will create Linear
tasks automatically.
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
