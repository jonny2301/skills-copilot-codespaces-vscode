import os
from pathlib import Path
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
