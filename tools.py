import requests
import yfinance as yf
import os
import pycountry

EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")

# ------------------------------
# Find currency of country
# ------------------------------
def get_currency(country_name):
    try:
        country = pycountry.countries.search_fuzzy(country_name)[0]
        code = country.alpha_2

        url = f"https://restcountries.com/v3.1/alpha/{code}"
        res = requests.get(url).json()[0]

        currency = list(res["currencies"].keys())[0]
        return currency
    except:
        return "Not found"


# ------------------------------
# Exchange rates
# ------------------------------
def get_exchange_rates(currency):
    try:
        url = f"https://open.er-api.com/v6/latest/{currency}"
        res = requests.get(url).json()

        if res.get("result") != "success":
            return {"error": "Exchange API failed", "details": res}

        rates = res["rates"]

        return {
            "USD": rates.get("USD"),
            "INR": rates.get("INR"),
            "GBP": rates.get("GBP"),
            "EUR": rates.get("EUR")
        }

    except Exception as e:
        return {"error": str(e)}

# ------------------------------
# Major stock indices mapping
# ------------------------------
index_map = {
    "india": {
        "Nifty 50": "^NSEI",
        "Sensex": "^BSESN",
        "hq": "National Stock Exchange Mumbai"
    },
    "usa": {
        "S&P 500": "^GSPC",
        "NASDAQ": "^IXIC",
        "Dow Jones": "^DJI",
        "hq": "New York Stock Exchange"
    },
    "japan": {
        "Nikkei 225": "^N225",
        "hq": "Tokyo Stock Exchange"
    },
    "uk": {
        "FTSE 100": "^FTSE",
        "hq": "London Stock Exchange"
    },
    "china": {
        "SSE Composite": "000001.SS",
        "hq": "Shanghai Stock Exchange"
    },
    "south korea": {
        "KOSPI": "^KS11",
        "hq": "Korea Exchange Seoul"
    }
}


# ------------------------------
# Get stock data
# ------------------------------
def get_stock_data(country):
    country = country.lower()

    if country not in index_map:
        return {"message": "Stock data not mapped yet"}

    data = {}
    indices = index_map[country]

    for name, ticker in indices.items():
        if name == "hq":
            continue
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            price = round(hist["Close"].iloc[-1], 2)
            data[name] = price
        except:
            data[name] = "NA"

    data["hq"] = indices["hq"]
    return data


# ------------------------------
# Google maps link
# ------------------------------
def get_map_link(place):
    return f"https://www.google.com/maps/search/?api=1&query={place.replace(' ','+')}"


# ------------------------------
# MASTER FUNCTION
# ------------------------------
def full_finance_data(country):
    import streamlit as st

    currency = get_currency(country)
    rates = get_exchange_rates(currency)
    stocks = get_stock_data(country)

    # map
    if isinstance(stocks, dict) and "hq" in stocks:
        map_link = get_map_link(stocks["hq"])
    else:
        map_link = "NA"

    # store map in session
    st.session_state["Google Maps Link"] = map_link

    return {
        "country": country,
        "currency": currency,
        "exchange_rates": rates,
        "stock_data": stocks,
        "map": map_link
    }