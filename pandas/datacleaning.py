import pandas as pd
import numpy as d
import csv
heath_data=pd.read_csv("Health_and_Lifestyle.csv")
# fixing issues of null values
null_values=heath_data['Sleep Disorder'][8:12]
# before cleaning
print(null_values)
# updated
updated_values=null_values.fillna("Normal")
print(updated_values)

