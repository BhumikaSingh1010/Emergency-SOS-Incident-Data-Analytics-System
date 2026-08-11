import streamlit as st
import pandas as pd
import pyodbc
import plotly.express as px

# Page settings
st.set_page_config(
    page_title="Emergency Incident Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Emergency Incident Analytics Dashboard")

# SQL Server connection
conn = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=.\SQLEXPRESS;"
    r"DATABASE=EmergencySOS;"
    r"Trusted_Connection=yes;"
)

# Get required data
query = """
SELECT Record_ID, Call_Date_Time, Priority, District,
       Description, Incident_Location, Neighborhood
FROM dbo.Emergency_Incidents
"""

df = pd.read_sql(query, conn)
conn.close()

# Convert date
df["Call_Date_Time"] = pd.to_datetime(
    df["Call_Date_Time"], errors="coerce"
)

# Sidebar filters
st.sidebar.header("🔍 Filters")

priority = st.sidebar.selectbox(
    "Priority",
    ["All"] + sorted(df["Priority"].dropna().astype(str).unique())
)

district = st.sidebar.selectbox(
    "District",
    ["All"] + sorted(df["District"].dropna().astype(str).unique())
)

# Apply filters
data = df.copy()

if priority != "All":
    data = data[data["Priority"].astype(str) == priority]

if district != "All":
    data = data[data["District"].astype(str) == district]

# KPI cards
st.subheader("📌 Key Information")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Incidents", f"{len(data):,}")

high = data["Priority"].astype(str).str.upper().str.contains(
    "HIGH", na=False
)
c2.metric("High Priority", f"{high.sum():,}")

c3.metric("Districts", data["District"].nunique())

latest = data["Call_Date_Time"].max()
c4.metric(
    "Latest Incident",
    latest.strftime("%d %b %Y") if pd.notna(latest) else "N/A"
)

st.divider()

# Priority pie chart
st.subheader("🚨 Incident Priority Distribution")

priority_data = data["Priority"].value_counts().reset_index()
priority_data.columns = ["Priority", "Count"]

fig1 = px.pie(
    priority_data,
    names="Priority",
    values="Count",
    hole=0.35
)

st.plotly_chart(fig1, use_container_width=True)

# District bar chart
st.subheader("📍 Incidents by District")

district_data = data["District"].value_counts().head(10).reset_index()
district_data.columns = ["District", "Count"]

fig2 = px.bar(
    district_data,
    x="District",
    y="Count",
    title="Top 10 Districts"
)

st.plotly_chart(fig2, use_container_width=True)

# Time trend line chart
st.subheader("📅 Incidents Over Time")

time_data = (
    data.dropna(subset=["Call_Date_Time"])
    .set_index("Call_Date_Time")
    .resample("ME")
    .size()
    .reset_index(name="Count")
)

fig3 = px.line(
    time_data,
    x="Call_Date_Time",
    y="Count",
    title="Monthly Incident Trend"
)

st.plotly_chart(fig3, use_container_width=True)

# Neighborhood chart
st.subheader("🏘️ Top 10 Neighborhoods")

neighborhood_data = (
    data["Neighborhood"]
    .value_counts()
    .head(10)
    .reset_index()
)

neighborhood_data.columns = ["Neighborhood", "Count"]

fig4 = px.bar(
    neighborhood_data,
    x="Neighborhood",
    y="Count",
    title="Top 10 Neighborhoods"
)

st.plotly_chart(fig4, use_container_width=True)

# Recent incidents
st.subheader("📋 Recent Incidents")

recent = data.sort_values(
    "Call_Date_Time",
    ascending=False
).head(100)

st.dataframe(
    recent,
    use_container_width=True
)