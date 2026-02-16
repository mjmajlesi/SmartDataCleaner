import seaborn as sns
import pandas as pd
import numpy as np


titanic = sns.load_dataset("titanic")

titanic.loc[23 , "embarked"] = " "
titanic.loc[45 , "embarked"] = "n/a"
titanic.loc[67 , "embarked"] = "?"
titanic["age"] = titanic["age"].astype("object")
titanic.loc[0, "age"] = "Unknown"
titanic.loc[1, "age"] = np.nan
titanic.loc[2, "age"] = "30.5"

titanic.to_csv("titanic.csv" , index=False)