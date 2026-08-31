from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.database import get_session
from app.db.models.lesson import Lesson
from app.db.models.progress import Progress
from app.db.models.user import User
from app.schemas.progress import ProgressResponse, ProgressUpdate

router = APIRouter(tags=["progress"])

def _out(p: Progress) -> ProgressResponse:
    return ProgressResponse(id=p.id, user_id=p.user_id, lesson_id=p.lesson_id, is_completed=p.is_completed, is_started=p.is_started, mastery_level=p.mastery_level, attempts=p.attempts, time_spent_seconds=p.time_spent_seconds, created_at=p.created_at.isoformat(), updated_at=p.updated_at.isoformat())

@router.get("", response_model=list[ProgressResponse])
def list_progress(session: Session = Depends(get_session), user: User = Depends(get_current_user)) -> list[ProgressResponse]:
    rows = (session.scalars(select(Progress).where(Progress.user_id == user.id))).all()
    return [_out(p) for p in rows]

@router.put("/{lesson_id}", response_model=ProgressResponse)
def upsert_progress(lesson_id: str, request: ProgressUpdate, session: Session = Depends(get_session), user: User = Depends(get_current_user)) -> ProgressResponse:
    if session.get(Lesson, lesson_id) is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    progress = session.scalar(select(Progress).where(Progress.user_id == user.id, Progress.lesson_id == lesson_id))
    if progress is None:
        progress = Progress(user_id=user.id, lesson_id=lesson_id)
        session.add(progress)
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(progress, key, value)
    session.commit(); session.refresh(progress)
    return _out(progress)
