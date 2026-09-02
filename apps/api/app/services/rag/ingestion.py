from pathlib import Path

from app.services.rag.chunker import chunk_text
from app.services.rag.embeddings import deterministic_embedding


def ingest_markdown_tree(root: Path) -> list[dict]:
    records: list[dict] = []
    for path in sorted(root.rglob("*.md")):
        for index, chunk in enumerate(chunk_text(path.read_text(encoding="utf-8"))):
            records.append({"path": str(path), "chunk_index": index, "text": chunk, "embedding": deterministic_embedding(chunk)})
    return records
