from pydantic import BaseModel, Field


class TokenResponse(BaseModel):
    """JWT token response."""

    access_token: str
    token_type: str = "bearer"
    expires_in: int


class LoginRequest(BaseModel):
    """User login credentials."""

    email: str
    password: str = Field(min_length=6)


class RegisterRequest(BaseModel):
    """User registration request."""

    email: str
    username: str = Field(min_length=3, max_length=255)
    password: str = Field(min_length=6, max_length=255)
    full_name: str | None = None


class UserResponse(BaseModel):
    """User profile response."""

    id: str
    email: str
    username: str
    full_name: str | None
    is_active: bool
    is_verified: bool
    created_at: str

    class Config:
        from_attributes = True
