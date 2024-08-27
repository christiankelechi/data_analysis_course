import pandas as pd

airline_data=pd.read_csv("updateddoc_1.csv")

# print(airline_data.info())
# print(airline_data.describe())
# print(airline_data.dtypes())
# updatedmonth_data=airline_data['Flying_month'].fillna("Flying_month not indicated")
airline_data['Flying_month'][2796]='Invalid Date'
airline_data.to_csv("updateddoc_1.csv",index=False)


# print(health_data.shape())