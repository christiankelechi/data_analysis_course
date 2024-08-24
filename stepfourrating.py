import pandas as pd

data_view=pd.read_csv("Health_and_Lifestyle.csv")
print(data_view['Quality_of_Sleep'])
dataa=data_view.query('Quality_of_Sleep>=6')
print(dataa['Quality_of_Sleep'])
