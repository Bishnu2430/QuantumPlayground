def rerank_by_score(items: list[dict], *, limit: int = 5) -> list[dict]:
    return sorted(items, key=lambda item: item.get("score", 0), reverse=True)[:limit]
