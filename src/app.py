import streamlit as st
import pandas as pd
from data_read import read_data
from show_details import std_data , missing_hidden_values

st.set_page_config(page_title="SmartDataCleaner", layout="wide")
st.title("SmartDataCleaner")

uploaded = st.file_uploader("Upload your dataset", type=["csv", "xlsx", "xls", "json", "txt"])

if uploaded:
    # ذخیره فایل آپلود شده
    with open(uploaded.name, "wb") as f:
        f.write(uploaded.getbuffer())

    df = read_data(uploaded.name)
    df = std_data(df)

    st.subheader("Preview")
    st.dataframe(df.head(20), use_container_width=True)

    st.subheader("Missing Values")
    missing_table = missing_hidden_values(df)
    st.dataframe(missing_table, use_container_width=True)


