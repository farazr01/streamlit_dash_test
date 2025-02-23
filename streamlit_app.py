import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def main():
    """
    A basic e-commerce dashboard mockup in Streamlit.
    Replace placeholders with real data or logic to
    connect to your database and generate charts.
    """

    # Set Streamlit page configuration
    st.set_page_config(
        page_title="E-commerce Dashboard",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # SIDEBAR for Navigation (Optional)
    st.sidebar.title("Navigation")
    pages = ["Dashboard", "Orders", "Products", "Customers", "Suppliers", "Reports"]
    page_selection = st.sidebar.radio("Go to", pages)

    # SIDEBAR date range filter (demo version)
    st.sidebar.title("Date Range")
    start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=30))
    end_date = st.sidebar.date_input("End Date", datetime.now())

    # MAIN DASHBOARD
    st.title("E-commerce Dashboard Mockup")

    # --- KPI SECTION ---
    # Use columns to arrange multiple KPIs in a row
    kpi_cols = st.columns(6)

    with kpi_cols[0]:
        # Example: total sales
        st.metric(label="Total Sales", value="£15,240", delta="+12% vs last month")

    with kpi_cols[1]:
        # Example: number of orders
        st.metric(label="Orders", value="342", delta="-5% vs last month")

    with kpi_cols[2]:
        # Example: average order value
        st.metric(label="Avg Order Value", value="£44.56", delta="+3% vs last month")

    with kpi_cols[3]:
        # Example: top category
        st.metric(label="Top Category", value="Electronics", delta="£8,200 rev")

    with kpi_cols[4]:
        # Example: new customers
        st.metric(label="New Customers", value="58", delta="+10% vs last month")

    with kpi_cols[5]:
        # Example: returning rate
        st.metric(label="Returning Rate", value="35%", delta="Slightly down")

    st.divider()

    # --- SALES & ORDERS CHARTS ---
    st.subheader("Sales & Orders Overview")
    col1, col2 = st.columns(2)

    with col1:
        # Placeholder for a Sales Trend Chart
        st.write("**Sales Trend Chart**")
        # Create some random data to mimic a trend
        sales_data = np.random.randint(100, 500, 10)
        st.line_chart(sales_data)

    with col2:
        # Placeholder for an Orders Trend Chart
        st.write("**Orders Trend Chart**")
        orders_data = np.random.randint(20, 100, 10)
        st.line_chart(orders_data)

    st.divider()

    # --- TOP PRODUCTS & CATEGORIES ---
    st.subheader("Top Products & Categories")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Top Products**")
        # Replace with actual product data
        top_products_data = {
            "Product": ["Product A", "Product B", "Product C"],
            "Units Sold": [120, 90, 75],
            "Revenue": ["£2,400", "£1,800", "£1,500"]
        }
        df_top_products = pd.DataFrame(top_products_data)
        st.table(df_top_products)

    with col2:
        st.write("**Top Categories**")
        # Replace with actual category data
        top_categories_data = {
            "Category": ["Electronics", "Home & Garden", "Fashion"],
            "Units Sold": [300, 180, 150],
            "Revenue": ["£8,200", "£3,600", "£2,700"]
        }
        df_top_categories = pd.DataFrame(top_categories_data)
        st.table(df_top_categories)

    st.divider()

    # --- INVENTORY & SUPPLIER PERFORMANCE ---
    st.subheader("Inventory & Supplier Performance")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Low Stock Items**")
        # Replace with actual inventory data
        low_stock_data = {
            "Product": ["Product A", "Product D"],
            "Stock Level": [8, 4],
            "Reorder Threshold": [10, 5]
        }
        df_low_stock = pd.DataFrame(low_stock_data)
        st.table(df_low_stock)

    with col2:
        st.write("**Supplier Performance**")
        # Replace with actual supplier performance data
        supplier_data = {
            "Supplier": ["Supplier X", "Supplier Y"],
            "Avg Lead Time (days)": [7, 10],
            "On-Time Delivery Rate": ["95%", "88%"]
        }
        df_supplier = pd.DataFrame(supplier_data)
        st.table(df_supplier)

    st.divider()

    # --- CUSTOMER INSIGHTS ---
    st.subheader("Customer Insights")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Customer Segmentation Chart (Placeholder)**")
        # Example placeholder data for segmentation
        segment_data = pd.DataFrame({
            "Segment": ["Segment A", "Segment B", "Segment C"],
            "Count": [50, 30, 20]
        })
        # Quick bar chart
        st.bar_chart(segment_data.set_index("Segment"))

    with col2:
        st.write("**Lifetime Value / Purchase Frequency (Placeholder)**")
        # Example data for LTV or purchase frequency
        freq_data = np.random.randint(1, 5, 10)
        st.line_chart(freq_data)

    st.divider()

    # --- SHIPPING & DELIVERY ---
    st.subheader("Shipping & Delivery")
    col1, col2 = st.columns(2)

    with col1:
        st.write("**Shipment Status**")
        # Replace with actual shipping status data
        shipping_status_data = {
            "Status": ["Pending", "In Transit", "Delivered", "Returned"],
            "Count": [20, 35, 280, 7]
        }
        df_shipping = pd.DataFrame(shipping_status_data)
        st.table(df_shipping)

    with col2:
        st.write("**Return Rate & Delivery Times**")
        st.write("Average Delivery Time: **3.2 days**")
        st.write("Return Rate: **2.1%**")

    st.divider()

    # --- ALERTS & NOTIFICATIONS ---
    st.subheader("Alerts & Notifications")
    alerts = [
        "Product D stock is critically low.",
        "Supplier Y shipment delayed by 2 days.",
        "Return rate for Product C is unusually high."
    ]
    for alert in alerts:
        st.warning(alert)

    st.divider()

    # --- CUSTOM REPORTS ---
    st.subheader("Custom Reports")
    st.write(
        "Generate or schedule detailed reports combining Orders, Payments, "
        "Shipping, and Inventory data."
    )
    if st.button("Create New Report"):
        st.success("Report creation process (placeholder).")

if __name__ == "__main__":
    main()
