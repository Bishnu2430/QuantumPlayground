from pathlib import Path
import re
import yaml
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.db.models.lesson import Lesson


def content_root() -> Path:
    return Path(__file__).resolve().parents[5] / "content"


def lesson_files() -> list[Path]:
    root = content_root() / "lessons"
    return sorted(root.rglob("*.md")) if root.exists() else []


def extract_title(markdown: str, fallback: str) -> str:
    return next((line.lstrip("# ").strip() for line in markdown.splitlines() if line.startswith("#")), fallback)



def ingest_content_lessons(session: Session) -> int:
    count = 0
    for path in lesson_files():
        relative = path.relative_to(content_root() / "lessons")
        slug = str(relative.with_suffix("")).replace("/", "-")
        markdown = path.read_text(encoding="utf-8")
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n", markdown, re.DOTALL)
        frontmatter = yaml.safe_load(match.group(1)) or {} if match else {}
        lesson = session.scalar(select(Lesson).where(Lesson.slug == slug))
        values = {
            "slug": slug,
            "title": frontmatter.get("title") or extract_title(markdown, path.stem.replace("-", " ").title()),
            "description": frontmatter.get("summary"),
            "content": markdown,
            "difficulty": {"beginner": 1, "intermediate": 3, "advanced": 4, "expert": 5}.get(frontmatter.get("level"), 2),
            "domain": frontmatter.get("domain") or relative.parts[0],
            "module": relative.parts[0],
            "order": count,
            "is_published": True,
        }
        if lesson is None:
            session.add(Lesson(**values))
        else:
            for key, value in values.items():
                setattr(lesson, key, value)
        count += 1
    session.commit()
    return count
