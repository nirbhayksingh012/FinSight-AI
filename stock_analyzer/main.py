from __future__ import annotations

import html
import textwrap
from datetime import date
from typing import Any

import pandas as pd
# pyrefly: ignore [missing-import]
import streamlit as st
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from streamlit_autorefresh import st_autorefresh

from stock_analyzer import charts, llm_agent, news, rag, sentiment, styles
from stock_analyzer.constants import (
    DEFAULT_START_DATE,
    DEFAULT_TICKER_SELECTION,
    PAGE_TITLE,
    TICKER_DICT,
)
from stock_analyzer.data import fetch_stock_data


def _chat_html(fragment: str) -> None:
    """Render chat HTML without Markdown treating indented lines as code blocks."""
    st.markdown(fragment.strip(), unsafe_allow_html=True)


def _inject_styles() -> None:
    st.markdown(styles.app_shell_css(), unsafe_allow_html=True)
    st.markdown(styles.title_block_html(), unsafe_allow_html=True)
    st.markdown(styles.chat_css(), unsafe_allow_html=True)
    st.markdown(styles.hide_streamlit_chrome_css(), unsafe_allow_html=True)


def _sidebar_inputs():
    st.sidebar.markdown(styles.sidebar_brand_html(), unsafe_allow_html=True)

    ticker_options = [f"{ticker} – {name}" for ticker, name in TICKER_DICT.items()]
    st.sidebar.markdown('<p class="sa-side-section">Tickers</p>', unsafe_allow_html=True)
    st.sidebar.caption("Selected symbols appear as chips; search to add more.")
    selected_display = st.sidebar.multiselect(
        "Portfolio",
        options=ticker_options,
        default=DEFAULT_TICKER_SELECTION,
        placeholder="+ Add ticker…",
        label_visibility="collapsed",
    )
    tickers = [item.split(" – ")[0] for item in selected_display]

    st.sidebar.markdown('<p class="sa-side-section">Date range</p>', unsafe_allow_html=True)
    c_from, c_to = st.sidebar.columns(2)
    with c_from:
        start_date = st.sidebar.date_input("From", DEFAULT_START_DATE)
    with c_to:
        end_date = st.sidebar.date_input("To", date.today())

    if start_date > end_date:
        st.sidebar.error("Start date cannot be after end date.")
        st.stop()

    st.sidebar.markdown('<p class="sa-side-section">Auto-refresh</p>', unsafe_allow_html=True)
    enable_refresh = st.sidebar.toggle("Auto-refresh", value=False)
    refresh_interval = 30
    if enable_refresh:
        refresh_interval = st.sidebar.slider("Interval (seconds)", 10, 120, 30)
        st.sidebar.caption(f"Every {refresh_interval} s")

    st.sidebar.markdown('<p class="sa-side-section">Views</p>', unsafe_allow_html=True)
    combined_chart = st.sidebar.toggle("Combined chart", value=True)
    show_ai_insights = st.sidebar.toggle("AI analyst", value=True)

    return (
        tickers,
        start_date,
        end_date,
        enable_refresh,
        refresh_interval,
        combined_chart,
        show_ai_insights,
    )


def _stock_text_summary(ticker: str, data: pd.DataFrame) -> str:
    """Compact, LLM-friendly summary derived from OHLCV history."""
    if data.empty or "Close" not in data.columns:
        return f"{ticker}: insufficient price history in the selected range."

    last = data.iloc[-1]
    first = data.iloc[0]
    close_last = float(last["Close"])
    close_first = float(first["Close"])
    change_pct = (close_last / close_first - 1.0) * 100.0 if close_first else 0.0

    high_52w = float(data["High"].max()) if "High" in data.columns else float("nan")
    low_52w = float(data["Low"].min()) if "Low" in data.columns else float("nan")
    avg_vol = float(data["Volume"].mean()) if "Volume" in data.columns else float("nan")

    last_date = str(last.get("Date", ""))
    return (
        f"Ticker: {ticker}\n"
        f"Last date: {last_date}\n"
        f"Last close: {close_last:.2f}\n"
        f"Period change (first→last close): {change_pct:.2f}%\n"
        f"Range high/low over window: {high_52w:.2f} / {low_52w:.2f}\n"
        f"Average volume: {avg_vol:,.0f}\n"
    )


@st.cache_data(ttl=900, show_spinner=False)
def _cached_headlines(ticker: str) -> list[dict[str, str]]:
    return news.fetch_google_news_headlines(ticker)


@st.cache_data(ttl=900, show_spinner=False)
def _cached_sentiment(headlines_key: tuple[str, ...]) -> dict[str, Any]:
    return sentiment.analyze_headlines_sentiment(list(headlines_key))


def _filter_df_by_chart_range(df: pd.DataFrame, rng: str) -> pd.DataFrame:
    if df.empty or "Date" not in df.columns:
        return df
    dts = pd.to_datetime(df["Date"])
    end = dts.max()
    if rng == "All":
        return df.copy()
    days_map = {"1M": 30, "3M": 90, "1Y": 365}
    start_cut = end - pd.Timedelta(days=days_map.get(rng, 365))
    out = df.loc[dts >= start_cut].copy()
    return out if len(out) >= 3 else df.copy()


def _sentiment_for_kpi(sent: dict[str, Any]) -> tuple[str, float, str]:
    if sent.get("error"):
        return "N/A", 0.0, "sa-kpi-sent-neu"
    lp = sent.get("labels_pct") or {}
    pos = float(lp.get("positive", 0.0))
    neg = float(lp.get("negative", 0.0))
    score = (pos - neg) / 100.0
    if pos > neg + 8.0:
        return "Bullish", score, "sa-kpi-sent-bull"
    if neg > pos + 8.0:
        return "Bearish", score, "sa-kpi-sent-bear"
    return "Neutral", score, "sa-kpi-sent-neu"


def _kpi_strip_html(
    last_close: float,
    day_pct: float,
    ma20: float,
    ma50: float,
    sent_label: str,
    sent_score: float,
    sent_cls: str,
) -> str:
    chg_cls = "sa-kpi-up" if day_pct >= 0 else "sa-kpi-dn"
    sign = "+" if day_pct >= 0 else ""
    ma20_s = f"{ma20:.2f}" if ma20 == ma20 else "—"
    ma50_s = f"{ma50:.2f}" if ma50 == ma50 else "—"
    sc = f"+{sent_score:.2f}" if sent_score >= 0 else f"{sent_score:.2f}"
    return f"""
    <div class="sa-kpi-row">
      <div class="sa-kpi-card">
        <div class="sa-kpi-label">Last close</div>
        <div class="sa-kpi-value">${last_close:,.2f}</div>
        <div class="sa-kpi-sub {chg_cls}">{sign}{day_pct:.2f}% today</div>
      </div>
      <div class="sa-kpi-card">
        <div class="sa-kpi-label">MA 20</div>
        <div class="sa-kpi-value">{ma20_s}</div>
        <div class="sa-kpi-sub">20-day avg</div>
      </div>
      <div class="sa-kpi-card">
        <div class="sa-kpi-label">MA 50</div>
        <div class="sa-kpi-value">{ma50_s}</div>
        <div class="sa-kpi-sub">50-day avg</div>
      </div>
      <div class="sa-kpi-card">
        <div class="sa-kpi-label">Sentiment</div>
        <div class="sa-kpi-value {sent_cls}">{sent_label}</div>
        <div class="sa-kpi-sub">{sc} score</div>
      </div>
    </div>
    """


def _render_sentiment_bars(labels_pct: dict[str, float]) -> None:
    c1, c2, c3 = st.columns(3)
    c1.metric("Positive", f"{labels_pct.get('positive', 0.0):.1f}%")
    c2.metric("Neutral", f"{labels_pct.get('neutral', 0.0):.1f}%")
    c3.metric("Negative", f"{labels_pct.get('negative', 0.0):.1f}%")


def _render_ai_insights_section(ticker: str, data: pd.DataFrame) -> None:
    """
    Lightweight insights under charts: RSS headlines + FinBERT sentiment.
    Full Groq report lives in the AI Analyst tab.
    """
    st.markdown("### AI insights")
    headlines = _cached_headlines(ticker)
    if not headlines:
        st.info("No recent headlines found (RSS empty or unreachable). Try again later.")
        return

    titles = [h["title"] for h in headlines]
    sent = _cached_sentiment(tuple(titles[:40]))
    if sent.get("error"):
        st.warning(sent["error"])
    else:
        _render_sentiment_bars(sent.get("labels_pct") or {})

    st.caption("Top headlines (Google News RSS)")
    for h in headlines[:5]:
        st.markdown(f"- [{h['title']}]({h['link']})")

    st.caption("Tip: open the **AI Analyst** tab for sentiment + Groq analysis + chat (RAG).")


def _prepare_ohlcv(data: pd.DataFrame) -> pd.DataFrame:
    df = data.copy()
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    if "Close" in df.columns:
        df["MA20"] = df["Close"].rolling(window=20).mean()
        df["MA50"] = df["Close"].rolling(window=50).mean()
    return df


def _render_ticker_dashboard(
    ticker: str,
    start_date,
    end_date,
    *,
    combined_chart: bool,
    show_ai_insights: bool,
) -> None:
    raw = fetch_stock_data(ticker, start_date, end_date)
    if raw.empty:
        st.warning(f"No data found for '{ticker}'")
        return

    data = _prepare_ohlcv(raw)
    headlines = _cached_headlines(ticker)
    titles = [h["title"] for h in headlines]
    sent = _cached_sentiment(tuple(titles[:40])) if titles else sentiment.analyze_headlines_sentiment([])

    last_full = data.iloc[-1]
    last_close = float(last_full["Close"])
    if len(data) >= 2:
        prev_close = float(data["Close"].iloc[-2])
        day_pct = (last_close / prev_close - 1.0) * 100.0 if prev_close else 0.0
    else:
        day_pct = 0.0

    ma20_v = (
        float(last_full["MA20"])
        if "MA20" in data.columns and pd.notna(last_full.get("MA20"))
        else float("nan")
    )
    ma50_v = (
        float(last_full["MA50"])
        if "MA50" in data.columns and pd.notna(last_full.get("MA50"))
        else float("nan")
    )
    sent_label, sent_score, sent_cls = _sentiment_for_kpi(sent)

    st.markdown(
        _kpi_strip_html(last_close, day_pct, ma20_v, ma50_v, sent_label, sent_score, sent_cls),
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        head1, head2, head3 = st.columns([2.2, 2.8, 1.4])
        with head1:
            st.markdown(
                f'<div class="sa-chart-title">{ticker} — price & volume</div>',
                unsafe_allow_html=True,
            )
        with head2:
            rng = st.pills(
                "Range",
                ["1M", "3M", "1Y", "All"],
                default="1Y",
                selection_mode="single",
                key=f"pill_rng_{ticker}",
                label_visibility="collapsed",
            )
        with head3:
            ai_ann = st.toggle("AI annotated", value=True, key=f"ai_ann_{ticker}")

        range_key = rng if rng in ("1M", "3M", "1Y", "All") else "1Y"
        view = _filter_df_by_chart_range(data, range_key)
        if view.empty:
            st.warning("Not enough rows in this window.")
            return

        if combined_chart:
            fig = charts.make_finsight_price_volume_figure(
                view,
                title=None,
                ai_annotated=bool(ai_ann),
            )
            st.plotly_chart(fig, width="stretch")
        else:
            st.plotly_chart(charts.make_candlestick_figure(view), width="stretch")
            st.plotly_chart(charts.make_volume_figure(view), width="stretch")

    if show_ai_insights:
        _render_ai_insights_section(ticker, data)


def _render_compare_tab(
    tickers: list[str],
    start_date,
    end_date,
    *,
    combined_chart: bool,
    show_ai_insights: bool,
) -> None:
    _ = combined_chart
    if len(tickers) < 2:
        st.info("Add at least two tickers in the sidebar to use Compare.")
        return

    datasets: dict[str, pd.DataFrame] = {}

    with st.container(border=True):
        bar1, bar2 = st.columns([2.2, 3.2])
        with bar1:
            st.markdown(
                '<div class="sa-chart-title">Compare — normalized return</div>',
                unsafe_allow_html=True,
            )
        with bar2:
            rng = st.pills(
                "Range",
                ["1M", "3M", "1Y", "All"],
                default="1Y",
                selection_mode="single",
                key="pill_rng_compare",
                label_visibility="collapsed",
            )

        range_key = rng if rng in ("1M", "3M", "1Y", "All") else "1Y"
        for t in tickers:
            raw = fetch_stock_data(t, start_date, end_date)
            if raw.empty:
                continue
            prep = _prepare_ohlcv(raw)
            datasets[t] = _filter_df_by_chart_range(prep, range_key)

        if len(datasets) < 2:
            st.warning("Could not load enough symbols to compare.")
            return

        fig = charts.make_compare_normalized_figure(datasets, title=None)
        st.plotly_chart(fig, width="stretch")

    if show_ai_insights:
        st.caption("Open a symbol tab for headline sentiment and the **AI analyst** tab for Groq + chat.")


def _run_app(
    tickers: list[str],
    start_date,
    end_date,
    *,
    combined_chart: bool,
    show_ai_insights: bool,
) -> None:
    if not tickers:
        st.warning("Please select at least one ticker.")
        return

    tab_labels = list(tickers) + (["Compare"] if len(tickers) >= 2 else [])
    tabs = st.tabs(tab_labels)
    for i, t in enumerate(tickers):
        with tabs[i]:
            _render_ticker_dashboard(
                t,
                start_date,
                end_date,
                combined_chart=combined_chart,
                show_ai_insights=show_ai_insights,
            )
    if len(tickers) >= 2:
        with tabs[-1]:
            _render_compare_tab(
                tickers,
                start_date,
                end_date,
                combined_chart=combined_chart,
                show_ai_insights=show_ai_insights,
            )


def _init_chat_state(primary: str) -> None:
    key = f"ai_chat_msgs::{primary}"
    if key not in st.session_state:
        st.session_state[key] = []


def _format_relative_time(_iso: str | None = None) -> str:
    return "Just now"


def _source_chips_for_hits(hits: dict[str, Any]) -> list[str]:
    metas = (hits.get("metadatas") or [[]])[0] or []
    chips: list[str] = []
    seen: set[str] = set()
    for m in metas:
        if not isinstance(m, dict):
            continue
        kind = str(m.get("kind", "doc")).lower()
        t = str(m.get("ticker", "")).upper()
        if kind == "news":
            label = f"News · {t}" if t else "News"
        elif kind == "summary":
            label = "Price data · yfinance"
        elif kind == "analysis":
            label = "Analyst report · Groq"
        else:
            label = kind.capitalize()
        if label not in seen:
            seen.add(label)
            chips.append(label)
    return chips[:4]


def _render_chat_header(primary: str, tickers: list[str]) -> str:
    """Render the RAG analyst card header + focus row. Returns selected focus ticker."""
    _chat_html(
        '<div class="sa-chat-card">'
        '<div class="sa-chat-header">'
        '<div class="sa-chat-header-left">'
        '<div class="sa-chat-avatar">AI</div>'
        '<div>'
        '<p class="sa-chat-title">RAG analyst</p>'
        '<p class="sa-chat-sub">Grounded in real price data + news</p>'
        '</div>'
        '</div>'
        '<div class="sa-chat-live"><span class="dot"></span> Live</div>'
        '</div>'
        '</div>'
    )
    fc1, fc2 = st.columns([0.5, 6])
    with fc1:
        st.markdown(
            "<div style='padding-top:6px;font-size:0.8rem;color:rgba(203,213,225,0.7);'>Focus:</div>",
            unsafe_allow_html=True,
        )
    with fc2:
        focus = st.pills(
            "Focus ticker",
            options=tickers,
            default=primary if primary in tickers else tickers[0],
            selection_mode="single",
            key="rag_focus_pills",
            label_visibility="collapsed",
        )
    return focus or primary


def _render_chat_message(msg: dict[str, Any]) -> None:
    role = msg.get("role", "user")
    raw_content = str(msg.get("content", ""))
    when = html.escape(str(msg.get("when") or _format_relative_time()))
    if role == "user":
        content = html.escape(raw_content)
        _chat_html(
            f'<div class="sa-msg-row user">'
            f'<div class="sa-chat-avatar user">You</div>'
            f'<div class="sa-msg-stack">'
            f'<div class="sa-msg-bubble">{content}</div>'
            f'<div class="sa-msg-meta">{when}</div>'
            f'</div>'
            f'</div>'
        )
        return

    sources = msg.get("sources") or []
    n_sources = int(msg.get("n_sources") or len(sources))
    badge = (
        f'<div class="sa-rag-badge"><span class="dot"></span> RAG · {n_sources} sources used</div>'
        if n_sources > 0
        else ""
    )
    chips_html = ""
    if sources:
        chips = "".join(
            f'<span class="sa-src-chip">{html.escape(s)}</span>' for s in sources
        )
        chips_html = f'<div class="sa-src-row">{chips}</div>'

    _chat_html(
        f'<div class="sa-msg-row">'
        f'<div class="sa-chat-avatar">AI</div>'
        f'<div class="sa-msg-stack">'
        f'{badge}'
        f'<div class="sa-msg-bubble">{raw_content}</div>'
        f'{chips_html}'
        f'<div class="sa-msg-meta">{when}</div>'
        f'</div>'
        f'</div>'
    )


def _render_typing_indicator() -> None:
    _chat_html(
        '<div class="sa-msg-row">'
        '<div class="sa-chat-avatar">AI</div>'
        '<div class="sa-typing"><span></span><span></span><span></span></div>'
        '</div>'
    )


def _generate_and_index_report(primary: str, stock_summary: str, headlines: list[dict[str, str]], sent: dict[str, Any]) -> str | None:
    """Helper to generate analysis report and update ChromaDB with all context (including the report)."""
    report_key = f"ai_md_report::{primary}"
    try:
        md = llm_agent.generate_stock_analysis(stock_summary, headlines, sent)
        st.session_state[report_key] = md

        try:
            collection = rag.get_or_create_collection()
            rag.delete_ticker_documents(collection, primary)

            docs: list[str] = []
            metas: list[dict[str, Any]] = []
            ids: list[str] = []

            docs.append(stock_summary)
            metas.append({"ticker": primary, "kind": "summary"})
            ids.append(f"{primary}::summary")

            for i, h in enumerate(headlines[:25]):
                docs.append(f"Headline: {h['title']}\nURL: {h['link']}")
                metas.append({"ticker": primary, "kind": "news"})
                ids.append(f"{primary}::news::{i}")

            docs.append(md)
            metas.append({"ticker": primary, "kind": "analysis"})
            ids.append(f"{primary}::analysis")

            rag.add_documents(collection, documents=docs, metadatas=metas, ids=ids)
        except Exception as exc:
            st.warning(f"Chroma indexing warning: {exc}")
        return md
    except Exception as exc:
        st.error(f"LLM error: {exc}")
        st.session_state.pop(report_key, None)
        return None


def _render_ai_analyst_tab(tickers: list[str], start_date, end_date) -> None:
    st.subheader("AI analyst")
    if not tickers:
        st.warning("Select at least one ticker in the sidebar.")
        return

    if "ai_analyst_primary" not in st.session_state or st.session_state["ai_analyst_primary"] not in tickers:
        st.session_state["ai_analyst_primary"] = tickers[0]

    primary = st.session_state["ai_analyst_primary"]

    st.markdown('<p class="sa-side-section" style="margin-top:0.2rem;margin-bottom:0.5rem;">Select Ticker Focus</p>', unsafe_allow_html=True)

    card_cols = st.columns(min(len(tickers), 6))
    for idx, t in enumerate(tickers):
        with card_cols[idx % min(len(tickers), 6)]:
            raw_t = fetch_stock_data(t, start_date, end_date)
            if not raw_t.empty:
                last_p = float(raw_t["Close"].iloc[-1])
                prev_p = float(raw_t["Close"].iloc[-2]) if len(raw_t) >= 2 else last_p
                pct_chg = (last_p / prev_p - 1.0) * 100.0 if prev_p else 0.0
                sign = "+" if pct_chg >= 0 else ""
                card_label = f"{t} · ${last_p:,.2f} ({sign}{pct_chg:.2f}%)"
            else:
                card_label = t

            is_active = (t == primary)
            btn_type = "primary" if is_active else "secondary"
            if st.button(card_label, key=f"ai_ticker_card_{t}", type=btn_type, use_container_width=True):
                st.session_state["ai_analyst_primary"] = t
                st.session_state["rag_focus_pills"] = t
                st.rerun()

    _init_chat_state(primary)

    raw_data = fetch_stock_data(primary, start_date, end_date)
    if raw_data.empty:
        st.error(f"No yfinance data for {primary} in the selected range.")
        return

    data = _prepare_ohlcv(raw_data)

    with st.spinner("Fetching latest headlines…"):
        headlines = _cached_headlines(primary)

    titles = [h["title"] for h in headlines]
    sent = _cached_sentiment(tuple(titles[:40])) if titles else sentiment.analyze_headlines_sentiment([])

    last_full = data.iloc[-1]
    last_close = float(last_full["Close"])
    if len(data) >= 2:
        prev_close = float(data["Close"].iloc[-2])
        day_pct = (last_close / prev_close - 1.0) * 100.0 if prev_close else 0.0
    else:
        day_pct = 0.0

    ma20_v = (
        float(last_full["MA20"])
        if "MA20" in data.columns and pd.notna(last_full.get("MA20"))
        else float("nan")
    )
    ma50_v = (
        float(last_full["MA50"])
        if "MA50" in data.columns and pd.notna(last_full.get("MA50"))
        else float("nan")
    )
    sent_label, sent_score, sent_cls = _sentiment_for_kpi(sent)

    st.markdown(
        _kpi_strip_html(last_close, day_pct, ma20_v, ma50_v, sent_label, sent_score, sent_cls),
        unsafe_allow_html=True,
    )

    stock_summary = _stock_text_summary(primary, data)

    st.markdown("#### News (Google News RSS)")
    if not headlines:
        st.warning("No headlines returned. The RSS feed may be empty or temporarily blocked.")
    else:
        for h in headlines[:12]:
            st.markdown(f"- [{h['title']}]({h['link']})")

    st.markdown("#### Sentiment (FinBERT)")
    if sent.get("error"):
        st.warning(sent["error"])
    else:
        _render_sentiment_bars(sent.get("labels_pct") or {})

    st.markdown("#### AI report (Groq)")
    report_key = f"ai_md_report::{primary}"

    # Auto-generate report on select if not already in session state
    if report_key not in st.session_state:
        with st.spinner(f"Generating AI analyst report for {primary}..."):
            _generate_and_index_report(primary, stock_summary, headlines, sent)

    col_rep1, col_rep2 = st.columns([8, 2])
    with col_rep1:
        st.caption("AI report automatically generated based on latest data.")
    with col_rep2:
        refresh_ai = st.button("Refresh report", key=f"refresh_report_{primary}")
        if refresh_ai:
            with st.spinner(f"Re-generating AI report for {primary}..."):
                _generate_and_index_report(primary, stock_summary, headlines, sent)
                st.rerun()

    if st.session_state.get(report_key):
        st.markdown(st.session_state[report_key])

    st.markdown("---")
    _render_chat_section(tickers, primary)


def _render_chat_section(tickers: list[str], default_focus: str) -> None:
    focus = _render_chat_header(default_focus, tickers)
    _init_chat_state(focus)
    chat_key = f"ai_chat_msgs::{focus}"

    history = st.session_state.get(chat_key, [])
    if not history:
        _render_chat_message(
            {
                "role": "assistant",
                "content": (
                    f"Hi — I'm the RAG analyst for <b>{html.escape(focus)}</b>. Ask me about "
                    "price moves, news drivers, sentiment, or risks. I'll cite the sources I used."
                ),
                "n_sources": 0,
                "when": "now",
            }
        )
    else:
        for msg in history:
            _render_chat_message(msg)

    pending = st.session_state.get(f"pending_user::{focus}")
    if pending:
        _render_typing_indicator()

    quick = st.pills(
        "Quick actions",
        options=[
            "Bull vs bear case?",
            f"Compare with {next((t for t in tickers if t != focus), 'peers')}",
            "Key risk factors",
            "Sentiment trend",
        ],
        selection_mode="single",
        key=f"rag_quick_{focus}",
        label_visibility="collapsed",
    )

    in_tag, in_box = st.columns([0.6, 9])
    with in_tag:
        st.markdown(
            f'<div class="sa-input-tag">{focus}</div>',
            unsafe_allow_html=True,
        )
    with in_box:
        prompt = st.chat_input(f"Ask about {focus}… e.g. Why might it be volatile?")

    st.markdown(
        '<p class="sa-chat-foot">Grounded in saved price data, news &amp; analyst summaries</p>',
        unsafe_allow_html=True,
    )

    user_text = prompt or (quick if isinstance(quick, str) else None)
    if not user_text:
        if pending:
            _process_pending_chat(focus, pending)
        return

    st.session_state[chat_key].append(
        {"role": "user", "content": user_text, "when": "Just now"}
    )
    st.session_state[f"pending_user::{focus}"] = user_text
    st.rerun()


def _process_pending_chat(focus: str, user_text: str) -> None:
    chat_key = f"ai_chat_msgs::{focus}"
    sources: list[str] = []
    n_sources = 0
    try:
        collection = rag.get_or_create_collection()
        hits = rag.query_documents(
            collection,
            query_text=user_text,
            n_results=6,
            where={"ticker": focus},
        )
        sources = _source_chips_for_hits(hits)
        n_sources = len(((hits.get("documents") or [[]])[0]) or [])
        ctx = rag.format_query_results(hits)
        answer = llm_agent.answer_with_rag(user_text, ctx, focus)
    except Exception as exc:
        answer = f"Chat error: {exc}"

    st.session_state[chat_key].append(
        {
            "role": "assistant",
            "content": answer,
            "sources": sources,
            "n_sources": n_sources,
            "when": "Just now",
        }
    )
    st.session_state.pop(f"pending_user::{focus}", None)
    st.rerun()


def _ensure_portfolio_indexed(tickers: list[str], start_date, end_date) -> None:
    """Ensure that stock summary and news for all tickers are loaded and indexed in ChromaDB."""
    for ticker in tickers:
        indexed_key = f"chroma_indexed::{ticker}::{start_date}::{end_date}"
        if indexed_key not in st.session_state:
            raw_data = fetch_stock_data(ticker, start_date, end_date)
            if not raw_data.empty:
                data = _prepare_ohlcv(raw_data)
                stock_summary = _stock_text_summary(ticker, data)
                headlines = _cached_headlines(ticker)
                
                try:
                    collection = rag.get_or_create_collection()
                    rag.delete_ticker_documents(collection, ticker)
                    
                    docs: list[str] = []
                    metas: list[dict[str, Any]] = []
                    ids: list[str] = []
                    
                    docs.append(stock_summary)
                    metas.append({"ticker": ticker, "kind": "summary"})
                    ids.append(f"{ticker}::summary")
                    
                    for i, h in enumerate(headlines[:25]):
                        docs.append(f"Headline: {h['title']}\nURL: {h['link']}")
                        metas.append({"ticker": ticker, "kind": "news"})
                        ids.append(f"{ticker}::news::{i}")
                        
                    rag.add_documents(collection, documents=docs, metadatas=metas, ids=ids)
                    st.session_state[indexed_key] = True
                except Exception as exc:
                    st.warning(f"Chroma background indexing warning for {ticker}: {exc}")


def run() -> None:
    load_dotenv()

    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    _inject_styles()

    (
        tickers,
        start_date,
        end_date,
        enable_refresh,
        refresh_interval,
        combined_chart,
        show_ai_insights,
    ) = _sidebar_inputs()

    if tickers:
        with st.spinner("Indexing portfolio news & data for AI Analyst..."):
            _ensure_portfolio_indexed(tickers, start_date, end_date)

    if enable_refresh:
        st_autorefresh(interval=refresh_interval * 1000, limit=None, key="refresh")

    tab_charts, tab_ai = st.tabs(["Dashboard", "AI analyst"])
    with tab_charts:
        with st.container(border=True):
            _run_app(
                tickers,
                start_date,
                end_date,
                combined_chart=combined_chart,
                show_ai_insights=show_ai_insights,
            )
    with tab_ai:
        with st.container(border=True):
            _render_ai_analyst_tab(tickers, start_date, end_date)
