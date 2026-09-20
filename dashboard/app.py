import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# Robust path handling - works no matter where streamlit is run from
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "processed" / "cleaned_data.csv"

st.set_page_config(page_title="Iris Dataset Dashboard", layout="wide")

st.title("Iris Dataset Explorer")
st.markdown("Interactive dashboard for exploring the Iris flower dataset — Statistics Superstars")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
species_options = df['species'].unique().tolist()
selected_species = st.sidebar.multiselect(
    "Select species to display",
    options=species_options,
    default=species_options
)

filtered_df = df[df['species'].isin(selected_species)]

# Summary stats
st.header("Summary Statistics")
st.dataframe(filtered_df.describe())

# Layout: two columns for charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("X-axis", df.select_dtypes(include='number').columns, index=0)
    y_axis = st.selectbox("Y-axis", df.select_dtypes(include='number').columns, index=2)
    
    fig_scatter = px.scatter(
        filtered_df, x=x_axis, y=y_axis, color='species',
        title=f"{x_axis} vs {y_axis} by Species"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    st.subheader("Box Plot")
    box_col = st.selectbox("Measurement to compare", df.select_dtypes(include='number').columns, index=2)
    
    fig_box = px.box(
        filtered_df, x='species', y=box_col, color='species',
        title=f"{box_col} by Species"
    )
    st.plotly_chart(fig_box, use_container_width=True)

# Correlation heatmap
st.header("Correlation Heatmap")
numeric_df = filtered_df.select_dtypes(include='number')
corr = numeric_df.corr()
fig_corr = px.imshow(
    corr, text_auto='.2f', color_continuous_scale='RdBu_r',
    title="Correlation Between Measurements"
)
st.plotly_chart(fig_corr, use_container_width=True)

# Raw data table
st.header("Raw Data")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("---")
st.markdown(f"Showing **{len(filtered_df)}** of **{len(df)}** total flowers")
