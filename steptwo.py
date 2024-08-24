import pandas as pd

data_view=pd.read_csv("Health_and_Lifestyle.csv")
print(data_view['Occupation'].value_counts())
print(data_view['Occupation'].value_counts().median())

