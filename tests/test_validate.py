import os
from pathlib import Path
from ghostframe_tasks import validate_templates


def test_validate_env(monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy")
    assert validate_templates.validate_env()


def test_validate_env_missing(monkeypatch, capsys):
    """validate_env should fail when API_KEY is unset."""
    monkeypatch.delenv("API_KEY", raising=False)
    assert not validate_templates.validate_env()
    captured = capsys.readouterr()
    assert "Missing environment variables" in captured.err


def test_validate_templates(tmp_path: Path, monkeypatch):
    monkeypatch.setenv("API_KEY", "dummy")
    json_dir = tmp_path
    json_file = json_dir / "example.json"
    json_file.write_text('{"lines": ["a", "b"]}')
    assert validate_templates.validate_templates(json_dir)


def test_validate_templates_malformed(tmp_path: Path, monkeypatch, capsys):
    """Malformed JSON should be reported and return False."""
    monkeypatch.setenv("API_KEY", "dummy")
    json_dir = tmp_path
    bad_file = json_dir / "bad.json"
    bad_file.write_text("{bad json}")
    assert not validate_templates.validate_templates(json_dir)
    captured = capsys.readouterr()
    assert str(bad_file) in captured.err
