import pandas as pd

def detect_outliers(data: pd.DataFrame):
  """ Detect outliers numeric and categorical columns.
    :param data: The input DataFrame.
    :return: A DataFrame with outliers marked as True and non-outliers as False.
  """
  col_numeric = data.select_dtypes(include="number").columns
  outliers_numeric = data[col_numeric].apply(detect_numeric)
  # Categorical columns
  col_categorical = data.select_dtypes(include=["object", "string", "category"]).columns
  max_unique = int(0.05 * len(data))
  outliers_categorical = data[col_categorical].apply(detect_categorical, max_unique=max_unique)
  return outliers_numeric, outliers_categorical


def detect_numeric(col: pd.Series) -> pd.Series:
  """ Detect outliers in a numeric column using the IQR method.
    :param col: The input Series representing a numeric column.
    :return: A Series with outliers marked as True and non-outliers as False.
  """
  Q25 = col.quantile(0.25)
  Q75 = col.quantile(0.75)
  iqr = Q75 - Q25
  lower_bound = Q25 - 1.5 * iqr
  upper_bound = Q75 + 1.5 * iqr
  outliers = (col < lower_bound) | (col > upper_bound)
  return outliers


def detect_categorical(col: pd.Series , max_unique: int) -> pd.Series:
  """ Detect outliers in a categorical column based on frequency.
    :param col: The input Series representing a categorical column.
    :return: A Series with outliers marked as True and non-outliers as False.
  """
  s = col.dropna()
  n = len(s)

  # Edge cases
  if n == 0:
    return pd.Series(False, index=col.index)

  nunique = s.nunique(dropna=True)
  unique_ratio = nunique / n

  # Skip high-cardinality columns (likely identifiers / free-text)
  if nunique > max_unique or unique_ratio > 0.3:
    return pd.Series(False, index=col.index)

  vc = s.value_counts(dropna=True)
  freq = vc / n

  rare_values = freq[freq < 0.01].index
  # also require small absolute count to avoid flagging common-but-slightly-below-threshold
  rare_values = [v for v in rare_values if vc[v] < 3]

  return col.isin(rare_values)