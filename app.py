import streamlit as st
import pandas as pd
from datetime import date
from data import get_stock_data, TICKERS
from charts import plot_prices, plot_performance, plot_volume

st.set_page_config(
    page_title="Dashboard de Ações 2025",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Dashboard de Ações Brasileiras — 2025")
st.caption("Petrobras (PETR4) · Vale (VALE3) · Itaú (ITUB4)")

# --- Sidebar ---
with st.sidebar:
    st.header("Filtros")

    selected = st.multiselect(
        "Ações",
        options=list(TICKERS.keys()),
        default=list(TICKERS.keys()),
    )

    min_date = date(2025, 1, 1)
    max_date = min(date.today(), date(2025, 12, 31))

    start_date, end_date = st.date_input(
        "Período",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

if not selected:
    st.warning("Selecione ao menos uma ação na barra lateral.")
    st.stop()

if start_date >= end_date:
    st.error("A data inicial deve ser anterior à data final.")
    st.stop()

# --- Busca de dados ---
with st.spinner("Buscando dados..."):
    data = get_stock_data(selected, str(start_date), str(end_date))

if not data:
    st.error("Não foi possível obter dados para o período selecionado.")
    st.stop()

# --- KPIs ---
st.subheader("Resumo do Período")
cols = st.columns(len(data))
for col, (name, df) in zip(cols, data.items()):
    retorno = df["Cumulative Return"].iloc[-1] * 100
    preco_atual = df["Close"].iloc[-1]
    preco_min = df["Close"].min()
    preco_max = df["Close"].max()
    volatilidade = df["Daily Return"].std() * 100

    with col:
        st.metric(
            label=name,
            value=f"R$ {preco_atual:.2f}",
            delta=f"{retorno:+.2f}% no período",
        )
        st.caption(f"Mín: R$ {preco_min:.2f} · Máx: R$ {preco_max:.2f}")
        st.caption(f"Volatilidade diária: {volatilidade:.2f}%")

st.divider()

# --- Gráficos ---
st.plotly_chart(plot_prices(data), use_container_width=True)
st.plotly_chart(plot_performance(data), use_container_width=True)
st.plotly_chart(plot_volume(data), use_container_width=True)
