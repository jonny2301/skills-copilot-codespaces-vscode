import os
from pathlib import Path
import subprocess
import sys
from ghostframe_tasks import validate_templates


def test_validate_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy")
    assert validate_templates.validate_env()


def test_validate_templates(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy")
    json_dir = tmp_path
    json_file = json_dir / "example.json"
    json_file.write_text('{"lines": ["a", "b"]}')
    assert validate_templates.validate_templates(json_dir)


def test_validate_usage(monkeypatch) -> None:
    monkeypatch.delenv("API_KEY", raising=False)
    result = subprocess.run([
        sys.executable,
        "-m",
        "ghostframe_tasks.validate_templates",
    ], capture_output=True, text=True)
    assert "python -m ghostframe_tasks.validate_templates" in result.stdout
    assert result.returncode == 1
