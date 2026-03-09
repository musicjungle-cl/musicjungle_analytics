import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="HOST",
    user="USER",
    password="PASSWORD",
    database="DATABASE"
)

sales_query = """
SELECT
product_id,
product_qty,
product_net_revenue,
date_created
FROM wpap_wc_order_product_lookup
WHERE date_created >= DATE_SUB(NOW(), INTERVAL 24 MONTH)
"""

sales = pd.read_sql(sales_query, conn)

sales.to_csv("data/sales.csv", index=False)
