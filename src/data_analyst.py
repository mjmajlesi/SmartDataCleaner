import pandas as pd
import numpy as np
import streamlit as st
from sklearn.impute import KNNImputer

def std_data(data : pd.DataFrame) -> pd.DataFrame:
  data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("(", "").str.replace(")", "")
  data.index = data.index + 1 # start by 1
  return data





def missing_values(data : pd.DataFrame) -> pd.DataFrame:
  """ count and concat the missing values with missing percent value and return dataframe

  :param data: The input DataFrame.
  :return: The missing values table.
  """
  # show missing values by column
  missing_count = data.isnull().sum()
  missing_precent = (missing_count / len(data)) * 100
  missing_table = pd.concat(
    [missing_count , missing_precent] , 
    axis=1 ,
    keys=["Missing Count", "Missing Percent"]
  )
  return missing_table



def missing_hidden_values(data: pd.DataFrame):
    data = data.copy()
    missing_tokens = {"?", "n/a", "na", "null", "none", "-", "--", "", " ", "-1",
                      "undefined", "unknown", "Unknown", "missing"}

    # روی object + string + category کار کن (نه فقط object)
    for col in data.columns:
        if pd.api.types.is_object_dtype(data[col]) or pd.api.types.is_string_dtype(data[col]) or pd.api.types.is_categorical_dtype(data[col]):
            s = data[col].astype("string")
            # normalize برای اینکه " None " هم بگیرد
            s_norm = s.str.strip().str.lower()
            data[col] = s.mask(s_norm.isin({x.lower() for x in missing_tokens}), pd.NA)

    missing_table = missing_values(data)
    return data, missing_table



def drop_missing_values(data: pd.DataFrame):
  """ Drop rows and columns with 90% or more missing values.

  :param data: The input DataFrame.
  :return: The cleaned DataFrame and the list of dropped columns and rows.
  """
  col = data.isna().mean(axis=0) # drop columns
  data = data.loc[:, col < 0.9]
  
  dropped_cols = col[col >= 0.9].index.tolist()

  row = data.isna().mean(axis=1) # drop rows
  data = data.loc[row < 0.9]
  
  dropped_rows = row[row >= 0.9].index.tolist()
  
  return data , dropped_cols , dropped_rows
  

def impute_dataframe(data: pd.DataFrame) -> pd.DataFrame:
  """Impute missing values in a DataFrame using KNN imputation.

  :param data: The input DataFrame.
  :return: The DataFrame with imputed missing values.
  """
  data = data.copy()

  num_cols = data.select_dtypes(include="number").columns
  cat_cols = data.select_dtypes(include=["object", "string", "category"]).columns
  date_cols = data.select_dtypes(include="datetime").columns

  imputer = KNNImputer(n_neighbors=5)

  if len(num_cols) > 0:
    data[num_cols] = imputer.fit_transform(data[num_cols]) # KNN imputation

  for col in cat_cols:
    if data[col].isna().any():
      data[col] = data[col].fillna(data[col].mode()[0]) # Mode imputation

  for col in date_cols:
    data[col] = data[col].fillna(method="ffill") # Forward fill 

  return data , num_cols



# Correlation Analysis
def detect_correlation(data: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    """Return numeric feature pairs with high absolute correlation.

    :param data: Input DataFrame.
    :param threshold: Keep pairs with absolute correlation greater than this value.
    :param method: Correlation method accepted by ``DataFrame.corr``.
    :return: DataFrame with columns ["Feature 1", "Feature 2", "Correlation"].
    """
    numeric_data = data.select_dtypes(include="number")
    columns = ["Feature 1", "Feature 2", "Correlation"]

    if numeric_data.shape[1] < 2:
        return pd.DataFrame(columns=columns)

    corr_matrix = numeric_data.corr(method="pearson").abs()
    upper_triangle = corr_matrix.where(np.triu(np.ones(corr_matrix.shape, dtype=bool), k=1))

    pairs = upper_triangle.stack().reset_index(name="Correlation")
    pairs.columns = columns

    result = pairs[pairs["Correlation"] > threshold]
    return result.sort_values("Correlation", ascending=False).reset_index(drop=True)


def remove_highly_correlated(data: pd.DataFrame, threshold: float = 0.95):
  """ Remove one of each pair of highly correlated numeric features.
    :param data: The input DataFrame.
    :param threshold: The correlation threshold above which to remove one of the features.
    :return: The DataFrame with highly correlated features removed and the list of dropped features.
  """
  numeric_data = data.select_dtypes(include="number")
  corr_matrix = numeric_data.corr().abs()

  upper = corr_matrix.where(
    np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
  )

  to_drop = [column for column in upper.columns if any(upper[column] > threshold)]

  return data.drop(columns=to_drop), to_drop
