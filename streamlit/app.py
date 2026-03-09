import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# Page settings
st.set_page_config(page_title="OLA Ride Insights", layout="wide")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="ola_project"
)

# Load data
query = "SELECT * FROM rides"
df = pd.read_csv("dataset/ola_cleaned.csv")

# Sidebar page selection
page = st.sidebar.selectbox(
    "Select Dashboard Page",
    ["Overview", "Vehicle & Rating Insights"]
)

# ==============================
# PAGE 1 — OVERVIEW
# ==============================

if page == "Overview":

    st.title("OLA Ride Insights Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Rides",
        f"{len(df):,}"
    )

    col2.metric(
        "Total Revenue",
        f"₹{df['Booking_Value'].sum():,.0f}"
    )

    col3.metric(
        "Average Rating",
        round(df["Customer_Rating"].mean(), 2)
    )

    st.subheader("Ride Volume Over Time")

    ride_trend = df.groupby("Date")["Booking_ID"].count().reset_index()

    fig1 = px.line(
        ride_trend,
        x="Date",
        y="Booking_ID",
        markers=True
    )

    st.plotly_chart(fig1, use_container_width=True)

    col4, col5 = st.columns(2)

    with col4:

        st.subheader("Booking Status Breakdown")

        status = df["Booking_Status"].value_counts().reset_index()
        status.columns = ["Booking_Status", "count"]

        fig2 = px.pie(
            status,
            names="Booking_Status",
            values="count"
        )

        st.plotly_chart(fig2, use_container_width=True)

    with col5:

        st.subheader("Revenue by Payment Method")

        payment = df.groupby("Payment_Method")["Booking_Value"].sum().reset_index()

        fig3 = px.pie(
            payment,
            names="Payment_Method",
            values="Booking_Value"
        )

        st.plotly_chart(fig3, use_container_width=True)

# ==============================
# PAGE 2 — VEHICLE & RATINGS
# ==============================

if page == "Vehicle & Rating Insights":

    st.title("Vehicle & Rating Insights")

    col6, col7 = st.columns(2)

    with col6:

        st.subheader("Top Vehicle Types by Ride Distance")

        vehicle = df.groupby("Vehicle_Type")["Ride_Distance"].sum().reset_index()

        fig4 = px.bar(
            vehicle,
            x="Vehicle_Type",
            y="Ride_Distance",
            color="Vehicle_Type"
        )

        st.plotly_chart(fig4, use_container_width=True)

    with col7:

        st.subheader("Ride Distance Distribution")

        fig5 = px.histogram(
            df,
            x="Ride_Distance",
            nbins=30
        )

        st.plotly_chart(fig5, use_container_width=True)

    col8, col9 = st.columns(2)

    with col8:

        st.subheader("Driver vs Customer Ratings")

        fig6 = px.scatter(
            df,
            x="Driver_Ratings",
            y="Customer_Rating",
            size="Booking_Value",
            color="Vehicle_Type"
        )

        st.plotly_chart(fig6, use_container_width=True)

    with col9:

        st.subheader("Driver Rating Distribution")

        rating = df.groupby("Driver_Ratings")["Booking_ID"].count().reset_index()

        fig7 = px.bar(
            rating,
            x="Driver_Ratings",
            y="Booking_ID"
        )

        st.plotly_chart(fig7, use_container_width=True)
