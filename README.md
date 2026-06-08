# FinSight AI — Stock Sentiment Analyzer & RAG-Powered Financial Assistant

## Overview

FinSight AI is an end-to-end financial intelligence platform that combines real-time market data, financial news sentiment analysis, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs) to help investors make data-driven decisions.

The platform automatically collects stock market data, analyzes financial news using FinBERT, generates AI-powered analyst reports, and enables users to interact with their investment data through a conversational AI assistant.

---

## Key Features

### Real-Time Market Analytics

* Live stock market data powered by Yahoo Finance
* Interactive candlestick and volume charts
* Technical indicators including 20-Day and 50-Day Moving Averages
* Multi-stock comparison dashboard with normalized performance tracking

### AI-Powered Sentiment Analysis

* Financial news aggregation using Google News RSS feeds
* Sentiment classification using FinBERT (Financial BERT)
* Classification into:

  * Bullish
  * Bearish
  * Neutral
* Automatic sentiment trend monitoring for selected stocks

### Retrieval-Augmented Generation (RAG)

* Automatic indexing of:

  * Financial news articles
  * Stock summaries
  * AI-generated analyst reports
* Vector storage using ChromaDB
* Semantic search for context-aware information retrieval

### Intelligent Financial Assistant

* Powered by Groq LLM APIs
* Context-aware financial question answering
* Source-grounded responses using retrieved financial data
* Example queries:

  * "Why did NVIDIA stock decline today?"
  * "What risks are associated with Tesla?"
  * "Summarize recent news affecting Apple stock."

### Automated Analyst Reports

* AI-generated stock analysis reports
* Market trend evaluation
* Sentiment-driven insights
* Risk assessment and investment observations

### Modern User Experience

* Premium dark-themed dashboard
* Responsive Streamlit interface
* Interactive Plotly visualizations
* Custom glassmorphism-inspired UI design

---

## System Architecture

Data Sources
↓
Yahoo Finance + Google News RSS
↓
Data Processing Layer
(Pandas)
↓
FinBERT Sentiment Analysis
↓
ChromaDB Vector Store
↓
Groq LLM + RAG Pipeline
↓
Interactive Streamlit Dashboard

---

## Technology Stack

| Category                 | Technologies                       |
| ------------------------ | ---------------------------------- |
| Frontend                 | Streamlit, HTML, CSS               |
| Visualization            | Plotly                             |
| Data Processing          | Pandas                             |
| Market Data              | yFinance                           |
| NLP & Sentiment Analysis | FinBERT, Hugging Face Transformers |
| Deep Learning Backend    | PyTorch                            |
| Vector Database          | ChromaDB                           |
| LLM Integration          | Groq API                           |
| Retrieval System         | RAG Architecture                   |
| Language                 | Python                             |

---

## Technical Highlights

* Built a complete Retrieval-Augmented Generation (RAG) pipeline for financial intelligence.
* Integrated FinBERT for domain-specific financial sentiment analysis.
* Developed automated vector indexing workflows for financial news and reports.
* Implemented semantic search using ChromaDB embeddings.
* Generated AI-powered analyst reports using Groq LLMs.
* Designed scalable modular architecture for future AI and financial analytics integrations.

---

## Impact

FinSight AI transforms raw financial data into actionable intelligence by combining machine learning, natural language processing, vector search, and generative AI. The platform demonstrates practical applications of AI in financial analytics, investment research, and conversational decision support systems.

---

## Future Enhancements

* Portfolio risk analysis
* Multi-agent financial research workflows
* Earnings call transcript analysis
* Real-time market alerts
* Advanced forecasting models
* Cloud deployment with CI/CD pipelines

---

## Author

Nirbhay Singh 

Artificial Intelligence & Machine Learning Engineer

Focused on building production-ready AI systems, RAG applications, NLP solutions, and intelligent data-driven products.
