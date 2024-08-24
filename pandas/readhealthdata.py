import pandas as pd
import numpy as d
import csv
heath_data=pd.read_csv("Health_and_Lifestyle.csv")

print(heath_data['Person ID'][:10])
heath_data['Person ID'][7]='8'
# print(heath_data['Person ID'][:10])
data={"Person ID":heath_data['Person ID'],'Gender':heath_data['Gender']}
new_data=pd.DataFrame(
    data=data
)
heath_data=heath_data
with open("cleaned_data.csv","w") as file:
    file.write(str(new_data))
    