# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## Architecture

A Streamlit dashboard for Brazilian stock market data (Petrobras/PETR4, Vale/VALE3, Itaú/ITUB4) with three modules:

- **data.py** — fetches OHLCV data via yfinance, computes daily/cumulative returns, caches results for 1 hour. Defines the `TICKERS` dict (name → Yahoo Finance symbol) and `COLORS` dict used globally.
- **charts.py** — three Plotly chart functions: `plot_prices`, `plot_performance`, `plot_cumulative_returns`, `plot_volume`.
- **app.py** — Streamlit entry point; sidebar filters (stock multiselect + date range), KPI cards per stock, then the three charts.

Data flows one way: `app.py` calls `get_stock_data()` from `data.py`, passes the resulting dict of DataFrames to chart functions in `charts.py`, and renders everything with `st.plotly_chart`.

## GitHub Repository

Repositório: [https://github.com/altics-solutions/ClaudeCode_Teste](https://github.com/altics-solutions/ClaudeCode_Teste)

### Sincronização automática

A cada arquivo editado ou criado pelo Claude Code, um hook `PostToolUse` (configurado em `.claude/settings.json`) executa automaticamente:

```bash
git add -A
git commit -m "Auto-update: sync changes"
git push
```

Isso mantém o repositório GitHub sempre atualizado com as últimas alterações do projeto.

### GitHub CLI

O GitHub CLI oficial está em `C:\Program Files\GitHub CLI\gh.exe` (o pacote npm `gh` tem prioridade no PATH, mas não é o CLI oficial). Para usar o CLI oficial diretamente:

```bash
"/c/Program Files/GitHub CLI/gh.exe" <comando>
```
