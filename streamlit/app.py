import streamlit as st
import pandas as pd
import plotly.express as px


# Set the page configuration
st.set_page_config(
    page_title="E-Commerce Dashboard",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_data
def load_data():
    # Load the CSV with low_memory=False to suppress mixed types warning
    data = pd.read_csv('/app/data.csv', encoding='ISO-8859-1', low_memory=False)
    # Convert 'InvoiceDate' to datetime and handle errors gracefully
    data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'], errors='coerce')
    return data

# Load data
data = load_data()


# Custom CSS for modern design
st.markdown("""
    <style>
        /* Set custom background color */
        .main {
            background-color: #f5f7fa;
        }

        /* Unique sidebar styling */
        section[data-testid="stSidebar"] {
            color: black;
        }
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3, 
        section[data-testid="stSidebar"] h4, 
        section[data-testid="stSidebar"] h5, 
        section[data-testid="stSidebar"] h6 {
            color: #000000;
        }

        /* Adjust text and card styles */
        .stMetricLabel {
            color: #2c3e50;
        }
        .stMarkdown {
            margin-bottom: 15px;
        }
        
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 E-Commerce Sales Dashboard")

# Top KPIs
st.markdown("### Key Metrics")
kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric(label="🛒 Total Transactions", value=data.shape[0], delta=None)

with kpi2:
    total_quantity = data["Quantity"].sum()
    st.metric(label="📦 Total Quantity Sold", value=f"{total_quantity:,}")

with kpi3:
    total_revenue = (data["Quantity"] * data["UnitPrice"]).sum()
    st.metric(label="💰 Total Revenue (€)", value=f"€{total_revenue:,.2f}")

# Sidebar for Filters
st.sidebar.header("Filter Data")
st.sidebar.markdown("Apply filters to customize the data view.")

country_filter = st.sidebar.multiselect(
    "🌍 Select Countries:",
    options=data['Country'].dropna().unique(),
    default=None
)

min_date, max_date = data['InvoiceDate'].min(), data['InvoiceDate'].max()
date_filter = st.sidebar.date_input(
    "📅 Date Range:",
    [min_date, max_date],
    min_value=min_date,
    max_value=max_date,
)

# Filter Data
filtered_data = data[
    (data['Country'].isin(country_filter)) &
    (data['InvoiceDate'] >= pd.Timestamp(date_filter[0])) &
    (data['InvoiceDate'] <= pd.Timestamp(date_filter[1]))
]

# Filtered Data Preview
st.markdown("### Filtered Data Preview")
st.dataframe(filtered_data.head(), use_container_width=True)

# Download Filtered Data
st.download_button(
    label="⬇️ Download Filtered Data",
    data=filtered_data.to_csv(index=False).encode('utf-8'),
    file_name='filtered_data.csv',
    mime='text/csv',
)

# Visualizations
st.markdown("### Visual Analytics")
chart1, chart2 = st.columns(2)

# Sales by Country
with chart1:
    st.subheader("🌍 Sales by Country")
    sales_by_country = (
        filtered_data.groupby("Country")["Quantity"].sum().reset_index().sort_values("Quantity", ascending=False)
    )
    fig = px.bar(
        sales_by_country,
        x="Country",
        y="Quantity",
        title="Quantity Sold by Country",
        color="Quantity",
        color_continuous_scale=px.colors.sequential.Blues,
    )
    st.plotly_chart(fig, use_container_width=True)

# Top Selling Products
with chart2:
    st.subheader("📦 Top Selling Products")
    top_products = (
        filtered_data.groupby("Description")["Quantity"].sum().reset_index().sort_values("Quantity", ascending=False).head(10)
    )
    fig = px.bar(
        top_products,
        x="Quantity",
        y="Description",
        orientation='h',
        title="Top Selling Products",
        color="Quantity",
        color_continuous_scale=px.colors.sequential.Purples,
    )
    st.plotly_chart(fig, use_container_width=True)

# Sales Trend Over Time
st.subheader("📈 Sales Trend Over Time")
sales_over_time = (
    filtered_data.groupby(filtered_data['InvoiceDate'].dt.date)["Quantity"].sum().reset_index()
)
fig = px.line(
    sales_over_time,
    x="InvoiceDate",
    y="Quantity",
    title="Sales Trend",
    markers=True,
    color_discrete_sequence=["#2A9D8F"],
)
st.plotly_chart(fig, use_container_width=True)

# Correlation Matrix
st.subheader("📊 Correlation Analysis")
correlation = filtered_data[['Quantity', 'UnitPrice']].corr()
fig = px.imshow(
    correlation,
    text_auto=True,
    color_continuous_scale=px.colors.sequential.Viridis,
    title="Correlation Matrix",
)
st.plotly_chart(fig, use_container_width=True)