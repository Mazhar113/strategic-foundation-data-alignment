
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Strategic Foundation", layout="wide")
st.markdown("<style>body{background-color:#0b1220;color:#e6eef8} .kpi{background:#0f172a;padding:12px;border-radius:12px}</style>", unsafe_allow_html=True)

DATA_DIR = "data"
@st.cache_data
def load_csv(name):
    path = os.path.join(DATA_DIR, f"{name}.csv")
    if os.path.exists(path):
        return pd.read_csv(path, parse_dates=True, infer_datetime_format=True)
    return pd.DataFrame()

st.title("🚀 Strategic Foundation — Executive Dashboard (Dark Mode)")
customers = load_csv("customers")
orders = load_csv("orders")

st.sidebar.header("Controls")
date_range = st.sidebar.date_input("Order date range", [orders["order_date"].min().date() if not orders.empty else None, orders["order_date"].max().date() if not orders.empty else None])
st.sidebar.markdown("Data source: CSV (local)")

if not orders.empty:
    orders["order_date"] = pd.to_datetime(orders["order_date"], errors='coerce')
    orders["month"] = orders["order_date"].dt.to_period("M").dt.to_timestamp()
    rev = orders.groupby("month")["order_value"].sum().reset_index()
    st.metric("Revenue (latest month)", f'${rev["order_value"].iloc[-1]:,.2f}' if not rev.empty else "N/A")
    fig = px.area(rev, x="month", y="order_value", title="Revenue (monthly)")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No orders loaded. Place CSVs in the data/ folder.")

st.markdown("## Top customers sample")
if not orders.empty and not customers.empty:
    top = orders.groupby("customer_id")["order_value"].sum().reset_index().sort_values("order_value", ascending=False).head(20)
    top = top.merge(customers, on="customer_id", how="left")
    st.dataframe(top[["customer_id","segment","region","order_value"]])
