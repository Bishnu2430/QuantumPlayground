import hashlib
import math


def deterministic_embedding(text: str, dimensions: int = 32) -> list[float]:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    values = [((digest[i % len(digest)] / 255.0) * 2.0) - 1.0 for i in range(dimensions)]
    norm = math.sqrt(sum(v * v for v in values)) or 1.0
    return [v / norm for v in values]
