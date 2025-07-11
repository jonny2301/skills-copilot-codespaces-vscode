from pathlib import Path
import subprocess
import sys
from ghostframe_tasks import sync_linear_issues


def test_sync_issues(capsys, tmp_path: Path) -> None:
    repo = tmp_path
    sync_linear_issues.sync_issues(repo)
    captured = capsys.readouterr()
    assert f"Syncing issues for repository at {repo}" in captured.out


def test_sync_usage() -> None:
    result = subprocess.run([
        sys.executable,
        "-m",
        "ghostframe_tasks.sync_linear_issues",
    ], capture_output=True, text=True)
    assert "python -m ghostframe_tasks.sync_linear_issues" in result.stdout
    assert result.returncode == 1
