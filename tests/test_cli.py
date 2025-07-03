from ghostframe_tasks import convert_txt_to_json, validate_templates, sync_linear_issues


def test_convert_cli_bad_args(monkeypatch):
    monkeypatch.setattr('sys.argv', ['convert_txt_to_json.py'])
    assert convert_txt_to_json.main() == 1


def test_validate_cli_bad_args(monkeypatch):
    monkeypatch.setattr('sys.argv', ['validate_templates.py'])
    assert validate_templates.main() == 1


def test_sync_cli_bad_args(monkeypatch):
    monkeypatch.setattr('sys.argv', ['sync_linear_issues.py'])
    assert sync_linear_issues.main() == 1
