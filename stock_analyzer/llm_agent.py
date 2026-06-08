"""
Groq-powered LLM helpers for structured stock commentary and RAG chat.
"""

from __future__ import annotations

import json
import os
from typing import Any

from stock_analyzer.constants import GROQ_MODEL


def _groq_client():
    """Return a Groq client or raise a clear error if configuration is missing."""
    # pyrefly: ignore [missing-import]
    from groq import Groq

    api_key = os.getenv("GROQ_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Add it to a `.env` file in the project root."
        )
    return Groq(api_key=api_key)


def _format_news_for_prompt(news: list[dict[str, str]], max_items: int = 12) -> str:
    lines: list[str] = []
    for i, item in enumerate(news[:max_items], start=1):
        title = item.get("title", "").strip()
        link = item.get("link", "").strip()
        lines.append(f"{i}. {title} ({link})")
    return "\n".join(lines) if lines else "(no headlines available)"


def _format_sentiment_for_prompt(sentiment: dict[str, Any]) -> str:
    pct = sentiment.get("labels_pct") or {}
    return json.dumps(pct, indent=2)


def generate_stock_analysis(
    stock_data: str,
    news: list[dict[str, str]],
    sentiment: dict[str, Any],
) -> str:
    """
    Ask the LLM for bull/bear cases, risks, and a verdict.

    `stock_data` should be a concise textual summary (not raw CSV dumps).
    """
    client = _groq_client()

    system = (
        "You are a careful financial research assistant. "
        "You are not providing personalized investment advice. "
        "Use only the supplied context; if data is missing, say so explicitly. "
        "Respond in Markdown with these sections exactly:\n"
        "## Bull case\n"
        "## Bear case\n"
        "## Risks\n"
        "## Final verdict\n"
        "Keep each section tight (a few bullets or short paragraphs)."
    )

    user = (
        "Context — recent price/volume summary:\n"
        f"{stock_data}\n\n"
        "Context — headlines (Google News RSS):\n"
        f"{_format_news_for_prompt(news)}\n\n"
        "Context — headline sentiment label mix (% of headlines):\n"
        f"{_format_sentiment_for_prompt(sentiment)}\n"
    )

    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        temperature=0.35,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return (completion.choices[0].message.content or "").strip()


def answer_with_rag(
    user_question: str,
    rag_context: str,
    ticker: str,
) -> str:
    """
    Answer a follow-up question using retrieved snippets plus the ticker focus.
    """
    client = _groq_client()

    system = (
        "You are an AI stock research assistant. "
        "Answer using the provided context snippets when possible; "
        "if the context is insufficient, say what is missing and give a cautious, generic outline. "
        "This is not personalized financial advice."
    )

    user = (
        f"Ticker focus: {ticker}\n\n"
        f"Retrieved context:\n{rag_context}\n\n"
        f"User question:\n{user_question}\n"
    )

    completion = client.chat.completions.create(
        model=GROQ_MODEL,
        temperature=0.25,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return (completion.choices[0].message.content or "").strip()
