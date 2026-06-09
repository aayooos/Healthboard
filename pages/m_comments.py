import streamlit as st 
import pandas as pd
import numpy as np
import gspread
from google.oauth2.service_account import Credentials
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
df["date"] = pd.to_datetime(df["date"])

colf, colt = st.columns(2)
with colf:
    from_date = st.date_input("From date", value = date.today()-timedelta(days=30))
with colt:
    to_date = st.date_input("To date", value = df["date"].max())
df["date"] = pd.to_datetime(df["date"]).dt.date
df = df[(df["date"]>=from_date) & (df["date"]<=to_date)]

comments_only = df[["date", "comments"]]
st.dataframe(comments_only)