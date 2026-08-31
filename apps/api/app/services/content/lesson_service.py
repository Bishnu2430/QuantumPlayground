from pathlib import Path


def content_root() -> Path:
    return Path(__file__).resolve().parents[5] / "content"


def lesson_files() -> list[Path]:
    root = content_root() / "lessons"
    return sorted(root.rglob("*.md")) if root.exists() else []


def extract_title(markdown: str, fallback: str) -> str:
    return next((line.lstrip("# ").strip() for line in markdown.splitlines() if line.startswith("#")), fallback)
