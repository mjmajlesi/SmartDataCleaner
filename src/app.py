import streamlit as st
import pandas as pd
from data_read import read_data
from data_analyst import std_data , missing_hidden_values , drop_missing_values  , impute_dataframe
from clean_dtype import std_data_types , detect_mixed_types
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns


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

    st.subheader("Data Types")
    col1 , col2 = st.columns(2)
    with col1:
        st.subheader("Mixed data:")
        mixed_types = detect_mixed_types(df)
        st.write(mixed_types if mixed_types else "No mixed data types detected. and all columns have consistent data types.")
    with col2:
        st.subheader("Cleaned Data Types")
        df , percent_lost = std_data_types(df)
        st.dataframe(df.dtypes, use_container_width=True)
        if percent_lost > 0:
            st.warning(f"Warning: {percent_lost:.2f}% of the data was lost during type conversion.")


    st.subheader("Missing Values")
    col1 , col2 = st.columns([2 , 3])

    with col1:
        st.subheader("Missing Values Table")
        df, missing_table = missing_hidden_values(df)
        st.dataframe(missing_table, use_container_width=True)
    with col2:
        st.subheader("Missing Values Visualization")
        fig, ax = plt.subplots(figsize=(10, 4))
        msno.matrix(df, ax=ax, fontsize=10)
        st.pyplot(fig)

    st.subheader("Clean missing values")
    col1 , col2 = st.columns(2)

    
    st.subheader("Drop rows and columns with 90% or more missing values")
    df , dropped_cols , dropped_rows = drop_missing_values(df)
    if dropped_cols or dropped_rows:
        st.write(f"Dropped columns: {', '.join(dropped_cols)}")
        st.write(f"Dropped rows: {', '.join(map(str, dropped_rows))}")
        st.write("Cleaned Data Preview")
        fig, ax = plt.subplots(figsize=(10, 4))
        msno.matrix(df, ax=ax, fontsize=10)
        st.pyplot(fig)
    else:
        st.write("No columns or rows were dropped. All columns and rows have less than 90% missing values.")

    
    st.subheader("fill missing values with KNN imputation and mode imputation")
    imputed , knn_cols = impute_dataframe(df)
    
    col1, col2 = st.columns(2)
    
    missing_before = df.isnull().sum()
    missing_after = imputed.isnull().sum()
    
    comparison_data = pd.DataFrame({
        'Column': missing_before.index,
        'Missing Before': missing_before.values,
        'Missing After': missing_after.values
    })
    
    with col1:
        st.subheader("Missing Values Comparison Table")
        st.dataframe(comparison_data, use_container_width=True)
    
    with col2:
        st.subheader("Imputation — (Before vs After)")
        selected_col = st.selectbox("Select a column to visualize imputation effect", df.columns)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        sns.histplot(df[selected_col] , kde=True, ax=ax1 , color='blue')
        sns.histplot(imputed[selected_col] , ax=ax2, kde=True, color='green')
        ax1.set_title("Missing Values Before Imputation")
        ax2.set_title("Missing Values After Imputation")
        plt.tight_layout()
        st.pyplot(fig)

