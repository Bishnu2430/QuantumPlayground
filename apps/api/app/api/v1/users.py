from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.database import get_session
from app.db.models.user import User
from app.schemas.auth import UserResponse
from app.schemas.users import UserUpdate

router = APIRouter(tags=["users"])


def _out(u: User) -> UserResponse:
    return UserResponse(id=u.id, email=u.email, username=u.username, full_name=u.full_name, is_active=u.is_active, is_verified=u.is_verified, created_at=u.created_at.isoformat())


@router.get("/me", response_model=UserResponse)
def get_profile(user: User = Depends(get_current_user)) -> UserResponse:
    return _out(user)


@router.patch("/me", response_model=UserResponse)
def update_profile(request: UserUpdate, session: Session = Depends(get_session), user: User = Depends(get_current_user)) -> UserResponse:
    if request.full_name is not None: user.full_name = request.full_name
    if request.email is not None: user.email = request.email
    session.commit(); session.refresh(user)
    return _out(user)
