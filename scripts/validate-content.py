#!/usr/bin/env python3
"""Validate the content tree without requiring extra Python packages."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRS = [
    ROOT / "content" / "curriculum",
    ROOT / "content" / "lessons",
    ROOT / "content" / "experiments",
    ROOT / "content" / "visualizations",
    ROOT / "content" / "references",
]

TEXT_EXTENSIONS = {".md", ".mdx", ".yaml", ".yml", ".json", ".svg", ".txt"}

def main() -> int:
    errors = []

    for directory in REQUIRED_DIRS:
        if not directory.exists():
            errors.append(f"Missing required directory: {directory}")

    checked = 0

    content_root = ROOT / "content"
    if content_root.exists():
        for path in content_root.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_EXTENSIONS:
                continue

            checked += 1
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError as exc:
                errors.append(f"Invalid UTF-8: {path}: {exc}")
                continue

            if path.suffix.lower() in {".md", ".mdx", ".yaml", ".yml", ".json"} and not text.strip():
                errors.append(f"Empty file: {path}")

    print(f"Checked {checked} content files.")

    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)

    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())
