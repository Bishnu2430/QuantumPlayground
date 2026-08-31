from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.config import get_settings
from app.core.security import create_access_token, hash_password, verify_password
from app.db.database import get_session
from app.db.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest, TokenResponse, UserResponse

router = APIRouter(tags=["auth"])


def _user_response(user: User) -> UserResponse:
    return UserResponse(
        id=user.id,
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        is_active=user.is_active,
        is_verified=user.is_verified,
        created_at=user.created_at.isoformat(),
    )


@router.post("/register", response_model=UserResponse, status_code=201)
def register(request: RegisterRequest, session: Session = Depends(get_session)) -> UserResponse:
    existing = session.scalar(select(User).where(or_(User.email == request.email, User.username == request.username)))
    if existing:
        raise HTTPException(status_code=409, detail="Email or username already registered")
    user = User(email=str(request.email), username=request.username, full_name=request.full_name, hashed_password=hash_password(request.password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return _user_response(user)


@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, session: Session = Depends(get_session)) -> TokenResponse:
    user = session.scalar(select(User).where(User.email == request.email))
    if user is None or not verify_password(request.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    settings = get_settings()
    token = create_access_token(user.id, timedelta(minutes=settings.access_token_expire_minutes))
    return TokenResponse(access_token=token, expires_in=settings.access_token_expire_minutes * 60)


@router.get("/me", response_model=UserResponse)
def me(user: User = Depends(get_current_user)) -> UserResponse:
    return _user_response(user)
