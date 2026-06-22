import streamlit as st
import pandas as pd

# 1. Set page configuration (title and layout)
st.set_page_config(page_title="HK Stock Quant Dashboard", layout="wide")

# 2. Display main title and description text
st.title("📈 Dual-Factor Quant Analysis Dashboard")
st.markdown("This is an automated quantitative signal monitoring panel. It combines the **MA50 Trend** and **RSI14 Momentum** to identify potential market reversal points.")
st.markdown("---") # Draw a horizontal separator line

# 3. Load the CSV report generated from the data pipeline
try:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv("daily_stock_report.csv")
    
    # 4. SIDEBAR CONTROLS: Add user interactive filters
    st.sidebar.header("🔍 Filter Options")
    
    # Filter by MA50 Status (All, Strong, Weak)
    status_options = ["All"] + list(df["MA50_Status"].unique())
    selected_status = st.sidebar.selectbox("Select MA50 Status:", status_options)
    
    # Filter by RSI Slider (0 to 100)
    rsi_threshold = st.sidebar.slider("Maximum RSI Level:", min_value=0, max_value=100, value=100)
    
    # Apply filters to the DataFrame
    filtered_df = df.copy()
    if selected_status != "All":
        filtered_df = filtered_df[filtered_df["MA50_Status"] == selected_status]
    filtered_df = filtered_df[filtered_df["RSI_14"] <= rsi_threshold]

    # 5. CONDITIONAL FORMATTING: Define styling functions for the table
    def style_ma50(val):
        """Color code the MA50 status: Light green for Strong, Light red for Weak"""
        if val == "Strong":
            return "background-color: #d4edda; color: #155724; font-weight: bold;"
        elif val == "Weak":
            return "background-color: #f8d7da; color: #721c24; font-weight: bold;"
        return ""

    def highlight_rsi(val):
        """Highlight oversold RSI (< 30) to signal potential buying opportunities"""
        if val < 30:
            return "background-color: #fff3cd; color: #856404; font-weight: bold; border: 2px solid #ffeeba;"
        return ""

    # Apply the styling styles to specific columns
    styled_df = filtered_df.style.map(style_ma50, subset=["MA50_Status"]).map(highlight_rsi, subset=["RSI_14"])
    
    # 6. DISPLAY: Render the beautifully styled and interactive table
    st.subheader("📊 Today's Stock Signal List")
    st.dataframe(styled_df, use_container_width=True)
    
except FileNotFoundError:
    # Fail-safe (Exception handling) in case the file is missing
    st.error("⚠️ `daily_stock_report.csv` not found! Please ensure the data pipeline was executed successfully and the CSV file is located in the same directory as this script.")
