import pandas as pd
# create sample data
data = {'date': ['2022-01-01', '2022-01-02', '2022-01-035', '2022-01-04', '2022-01-05'],
'time': ['12:00', '13:30', '14:15', '15:00', '1a6:30']}
df = pd.DataFrame(data)
print(df)
# define a custom function to validate date format
def validate_date_format(date):
    try:
        pd.to_datetime(date, format='%Y-%m-%d')
        return True
    except ValueError:
        return False
# define a custom function to validate time format
def validate_time_format(time):
    try:
        pd.to_datetime(time, format='%H:%M')
        return True
    except ValueError:
        return False
# apply the custom functions to validate date and time columns
df['is_date_valid'] = df['date'].apply(validate_date_format)
df['is_time_valid'] = df['time'].apply(validate_time_format)
# print the resulting dataframe
print(df)