import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Análisis Estratégico de Inditex", page_icon="📊", layout="wide")

# ---------- Paleta ----------
INK = "#1F2A37"
ACCENT = "#B5543C"   # terracota
SOFT = "#D9A38F"
MUTED = "#8A94A6"
GRID = "rgba(138,148,166,0.18)"

st.markdown(
    f"""
    <style>
    .block-container {{max-width: 1100px; padding-top: 2.5rem;}}
    h1, h2, h3 {{color: {INK};}}
    .kicker {{color:{MUTED}; font-size:0.85rem; letter-spacing:0.08em; text-transform:uppercase;}}
    .callout {{border-left:4px solid {ACCENT}; padding:0.8rem 1.1rem; background:rgba(181,84,60,0.06);
               border-radius:4px; margin:1rem 0;}}
    .hyp {{border-left:4px solid {MUTED}; padding:0.8rem 1.1rem; background:rgba(138,148,166,0.08);
           border-radius:4px; margin:1rem 0;}}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Datos ----------
# Fuente: reportes anuales de Inditex (confirmar y citar cada cifra).
df = pd.DataFrame({
    "Año":             [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "Ventas_B_EUR":    [25.3, 26.1, 28.286, 20.402, 27.716, 32.569, 35.947, 38.632, 39.864],
    "Tiendas":         [7475, 7490, 7469, 6829, 6477, 5815, 5692, 5563, 5460],
    "Online_B_EUR":    [2.53, 3.13, 3.9, 6.612, 7.5, 7.806, 9.064, 10.163, 10.656],
    "EBITDA_B_EUR":    [np.nan, np.nan, 7.598, 4.552, 7.183, 8.649, 9.85, 10.728, 11.267],
    "Beneficio_B_EUR": [np.nan, np.nan, 3.639, 1.106, 3.243, 4.13, 5.381, 5.866, 6.22],
})
df["Online_%"] = df["Online_B_EUR"] / df["Ventas_B_EUR"] * 100
df["Fisico_B_EUR"] = df["Ventas_B_EUR"] - df["Online_B_EUR"]
df["Ventas_por_tienda_M"] = df["Ventas_B_EUR"] / df["Tiendas"] * 1000
df["Fisico_por_tienda_M"] = df["Fisico_B_EUR"] / df["Tiendas"] * 1000
df["Margen_EBITDA_%"] = df["EBITDA_B_EUR"] / df["Ventas_B_EUR"] * 100

r19 = df.loc[df["Año"] == 2019].iloc[0]
r25 = df.loc[df["Año"] == 2025].iloc[0]
pct = lambda a, b: (b / a - 1) * 100


def base_layout(fig, title, ytitle):
    fig.update_layout(
        title=dict(text=title, font=dict(size=17, color=INK)),
        template="simple_white",
        height=380,
        margin=dict(l=10, r=10, t=60, b=10),
        yaxis=dict(title=ytitle, gridcolor=GRID, showgrid=True),
        xaxis=dict(dtick=1),
        legend=dict(orientation="h", y=1.02, x=1, xanchor="right", yanchor="bottom"),
        hovermode="x unified",
    )
    return fig


def mark_2020(fig):
    fig.add_vrect(x0=2019.5, x1=2020.5, fillcolor=MUTED, opacity=0.08, line_width=0)
    fig.add_annotation(x=2020, y=1, yref="paper", text="Pandemia", showarrow=False,
                       font=dict(size=11, color=MUTED), yanchor="bottom")
    return fig


# ---------- Header ----------
st.markdown('<div class="kicker">Retail Strategy • Omnichannel • Consumer Analysis</div>', unsafe_allow_html=True)
st.title("Inditex: menos tiendas, más ventas (2017–2025)")
st.markdown(
    "**Pregunta de negocio:** ¿cómo aumentó Inditex sus ventas un "
    f"{pct(r19.Ventas_B_EUR, r25.Ventas_B_EUR):.0f}% entre 2019 y 2025 mientras cerraba "
    f"{int(r19.Tiendas - r25.Tiendas):,} tiendas?"
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Ventas 2025", f"€{r25.Ventas_B_EUR:.1f}B", f"{pct(r19.Ventas_B_EUR, r25.Ventas_B_EUR):+.0f}% vs 2019")
c2.metric("Tiendas 2025", f"{int(r25.Tiendas):,}", f"{pct(r19.Tiendas, r25.Tiendas):+.0f}% vs 2019", delta_color="inverse")
c3.metric("Ventas por tienda", f"€{r25.Ventas_por_tienda_M:.1f}M", f"{pct(r19.Ventas_por_tienda_M, r25.Ventas_por_tienda_M):+.0f}% vs 2019")
c4.metric("Venta online", f"{r25['Online_%']:.1f}%", f"{r25['Online_%'] - r19['Online_%']:+.1f} pts vs 2019")

st.markdown(
    f"""<div class="callout"><b>Hallazgo principal.</b> Cada tienda de Inditex vende hoy casi el doble que en 2019.
    Y no es solo efecto del canal online: aun quitando las ventas digitales, la venta física por tienda subió
    <b>{pct(r19.Fisico_por_tienda_M, r25.Fisico_por_tienda_M):.0f}%</b>
    (€{r19.Fisico_por_tienda_M:.1f}M → €{r25.Fisico_por_tienda_M:.1f}M). Inditex no abandonó la tienda física:
    cerró las menos productivas y reforzó las que quedaron.</div>""",
    unsafe_allow_html=True,
)

# ---------- Gráfica estrella ----------
fig = go.Figure()
fig.add_bar(x=df["Año"], y=df["Fisico_por_tienda_M"], name="Venta física por tienda", marker_color=INK)
fig.add_bar(x=df["Año"], y=df["Ventas_por_tienda_M"] - df["Fisico_por_tienda_M"],
            name="Venta online (atribuida por tienda)", marker_color=SOFT)
fig.update_layout(barmode="stack")
fig.update_traces(hovertemplate="€%{y:.2f}M")
st.plotly_chart(mark_2020(base_layout(fig, "Ventas por tienda: física + online", "Millones de EUR por tienda")),
                width="stretch")
st.caption("La parte online se divide entre el número de tiendas solo para comparar escala; "
           "no implica que cada tienda genere esas ventas digitales.")

# ---------- Contexto ----------
st.header("1. El punto de partida (2017–2019)")
st.markdown(
    "Antes de 2020, la ventaja de Inditex descansaba en tres cosas: una cadena de suministro capaz de llevar "
    "tendencias a tienda en semanas, una red de más de 7,400 tiendas en ubicaciones clave y un posicionamiento "
    "de moda accesible con estética aspiracional. La tienda física era, al mismo tiempo, canal de venta y barrera competitiva."
)

st.header("2. Tiendas vs. ventas: el desacoplamiento")
fig = go.Figure()
fig.add_scatter(x=df["Año"], y=df["Ventas_B_EUR"], name="Ventas (B EUR)", mode="lines+markers",
                line=dict(color=ACCENT, width=3))
fig.add_scatter(x=df["Año"], y=df["Tiendas"], name="Tiendas", mode="lines+markers",
                line=dict(color=INK, width=2, dash="dot"), yaxis="y2")
base_layout(fig, "Ventas suben mientras las tiendas bajan", "Ventas (B EUR)")
fig.update_layout(yaxis2=dict(title="Tiendas", overlaying="y", side="right", showgrid=False))
st.plotly_chart(mark_2020(fig), width="stretch")
st.markdown(
    "Desde 2021 las dos líneas se mueven en sentido opuesto: la red de tiendas se reduce año con año y las ventas "
    "superan el nivel prepandemia desde 2022."
)

st.header("3. El canal digital")
fig = go.Figure()
fig.add_scatter(x=df["Año"], y=df["Online_%"], mode="lines+markers", name="% ventas online",
                line=dict(color=ACCENT, width=3), fill="tozeroy", fillcolor="rgba(181,84,60,0.10)")
fig.update_traces(hovertemplate="%{y:.1f}%")
st.plotly_chart(mark_2020(base_layout(fig, "Participación de ventas online", "% de ventas totales")),
                width="stretch")
st.markdown(
    "El salto a 32% en 2020 fue forzado por el cierre de tiendas durante la pandemia. Al reabrir, la participación "
    "bajó y se estabilizó alrededor de 25–27%: más del doble que en 2019, pero lejos de reemplazar lo físico. "
    "El online se volvió complemento estructural, no sustituto."
)

st.header("4. Rentabilidad")
fig = go.Figure()
fig.add_bar(x=df["Año"], y=df["EBITDA_B_EUR"], name="EBITDA (B EUR)", marker_color=INK)
fig.add_bar(x=df["Año"], y=df["Beneficio_B_EUR"], name="Beneficio neto (B EUR)", marker_color=ACCENT)
fig.update_layout(barmode="group")
st.plotly_chart(mark_2020(base_layout(fig, "EBITDA y beneficio neto", "Miles de millones de EUR")),
                width="stretch")
st.markdown(
    f"El margen EBITDA pasó de {r19['Margen_EBITDA_%']:.1f}% en 2019 a {r25['Margen_EBITDA_%']:.1f}% en 2025: "
    "la empresa no solo vende más, convierte una parte mayor de cada euro en utilidad operativa."
)
st.caption("EBITDA y beneficio neto de 2017–2018 no están incluidos en el dataset.")

# ---------- Interpretación ----------
st.header("5. Interpretación: por qué funciona")
a, b, c = st.columns(3)
a.markdown("**Poda selectiva**  \nSe cierran tiendas de baja productividad; las que quedan concentran tráfico y ventas.")
b.markdown("**Integración omnicanal**  \nLa tienda funciona también como punto de recogida, devolución e inventario para el online.")
c.markdown("**Eficiencia operativa**  \nMenos puntos de venta con más ventas cada uno mejora el margen.")

st.markdown(
    """<div class="hyp"><b>Hipótesis por validar: ¿sigue siendo fast fashion?</b><br>
    La reducción de tiendas y la mejora de margen son consistentes con un reposicionamiento hacia un segmento más
    alto, entre el lujo y el ultra-fast fashion (Shein, Temu). Este dataset no incluye precios ni ticket promedio,
    así que la hipótesis requiere datos adicionales para confirmarse.</div>""",
    unsafe_allow_html=True,
)

st.header("Implicaciones para otros retailers")
st.markdown(
    "- Cerrar tiendas no es sinónimo de retroceso si se mide productividad por tienda, no número de tiendas.\n"
    "- El canal online rinde más cuando se apoya en la red física en lugar de competir con ella.\n"
    "- La métrica relevante pasó de *cobertura* a *rendimiento por punto de venta*."
)

# ---------- Datos y fuentes ----------
with st.expander("Ver datos y metodología"):
    show = df[["Año", "Ventas_B_EUR", "Tiendas", "Online_B_EUR", "Online_%", "Ventas_por_tienda_M",
               "Fisico_por_tienda_M", "EBITDA_B_EUR", "Beneficio_B_EUR", "Margen_EBITDA_%"]]
    st.dataframe(show.style.format(precision=2, na_rep="—"), width="stretch", hide_index=True)
    st.markdown(
        "**Métricas derivadas**\n"
        "- Ventas por tienda = Ventas totales / Tiendas\n"
        "- Venta física = Ventas totales − Ventas online\n"
        "- Margen EBITDA = EBITDA / Ventas\n\n"
        "**Fuentes:** Inditex, reportes anuales 2017–2025 (agregar links)."
    )
