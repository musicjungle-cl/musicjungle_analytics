import pandas as pd

sales = pd.read_csv("data/sales.csv")

ventas_totales = sales["product_net_revenue"].sum()

unidades = sales["product_qty"].sum()

ticket = ventas_totales / sales["product_qty"].count()

metrics = {
    "ventas": ventas_totales,
    "unidades": unidades,
    "ticket": ticket
}

print(metrics)
