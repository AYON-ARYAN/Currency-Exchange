# 🌍 Global Finance Intelligence Dashboard

A smart, agent-powered financial dashboard that provides real-time currency exchange rates, stock market indices, and geographical intelligence for major global economies.

## 🚀 Features

- **Financial Intelligence Agent**: Uses Large Language Models (LLM) to synthesize and format complex financial data.
- **Real-time Exchange Rates**: Fetches live currency data from reliable Open Exchange APIs.
- **Stock Market Tracking**: Monitors major indices like Nifty 50, S&P 500, Nikkei 225, FTSE 100, etc., via Yahoo Finance.
- **Currency Converter**: A built-in tool for quick currency conversions across major global currencies.
- **Geographical Insights**: Integrated Google Maps view of representative stock exchange headquarters.
- **Interactive UI**: Built with Streamlit for a fast, responsive, and user-friendly experience.

## 🛠 Tech Stack

- **Frontend/App Framework**: [Streamlit](https://streamlit.io/)
- **AI/LLM**: [Groq](https://groq.com/) (using Llama 3.3 70B)
- **Financial Data**: `yfinance` (Yahoo Finance), `Open Exchange Rates API`
- **Country Intelligence**: `pycountry`, `restcountries.com`
- **Environment Management**: `python-dotenv`

## 📋 Prerequisites

- Python 3.8+
- [Groq API Key](https://console.groq.com/keys)
- [Exchange Rates API Key](https://open.er-api.com/) (Open access)

## ⚙️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/AYON-ARYAN/Currency-Exchange.git
   cd Currency-Exchange
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install streamlit groq yfinance requests pycountry python-dotenv
   ```

## 🔑 Configuration

Create a `.env` file in the root directory and add your API keys:

```env
GROQ_API_KEY="your_groq_api_key_here"
EXCHANGE_API_KEY="your_exchange_api_key_here"
```

## 🎮 Usage

Launch the dashboard by running:

```bash
streamlit run app.py
```

Once the app is running, you can:

1. Select a country from the dropdown to get a comprehensive financial overview.
2. Use the **Currency Converter** section to perform real-time conversions.
3. View the location of the major stock exchange in the integrated map.

## 📂 Project Structure

- `app.py`: The main Streamlit interface and application logic.
- `agent.py`: Orchestrates the AI agent and formats the financial insights.
- `tools.py`: Contains the engine for fetching stock data, exchange rates, and country details.
- `.env`: (Ignored by git) Stores sensitive credentials.

## 🧠 How it Works

The application follows an **agentic pattern**:

1. **Tool Execution**: When a country is selected, `tools.py` gathers data from multiple sources (Exchange API, YFinance, RestCountries).
2. **Context Synthesis**: This raw data is passed to `agent.py`, where a Groq-powered LLM (Llama 3.3) processes the data.
3. **Formatted UI**: The LLM returns a clean, human-readable summary which is then rendered in the Streamlit dashboard alongside interactive map components.

---

Developed by [AYON-ARYAN](https://github.com/AYON-ARYAN)
