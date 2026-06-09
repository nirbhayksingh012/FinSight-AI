"""
Fetch recent headlines for a stock ticker via Google News RSS (no API key).
"""

from __future__ import annotations

import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


# Google News RSS endpoint (public; rate-limit friendly usage recommended).
_GOOGLE_NEWS_RSS = (
    "https://news.google.com/rss/search?q={query}&hl=en-US&gl=US&ceid=US:en"
)

# A normal browser-like User-Agent reduces empty/blocked responses from some feeds.
_DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


def _build_rss_url(ticker: str) -> str:
    # Include "stock" to bias results toward finance coverage.
    query = urllib.parse.quote_plus(f"{ticker.strip().upper()} stock")
    return _GOOGLE_NEWS_RSS.format(query=query)


def fetch_google_news_headlines(ticker: str, limit: int = 20) -> list[dict[str, str]]:
    """
    Return a list of dicts with keys: title, link.

    On failure or empty feed, returns an empty list (caller shows UI message).
    """
    ticker = (ticker or "").strip()
    if not ticker:
        return []

    url = _build_rss_url(ticker)
    req = urllib.request.Request(url, headers={"User-Agent": _DEFAULT_UA})

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read()
    except Exception:
        return []

    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return []

    items: list[dict[str, str]] = []
    # RSS 2.0: channel/item; tolerate missing channel.
    for item in root.findall(".//item"):
        title_el = item.find("title")
        link_el = item.find("link")
        title = (title_el.text or "").strip() if title_el is not None else ""
        link = (link_el.text or "").strip() if link_el is not None else ""
        if not title:
            continue
        items.append({"title": title, "link": link or "#"})
        if len(items) >= limit:
            break

    return items
