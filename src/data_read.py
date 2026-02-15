# read and load data
import pandas as pd

def read_data(file_path : str) -> pd.DataFrame:
  """ Read data from a file and return a DataFrame.

  :param file_path: The path to the file to be read.
  :return: The loaded DataFrame.
  """
  file_path = file_path.lower()
  if file_path.endswith(".csv"):
    data = pd.read_csv(file_path)
  elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
    data = pd.read_excel(file_path)
  elif file_path.endswith(".json"):
    data = pd.read_json(file_path)
  elif file_path.endswith(".txt"):
    data = pd.read_csv(file_path, delimiter="\t")
  else:
    raise ValueError("Unsupported file type. Please provide a csv, excel, json, or txt file.")
  return data
