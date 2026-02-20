import streamlit as st
import pandas as pd
from data_read import read_data
from data_analyst import std_data , missing_hidden_values , drop_missing_values  , impute_dataframe
from clean_dtype import std_data_types , detect_mixed_types
from data_outlier import detect_outliers
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
        st.info(mixed_types if mixed_types else "No mixed data types detected. and all columns have consistent data types.")
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
        st.info("No columns or rows were dropped. All columns and rows have less than 90% missing values.")

    
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
        st.subheader("Imputation Summary")
        col11, col12, col13 = st.columns(3)
        with col11:
            total_missing_before = df.isnull().sum().sum()
            st.metric("Total Missing Before", int(total_missing_before))
            total_values_before = df.shape[0] * df.shape[1]
            st.metric("Total Values", int(total_values_before))
        with col12:
            total_missing_after = imputed.isnull().sum().sum()
            st.metric("Total Missing After", int(total_missing_after))
        with col13:
            imputed_count = total_missing_before - total_missing_after
            st.metric("Values Imputed", int(imputed_count))
            imputation_percentage = (imputed_count / total_values_before * 100) if total_values_before > 0 else 0
            st.metric("Imputation Percentage", f"{imputation_percentage:.2f}%")
    
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

    
    # Outlier Detection ----------------------------------------------------
    out_num, out_cat = detect_outliers(df)


    st.subheader("Outlier Detection Summary")
    num_summary = out_num.sum().sort_values(ascending=False)
    cat_summary = out_cat.sum().sort_values(ascending=False)
    num_precent = (num_summary / len(df) * 100).round(2)
    cat_precent = (cat_summary / len(df) * 100).round(2)

    col1, col2 = st.columns(2)
    with col1:
        st.write("Numeric outliers (IQR) — count per column")
        st.dataframe(num_summary.rename("outlier_count").to_frame().assign(percent=num_precent), use_container_width=True)

    with col2:
        st.write("Categorical outliers (rare categories) — count per column")
        st.dataframe(cat_summary.rename("outlier_count").to_frame().assign(percent=cat_precent), use_container_width=True)


    st.subheader("Numeric Outliers(IQR) — Scatter Plot")

    num_cols = df.select_dtypes(include="number").columns.tolist()
    if not num_cols:
        st.info("No numeric columns found.")
    else:
        col = st.selectbox("Select column", num_cols)

    plot_df = df[[col]].copy()
    plot_df["index"] = df.index
    plot_df["Outlier"] = out_num[col].map({True: "Outlier", False: "Normal"})

    fig, ax = plt.subplots(figsize=(12, 4))

    sns.scatterplot(
        data=plot_df,
        x="index",
        y=col,
        hue="Outlier",
        palette={"Normal": "steelblue", "Outlier": "red"},
        ax=ax
    )
    ax.set_title(f"Outlier Detection — {col} (IQR)")
    ax.set_xlabel("Row Index")
    st.pyplot(fig)


    st.subheader("Categorical Outlier(Rare categories)")
    if not cat_summary.any():
        st.info("No rare categories detected.")
    else:
        st.dataframe(cat_summary[cat_summary > 0])  # Show only columns with rare categories







