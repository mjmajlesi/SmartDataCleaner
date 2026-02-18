import pandas as pd
import streamlit as st
import dateparser


def std_data_types(data: pd.DataFrame):
  """ Standardize data types in the DataFrame.

  :param data: The input DataFrame.
  :return: The DataFrame with standardized data types and the total percentage of data lost.
  """
  precent_lost = 0
  data = data.convert_dtypes()
  mixed_types = detect_mixed_types(data)
  for col, type_counts in mixed_types.items():
      dominant_type = max(type_counts, key=type_counts.get)
      if dominant_type in ["int" , "float" , "int64" , "float64"]:
          data[col] , percent_lost = clean_numeric_column(data[col])
          precent_lost += percent_lost
      elif dominant_type == "str":
        data[col] = data[col].astype("string")
      elif dominant_type == "bool":
        data[col] = clean_boolean_column(data[col])
      elif dominant_type == ["datetime" , "Timestamp"]:
        data[col] = data[col].apply(lambda x: convert_to_iso(str(x)))

  return data , precent_lost
  


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
  percent_lost = (col.dropna().size - numeric.count()) / col.size * 100

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

