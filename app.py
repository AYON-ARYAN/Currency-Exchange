import streamlit as st
from agent import run_agent
from tools import get_exchange_rates
import requests
import os
st.set_page_config(page_title="Global Finance Dashboard", layout="wide")

st.title("🌍 Global Finance Intelligence Dashboard")

# -------- COUNTRY DROPDOWN --------
countries = [
    "India", "USA", "Japan", "UK", "China",
    "South Korea", "Germany", "France", "Canada", "Australia"
]

col1, col2 = st.columns([2,1])

with col1:
    country = st.selectbox("Select Country", countries)

    if st.button("Get Financial Data"):
        with st.spinner("Fetching live financial data..."):
            result = run_agent(country)

        st.subheader("📊 Financial Overview")
        st.write(result)

with col2:
    st.subheader("📍 Stock Exchange Location")
    # map will show after result
    if "Google Maps Link" in st.session_state:
        st.components.v1.iframe(st.session_state["Google Maps Link"], height=300)

# -------- CURRENCY CONVERTER --------
st.divider()
st.subheader("💱 Currency Converter")

c1, c2, c3 = st.columns(3)

with c1:
    amount = st.number_input("Amount", value=1.0)

with c2:
    from_currency = st.selectbox(
        "From Currency",
        ["USD","INR","EUR","GBP","JPY","CNY"]
    )

with c3:
    to_currency = st.selectbox(
        "To Currency",
        ["INR","USD","EUR","GBP","JPY","CNY"]
    )

if st.button("Convert Currency"):

    try:
        rates = get_exchange_rates(from_currency)

        if "error" in rates:
            st.error("Currency API failed")
        else:
            rate = rates.get(to_currency)

            if rate:
                converted = amount * rate
                st.success(f"{amount} {from_currency} = {round(converted,2)} {to_currency}")
            else:
                st.warning("Conversion not available")

    except Exception as e:
        st.error(str(e))