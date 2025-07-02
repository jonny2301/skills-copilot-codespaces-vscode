"""Utilities for validating text template JSON files."""

import json
import os
import sys
from pathlib import Path
from jsonschema import ValidationError, validate

TEMPLATE_SCHEMA = {
    'type': 'object',
    'properties': {
        'lines': {
            'type': 'array',
            'items': {'type': 'string'}
        }
    },
    'required': ['lines']
}

REQUIRED_ENV_VARS = ['API_KEY']


def validate_env() -> bool:
    """Ensure required environment variables are present."""

    missing = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
    if missing:
        print(f"Missing environment variables: {', '.join(missing)}", file=sys.stderr)
        return False
    return True


def validate_templates(directory: Path) -> bool:
    """Validate all JSON templates in *directory* against the schema."""

    ok = True
    for json_file in directory.glob("*.json"):
        try:
            data = json.loads(json_file.read_text())
            validate(instance=data, schema=TEMPLATE_SCHEMA)
        except (json.JSONDecodeError, ValidationError) as exc:
            print(f"Validation failed for {json_file}: {exc}", file=sys.stderr)
            ok = False
    return ok


def main() -> int:
    """CLI entry point."""

    if len(sys.argv) != 2:
        print("Usage: validate_templates.py <directory>")
        return 1
    if not validate_env():
        return 1
    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f"Directory {directory} not found", file=sys.stderr)
        return 1
    return 0 if validate_templates(directory) else 1


if __name__ == '__main__':
    raise SystemExit(main())
