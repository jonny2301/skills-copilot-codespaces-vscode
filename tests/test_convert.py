from pathlib import Path
import json
from ghostframe_tasks import convert_txt_to_json


def test_convert_directory(tmp_path: Path) -> None:
    src = tmp_path / "src"
    dest = tmp_path / "dest"
    src.mkdir()
    txt_file = src / "example.txt"
    txt_file.write_text("hello\nworld\n")
    convert_txt_to_json.convert_directory(src, dest)
    json_file = dest / "example.json"
    assert json_file.exists()
    data = json.loads(json_file.read_text())
    assert data == {"lines": ["hello", "world"]}
