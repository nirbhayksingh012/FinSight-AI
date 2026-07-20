"""
ChromaDB helpers for lightweight RAG over news + stock summaries.
"""
from __future__ import annotations
from pathlib import Path
from typing import Any
# pyrefly: ignore [missing-import]
import chromadb


def _persist_directory() -> str:
    # Store alongside the repo (gitignored in practice if you add `.chroma_stock_analyzer/`).
    root = Path(__file__).resolve().parent.parent
    path = root / ".chroma_stock_analyzer"
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


def _client() -> chromadb.PersistentClient:
    return chromadb.PersistentClient(path=_persist_directory())


def get_or_create_collection(name: str = "stock_research"):
    """Return a persistent collection used for news + summaries."""
    return _client().get_or_create_collection(name=name)


def add_documents(
    collection,
    documents: list[str],
    metadatas: list[dict[str, Any]] | None,
    ids: list[str],
) -> None:
    """
    Upsert documents into Chroma.

    - `documents`: plain text chunks
    - `metadatas`: optional list aligned with documents (e.g., {"ticker": "AAPL", "kind": "news"})
    - `ids`: stable ids (duplicates overwrite)
    """
    if not documents or not ids:
        return
    if len(documents) != len(ids):
        raise ValueError("documents and ids must have the same length")
    if metadatas is not None and len(metadatas) != len(documents):
        raise ValueError("metadatas must match documents length")

    collection.add(documents=documents, metadatas=metadatas, ids=ids)


def query_documents(
    collection,
    query_text: str,
    n_results: int = 6,
    where: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """
    Query Chroma for nearest neighbors.

    Returns Chroma's query result dict (documents, metadatas, distances, ids).
    """
    if not query_text.strip():
        return {"documents": [[]], "metadatas": [[]], "distances": [[]], "ids": [[]]}

    return collection.query(
        query_texts=[query_text],
        n_results=max(1, int(n_results)),
        where=where,
    )


def delete_ticker_documents(collection, ticker: str) -> None:
    """
    Remove prior vectors for a ticker so re-runs do not duplicate retrieval results.
    """
    ticker = ticker.strip().upper()
    if not ticker:
        return

    # Chroma where-filter: match ticker metadata if present.
    try:
        existing = collection.get(where={"ticker": ticker})
        ids = existing.get("ids") or []
        if ids:
            collection.delete(ids=ids)
    except Exception:
        # If metadata indexing differs by version, fail open.
        return


def format_query_results(results: dict[str, Any]) -> str:
    """Turn Chroma query output into a compact string for the LLM."""
    docs = (results.get("documents") or [[]])[0] or []
    metas = (results.get("metadatas") or [[]])[0] or []

    chunks: list[str] = []
    for i, doc in enumerate(docs, start=1):
        meta = metas[i - 1] if i - 1 < len(metas) else {}
        prefix = ""
        if isinstance(meta, dict):
            kind = meta.get("kind")
            t = meta.get("ticker")
            prefix = f"[{kind or 'doc'} | {t or 'n/a'}] "
        chunks.append(f"{prefix}{doc}".strip())
    return "\n\n".join(chunks) if chunks else "(no retrieved context)"
