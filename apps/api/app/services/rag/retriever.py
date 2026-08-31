from pathlib import Path

from app.services.rag.chunker import chunk_text


def retrieve_local_markdown(query: str, root: Path, *, limit: int = 5) -> list[dict[str, str | int]]:
    terms = {term.lower() for term in query.split() if term.strip()}
    matches: list[dict[str, str | int]] = []
    for path in sorted(root.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for index, chunk in enumerate(chunk_text(text)):
            score = sum(chunk.lower().count(term) for term in terms)
            if score:
                matches.append({"path": str(path), "chunk": chunk, "chunk_index": index, "score": score})
    return sorted(matches, key=lambda item: int(item["score"]), reverse=True)[:limit]
