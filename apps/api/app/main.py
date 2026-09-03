from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.db.database import SessionLocal, init_db
from app.services.content.lesson_service import ingest_content_lessons

settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.api_version)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",") if origin.strip()],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router, prefix="/api")


@app.on_event("startup")
def startup() -> None:
    init_db()
    with SessionLocal() as session:
        ingest_content_lessons(session)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "environment": settings.environment}
