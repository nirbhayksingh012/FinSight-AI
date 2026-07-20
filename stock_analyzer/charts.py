from __future__ import annotations

import pandas as pd
# pyrefly: ignore [missing-import]
import plotly.graph_objects as go
# pyrefly: ignore [missing-import]
from plotly.subplots import make_subplots
from stock_analyzer.constants import CHART_LAYOUT


def _apply_dark_layout(fig: go.Figure, **extra) -> go.Figure:
    layout = {**CHART_LAYOUT, **extra}
    fig.update_layout(**layout)
    return fig


def make_candlestick_figure(data: pd.DataFrame) -> go.Figure:
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data["Date"],
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
                increasing_line_color="#22c55e",
                decreasing_line_color="#ef4444",
            )
        ]
    )
    fig.add_trace(
        go.Scatter(
            x=data["Date"],
            y=data["MA20"],
            mode="lines",
            name="MA20",
            line=dict(color="#818cf8", width=1),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data["Date"],
            y=data["MA50"],
            mode="lines",
            name="MA50",
            line=dict(color="#fbbf24", width=1.5),
        )
    )
    return _apply_dark_layout(fig)


def make_volume_figure(data: pd.DataFrame) -> go.Figure:
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=data["Date"],
            y=data["Volume"],
            name="Volume",
            marker_color="#6366f1",
        )
    )
    return _apply_dark_layout(fig)


def _volume_bar_colors(data: pd.DataFrame) -> list[str]:
    colors: list[str] = []
    for i in range(len(data)):
        o = float(data["Open"].iloc[i])
        c = float(data["Close"].iloc[i])
        colors.append("#22c55e" if c >= o else "#ef4444")
    return colors


def make_finsight_price_volume_figure(
    data: pd.DataFrame,
    *,
    title: str | None = None,
    ai_annotated: bool = False,
    annotation_text: str = "AI: earnings beat",
) -> go.Figure:
    """Line price + MAs on top, green/red volume bars below (FinSight-style)."""
    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        row_heights=[0.68, 0.32],
    )

    fig.add_trace(
        go.Scatter(
            x=data["Date"],
            y=data["Close"],
            mode="lines",
            name="Close",
            line=dict(color="#38bdf8", width=2.2),
        ),
        row=1,
        col=1,
    )
    if "MA50" in data.columns and data["MA50"].notna().any():
        fig.add_trace(
            go.Scatter(
                x=data["Date"],
                y=data["MA50"],
                mode="lines",
                name="MA 50",
                line=dict(color="#fbbf24", width=1.6),
            ),
            row=1,
            col=1,
        )
    if "MA20" in data.columns and data["MA20"].notna().any():
        fig.add_trace(
            go.Scatter(
                x=data["Date"],
                y=data["MA20"],
                mode="lines",
                name="MA 20",
                line=dict(color="rgba(129, 140, 248, 0.55)", width=1),
            ),
            row=1,
            col=1,
        )

    fig.add_trace(
        go.Bar(
            x=data["Date"],
            y=data["Volume"],
            name="Volume",
            marker_color=_volume_bar_colors(data),
            opacity=0.85,
        ),
        row=2,
        col=1,
    )

    fig.update_xaxes(showgrid=True, gridcolor="rgba(255,255,255,0.06)", zeroline=False)
    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(255,255,255,0.06)",
        zeroline=False,
        title_text="Price",
        row=1,
        col=1,
    )
    fig.update_yaxes(title_text="Volume", row=2, col=1)

    if ai_annotated and len(data) > 3:
        work = data.copy()
        dr = work["Close"].pct_change()
        if dr.notna().any():
            idx = dr.idxmax()
            if float(dr.loc[idx]) > 0:
                xd = work.loc[idx, "Date"]
                y_top = float(work["Close"].max()) * 1.02
                fig.add_vline(
                    x=xd,
                    line_width=1,
                    line_dash="dash",
                    line_color="#a78bfa",
                    row=1,
                    col=1,
                )
                fig.add_annotation(
                    x=xd,
                    y=y_top,
                    text=annotation_text,
                    showarrow=False,
                    yshift=0,
                    font=dict(size=11, color="#e9d5ff"),
                    bgcolor="rgba(99, 102, 241, 0.25)",
                    bordercolor="rgba(167, 139, 250, 0.5)",
                    borderwidth=1,
                    borderpad=4,
                    row=1,
                    col=1,
                )

    layout_updates: dict = {
        **CHART_LAYOUT,
        "legend": dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(0,0,0,0)",
            font=dict(size=11),
        ),
        "margin": dict(l=52, r=24, t=56 if title else 28, b=40),
        "hovermode": "x unified",
        "bargap": 0.15,
    }
    if title:
        layout_updates["title"] = dict(text=title, x=0.02, font=dict(size=15, color="#f1f5f9"))
    fig.update_layout(**layout_updates)
    fig.update_xaxes(rangeslider_visible=False)
    return fig


def make_compare_normalized_figure(
    datasets: dict[str, pd.DataFrame],
    *,
    title: str | None = None,
) -> go.Figure:
    """Overlay normalized close (% from series start) for multiple tickers."""
    fig = go.Figure()
    palette = ["#38bdf8", "#a78bfa", "#fbbf24", "#34d399", "#f472b6", "#94a3b8"]
    for i, (ticker, d) in enumerate(datasets.items()):
        if d.empty or "Close" not in d.columns:
            continue
        base = float(d["Close"].iloc[0])
        if base <= 0:
            continue
        y = (d["Close"].astype(float) / base - 1.0) * 100.0
        color = palette[i % len(palette)]
        fig.add_trace(
            go.Scatter(
                x=d["Date"],
                y=y,
                mode="lines",
                name=ticker,
                line=dict(width=2, color=color),
            )
        )
    layout_c: dict = {
        **CHART_LAYOUT,
        "yaxis_title": "Return from start (%)",
        "legend": dict(orientation="h", y=1.08, x=0, bgcolor="rgba(0,0,0,0)"),
        "margin": dict(l=52, r=24, t=28 if not title else 72, b=48),
        "hovermode": "x unified",
    }
    if title:
        layout_c["title"] = dict(text=title, x=0.02, font=dict(size=15, color="#f1f5f9"))
    fig.update_layout(**layout_c)
    fig.update_xaxes(showgrid=True, gridcolor="rgba(255,255,255,0.06)")
    fig.update_yaxes(showgrid=True, gridcolor="rgba(255,255,255,0.06)")
    return fig
