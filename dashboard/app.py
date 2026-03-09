import streamlit as st
import pandas as pd

sales = pd.read_csv("../data/sales.csv")

ventas = sales["product_net_revenue"].sum()
unidades = sales["product_qty"].sum()

st.title("Music Jungle Analytics")

col1, col2, col3 = st.columns(3)

col1.metric("Ventas totales", f"${ventas:,.0f}")
col2.metric("Unidades vendidas", f"{unidades}")
col3.metric("Ticket promedio", f"${ventas/unidades:,.0f}")
