from datetime import date

PAGE_TITLE = "FinSight AI"

# Groq model id (free tier; Llama 3 family).
GROQ_MODEL = "llama-3.3-70b-versatile"

DEFAULT_START_DATE = date(2023, 1, 1)

DEFAULT_TICKER_SELECTION = [
    "AAPL – Apple Inc.",
    "MSFT – Microsoft Corporation",
    "NVDA – NVIDIA Corporation",
]

TICKER_DICT: dict[str, str] = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc.",
    "AMZN": "Amazon.com Inc.",
    "TSLA": "Tesla Inc.",
    "META": "Meta Platforms Inc.",
    "NFLX": "Netflix Inc.",
    "NVDA": "NVIDIA Corporation",
    "AMD": "Advanced Micro Devices",
    "INTC": "Intel Corporation",
    "BABA": "Alibaba Group",
    "ADBE": "Adobe Inc.",
    "ORCL": "Oracle Corporation",
    "CRM": "Salesforce.com Inc.",
    "PYPL": "PayPal Holdings",
    "UBER": "Uber Technologies",
    "JPM": "JPMorgan Chase & Co.",
    "BAC": "Bank of America",
    "WMT": "Walmart Inc.",
    "T": "AT&T Inc.",
    "VZ": "Verizon Communications",
    "DIS": "The Walt Disney Company",
    "PEP": "PepsiCo Inc.",
    "KO": "Coca-Cola Company",
    "NKE": "Nike Inc.",
    "COST": "Costco Wholesale",
    "MCD": "McDonald’s Corporation",
    "IBM": "IBM",
    "GE": "General Electric",
    "SBUX": "Starbucks",
    "PFE": "Pfizer",
    "MRNA": "Moderna",
    "XOM": "Exxon Mobil",
    "CVX": "Chevron",
}

CHART_LAYOUT = {
    "paper_bgcolor": "rgba(8, 15, 28, 0.96)",
    "plot_bgcolor": "rgba(8, 15, 28, 0.96)",
    "font": {"color": "#e8eef6", "family": "Segoe UI, system-ui, sans-serif"},
}
