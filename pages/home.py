import streamlit as st

st.title("Welcome to the Health Dashboard")
st.text("This tool monitors daily health metrics for Ratan Lal Tiwari and Maya Tiwari.")
st.info("Please follow the instructions: \n" \
"1. Fill the data for both people in the respective tabs. Do not exchange the data.\n" \
"2. Do not forget to click submit after entering the data. \n" \
"3. The tool offers you to view the trends by clicking on the observations tab of the respective person.\n" \
"4. You can view the comments of each day directly by clicking on the comments tab of the respective person.")

st.divider()
st.caption("⚠️ Please enter data only once a day. This app is for personal health tracking only and is not a substitute for medical advice.")