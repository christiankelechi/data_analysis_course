import pandas as pd

health_data=pd.read_csv("Health_and_Lifestyle.csv")

print(health_data.describe())
# print(health_data.shape())