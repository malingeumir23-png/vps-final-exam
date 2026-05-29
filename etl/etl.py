import pandas as pd
from sqlalchemy import create_engine

MAIN_DB = "postgresql://ecommerce_user:CloudComp%232026@localhost:5432/ecommerce_db"
ANALYTICS_DB = "postgresql://ecommerce_user:CloudComp%232026@localhost:5432/analytics_db"

main_engine = create_engine(MAIN_DB)
analytics_engine = create_engine(ANALYTICS_DB)

orders = pd.read_sql("SELECT * FROM orders", main_engine)

if orders.empty:
    print("No orders found. ETL stopped.")
    exit()

orders["total_price"] = orders["quantity"] * 100

summary = pd.DataFrame([{
    "total_orders": len(orders),
    "total_revenue": orders["total_price"].sum()
}])

top_products = orders.groupby("product_id").size().reset_index(name="count")

# LOAD
summary.to_sql("sales_summary", analytics_engine, if_exists="replace", index=False)
top_products.to_sql("top_products", analytics_engine, if_exists="replace", index=False)

print("ETL SUCCESS")