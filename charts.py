import plotly.graph_objects as go
from data import COLORS


def plot_prices(data: dict) -> go.Figure:
    fig = go.Figure()
    for name, df in data.items():
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df["Close"].round(2),
            name=name,
            line=dict(color=COLORS[name], width=2),
            hovertemplate=(
                "<b>%{fullData.name}</b><br>"
                "Data: %{x|%d/%m/%Y}<br>"
                "Preço: R$ %{y:.2f}<extra></extra>"
            ),
        ))
    fig.update_layout(
        title="Cotação — Preço de Fechamento (R$)",
        xaxis_title="Data",
        yaxis_title="Preço (R$)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified",
        template="plotly_white",
    )
    return fig


def plot_performance(data: dict) -> go.Figure:
    fig = go.Figure()
    for name, df in data.items():
        fig.add_trace(go.Scatter(
            x=df.index,
            y=(df["Cumulative Return"] * 100).round(2),
            name=name,
            line=dict(color=COLORS[name], width=2),
            hovertemplate=(
                "<b>%{fullData.name}</b><br>"
                "Data: %{x|%d/%m/%Y}<br>"
                "Retorno: %{y:.2f}%<extra></extra>"
            ),
        ))
    fig.add_hline(y=0, line_dash="dash", line_color="gray", opacity=0.5)
    fig.update_layout(
        title="Performance Acumulada no Período (%)",
        xaxis_title="Data",
        yaxis_title="Retorno Acumulado (%)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified",
        template="plotly_white",
    )
    return fig


def plot_volume(data: dict) -> go.Figure:
    fig = go.Figure()
    for name, df in data.items():
        fig.add_trace(go.Bar(
            x=df.index,
            y=df["Volume"],
            name=name,
            marker_color=COLORS[name],
            opacity=0.7,
            hovertemplate=(
                "<b>%{fullData.name}</b><br>"
                "Data: %{x|%d/%m/%Y}<br>"
                "Volume: %{y:,.0f}<extra></extra>"
            ),
        ))
    fig.update_layout(
        title="Volume Negociado Diário",
        xaxis_title="Data",
        yaxis_title="Volume (ações)",
        barmode="group",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        hovermode="x unified",
        template="plotly_white",
    )
    return fig
