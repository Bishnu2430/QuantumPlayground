from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Quantum Lab API"
    api_version: str = "v1"
    environment: str = "development"
    cors_origins: str = "http://localhost:3000"
    database_url: str = "sqlite+aiosqlite:///./quantum_lab.db"
    redis_url: str = "redis://localhost:6379/0"
    groq_api_key: str | None = None
    groq_model: str = "llama-3.3-70b-versatile"
    max_sync_qubits: int = 12
    max_shots: int = 100_000
    code_runner_timeout_seconds: int = 8

    model_config = SettingsConfigDict(
        env_file=(".env", ".env.example"),
        env_prefix="",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
