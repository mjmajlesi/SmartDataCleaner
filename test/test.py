import seaborn as sns
import pandas as pd


titanic = sns.load_dataset("titanic")

titanic.loc[23 , "embarked"] = " "
titanic.loc[45 , "embarked"] = "n/a"
titanic.loc[67 , "embarked"] = "?"

titanic.to_csv("titanic.csv" , index=False)