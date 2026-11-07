import streamlit as st

st.set_page_config(page_title="Hello World", layout="wide")

st.title("Hello world!")
st.write("Welcome to your Databricks app.")

count = st.slider("Number of bars", min_value=1, max_value=20, value=5)
st.bar_chart({"value": [2 ** n for n in range(count)]})
