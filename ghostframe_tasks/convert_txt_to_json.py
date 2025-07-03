"""Utilities for converting text template files to JSON."""

import json
import sys
from pathlib import Path


def convert_directory(src_dir: Path, dest_dir: Path) -> None:
    """Convert all ``.txt`` files in *src_dir* to JSON files under *dest_dir*."""

    dest_dir.mkdir(parents=True, exist_ok=True)
    for txt_file in src_dir.glob("*.txt"):
        json_file = dest_dir / f"{txt_file.stem}.json"
        with txt_file.open("r", encoding="utf-8") as fh:
            lines = [line.rstrip("\n") for line in fh]
        with json_file.open("w", encoding="utf-8") as fh:
            json.dump({"lines": lines}, fh, indent=2)


def main() -> int:
    """CLI entry point."""

    if len(sys.argv) != 3:
        print("Usage: python -m ghostframe_tasks.convert_txt_to_json <src_dir> <dest_dir>")
        return 1
    src = Path(sys.argv[1])
    dest = Path(sys.argv[2])
    if not src.is_dir():
        print(f"Source directory {src} does not exist", file=sys.stderr)
        return 1
    convert_directory(src, dest)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
