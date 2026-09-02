from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_session
from app.db.models.lesson import Lesson
from app.schemas.lessons import LessonCreate, LessonResponse

router = APIRouter(tags=["lessons"])


def _out(l: Lesson) -> LessonResponse:
    return LessonResponse(id=l.id, slug=l.slug, title=l.title, description=l.description, content=l.content, difficulty=l.difficulty, domain=l.domain, module=l.module, order=l.order, is_published=l.is_published, prerequisites=l.prerequisites, created_at=l.created_at.isoformat(), updated_at=l.updated_at.isoformat())


@router.get("", response_model=list[LessonResponse])
def list_lessons(domain: str | None = None, published: bool | None = Query(default=None), session: Session = Depends(get_session)) -> list[LessonResponse]:
    stmt = select(Lesson)
    if domain: stmt = stmt.where(Lesson.domain == domain)
    if published is not None: stmt = stmt.where(Lesson.is_published == published)
    lessons = (session.scalars(stmt.order_by(Lesson.domain, Lesson.order, Lesson.title))).all()
    return [_out(l) for l in lessons]


@router.post("", response_model=LessonResponse, status_code=201)
def create_lesson(request: LessonCreate, session: Session = Depends(get_session)) -> LessonResponse:
    if session.scalar(select(Lesson).where(Lesson.slug == request.slug)):
        raise HTTPException(status_code=409, detail="Lesson slug already exists")
    lesson = Lesson(**request.model_dump())
    session.add(lesson); session.commit(); session.refresh(lesson)
    return _out(lesson)


@router.post("/ingest", response_model=dict)
def ingest_lessons(session: Session = Depends(get_session)) -> dict[str, int]:
    root = Path(__file__).resolve().parents[5] / "content" / "lessons"
    count = 0
    for path in root.rglob("*.md"):
        rel = path.relative_to(root)
        slug = str(rel.with_suffix("")).replace("/", "-")
        content = path.read_text(encoding="utf-8")
        title = next((line.lstrip("# ").strip() for line in content.splitlines() if line.startswith("#")), slug.replace("-", " ").title())
        lesson = session.scalar(select(Lesson).where(Lesson.slug == slug))
        if lesson is None:
            lesson = Lesson(slug=slug, title=title, description=None, content=content, difficulty=1, domain=rel.parts[0], module=rel.stem, order=count, is_published=True, prerequisites=None)
            session.add(lesson)
        else:
            lesson.title = title; lesson.content = content; lesson.is_published = True
        count += 1
    session.commit()
    return {"ingested": count}


@router.get("/{slug}", response_model=LessonResponse)
def get_lesson(slug: str, session: Session = Depends(get_session)) -> LessonResponse:
    lesson = session.scalar(select(Lesson).where(Lesson.slug == slug))
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return _out(lesson)
