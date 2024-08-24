import pandas as pd

data_view=pd.read_csv("Health_and_Lifestyle.csv")
print(data_view.loc[100:124,['Occupation','Gender']])
import math
