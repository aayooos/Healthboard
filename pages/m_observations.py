import streamlit as st 
import pandas as pd
import numpy as np
import gspread
from google.oauth2.service_account import Credentials
import plotly.express as px
from datetime import date, timedelta

scope = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_info(
    dict(st.secrets["gcp_service_account"]),
    scopes=scope
)
client = gspread.authorize(creds)
sheet_id = "1muLk82UaRmXLPyxSGlaD7U7EEKNoCJC0WapaqjeG5p0"
sheet = client.open_by_key(sheet_id)
worksheet = sheet.sheet1


records = worksheet.get_all_records()
df = pd.DataFrame(records)
df["bp_high"] = pd.to_numeric(df["bp_high"])
df["bp_low"] = pd.to_numeric(df["bp_low"])
df["sugar"] = pd.to_numeric(df["sugar"])
df["pulse"] = pd.to_numeric(df["pulse"])
df["oxygen"] = pd.to_numeric(df["oxygen"])
df["temperature"] = pd.to_numeric(df["temperature"])

st.title("Trends based on the collected data")

colf, colt = st.columns(2)
with colf:
    from_date = st.date_input("From date", value = date.today() - timedelta(days=30))
with colt:
    to_date = st.date_input("To date", value = df["date"].max())
df["date"] = pd.to_datetime(df["date"]).dt.date
df = df[(df["date"]>=from_date) & (df["date"]<=to_date)]

col1, col2 = st.columns(2)
with col1:
    fig = px.line(df, x="date", y="bp_high")
    st.plotly_chart(fig)
with col2:
    fig = px.line(df, x="date", y="bp_low")
    st.plotly_chart(fig)

col3, col4 = st.columns(2)
with col3:
    fig = px.line(df, x="date", y="oxygen")
    st.plotly_chart(fig)
with col4:
    fig = px.line(df, x="date", y="sugar")
    st.plotly_chart(fig)

col5, col6 = st.columns(2)
with col5:
    fig = px.line(df, x="date", y="temperature")
    st.plotly_chart(fig)
with col6:
    fig = px.scatter(df, x="date", y="swelling")
    st.plotly_chart(fig)

col7, = st.columns(1)
with col7:
    fig = px.line(df, x="date", y="pulse")
    st.plotly_chart(fig)


if(st.button("Click to view the full spreadsheet.")):
    st.dataframe(df)
