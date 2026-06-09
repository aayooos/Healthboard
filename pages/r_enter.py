import streamlit as st 
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import date

scope = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_info(
    dict(st.secrets["gcp_service_account"]),
    scopes=scope
)
client = gspread.authorize(creds)
sheet_id = "1muLk82UaRmXLPyxSGlaD7U7EEKNoCJC0WapaqjeG5p0"
sheet = client.open_by_key(sheet_id)
worksheet = sheet.worksheet("Sheet2")

st.title("Maya Tiwari")

today = date.today()
st.write("Date: ", today.strftime("%d/%m/%y"))

col1, col2 = st.columns(2)
with col1:
    bpH = st.number_input("Enter the Systolic value: ", value=0)
with col2:
    bpL = st.number_input("Enter the Diastolic value: ", value=0)

oxy = st.number_input("Enter the oxygen value: ", value=0)
temp = st.number_input("Enter the temperature: ", value=0)
sugar = st.number_input("Enter the sugar value: ", value=0)
swelling = st.checkbox("Is there swelling?")
comment = st.text_input("Any other observations?")

data = [today.strftime("%Y-%m-%d"), bpH, bpL, sugar, oxy, temp, swelling, comment]

if st.button("Click to submit the data"):
    if bpH <= 0 or bpL <= 0 or oxy <= 0 or temp <= 0:
        st.error("All values must be greater than 0.")
    elif bpH > 300 or bpL > 200:
        st.error("BP values seem unrealistic. Please check.")
    elif oxy > 100:
        st.error("Oxygen cannot exceed 100%.")
    elif temp > 110 or temp < 80:
        st.error("Temperature seems unrealistic. Please check.")
    else:
        worksheet.append_row(data)
        st.toast("Data submitted successfully!", icon="🎉")