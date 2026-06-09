"""
Headline sentiment using FinBERT (Hugging Face transformers).
"""

from __future__ import annotations

from functools import lru_cache
from typing import Any

# Lazy import inside pipeline getter keeps import errors localized (optional deps).


@lru_cache(maxsize=1)
def _sentiment_pipeline() -> Any:
    """Load FinBERT once per process (cached)."""
    # pyrefly: ignore [missing-import]
    from transformers import pipeline

    return pipeline(
        "sentiment-analysis",
        model="ProsusAI/finbert",
        tokenizer="ProsusAI/finbert",
        truncation=True,
        max_length=512,
        device=-1,  # CPU; set to 0 for CUDA if available.
    )


def analyze_headlines_sentiment(headlines: list[str]) -> dict[str, Any]:
    """
    Run FinBERT on each headline and aggregate label distribution.

    Returns:
        labels_pct: approximate share 0–100 for positive / negative / neutral
        details: per-headline list of {text, label, score}
        error: optional user-facing message when nothing could be scored
    """
    clean = [h.strip() for h in headlines if isinstance(h, str) and h.strip()]
    if not clean:
        return {
            "labels_pct": {"positive": 0.0, "negative": 0.0, "neutral": 0.0},
            "details": [],
            "error": "No headlines to analyze.",
        }

    try:
        clf = _sentiment_pipeline()
        # Batch inference keeps the UI more responsive than one-by-one calls.
        raw = clf(clean)
    except Exception as exc:  # pragma: no cover - runtime / model issues
        return {
            "labels_pct": {"positive": 0.0, "negative": 0.0, "neutral": 0.0},
            "details": [],
            "error": f"Sentiment model failed to load or run: {exc}",
        }

    # pipeline may return list[dict] or dict for batch depending on version
    rows: list[dict[str, Any]] = raw if isinstance(raw, list) else [raw]
    if len(rows) != len(clean):
        # Rare version mismatch — score headlines individually to stay consistent.
        rows = []
        for line in clean:
            one = clf(line)
            rows.append(one[0] if isinstance(one, list) else one)

    counts = {"positive": 0, "negative": 0, "neutral": 0}
    details: list[dict[str, Any]] = []
    paired = list(zip(clean, rows))
    for text, row in paired:
        label = str(row.get("label", "neutral")).lower()
        score = float(row.get("score", 0.0))
        # FinBERT uses POSITIVE/NEGATIVE/NEUTRAL — normalize.
        if "pos" in label:
            key = "positive"
        elif "neg" in label:
            key = "negative"
        else:
            key = "neutral"
        counts[key] += 1
        details.append({"text": text, "label": key, "score": score})

    total = max(len(clean), 1)
    labels_pct = {k: round(100.0 * v / total, 1) for k, v in counts.items()}
    return {"labels_pct": labels_pct, "details": details, "error": None}
