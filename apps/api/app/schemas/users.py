from pydantic import BaseModel


class UserUpdate(BaseModel):
    """User profile update request."""

    full_name: str | None = None
    email: str | None = None

    class Config:
        from_attributes = True
