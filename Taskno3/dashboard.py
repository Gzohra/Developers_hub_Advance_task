import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('Global_Superstore2.csv', encoding='latin1', parse_dates=['Order Date'])

# Sidebar filters
st.sidebar.header(" Filter Options")
regions = st.sidebar.multiselect("Select Region", df['Region'].dropna().unique(), default=df['Region'].unique())
categories = st.sidebar.multiselect("Select Category", df['Category'].dropna().unique(), default=df['Category'].unique())
sub_categories = st.sidebar.multiselect("Select Sub-Category", df['Sub-Category'].dropna().unique(), default=df['Sub-Category'].unique())

# Filter data
filtered_data = df[
    (df['Region'].isin(regions)) &
    (df['Category'].isin(categories)) &
    (df['Sub-Category'].isin(sub_categories))
]

# Title
st.title(" Global Superstore Dashboard")

# KPIs
total_sales = filtered_data['Sales'].sum()
total_profit = filtered_data['Profit'].sum()
profit_margin = (total_profit / total_sales) * 100 if total_sales else 0

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"{total_sales:,.2f}")
col2.metric("Total Profit", f"{total_profit:,.2f}")
col3.metric("Profit Margin %", f"{profit_margin:.2f}%")

# --- Chart 1: Top 5 Customers by Sales ---
st.markdown("### 🧑‍💼 Top 5 Customers by Sales")
top_customers = (
    filtered_data.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

fig1, ax1 = plt.subplots()
top_customers.plot(kind='barh', color='lightgreen', ax=ax1)
plt.xlabel("Sales")
plt.ylabel("Customer Name")
plt.title("Top 5 Customers")
plt.gca().invert_yaxis()
st.pyplot(fig1)

# --- Chart 2: Time Series Trend ---
if 'Order Date' in df.columns:
    st.markdown("###  Monthly Sales Trend")
    time_series = (
        filtered_data.set_index('Order Date')
        .resample('M')['Sales']
        .sum()
    )

    fig2, ax2 = plt.subplots()
    time_series.plot(ax=ax2, color='royalblue')
    plt.ylabel("Sales")
    plt.xlabel("Month")
    plt.title("Sales Over Time")
    st.pyplot(fig2)
