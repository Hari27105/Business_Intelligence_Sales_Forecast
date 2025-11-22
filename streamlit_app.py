import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title="Sales Forecasting System",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Sales Forecasting & Business Intelligence System")
st.markdown("### Built by **Hari Prasad Kadu**")
st.markdown("[GitHub: Hari27105](https://github.com/Hari27105) | [LinkedIn](https://linkedin.com/in/hariprasad-kadu-855382314) | kaduhariprasad@gmail.com")
st.markdown("---")

# Load model and data
@st.cache_resource
def load_model():
    return joblib.load('../models/sales_forecast_model.pkl')

@st.cache_data
def load_data():
    return pd.read_csv('../data/cleaned_sales_data.csv')

try:
    model = load_model()
    df = load_data()

    # Sidebar
    st.sidebar.header("🎯 Navigation")
    page = st.sidebar.radio("Choose a page:", 
                            ["📈 Dashboard", "🔮 Sales Prediction", "📊 Data Analysis"])

    if page == "📈 Dashboard":
        st.header("📈 Sales Dashboard")

        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            total_revenue = df['Revenue'].sum()
            st.metric("Total Revenue", f"₹{total_revenue:,.0f}")

        with col2:
            avg_revenue = df['Revenue'].mean()
            st.metric("Avg Revenue", f"₹{avg_revenue:,.0f}")

        with col3:
            total_units = df['Units_Sold'].sum()
            st.metric("Total Units Sold", f"{total_units:,.0f}")

        with col4:
            num_products = df['Product'].nunique()
            st.metric("Products", num_products)

        st.markdown("---")

        # Charts
        col1, col2 = st.columns(2)

        with col1:
            df['Date'] = pd.to_datetime(df['Date'])
            monthly_revenue = df.groupby(df['Date'].dt.to_period('M'))['Revenue'].sum()
            fig1 = px.line(x=monthly_revenue.index.astype(str), y=monthly_revenue.values,
                          title='Monthly Revenue Trend',
                          labels={'x': 'Month', 'y': 'Revenue (₹)'})
            fig1.update_traces(line_color='#2563eb', line_width=3)
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(5)
            fig2 = px.bar(x=top_products.values, y=top_products.index, 
                         orientation='h',
                         title='Top 5 Products by Revenue',
                         labels={'x': 'Revenue (₹)', 'y': 'Product'})
            fig2.update_traces(marker_color='#10b981')
            st.plotly_chart(fig2, use_container_width=True)

    elif page == "🔮 Sales Prediction":
        st.header("🔮 Sales Revenue Prediction")
        st.markdown("Enter the parameters below to predict sales revenue:")

        col1, col2 = st.columns(2)

        with col1:
            units_sold = st.number_input("Units to Sell", min_value=1, max_value=10000, value=100)
            unit_price = st.number_input("Unit Price (₹)", min_value=1, max_value=100000, value=500)

        with col2:
            month = st.selectbox("Month", list(range(1, 13)), 
                               format_func=lambda x: pd.to_datetime(f'2024-{x}-01').strftime('%B'))
            quarter = st.selectbox("Quarter", [1, 2, 3, 4])

        if st.button("🚀 Predict Revenue"):
            input_data = [[units_sold, unit_price, month, quarter]]
            prediction = model.predict(input_data)[0]

            st.success("### Prediction Results")
            st.metric("Predicted Revenue", f"₹{prediction:,.2f}")

            total_cost = units_sold * unit_price * 0.6
            expected_profit = prediction - total_cost
            profit_margin = (expected_profit / prediction) * 100 if prediction > 0 else 0

            col1, col2, col3 = st.columns(3)
            with col1:
                st.info(f"**Expected Cost:** ₹{total_cost:,.2f}")
            with col2:
                st.success(f"**Expected Profit:** ₹{expected_profit:,.2f}")
            with col3:
                st.warning(f"**Profit Margin:** {profit_margin:.1f}%")

    else:
        st.header("📊 Data Analysis")

        st.subheader("📋 Sales Data")
        st.dataframe(df.head(100), use_container_width=True)

        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download Full Dataset",
            data=csv,
            file_name="sales_data.csv",
            mime="text/csv"
        )

        st.subheader("📈 Statistical Summary")
        st.write(df.describe())

except FileNotFoundError:
    st.error("⚠️ Model or data file not found. Please ensure all files are in the correct location.")
    st.info("Expected files: `models/sales_forecast_model.pkl` and `data/cleaned_sales_data.csv`")
