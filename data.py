import yfinance as yf
import pandas as pd
import streamlit as st

TICKERS = {
    "Petrobras (PETR4)": "PETR4.SA",
    "Vale (VALE3)": "VALE3.SA",
    "Itaú (ITUB4)": "ITUB4.SA",
}

COLORS = {
    "Petrobras (PETR4)": "#0066CC",
    "Vale (VALE3)": "#009933",
    "Itaú (ITUB4)": "#FF6600",
}


@st.cache_data(ttl=3600)
def get_stock_data(selected_names: list[str], start: str, end: str) -> dict[str, pd.DataFrame]:
    data = {}
    tickers_to_fetch = [TICKERS[name] for name in selected_names]
    raw = yf.download(tickers_to_fetch, start=start, end=end, auto_adjust=True, progress=False)

    for name in selected_names:
        ticker = TICKERS[name]
        if len(selected_names) == 1:
            df = raw[["Close", "Volume"]].copy()
        else:
            df = raw[["Close", "Volume"]].xs(ticker, axis=1, level=1).copy()
        df.index = pd.to_datetime(df.index)
        df = df.dropna()
        df["Daily Return"] = df["Close"].pct_change()
        df["Cumulative Return"] = (1 + df["Daily Return"]).cumprod() - 1
        data[name] = df

    return data
