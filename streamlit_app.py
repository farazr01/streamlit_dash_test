import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import openai

# -----------------------------
# Function to Get Chatbot Response
# -----------------------------
def get_chatbot_response():
    """
    Calls the OpenAI ChatCompletion API using the conversation history stored in st.session_state.messages.
    The assistant's response is appended to the conversation.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change this if needed.
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=300
        )
        # Append the assistant's message to the conversation history.
        st.session_state.messages.append(response["choices"][0]["message"])
    except Exception as e:
        st.error(f"Error while calling OpenAI API: {e}")

# -----------------------------
# Main App Function
# -----------------------------
def main():
    # Configure the Streamlit page
    st.set_page_config(
        page_title="E-commerce Dashboard & Chatbot Insights",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # -----------------------------
    # Sidebar: Navigation and API Key Setup
    # -----------------------------
    st.sidebar.title("Navigation")
    pages = ["Dashboard", "Chatbot Insights"]
    page_selection = st.sidebar.radio("Go to", pages)

    # Set up the OpenAI API key
    if "openai_api_key" not in st.session_state:
        st.session_state["openai_api_key"] = st.secrets.get("OPENAI_API_KEY", "")
    if not st.session_state["openai_api_key"]:
        st.session_state["openai_api_key"] = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
    openai.api_key = st.session_state["openai_api_key"]

    # Sidebar Date Range Filter (used on the Dashboard page)
    st.sidebar.title("Date Range")
    start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=30))
    end_date = st.sidebar.date_input("End Date", datetime.now())

    # -----------------------------
    # Dashboard Page
    # -----------------------------
    if page_selection == "Dashboard":
        st.title("E-commerce Dashboard Mockup")

        # --- KPI SECTION ---
        kpi_cols = st.columns(6)
        with kpi_cols[0]:
            st.metric(label="Total Sales", value="£15,240", delta="+12% vs last month")
        with kpi_cols[1]:
            st.metric(label="Orders", value="342", delta="-5% vs last month")
        with kpi_cols[2]:
            st.metric(label="Avg Order Value", value="£44.56", delta="+3% vs last month")
        with kpi_cols[3]:
            st.metric(label="Top Category", value="Electronics", delta="£8,200 rev")
        with kpi_cols[4]:
            st.metric(label="New Customers", value="58", delta="+10% vs last month")
        with kpi_cols[5]:
            st.metric(label="Returning Rate", value="35%", delta="Slightly down")

        st.divider()

        # --- SALES & ORDERS CHARTS ---
        st.subheader("Sales & Orders Overview")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Sales Trend Chart**")
            # Placeholder: Replace with your real sales data.
            sales_data = np.random.randint(100, 500, 10)
            st.line_chart(sales_data)
        with col2:
            st.write("**Orders Trend Chart**")
            # Placeholder: Replace with your real orders data.
            orders_data = np.random.randint(20, 100, 10)
            st.line_chart(orders_data)

        st.divider()

        # --- TOP PRODUCTS & CATEGORIES ---
        st.subheader("Top Products & Categories")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Top Products**")
            # Replace the sample data with your actual product query.
            top_products_data = {
                "Product": ["Product A", "Product B", "Product C"],
                "Units Sold": [120, 90, 75],
                "Revenue": ["£2,400", "£1,800", "£1,500"]
            }
            df_top_products = pd.DataFrame(top_products_data)
            st.table(df_top_products)
        with col2:
            st.write("**Top Categories**")
            # Replace with your actual category data.
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
            # Replace with your real inventory data.
            low_stock_data = {
                "Product": ["Product A", "Product D"],
                "Stock Level": [8, 4],
                "Reorder Threshold": [10, 5]
            }
            df_low_stock = pd.DataFrame(low_stock_data)
            st.table(df_low_stock)
        with col2:
            st.write("**Supplier Performance**")
            # Replace with your supplier performance data.
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
            # Replace with segmentation data.
            segment_data = pd.DataFrame({
                "Segment": ["Segment A", "Segment B", "Segment C"],
                "Count": [50, 30, 20]
            })
            st.bar_chart(segment_data.set_index("Segment"))
        with col2:
            st.write("**Lifetime Value / Purchase Frequency (Placeholder)**")
            # Replace with actual lifetime value or purchase frequency data.
            freq_data = np.random.randint(1, 5, 10)
            st.line_chart(freq_data)

        st.divider()

        # --- SHIPPING & DELIVERY ---
        st.subheader("Shipping & Delivery")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Shipment Status**")
            # Replace with your shipment status data.
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
            "Generate or schedule detailed reports combining Orders, Payments, Shipping, and Inventory data."
        )
        if st.button("Create New Report"):
            st.success("Report creation process (placeholder).")

    # -----------------------------
    # Chatbot Insights Page (Configured to Look Like Demo‑QSR)
    # -----------------------------
    elif page_selection == "Chatbot Insights":
        st.title("Chatbot Insights")
        st.write(
            "Ask any question about our entire data model (Orders, Payments, Products, Inventory, Customers, Suppliers, Shipping, etc.) and receive detailed insights."
        )

        # Initialize the conversation history in session_state if it doesn't exist.
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system",
                    "content": (
                        "You are an expert in e-commerce business analytics. You have deep knowledge of the entire data model including Orders, Payments, "
                        "Products, Inventory, Customers, Suppliers, Shipping, and other related tables. Provide insightful analysis and recommendations."
                    )
                }
            ]

        # Display the conversation history using Streamlit's chat components.
        # Note: The system message is not displayed to the user.
        for message in st.session_state.messages[1:]:
            if message["role"] == "assistant":
                st.chat_message("assistant").write(message["content"])
            elif message["role"] == "user":
                st.chat_message("user").write(message["content"])

        # Get user input using the built-in chat input (available in recent versions of Streamlit).
        user_input = st.chat_input("Ask your question about the data model:")
        if user_input:
            # Append the user's message to the conversation history.
            st.session_state.messages.append({"role": "user", "content": user_input})
            st.chat_message("user").write(user_input)
            with st.spinner("Generating response..."):
                get_chatbot_response()
            # Display the latest assistant message.
            st.chat_message("assistant").write(st.session_state.messages[-1]["content"])

# -----------------------------
# Run the App
# -----------------------------
if __name__ == "__main__":
    main()
