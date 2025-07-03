from pathlib import Path
from ghostframe_tasks import sync_linear_issues


def test_sync_issues(capsys, tmp_path: Path) -> None:
    repo = tmp_path
    sync_linear_issues.sync_issues(repo)
    captured = capsys.readouterr()
    assert f"Syncing issues for repository at {repo}" in captured.out
