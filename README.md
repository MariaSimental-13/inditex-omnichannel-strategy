# Inditex: menos tiendas, más ventas (2017–2025)

**Análisis de estrategia omnicanal de retail**: cómo Inditex aumentó sus ventas un **41%** entre 2019 y 2025 mientras cerraba **27%** de sus tiendas.

🔗 **[Ver la app interactiva en Streamlit](PEGA_AQUI_TU_LINK)**

![Ventas por tienda de Inditex](assets/ventas_por_tienda.png)

---

## Pregunta de negocio

¿Cómo puede un retailer vender más que nunca mientras reduce su red de tiendas físicas? ¿Lo explica el canal online o cambió la tienda misma?

## Hallazgos principales

| Métrica | 2019 | 2025 | Cambio |
|---|---|---|---|
| Ventas totales | €28.3B | €39.9B | **+41%** |
| Número de tiendas | 7,469 | 5,460 | **−27%** |
| Ventas por tienda | €3.8M | €7.3M | **+93%** |
| Venta física por tienda (sin online) | €3.3M | €5.3M | **+64%** |
| % de ventas online | 13.8% | 26.7% | **+12.9 pts** |
| Margen EBITDA | 26.9% | 28.3% | **+1.4 pts** |

1. **La tienda física no perdió importancia, se volvió más productiva.** Aun quitando todas las ventas online, cada tienda vende 64% más que en 2019. Inditex cerró las tiendas menos rentables y reforzó las que quedaron.
2. **El online es complemento, no sustituto.** Llegó a 32% de las ventas en 2020 por los cierres de la pandemia, bajó al reabrir las tiendas y se estabilizó en ~26–27%, el doble que antes de 2020.
3. **Menos tiendas, mejor margen.** El margen EBITDA pasó de 26.9% a 28.3%, así que la empresa no solo vende más: cada euro que vende le deja más utilidad operativa.

## Implicaciones para otros retailers

- La métrica relevante ya no es cuántas tiendas tienes (*cobertura*), sino cuánto rinde cada una (*productividad por punto de venta*).
- El canal digital rinde más cuando se apoya en la red física (pickup, devoluciones, inventario) en lugar de competir con ella.
- Cerrar tiendas puede ser una estrategia de crecimiento, no de retroceso.

## Hipótesis por validar

La reducción de tiendas y la mejora de margen son consistentes con un **reposicionamiento hacia un segmento más alto**, entre el lujo y el ultra fast fashion (Shein, Temu). Este análisis no incluye datos de precios ni de ticket promedio, así que queda como hipótesis para una siguiente iteración.

## Metodología

- **Datos:** ventas totales, número de tiendas, ventas online, EBITDA y beneficio neto, 2017–2025.
- **Métricas derivadas:**
  - Ventas por tienda = Ventas totales / Número de tiendas
  - Venta física = Ventas totales − Ventas online
  - Margen EBITDA = EBITDA / Ventas
- **Limitaciones:** EBITDA y beneficio de 2017–2018 no están en el dataset. Las ventas online por tienda se calculan solo para comparar escala, no porque cada tienda genere esas ventas.

## Stack

Python · Pandas · NumPy · Plotly · Streamlit

## Cómo correrlo

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Fuentes

- Inditex, Informes Anuales 2017–2025 → [inditex.com/itxcomweb/es/es/accionistas-e-inversores](https://www.inditex.com/itxcomweb/es/es/accionistas-e-inversores)

---

**María Simental** · [GitHub](https://github.com/MariaSimental-13) · [LinkedIn](PEGA_AQUI_TU_LINKEDIN)
