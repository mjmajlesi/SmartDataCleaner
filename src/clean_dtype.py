import pandas as pd
import streamlit as st
import dateparser


def std_data_types(data: pd.DataFrame):
  """ Standardize data types in the DataFrame.

  :param data: The input DataFrame.
  :return: The DataFrame with standardized data types and the total percentage of data lost.
  """
  precent_lost_mix = 0
  data = data.convert_dtypes()
  mixed_types = detect_mixed_types(data)

  for col, type_counts in mixed_types.items():
    dominant_type = max(type_counts, key=type_counts.get)

    if dominant_type in ["int", "float", "int64", "float64"]:
      data[col], precent_lost_mix = clean_numeric_column(data[col])

    elif dominant_type == "str":
      data[col] = data[col].astype("string")

    elif dominant_type == "bool":
      data[col] = clean_boolean_column(data[col])

    elif dominant_type in ["datetime", "Timestamp"]:
      data[col] = pd.to_datetime(data[col], errors="coerce")

  data_cleaned = detect_dtypes(data)

  return data_cleaned, precent_lost_mix
  


def detect_mixed_types(data: pd.DataFrame) -> dict:
  """ Detect columns with mixed data types in the DataFrame.
  :param data: The input DataFrame.
  :return: A dictionary with columns that have mixed data types and their respective type counts.
  """
  mixed_types = {}
  for column in data.columns:
      types = data[column].apply(lambda v: type(v).__name__).value_counts()
      if len(types) > 1:
          mixed_types[column] = types.to_dict()
  return mixed_types


def clean_numeric_column(col: pd.Series):
  """ Clean a numeric column by converting non-numeric values to NaN.

  :param col: The input Series representing a numeric column.
  :return: The cleaned Series with non-numeric values converted to NaN.
  """
  numeric = pd.to_numeric(col, errors='coerce')
  # Check what percentage of data was lost
  precent_lost = (numeric.isna().sum() / len(col)) * 100

  return numeric , percent_lost

def clean_boolean_column(col: pd.Series):
    # Define values to be considered as True
    true_values = [True, "True", "true", "YES", "yes", "Y", "y", 1]
    cleaned_col = col.isin(true_values)

    print(f"Unique values: {cleaned_col.unique()}")
    return cleaned_col



def convert_to_iso(date_string):
    # Parse the date string
    parsed_date = dateparser.parse(date_string)

    if parsed_date is None:
        return "Invalid date format"

    # Convert to ISO format
    iso_date = parsed_date.isoformat()

    return iso_date


def detect_dtypes(data: pd.DataFrame) -> pd.DataFrame:
  """ Detect and standardize data types in the DataFrame.
  :param data: The input DataFrame.
  :return: The DataFrame with standardized data types.
  """
  for col in data.columns:
    if data[col].dtype in ["object", "string"]:
      # 1) numeric test
      num_try = pd.to_numeric(data[col], errors="coerce")
      if num_try.notna().median() > 0.9:
        data[col] = num_try
        continue

      # 2) datetime test
      dt_try = pd.to_datetime(data[col], errors="coerce")
      if dt_try.notna().mean() > 0.9:
        data[col] = dt_try
        continue

      # 3) boolean test
      if set(data[col].dropna().unique()).issubset({"True","False","true","false",1,0}):
        data[col] = data[col].astype("bool")
        continue

      # 4) else → categorical
      data[col] = data[col].astype("string")
  return data