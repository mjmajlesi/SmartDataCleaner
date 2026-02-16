import pandas as pd
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



def missing_hidden_values(data : pd.DataFrame) -> pd.DataFrame:
  """ Detect hidden missing values in the DataFrame and replace them with pd.NA.

  :param data: The input DataFrame.
  :return: The DataFrame with hidden missing values replaced by pd.NA.
  """
  missing = ["?", "n/a", "na", "null", "none", "-", "--", " ", "" , "-1", "undefined" , "unknown" , "missing"]
  for val in data.columns:
    if data[val].dtype == "object": # only srtings
      value_counts = data[val].value_counts(dropna=False)
      for value in missing:
        if value in value_counts.index:
          st.write(f"Column '{val}' has {value_counts[value]} hidden missing values represented as '{value}'.")
          data[val] = data[val].replace(value , pd.NA)

  missing_table = missing_values(data)
  return missing_table


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

def impute_missing_value(data: pd.DataFrame):
  """ Impute missing values using KNN imputation.

  :param data: The input DataFrame.
  :return: The DataFrame with imputed missing values.
  """
  imputer = KNNImputer(n_neighbors=5)
  data_imputed = pd.DataFrame(
    imputer.fit_transform(data) , columns=data.columns , index=data.index
  )
  return data_imputed
  

  