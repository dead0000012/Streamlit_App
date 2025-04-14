import streamlit as st

st.title("My Streamlit App")
cal1, cal2 = st.columns(2)
a = cal1.number_input("", min_value=0.0, value=1.0)
rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.70}
currency = cal2.selectbox("Валюта", list(rates))
st.success(f"{a* rates[currency]:,.2f} UZS")