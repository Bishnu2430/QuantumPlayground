FROM python:3.13-slim
WORKDIR /app
COPY apps/api/pyproject.toml ./
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
