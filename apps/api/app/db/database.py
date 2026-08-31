from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings
from app.db.models import Base

settings = get_settings()
sync_database_url = settings.database_url.replace("sqlite+aiosqlite", "sqlite+pysqlite").replace("postgresql+asyncpg", "postgresql+psycopg")
engine = create_engine(sync_database_url, echo=settings.environment == "development", pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)


def init_db() -> None:
    from app.db.models import circuit, conversation, lesson, progress, simulation, user  # noqa: F401
    Base.metadata.create_all(bind=engine)


def get_session() -> Session:
    with SessionLocal() as session:
        yield session
