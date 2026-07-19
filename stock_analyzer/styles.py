def sidebar_brand_html() -> str:
    return """
    <div class="sa-side-brand">FinSight<span>AI</span></div>
    """

def app_shell_css() -> str:
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&family=Space+Mono:wght@400;700&display=swap');

    :root {
        --sa-accent:        #38bdf8;
        --sa-accent-2:      #818cf8;
        --sa-accent-3:      #f472b6;
        --sa-accent-glow:   rgba(56, 189, 248, 0.16);
        --sa-accent-ring:   rgba(56, 189, 248, 0.40);
        --sa-surface:       rgba(15, 23, 42, 0.85);
        --sa-surface-soft:  rgba(255, 255, 255, 0.04);
        --sa-card:          rgba(17, 26, 46, 0.92);
        --sa-border:        rgba(148, 163, 184, 0.12);
        --sa-border-soft:   rgba(255, 255, 255, 0.06);
        --sa-text:          #f1f5f9;
        --sa-text-muted:    rgba(226, 232, 240, 0.55);
        --sa-text-dim:      rgba(226, 232, 240, 0.32);
        --sa-up:            #4ade80;
        --sa-dn:            #f87171;
        --sa-ai:            #a78bfa;
        --sa-glow-cyan:     0 0 24px rgba(56,189,248,0.22), 0 0 48px rgba(56,189,248,0.08);
        --sa-glow-purple:   0 0 24px rgba(167,139,250,0.22), 0 0 48px rgba(167,139,250,0.08);
        --sa-glow-green:    0 0 16px rgba(74,222,128,0.30);
        --sa-radius-card:   16px;
        --sa-radius-sm:     10px;
        --sa-transition:    0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ── Page load animation ── */
    @keyframes saPageIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes saFadeUp {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes saPulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    @keyframes saShimmer {
        0%   { background-position: -200% center; }
        100% { background-position:  200% center; }
    }
    @keyframes saRotate {
        from { transform: rotate(0deg); }
        to   { transform: rotate(360deg); }
    }
    @keyframes saGlow {
        0%, 100% { box-shadow: 0 0 12px rgba(56,189,248,0.18); }
        50%       { box-shadow: 0 0 28px rgba(56,189,248,0.42), 0 0 56px rgba(56,189,248,0.12); }
    }
    @keyframes saSlideIn {
        from { opacity: 0; transform: translateX(-8px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes saBorderSpin {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* ── Base ── */
    .stApp {
        background:
            radial-gradient(ellipse 80% 50% at 50% -10%, rgba(56,189,248,0.06) 0%, transparent 60%),
            radial-gradient(ellipse 60% 40% at 80% 80%, rgba(129,140,248,0.05) 0%, transparent 50%),
            linear-gradient(165deg, #080d18 0%, #0a1020 45%, #080c18 100%);
        color: var(--sa-text);
        font-family: "DM Sans", system-ui, -apple-system, sans-serif;
        animation: saPageIn 0.5s ease-out forwards;
    }

    /* Subtle animated background grid */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background-image:
            linear-gradient(rgba(56,189,248,0.025) 1px, transparent 1px),
            linear-gradient(90deg, rgba(56,189,248,0.025) 1px, transparent 1px);
        background-size: 60px 60px;
        pointer-events: none;
        z-index: 0;
        mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 40%, transparent 100%);
    }

    .main .block-container {
        padding-top: 0.75rem;
        padding-bottom: 4rem;
        max-width: 1400px;
        position: relative;
        z-index: 1;
    }

    /* ── Brand ── */
    .sa-side-brand {
        font-size: 1.4rem;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin: 0 0 1.5rem;
        color: #f8fafc;
        line-height: 1.15;
        position: relative;
        display: inline-block;
        animation: saSlideIn 0.5s ease-out forwards;
    }
    .sa-side-brand span {
        background: linear-gradient(105deg, #38bdf8 0%, #818cf8 50%, #f472b6 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: saShimmer 4s linear infinite;
    }
    .sa-side-section {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: rgba(148, 163, 184, 0.7);
        margin: 1.1rem 0 0.4rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .sa-side-section::before {
        content: "";
        display: block;
        width: 14px;
        height: 1px;
        background: linear-gradient(90deg, var(--sa-accent), transparent);
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        border-right: 0.5px solid var(--sa-border);
    }
    [data-testid="stSidebar"] > div:first-child {
        background:
            radial-gradient(ellipse 60% 30% at 50% 0%, rgba(56,189,248,0.04) 0%, transparent 60%),
            linear-gradient(180deg, rgba(7, 11, 22, 0.99) 0%, rgba(9, 14, 28, 0.99) 100%);
        border-right: none;
        padding: 1.35rem 1.1rem;
        height: 100%;
        backdrop-filter: blur(12px);
    }
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] p {
        color: var(--sa-text-muted) !important;
        font-size: 0.8rem !important;
        transition: color var(--sa-transition) !important;
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
        transition: all var(--sa-transition) !important;
    }
    [data-testid="stMultiSelect"] [data-baseweb="tag"]:hover {
        background: rgba(56,189,248,0.24) !important;
        border-color: rgba(56,189,248,0.6) !important;
    }
    [data-testid="stMultiSelect"] [data-baseweb="input"] {
        background: var(--sa-surface-soft) !important;
        border: 0.5px solid var(--sa-border) !important;
        border-radius: 8px !important;
        transition: border-color var(--sa-transition) !important;
    }
    [data-testid="stMultiSelect"] [data-baseweb="input"]:focus-within {
        border-color: rgba(56,189,248,0.45) !important;
        box-shadow: 0 0 0 3px rgba(56,189,248,0.08) !important;
    }

    /* Slider */
    [data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
        background: var(--sa-accent) !important;
        box-shadow: 0 0 0 4px var(--sa-accent-glow), var(--sa-glow-cyan) !important;
        transition: box-shadow var(--sa-transition) !important;
    }
    [data-testid="stSlider"] [data-baseweb="slider"] [role="slider"]:hover {
        box-shadow: 0 0 0 6px rgba(56,189,248,0.2), 0 0 20px rgba(56,189,248,0.35) !important;
    }
    [data-testid="stSlider"] [data-baseweb="slider"] [data-testid="stSliderTrackFill"] {
        background: linear-gradient(90deg, var(--sa-accent), var(--sa-accent-2)) !important;
    }

    /* Date inputs */
    [data-testid="stDateInput"] input {
        background: var(--sa-surface-soft) !important;
        border: 0.5px solid var(--sa-border) !important;
        border-radius: 8px !important;
        color: var(--sa-text) !important;
        font-size: 0.8rem !important;
        transition: all var(--sa-transition) !important;
    }
    [data-testid="stDateInput"] input:focus {
        border-color: rgba(56,189,248,0.5) !important;
        box-shadow: 0 0 0 3px rgba(56,189,248,0.08), 0 0 12px rgba(56,189,248,0.12) !important;
        outline: none !important;
    }

    /* Checkbox */
    [data-testid="stCheckbox"] label {
        font-size: 0.8rem !important;
        color: var(--sa-text-muted) !important;
        transition: color var(--sa-transition) !important;
    }
    [data-testid="stCheckbox"]:hover label {
        color: var(--sa-text) !important;
    }
    [data-testid="stCheckbox"] [data-baseweb="checkbox"] [data-checked="true"] {
        background: linear-gradient(135deg, var(--sa-accent), var(--sa-accent-2)) !important;
        border-color: transparent !important;
        box-shadow: 0 0 10px rgba(56,189,248,0.35) !important;
    }

    /* Toggle switches */
    [data-testid="stToggle"] label {
        font-size: 0.82rem !important;
        color: #cbd5e1 !important;
        font-weight: 500 !important;
        transition: color var(--sa-transition) !important;
    }
    [data-testid="stToggle"] [data-baseweb="switch"] {
        background-color: rgba(51, 65, 85, 0.9) !important;
        transition: background var(--sa-transition), box-shadow var(--sa-transition) !important;
    }
    [data-testid="stToggle"] [data-baseweb="switch"][data-checked="true"] {
        background: linear-gradient(90deg, #38bdf8, #6366f1) !important;
        box-shadow: 0 0 14px rgba(56,189,248,0.30) !important;
    }

    /* Pills (time range) */
    [data-testid="stPills"] button {
        border-radius: 8px !important;
        font-size: 0.78rem !important;
        font-weight: 600 !important;
        border: 0.5px solid var(--sa-border) !important;
        background: rgba(255,255,255,0.03) !important;
        color: var(--sa-text-muted) !important;
        transition: all var(--sa-transition) !important;
        position: relative;
        overflow: hidden;
    }
    [data-testid="stPills"] button::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(135deg, rgba(56,189,248,0.12), rgba(129,140,248,0.08));
        opacity: 0;
        transition: opacity var(--sa-transition);
    }
    [data-testid="stPills"] button:hover::before { opacity: 1; }
    [data-testid="stPills"] button:hover {
        border-color: var(--sa-accent-ring) !important;
        color: #93c5fd !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.25);
    }
    [data-testid="stPills"] button[aria-pressed="true"] {
        background: linear-gradient(135deg, rgba(56,189,248,0.18), rgba(129,140,248,0.14)) !important;
        border-color: var(--sa-accent-ring) !important;
        color: #7dd3fc !important;
        box-shadow: 0 0 16px rgba(56,189,248,0.18), inset 0 1px 0 rgba(255,255,255,0.06) !important;
    }

    /* Active Ticker Button & Card Styles */
    div.stButton > button[kind="primary"],
    [data-testid="stBaseButton-primary"] {
        background: linear-gradient(135deg, rgba(56,189,248,0.28) 0%, rgba(99,102,241,0.32) 100%) !important;
        border: 1.5px solid #38bdf8 !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        box-shadow: 0 0 18px rgba(56,189,248,0.4), inset 0 1px 0 rgba(255,255,255,0.2) !important;
        border-radius: 10px !important;
        transition: all var(--sa-transition) !important;
    }
    div.stButton > button[kind="primary"]:hover,
    [data-testid="stBaseButton-primary"]:hover {
        background: linear-gradient(135deg, rgba(56,189,248,0.4) 0%, rgba(99,102,241,0.45) 100%) !important;
        border-color: #7dd3fc !important;
        box-shadow: 0 0 26px rgba(56,189,248,0.6) !important;
        transform: translateY(-1px) !important;
    }

    div.stButton > button[kind="secondary"],
    [data-testid="stBaseButton-secondary"] {
        background: rgba(17, 26, 46, 0.75) !important;
        border: 1px solid rgba(148, 163, 184, 0.2) !important;
        color: rgba(226, 232, 240, 0.75) !important;
        font-weight: 500 !important;
        border-radius: 10px !important;
        transition: all var(--sa-transition) !important;
    }
    div.stButton > button[kind="secondary"]:hover,
    [data-testid="stBaseButton-secondary"]:hover {
        background: rgba(30, 41, 59, 0.9) !important;
        border-color: rgba(56, 189, 248, 0.4) !important;
        color: #f1f5f9 !important;
        transform: translateY(-1px) !important;
    }

    /* Active Ticker Focus Banner */
    .sa-active-ticker-banner {
        display: flex;
        align-items: center;
        gap: 12px;
        background: linear-gradient(90deg, rgba(56, 189, 248, 0.14) 0%, rgba(129, 140, 248, 0.08) 100%);
        border: 1px solid rgba(56, 189, 248, 0.3);
        border-left: 4px solid #38bdf8;
        border-radius: 10px;
        padding: 11px 16px;
        margin: 14px 0 18px 0;
        font-size: 0.88rem;
        color: #f1f5f9;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
    }
    .sa-active-badge {
        background: #38bdf8;
        color: #080d18;
        font-weight: 800;
        font-size: 0.68rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        padding: 3px 8px;
        border-radius: 6px;
        display: inline-flex;
        align-items: center;
        box-shadow: 0 0 12px rgba(56, 189, 248, 0.5);
    }
    .sa-active-title {
        color: #cbd5e1;
    }
    .sa-active-title strong {
        color: #38bdf8;
        font-weight: 700;
    }

    /* ── KPI strip ── */
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
        background:
            linear-gradient(135deg, rgba(17,26,46,0.95) 0%, rgba(12,18,36,0.92) 100%);
        border: 0.5px solid var(--sa-border);
        border-radius: var(--sa-radius-card);
        padding: 1.1rem 1.2rem;
        min-height: 96px;
        position: relative;
        overflow: hidden;
        transition: transform var(--sa-transition), box-shadow var(--sa-transition), border-color var(--sa-transition);
        animation: saFadeUp 0.5s ease-out both;
    }
    .sa-kpi-card:nth-child(1) { animation-delay: 0.05s; }
    .sa-kpi-card:nth-child(2) { animation-delay: 0.10s; }
    .sa-kpi-card:nth-child(3) { animation-delay: 0.15s; }
    .sa-kpi-card:nth-child(4) { animation-delay: 0.20s; }

    /* Top accent line */
    .sa-kpi-card::before {
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 1.5px;
        background: linear-gradient(90deg, transparent, var(--sa-accent), transparent);
        opacity: 0;
        transition: opacity var(--sa-transition);
    }
    /* Ambient glow orb */
    .sa-kpi-card::after {
        content: "";
        position: absolute;
        top: -30px; right: -20px;
        width: 80px; height: 80px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(56,189,248,0.08) 0%, transparent 70%);
        pointer-events: none;
        transition: opacity var(--sa-transition);
        opacity: 0;
    }
    .sa-kpi-card:hover {
        transform: translateY(-2px);
        border-color: rgba(56,189,248,0.25);
        box-shadow: 0 8px 32px rgba(0,0,0,0.4), 0 0 0 0.5px rgba(56,189,248,0.15);
    }
    .sa-kpi-card:hover::before,
    .sa-kpi-card:hover::after { opacity: 1; }

    .sa-kpi-label {
        font-size: 0.67rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--sa-text-dim);
        margin-bottom: 0.4rem;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .sa-kpi-value {
        font-size: 1.65rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        color: #f8fafc;
        line-height: 1.1;
        font-family: "Space Mono", monospace;
        background: linear-gradient(135deg, #f8fafc 60%, rgba(248,250,252,0.7) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .sa-kpi-sub {
        font-size: 0.77rem;
        color: var(--sa-text-muted);
        margin-top: 0.3rem;
        display: flex;
        align-items: center;
        gap: 4px;
    }
    .sa-kpi-up { color: var(--sa-up) !important; font-weight: 700; }
    .sa-kpi-dn { color: var(--sa-dn) !important; font-weight: 700; }
    .sa-kpi-sent-bull { color: var(--sa-up) !important; }
    .sa-kpi-sent-bear { color: var(--sa-dn) !important; }
    .sa-kpi-sent-neu  { color: #cbd5e1 !important; }

    /* ── Chart card header ── */
    .sa-chart-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin-bottom: 0.75rem;
    }
    .sa-chart-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #f8fafc;
        letter-spacing: -0.025em;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .sa-chart-title::before {
        content: "";
        display: block;
        width: 3px;
        height: 18px;
        border-radius: 2px;
        background: linear-gradient(180deg, var(--sa-accent), var(--sa-accent-2));
        box-shadow: 0 0 8px rgba(56,189,248,0.5);
    }

    /* ── Tabs ── */
    [data-testid="stTabs"] [data-baseweb="tab-list"] {
        gap: 4px;
        background: rgba(10, 18, 32, 0.7);
        border-radius: var(--sa-radius-sm);
        padding: 4px;
        border: 0.5px solid var(--sa-border);
        margin-bottom: 1.25rem;
        backdrop-filter: blur(8px);
    }
    [data-testid="stTabs"] [data-baseweb="tab"] {
        border-radius: 7px;
        color: var(--sa-text-muted);
        font-size: 0.8rem;
        padding: 0.45rem 1rem;
        transition: all var(--sa-transition);
        position: relative;
    }
    [data-testid="stTabs"] [data-baseweb="tab"]:hover:not([aria-selected="true"]) {
        color: var(--sa-text) !important;
        background: rgba(255,255,255,0.04) !important;
    }
    [data-testid="stTabs"] [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(56,189,248,0.20), rgba(129,140,248,0.16)) !important;
        color: #e0f2fe !important;
        border: 0.5px solid var(--sa-accent-ring) !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 12px rgba(56,189,248,0.12), inset 0 1px 0 rgba(255,255,255,0.08) !important;
    }

    /* ── Expanders ── */
    div[data-testid="stExpander"] {
        background: rgba(10,16,28,0.6);
        border: 0.5px solid var(--sa-border) !important;
        border-radius: var(--sa-radius-sm);
        overflow: hidden;
        margin-bottom: 0.75rem;
        transition: border-color var(--sa-transition), box-shadow var(--sa-transition);
    }
    div[data-testid="stExpander"]:hover {
        border-color: rgba(56,189,248,0.22) !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25);
    }
    div[data-testid="stExpander"] summary {
        font-size: 0.85rem;
        font-weight: 500;
        color: var(--sa-text) !important;
        padding: 0.7rem 1rem;
        transition: background var(--sa-transition);
    }
    div[data-testid="stExpander"] summary:hover {
        background: rgba(56,189,248,0.04);
    }

    /* ── Metric cards ── */
    [data-testid="stMetric"] {
        background: rgba(12,18,34,0.7);
        border: 0.5px solid var(--sa-border);
        border-radius: var(--sa-radius-sm);
        padding: 0.9rem 1rem;
        transition: all var(--sa-transition);
        position: relative;
        overflow: hidden;
    }
    [data-testid="stMetric"]::after {
        content: "";
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(56,189,248,0.25), transparent);
        opacity: 0;
        transition: opacity var(--sa-transition);
    }
    [data-testid="stMetric"]:hover {
        border-color: rgba(56,189,248,0.22);
        transform: translateY(-1px);
        box-shadow: 0 6px 24px rgba(0,0,0,0.3);
    }
    [data-testid="stMetric"]:hover::after { opacity: 1; }
    [data-testid="stMetricValue"] {
        color: var(--sa-text) !important;
        font-size: 1.4rem !important;
        font-weight: 700 !important;
        letter-spacing: -0.025em;
        font-family: "Space Mono", monospace;
    }
    [data-testid="stMetricLabel"] {
        color: var(--sa-text-dim) !important;
        font-size: 0.72rem !important;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-weight: 600 !important;
    }
    [data-testid="stMetricDelta"] svg { display: none; }
    [data-testid="stMetricDelta"] [data-testid="stMetricDeltaPositive"] {
        color: var(--sa-up) !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        text-shadow: 0 0 8px rgba(74,222,128,0.4);
    }
    [data-testid="stMetricDelta"] [data-testid="stMetricDeltaNegative"] {
        color: var(--sa-dn) !important;
        font-size: 0.72rem !important;
        font-weight: 600 !important;
        text-shadow: 0 0 8px rgba(248,113,113,0.4);
    }

    /* ── Dataframe ── */
    [data-testid="stDataFrame"] {
        border: 0.5px solid var(--sa-border) !important;
        border-radius: var(--sa-radius-sm) !important;
        overflow: hidden;
        transition: box-shadow var(--sa-transition);
    }
    [data-testid="stDataFrame"]:hover {
        box-shadow: 0 4px 24px rgba(0,0,0,0.3);
    }
    [data-testid="stDataFrame"] th {
        background: rgba(255,255,255,0.04) !important;
        color: var(--sa-text-dim) !important;
        font-size: 0.7rem !important;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        font-weight: 700 !important;
    }
    [data-testid="stDataFrame"] td {
        color: var(--sa-text) !important;
        font-size: 0.8rem !important;
        border-top: 0.5px solid var(--sa-border-soft) !important;
        font-family: "Space Mono", monospace;
        transition: background var(--sa-transition);
    }
    [data-testid="stDataFrame"] tr:hover td {
        background: rgba(56,189,248,0.04) !important;
    }

    /* ── Chat / AI messages ── */
    div[data-testid="stChatMessage"] {
        border-radius: var(--sa-radius-sm);
        border: 0.5px solid var(--sa-border);
        background: rgba(10, 18, 32, 0.55);
        padding: 0.9rem 1rem;
        margin-bottom: 0.5rem;
        transition: all var(--sa-transition);
        animation: saFadeUp 0.35s ease-out forwards;
    }
    div[data-testid="stChatMessage"]:hover {
        border-color: rgba(148,163,184,0.2);
        box-shadow: 0 4px 16px rgba(0,0,0,0.2);
    }
    div[data-testid="stChatMessage"][data-testid*="assistant"] {
        border-left: 2px solid var(--sa-ai);
        background: rgba(167, 139, 250, 0.04);
        box-shadow: -4px 0 16px rgba(167,139,250,0.06);
    }
    [data-testid="stChatInputContainer"] {
        border: 0.5px solid var(--sa-border) !important;
        border-radius: var(--sa-radius-sm) !important;
        background: rgba(10, 20, 36, 0.8) !important;
        backdrop-filter: blur(8px) !important;
        transition: border-color var(--sa-transition), box-shadow var(--sa-transition) !important;
    }
    [data-testid="stChatInputContainer"]:focus-within {
        border-color: rgba(56,189,248,0.40) !important;
        box-shadow: 0 0 0 3px rgba(56,189,248,0.08), 0 0 20px rgba(56,189,248,0.10) !important;
    }

    /* ── Alerts ── */
    .stAlert {
        border-radius: 8px !important;
        border: 0.5px solid var(--sa-border) !important;
        font-size: 0.82rem !important;
        animation: saFadeUp 0.4s ease-out forwards;
    }
    div[data-baseweb="notification"][kind="positive"] {
        background: rgba(74, 222, 128, 0.06) !important;
        border-color: rgba(74, 222, 128, 0.25) !important;
        color: #86efac !important;
        box-shadow: 0 0 16px rgba(74,222,128,0.08) !important;
    }
    div[data-baseweb="notification"][kind="warning"] {
        background: rgba(251, 191, 36, 0.06) !important;
        border-color: rgba(251, 191, 36, 0.25) !important;
        color: #fde68a !important;
    }

    /* ── Buttons ── */
    .stButton button {
        background: rgba(56,189,248,0.1) !important;
        border: 0.5px solid var(--sa-accent-ring) !important;
        border-radius: 8px !important;
        color: #93c5fd !important;
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        padding: 0.45rem 1.1rem !important;
        transition: all var(--sa-transition) !important;
        position: relative;
        overflow: hidden;
        letter-spacing: 0.02em;
    }
    .stButton button::before {
        content: "";
        position: absolute;
        top: 50%; left: 50%;
        width: 0; height: 0;
        border-radius: 50%;
        background: rgba(56,189,248,0.15);
        transform: translate(-50%, -50%);
        transition: width 0.4s ease, height 0.4s ease, opacity 0.4s ease;
        opacity: 0;
    }
    .stButton button:hover {
        background: rgba(56,189,248,0.20) !important;
        border-color: rgba(56,189,248,0.60) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 16px rgba(56,189,248,0.18), 0 0 0 1px rgba(56,189,248,0.15) !important;
        color: #bae6fd !important;
    }
    .stButton button:active {
        transform: translateY(0) !important;
        box-shadow: none !important;
    }
    .stButton button:active::before {
        width: 200px; height: 200px;
        opacity: 1;
    }

    /* ── Plotly charts ── */
    [data-testid="stPlotlyChart"] {
        border: 0.5px solid var(--sa-border);
        border-radius: var(--sa-radius-card);
        overflow: hidden;
        background: rgba(6, 12, 24, 0.8);
        transition: box-shadow var(--sa-transition), border-color var(--sa-transition);
    }
    [data-testid="stPlotlyChart"]:hover {
        border-color: rgba(56,189,248,0.20);
        box-shadow: 0 8px 40px rgba(0,0,0,0.4);
    }

    /* ── Bordered main panels ── */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px !important;
        border-color: var(--sa-border) !important;
        background:
            linear-gradient(135deg, rgba(14,22,40,0.45) 0%, rgba(10,16,30,0.35) 100%) !important;
        padding: 1rem 1.2rem !important;
        backdrop-filter: blur(4px) !important;
        transition: border-color var(--sa-transition), box-shadow var(--sa-transition) !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        border-color: rgba(56,189,248,0.18) !important;
    }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 4px; height: 4px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: rgba(56,189,248,0.25);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(56,189,248,0.45);
    }

    /* ── Select boxes ── */
    [data-testid="stSelectbox"] [data-baseweb="select"] > div {
        background: rgba(10,16,28,0.8) !important;
        border: 0.5px solid var(--sa-border) !important;
        border-radius: 8px !important;
        transition: all var(--sa-transition) !important;
    }
    [data-testid="stSelectbox"] [data-baseweb="select"] > div:hover {
        border-color: rgba(56,189,248,0.35) !important;
    }
    </style>
    """


def title_block_html() -> str:
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,700;0,9..40,800&family=Space+Mono:wght@700&display=swap');

    @keyframes saFadeUp {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes saDotPulse {
        0%, 100% { box-shadow: 0 0 0 0 rgba(167,139,250,0.6); }
        50%       { box-shadow: 0 0 0 6px rgba(167,139,250,0); }
    }
    @keyframes saShimmer {
        0%   { background-position: -200% center; }
        100% { background-position:  200% center; }
    }
    @keyframes saBorderGlow {
        0%, 100% { border-color: rgba(56,189,248,0.20); }
        50%       { border-color: rgba(56,189,248,0.45); }
    }
    @keyframes saLineIn {
        from { width: 0; }
        to   { width: 100%; }
    }

    .sa-hero {
        padding: 0.5rem 0 1.25rem;
        margin-bottom: 1.25rem;
        position: relative;
    }
    .sa-hero::after {
        content: "";
        position: absolute;
        bottom: 0; left: 0;
        height: 0.5px;
        width: 0;
        background: linear-gradient(90deg, rgba(56,189,248,0.6), rgba(129,140,248,0.4), transparent);
        animation: saLineIn 0.8s ease-out 0.3s forwards;
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
        padding: 7px 16px;
        border-radius: 999px;
        background: rgba(129, 140, 248, 0.10);
        border: 0.5px solid rgba(167, 139, 250, 0.30);
        font-size: 0.76rem;
        font-weight: 600;
        color: #ddd6fe;
        letter-spacing: 0.03em;
        animation: saBorderGlow 3s ease-in-out infinite, saFadeUp 0.6s ease-out 0.3s both;
        backdrop-filter: blur(6px);
    }
    .sa-hero-ai-pill .sa-dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #a78bfa;
        box-shadow: 0 0 10px rgba(167, 139, 250, 0.7);
        animation: saDotPulse 2s ease-in-out infinite;
    }
    .sa-eyebrow {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--sa-accent, #38bdf8);
        margin-bottom: 0.35rem;
        display: flex;
        align-items: center;
        gap: 8px;
        animation: saFadeUp 0.5s ease-out both;
    }
    .sa-eyebrow::before {
        content: "";
        display: block;
        width: 18px;
        height: 1px;
        background: currentColor;
        opacity: 0.6;
    }
    .sa-title {
        font-size: clamp(1.55rem, 3.5vw, 2.1rem);
        font-weight: 800;
        letter-spacing: -0.04em;
        color: #f0f4f8;
        margin: 0 0 0.3rem;
        animation: saFadeUp 0.55s ease-out 0.08s both;
        line-height: 1.1;
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 0.4rem;
    }
    .sa-sub {
        font-size: 0.82rem;
        color: rgba(240,244,248,0.40);
        margin: 0;
        animation: saFadeUp 0.55s ease-out 0.16s both;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .sa-sub::before {
        content: "";
        display: block;
        width: 4px;
        height: 4px;
        border-radius: 50%;
        background: rgba(56,189,248,0.5);
    }
    .sa-badge {
        display: inline-flex;
        align-items: center;
        gap: 5px;
        background: rgba(167,139,250,0.10);
        border: 0.5px solid rgba(167,139,250,0.28);
        border-radius: 6px;
        padding: 3px 10px;
        font-size: 0.65rem;
        font-weight: 700;
        color: #c4b5fd;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }
    .sa-badge::before {
        content: "";
        display: inline-block;
        width: 5px;
        height: 5px;
        background: #a78bfa;
        border-radius: 50%;
        box-shadow: 0 0 6px rgba(167,139,250,0.6);
        animation: saDotPulse 2.5s ease-in-out infinite;
    }
    </style>
    <div class="sa-hero">
      <div class="sa-hero-flex">
        <div>
          <div class="sa-eyebrow">AI-powered Analytics</div>
          <h1 class="sa-title">
            AI Stock Analyst
            <span class="sa-badge">Gen AI</span>
          </h1>
          <p class="sa-sub">Charts · news sentiment · AI insights</p>
        </div>
        <div class="sa-hero-ai-pill">
          <span class="sa-dot"></span> AI analyst active
        </div>
      </div>
    </div>
    """


def chat_css() -> str:
    return """
    <style>
    @keyframes saFadeUp {
        from { opacity: 0; transform: translateY(8px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes saTyping {
        0%, 60%, 100% { opacity: 0.25; transform: translateY(0); }
        30%            { opacity: 1;    transform: translateY(-3px); }
    }
    @keyframes saDotPulse {
        0%, 100% { box-shadow: 0 0 0 0   rgba(74,222,128,0.6); }
        50%       { box-shadow: 0 0 0 5px rgba(74,222,128,0); }
    }
    @keyframes saMsgIn {
        from { opacity: 0; transform: translateX(-6px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes saMsgInRight {
        from { opacity: 0; transform: translateX(6px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    .sa-chat-card {
        background:
            linear-gradient(135deg, rgba(10,16,30,0.75) 0%, rgba(8,13,26,0.70) 100%);
        border: 0.5px solid rgba(148, 163, 184, 0.12);
        border-radius: 18px;
        padding: 0;
        margin-bottom: 1rem;
        overflow: hidden;
        backdrop-filter: blur(12px);
        box-shadow: 0 16px 48px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.04);
        transition: border-color 0.22s ease, box-shadow 0.22s ease;
    }
    .sa-chat-card:hover {
        border-color: rgba(148,163,184,0.20);
        box-shadow: 0 20px 60px rgba(0,0,0,0.40), inset 0 1px 0 rgba(255,255,255,0.05);
    }

    .sa-chat-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.95rem 1.15rem;
        border-bottom: 0.5px solid rgba(148, 163, 184, 0.08);
        background: rgba(12, 20, 36, 0.60);
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
        border: 0.5px solid rgba(167,139,250,0.40);
        display: flex;
        align-items: center;
        justify-content: center;
        color: #c4b5fd;
        font-weight: 700;
        font-size: 0.78rem;
        letter-spacing: 0.04em;
        box-shadow: 0 0 14px rgba(167,139,250,0.15);
        transition: box-shadow 0.22s ease;
    }
    .sa-chat-avatar:hover {
        box-shadow: 0 0 20px rgba(167,139,250,0.30);
    }
    .sa-chat-avatar.user {
        background: linear-gradient(135deg, rgba(56,189,248,0.18), rgba(59,130,246,0.18));
        border-color: rgba(56,189,248,0.40);
        color: #7dd3fc;
        box-shadow: 0 0 14px rgba(56,189,248,0.15);
    }
    .sa-chat-title {
        font-size: 1rem;
        font-weight: 700;
        color: #f1f5f9;
        line-height: 1.15;
        margin: 0;
    }
    .sa-chat-sub {
        font-size: 0.76rem;
        color: rgba(203,213,225,0.55);
        margin: 2px 0 0;
    }
    .sa-chat-live {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 0.74rem;
        font-weight: 600;
        color: #86efac;
        padding: 4px 10px;
        border-radius: 999px;
        background: rgba(74,222,128,0.08);
        border: 0.5px solid rgba(74,222,128,0.22);
    }
    .sa-chat-live .dot {
        width: 7px;
        height: 7px;
        border-radius: 50%;
        background: #4ade80;
        box-shadow: 0 0 8px rgba(74,222,128,0.7);
        animation: saDotPulse 2s ease-in-out infinite;
    }
    .sa-chat-focus {
        display: flex;
        align-items: center;
        gap: 0.65rem;
        padding: 0.65rem 1.15rem;
        border-bottom: 0.5px solid rgba(148, 163, 184, 0.07);
        font-size: 0.78rem;
        color: rgba(203,213,225,0.65);
        background: rgba(8,14,26,0.30);
    }
    .sa-chat-body {
        padding: 1rem 1.15rem;
        min-height: 200px;
    }
    .sa-msg-row {
        display: flex;
        gap: 12px;
        margin: 0.6rem 0 1rem;
        align-items: flex-start;
        animation: saMsgIn 0.3s ease-out forwards;
    }
    .sa-msg-row.user {
        flex-direction: row-reverse;
        animation-name: saMsgInRight;
    }
    .sa-msg-bubble {
        max-width: 70%;
        padding: 0.8rem 1rem;
        border-radius: 14px;
        font-size: 0.88rem;
        line-height: 1.55;
        color: #e2e8f0;
        background: rgba(16, 26, 44, 0.90);
        border: 0.5px solid rgba(148, 163, 184, 0.12);
        transition: border-color 0.22s ease;
    }
    .sa-msg-bubble:hover {
        border-color: rgba(148,163,184,0.22);
    }
    .sa-msg-row.user .sa-msg-bubble {
        background: rgba(56, 189, 248, 0.10);
        border-color: rgba(56, 189, 248, 0.28);
        color: #e0f2fe;
        box-shadow: 0 0 16px rgba(56,189,248,0.06);
    }
    .sa-msg-meta {
        font-size: 0.67rem;
        color: rgba(148,163,184,0.45);
        margin-top: 0.3rem;
    }
    .sa-msg-stack {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 0;
        max-width: 78%;
    }
    .sa-msg-row.user .sa-msg-stack { align-items: flex-end; }

    .sa-rag-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.7rem;
        font-weight: 600;
        color: #c4b5fd;
        background: rgba(167,139,250,0.10);
        border: 0.5px solid rgba(167,139,250,0.28);
        border-radius: 999px;
        padding: 3px 10px;
        margin-bottom: 6px;
        transition: background 0.22s ease;
    }
    .sa-rag-badge:hover { background: rgba(167,139,250,0.16); }
    .sa-rag-badge .dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #a78bfa;
        box-shadow: 0 0 6px rgba(167,139,250,0.5);
    }

    .sa-src-row {
        display: flex;
        flex-wrap: wrap;
        gap: 6px;
        margin-top: 8px;
    }
    .sa-src-chip {
        font-size: 0.69rem;
        color: rgba(203,213,225,0.65);
        background: rgba(255,255,255,0.03);
        border: 0.5px solid rgba(148,163,184,0.16);
        border-radius: 7px;
        padding: 3px 9px;
        display: inline-flex;
        align-items: center;
        gap: 5px;
        transition: all 0.22s ease;
        cursor: default;
    }
    .sa-src-chip:hover {
        background: rgba(56,189,248,0.07);
        border-color: rgba(56,189,248,0.28);
        color: #93c5fd;
    }
    .sa-src-chip::before {
        content: "ⓘ";
        opacity: 0.5;
        font-size: 0.68rem;
    }

    .sa-typing {
        display: inline-flex;
        gap: 4px;
        padding: 9px 14px;
        background: rgba(16, 26, 44, 0.90);
        border: 0.5px solid rgba(148, 163, 184, 0.12);
        border-radius: 14px;
    }
    .sa-typing span {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: rgba(56,189,248,0.7);
        animation: saTyping 1.3s infinite;
    }
    .sa-typing span:nth-child(2) { animation-delay: 0.18s; }
    .sa-typing span:nth-child(3) { animation-delay: 0.36s; }

    .sa-chat-foot {
        font-size: 0.71rem;
        color: rgba(148,163,184,0.50);
        text-align: center;
        margin-top: 0.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
    }
    .sa-chat-foot::before,
    .sa-chat-foot::after {
        content: "";
        display: block;
        flex: 1;
        height: 0.5px;
        background: rgba(148,163,184,0.10);
        max-width: 60px;
    }

    .sa-input-tag {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 0.72rem;
        font-weight: 700;
        color: #93c5fd;
        background: rgba(56,189,248,0.10);
        border: 0.5px solid rgba(56,189,248,0.28);
        border-radius: 8px;
        padding: 7px 10px;
        height: 38px;
        letter-spacing: 0.02em;
        transition: all 0.22s ease;
    }
    .sa-input-tag:hover {
        background: rgba(56,189,248,0.18);
        border-color: rgba(56,189,248,0.50);
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