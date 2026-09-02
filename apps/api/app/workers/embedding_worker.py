from pathlib import Path

from app.services.rag.ingestion import ingest_markdown_tree


def run_embedding_job(root: Path) -> list[dict]:
    return ingest_markdown_tree(root)
