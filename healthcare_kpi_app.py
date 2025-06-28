
import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# Title
st.title("🏥 Healthcare KPI Tracker")

# Connect to SQLite database
conn = sqlite3.connect("healthcare_kpi.db")
query = "SELECT * FROM kpi_data"
df = pd.read_sql(query, conn)
conn.close()

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Sidebar filters
departments = df['department'].unique()
selected_dept = st.sidebar.selectbox("Select Department", departments)
selected_kpi = st.sidebar.selectbox("Select KPI", [
    "avg_wait_time_minutes", 
    "infection_rate_percent", 
    "avg_cost_per_patient_usd", 
    "readmission_rate_percent"
])

# Filter data
filtered_df = df[df['department'] == selected_dept]

# Line chart
fig = px.line(
    filtered_df, 
    x="date", 
    y=selected_kpi, 
    title=f"{selected_kpi.replace('_', ' ').title()} Over Time - {selected_dept}",
    markers=True
)
st.plotly_chart(fig)

# Show data table
st.subheader("Raw Data")
st.dataframe(filtered_df)
