#!/usr/bin/env python3
"""
Repository-level entrypoint for embedding generation.

Provider and batching details belong inside the RAG service so the project can
switch embedding providers without changing the repository command.
"""

import os

def main() -> int:
    provider = os.getenv("EMBEDDING_PROVIDER")

    if not provider:
        print("EMBEDDING_PROVIDER is not configured.")
        return 0

    print(f"Embedding provider: {provider}")
    print("Embedding generation service not wired yet.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
