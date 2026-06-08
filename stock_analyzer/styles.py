def sidebar_brand_html() -> str:
    return """
    <div class="sa-side-brand">FinSight <span>AI</span></div>
    """


def app_shell_css() -> str:
    return """
    <style>
    :root {
        --sa-accent:       #38bdf8;
        --sa-accent-2:     #818cf8;
        --sa-accent-glow:  rgba(56, 189, 248, 0.16);
        --sa-accent-ring:  rgba(56, 189, 248, 0.4);
        --sa-surface:      rgba(15, 23, 42, 0.85);
        --sa-surface-soft: rgba(255, 255, 255, 0.04);
        --sa-card:         rgba(17, 26, 46, 0.92);
        --sa-border:       rgba(148, 163, 184, 0.12);
        --sa-border-soft:  rgba(255, 255, 255, 0.06);
        --sa-text:         #f1f5f9;
        --sa-text-muted:   rgba(226, 232, 240, 0.55);
        --sa-text-dim:     rgba(226, 232, 240, 0.32);
        --sa-up:           #4ade80;
        --sa-dn:           #f87171;
        --sa-ai:           #a78bfa;
    }

    /* ── Base ── */
    .stApp {
        background: linear-gradient(165deg, #0a0f1a 0%, #0c1426 45%, #0a1020 100%);
        color: var(--sa-text);
        font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
    }
    .main .block-container {
        padding-top: 0.75rem;
        padding-bottom: 4rem;
        max-width: 1400px;
    }

    .sa-side-brand {
        font-size: 1.35rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin: 0 0 1.35rem;
        color: #f8fafc;
        line-height: 1.15;
    }
    .sa-side-brand span {
        background: linear-gradient(105deg, #38bdf8, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .sa-side-section {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: rgba(148, 163, 184, 0.9);
        margin: 1rem 0 0.35rem;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        border-right: 0.5px solid var(--sa-border);
    }
    [data-testid="stSidebar"] > div:first-child {
        background: linear-gradient(180deg, rgba(8, 12, 24, 0.98) 0%, rgba(10, 16, 32, 0.99) 100%);
        border-right: none;
        padding: 1.35rem 1.1rem;
        margin: 0;
        height: 100%;
    }
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] p {
        color: var(--sa-text-muted) !important;
        font-size: 0.8rem !important;
    }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: var(--sa-text) !important;
        font-size: 0.85rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }

    /* Multiselect pills */
    [data-testid="stMultiSelect"] [data-baseweb="tag"] {
        background: var(--sa-accent-glow) !important;
        border: 0.5px solid var(--sa-accent-ring) !important;
        border-radius: 6px !important;
        color: #93c5fd !important;
        font-size: 0.72rem !important;
    }
    [data-testid="stMultiSelect"] [data-baseweb="input"] {
        background: var(--sa-surface-soft) !important;
        border: 0.5px solid var(--sa-border) !important;
        border-radius: 8px !important;
    }

    /* Slider */
    [data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
        background: var(--sa-accent) !important;
        box-shadow: 0 0 0 4px var(--sa-accent-glow) !important;
    }
    [data-testid="stSlider"] [data-baseweb="slider"] [data-testid="stSliderTrackFill"] {
        background: var(--sa-accent) !important;
    }

    /* Date inputs */
    [data-testid="stDateInput"] input {
        background: var(--sa-surface-soft) !important;
        border: 0.5px solid var(--sa-border) !important;
        border-radius: 8px !important;
        color: var(--sa-text) !important;
        font-size: 0.8rem !important;
    }

    /* Checkbox */
    [data-testid="stCheckbox"] label {
        font-size: 0.8rem !important;
        color: var(--sa-text-muted) !important;
    }
    [data-testid="stCheckbox"] [data-baseweb="checkbox"] [data-checked="true"] {
        background: var(--sa-accent) !important;
        border-color: var(--sa-accent) !important;
    }

    /* Toggle switches (FinSight-style) */
    [data-testid="stToggle"] label {
        font-size: 0.82rem !important;
        color: #cbd5e1 !important;
        font-weight: 500 !important;
    }
    [data-testid="stToggle"] [data-baseweb="switch"] {
        background-color: rgba(51, 65, 85, 0.9) !important;
    }
    [data-testid="stToggle"] [data-baseweb="switch"][data-checked="true"] {
        background: linear-gradient(90deg, #38bdf8, #6366f1) !important;
    }

    /* Pills (time range) */
    [data-testid="stPills"] button {
        border-radius: 8px !important;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        border: 0.5px solid var(--sa-border) !important;
        background: rgba(255,255,255,0.03) !important;
        color: var(--sa-text-muted) !important;
    }
    [data-testid="stPills"] button[aria-pressed="true"] {
        background: var(--sa-accent-glow) !important;
        border-color: var(--sa-accent-ring) !important;
        color: #7dd3fc !important;
    }

    /* KPI strip (HTML cards) */
    .sa-kpi-row {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 12px;
        margin-bottom: 1.25rem;
    }
    @media (max-width: 900px) {
        .sa-kpi-row { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    }
    .sa-kpi-card {
        background: var(--sa-card);
        border: 0.5px solid var(--sa-border);
        border-radius: 14px;
        padding: 1rem 1.1rem;
        min-height: 92px;
    }
    .sa-kpi-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--sa-text-dim);
        margin-bottom: 0.35rem;
    }
    .sa-kpi-value {
        font-size: 1.55rem;
        font-weight: 700;
        letter-spacing: -0.02em;
        color: #f8fafc;
        line-height: 1.15;
    }
    .sa-kpi-sub {
        font-size: 0.78rem;
        color: var(--sa-text-muted);
        margin-top: 0.25rem;
    }
    .sa-kpi-up { color: var(--sa-up) !important; font-weight: 600; }
    .sa-kpi-dn { color: var(--sa-dn) !important; font-weight: 600; }
    .sa-kpi-sent-bull { color: var(--sa-up) !important; }
    .sa-kpi-sent-bear { color: var(--sa-dn) !important; }
    .sa-kpi-sent-neu { color: #cbd5e1 !important; }

    /* Chart card header row */
    .sa-chart-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin-bottom: 0.65rem;
    }
    .sa-chart-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #f8fafc;
        letter-spacing: -0.02em;
    }

    /* ── Tabs ── */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        gap: 4px;
        background: rgba(13, 27, 45, 0.6);
        border-radius: 10px;
        padding: 4px;
        border: 0.5px solid var(--sa-border);
        margin-bottom: 1.25rem;
    }
    [data-testid="stTabs"] [data-baseweb="tab"] {
        border-radius: 8px;
        color: var(--sa-text-muted);
        font-size: 0.8rem;
        padding: 0.45rem 1rem;
        transition: background 0.15s, color 0.15s;
    }
    [data-testid="stTabs"] [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(56,189,248,0.22), rgba(129,140,248,0.18)) !important;
        color: #e0f2fe !important;
        border: 0.5px solid var(--sa-accent-ring) !important;
        font-weight: 600 !important;
    }

    /* ── Expanders ── */
    div[data-testid="stExpander"] {
        background: var(--sa-surface-soft);
        border: 0.5px solid var(--sa-border) !important;
        border-radius: 10px;
        overflow: hidden;
        margin-bottom: 0.75rem;
    }
    div[data-testid="stExpander"] summary {
        font-size: 0.85rem;
        font-weight: 500;
        color: var(--sa-text) !important;
        padding: 0.65rem 1rem;
    }
    div[data-testid="stExpander"] summary:hover {
        background: var(--sa-surface-soft);
    }

    /* ── Metric cards ── */
    [data-testid="stMetric"] {
        background: var(--sa-surface-soft);
        border: 0.5px solid var(--sa-border);
        border-radius: 10px;
        padding: 0.85rem 1rem;
    }
    [data-testid="stMetricValue"] {
        color: var(--sa-text) !important;
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em;
    }
    [data-testid="stMetricLabel"] {
        color: var(--sa-text-dim) !important;
        font-size: 0.72rem !important;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    [data-testid="stMetricDelta"] svg { display: none; }
    [data-testid="stMetricDelta"] [data-testid="stMetricDeltaPositive"] {
        color: var(--sa-up) !important;
        font-size: 0.72rem !important;
    }
    [data-testid="stMetricDelta"] [data-testid="stMetricDeltaNegative"] {
        color: var(--sa-dn) !important;
        font-size: 0.72rem !important;
    }

    /* ── Dataframe ── */
    [data-testid="stDataFrame"] {
        border: 0.5px solid var(--sa-border) !important;
        border-radius: 10px !important;
        overflow: hidden;
    }
    [data-testid="stDataFrame"] th {
        background: rgba(255,255,255,0.04) !important;
        color: var(--sa-text-dim) !important;
        font-size: 0.72rem !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    [data-testid="stDataFrame"] td {
        color: var(--sa-text) !important;
        font-size: 0.8rem !important;
        border-top: 0.5px solid var(--sa-border-soft) !important;
    }

    /* ── Chat / AI messages ── */
    div[data-testid="stChatMessage"] {
        border-radius: 10px;
        border: 0.5px solid var(--sa-border);
        background: rgba(10, 20, 34, 0.5);
        padding: 0.85rem 1rem;
        margin-bottom: 0.5rem;
    }
    div[data-testid="stChatMessage"][data-testid*="assistant"] {
        border-left: 2px solid var(--sa-ai);
        background: rgba(167, 139, 250, 0.04);
    }
    [data-testid="stChatInputContainer"] {
        border: 0.5px solid var(--sa-border) !important;
        border-radius: 10px !important;
        background: rgba(13, 27, 45, 0.7) !important;
    }

    /* ── Alerts ── */
    .stAlert {
        border-radius: 8px !important;
        border: 0.5px solid var(--sa-border) !important;
        font-size: 0.82rem !important;
    }
    div[data-baseweb="notification"][kind="positive"] {
        background: rgba(74, 222, 128, 0.06) !important;
        border-color: rgba(74, 222, 128, 0.25) !important;
        color: #86efac !important;
    }
    div[data-baseweb="notification"][kind="warning"] {
        background: rgba(251, 191, 36, 0.06) !important;
        border-color: rgba(251, 191, 36, 0.25) !important;
        color: #fde68a !important;
    }

    /* ── Buttons ── */
    .stButton button {
        background: var(--sa-accent-glow) !important;
        border: 0.5px solid var(--sa-accent-ring) !important;
        border-radius: 8px !important;
        color: #93c5fd !important;
        font-size: 0.8rem !important;
        font-weight: 500 !important;
        padding: 0.45rem 1rem !important;
        transition: background 0.15s !important;
    }
    .stButton button:hover {
        background: rgba(78, 154, 241, 0.28) !important;
    }

    /* ── Plotly charts ── */
    [data-testid="stPlotlyChart"] {
        border: 0.5px solid var(--sa-border);
        border-radius: 14px;
        overflow: hidden;
        background: rgba(8, 15, 28, 0.75);
    }

    /* Bordered main panels */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 16px !important;
        border-color: var(--sa-border) !important;
        background: rgba(12, 18, 34, 0.35) !important;
        padding: 1rem 1.15rem !important;
    }
    </style>
    """


def title_block_html() -> str:
    return """
    <style>
    .sa-hero {
        padding: 0.5rem 0 1rem;
        border-bottom: 0.5px solid rgba(255,255,255,0.07);
        margin-bottom: 1.25rem;
    }
    .sa-hero-flex {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        gap: 1rem;
        flex-wrap: wrap;
    }
    .sa-hero-ai-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 14px;
        border-radius: 999px;
        background: rgba(129, 140, 248, 0.12);
        border: 0.5px solid rgba(167, 139, 250, 0.35);
        font-size: 0.78rem;
        font-weight: 600;
        color: #ddd6fe;
        margin-bottom: 0.15rem;
    }
    .sa-hero-ai-pill .sa-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #a78bfa;
        box-shadow: 0 0 10px rgba(167, 139, 250, 0.7);
    }
    .sa-eyebrow {
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #38bdf8;
        margin-bottom: 0.3rem;
    }
    .sa-title {
        font-size: clamp(1.5rem, 3vw, 2rem);
        font-weight: 700;
        letter-spacing: -0.03em;
        color: #f0f4f8;
        margin: 0 0 0.25rem;
        animation: saFadeUp 0.6s ease-out forwards;
        opacity: 0;
    }
    .sa-sub {
        font-size: 0.82rem;
        color: rgba(240,244,248,0.45);
        margin: 0;
        animation: saFadeUp 0.6s ease-out 0.1s forwards;
        opacity: 0;
    }
    .sa-badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: rgba(167,139,250,0.1);
        border: 0.5px solid rgba(167,139,250,0.3);
        border-radius: 6px;
        padding: 2px 10px;
        font-size: 0.68rem;
        font-weight: 500;
        color: #c4b5fd;
        margin-left: 10px;
        vertical-align: middle;
        letter-spacing: 0.04em;
    }
    .sa-badge::before {
        content: "";
        display: inline-block;
        width: 5px;
        height: 5px;
        background: #a78bfa;
        border-radius: 50%;
    }
    @keyframes saFadeUp {
        from { opacity:0; transform: translateY(10px); }
        to   { opacity:1; transform: translateY(0); }
    }
    </style>
    <div class="sa-hero sa-hero-flex">
        <div>
            <div class="sa-eyebrow">AI-powered</div>
            <h1 class="sa-title">
                AI Stock Analyst
                <span class="sa-badge">Gen AI</span>
            </h1>
            <p class="sa-sub">Charts · news sentiment · AI insights</p>
        </div>
        <div class="sa-hero-ai-pill"><span class="sa-dot"></span> AI analyst</div>
    </div>
    """


def chat_css() -> str:
    return """
    <style>
    .sa-chat-card {
        background: rgba(12, 18, 32, 0.65);
        border: 0.5px solid rgba(148, 163, 184, 0.12);
        border-radius: 16px;
        padding: 0;
        margin-bottom: 1rem;
        overflow: hidden;
    }
    .sa-chat-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.95rem 1.1rem;
        border-bottom: 0.5px solid rgba(148, 163, 184, 0.10);
        background: rgba(15, 22, 38, 0.55);
    }
    .sa-chat-header-left {
        display: flex;
        align-items: center;
        gap: 0.85rem;
    }
    .sa-chat-avatar {
        width: 38px;
        height: 38px;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(167,139,250,0.22), rgba(99,102,241,0.18));
        border: 0.5px solid rgba(167,139,250,0.45);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #c4b5fd;
        font-weight: 700;
        font-size: 0.78rem;
        letter-spacing: 0.04em;
    }
    .sa-chat-avatar.user {
        background: linear-gradient(135deg, rgba(56,189,248,0.18), rgba(59,130,246,0.18));
        border-color: rgba(56,189,248,0.45);
        color: #7dd3fc;
    }
    .sa-chat-title {
        font-size: 1rem;
        font-weight: 700;
        color: #f1f5f9;
        line-height: 1.15;
        margin: 0;
    }
    .sa-chat-sub {
        font-size: 0.78rem;
        color: rgba(203,213,225,0.65);
        margin: 2px 0 0;
    }
    .sa-chat-live {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 0.75rem;
        font-weight: 600;
        color: #86efac;
    }
    .sa-chat-live .dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #4ade80;
        box-shadow: 0 0 8px rgba(74,222,128,0.7);
    }

    .sa-chat-focus {
        display: flex;
        align-items: center;
        gap: 0.65rem;
        padding: 0.7rem 1.1rem;
        border-bottom: 0.5px solid rgba(148, 163, 184, 0.08);
        font-size: 0.8rem;
        color: rgba(203,213,225,0.7);
    }

    .sa-chat-body {
        padding: 1rem 1.1rem;
        min-height: 200px;
    }

    .sa-msg-row {
        display: flex;
        gap: 12px;
        margin: 0.6rem 0 1rem;
        align-items: flex-start;
    }
    .sa-msg-row.user { flex-direction: row-reverse; }

    .sa-msg-bubble {
        max-width: 70%;
        padding: 0.75rem 1rem;
        border-radius: 14px;
        font-size: 0.9rem;
        line-height: 1.5;
        color: #e2e8f0;
        background: rgba(20, 30, 50, 0.85);
        border: 0.5px solid rgba(148, 163, 184, 0.14);
    }
    .sa-msg-row.user .sa-msg-bubble {
        background: rgba(56, 189, 248, 0.13);
        border-color: rgba(56, 189, 248, 0.32);
        color: #e0f2fe;
    }
    .sa-msg-meta {
        font-size: 0.68rem;
        color: rgba(148,163,184,0.55);
        margin-top: 0.3rem;
    }
    .sa-msg-row.user .sa-msg-stack { align-items: flex-end; }
    .sa-msg-stack {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 0;
        max-width: 78%;
    }

    .sa-rag-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.7rem;
        font-weight: 600;
        color: #c4b5fd;
        background: rgba(167,139,250,0.10);
        border: 0.5px solid rgba(167,139,250,0.32);
        border-radius: 999px;
        padding: 3px 10px;
        margin-bottom: 6px;
    }
    .sa-rag-badge .dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #a78bfa;
    }

    .sa-src-row {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 8px;
    }
    .sa-src-chip {
        font-size: 0.7rem;
        color: rgba(203,213,225,0.7);
        background: rgba(255,255,255,0.03);
        border: 0.5px solid rgba(148,163,184,0.18);
        border-radius: 8px;
        padding: 3px 9px;
        display: inline-flex;
        align-items: center;
        gap: 6px;
    }
    .sa-src-chip::before {
        content: "ⓘ";
        opacity: 0.55;
        font-size: 0.7rem;
    }

    .sa-typing {
        display: inline-flex;
        gap: 4px;
        padding: 8px 14px;
        background: rgba(20, 30, 50, 0.85);
        border: 0.5px solid rgba(148, 163, 184, 0.14);
        border-radius: 14px;
    }
    .sa-typing span {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: rgba(203,213,225,0.65);
        animation: saTyping 1.2s infinite;
    }
    .sa-typing span:nth-child(2) { animation-delay: 0.15s; }
    .sa-typing span:nth-child(3) { animation-delay: 0.3s; }
    @keyframes saTyping {
        0%, 60%, 100% { opacity: 0.3; transform: translateY(0); }
        30% { opacity: 1; transform: translateY(-2px); }
    }

    .sa-chat-foot {
        font-size: 0.72rem;
        color: rgba(148,163,184,0.6);
        text-align: center;
        margin-top: 0.5rem;
    }

    .sa-input-tag {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.72rem;
        font-weight: 700;
        color: #93c5fd;
        background: rgba(56,189,248,0.13);
        border: 0.5px solid rgba(56,189,248,0.32);
        border-radius: 8px;
        padding: 7px 10px;
        height: 38px;
    }
    </style>
    """


def hide_streamlit_chrome_css() -> str:
    return """
    <style> 
    #MainMenu  { visibility: hidden; }
    footer     { visibility: hidden; }
    header     { visibility: hidden; }
    </style>
    """