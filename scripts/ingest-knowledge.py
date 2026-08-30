#!/usr/bin/env python3
"""
Repository-level entrypoint for quantum knowledge ingestion.

The implementation should delegate to the RAG service under:
apps/api/app/services/rag/
"""

from pathlib import Path
import os
import sys

def main() -> int:
    root = Path(__file__).resolve().parents[1]
    source = root / os.getenv("KNOWLEDGE_SOURCE_DIR", "knowledge-base/raw")

    if not source.exists():
        print(f"ERROR: knowledge source does not exist: {source}", file=sys.stderr)
        return 1

    print(f"Knowledge source: {source}")
    print("RAG ingestion service not wired yet.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
