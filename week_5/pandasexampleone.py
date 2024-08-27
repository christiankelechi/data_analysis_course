import pandas as pd
df = pd.DataFrame({
'Name': ['John', 'Jane', 'Adam', 'Ava'],
'Age': [25, 30, 28, 24],
'Salary': [50000.00, 60000.00, 55000.00, 45000.00]
})
print(df)
# check data types of columns
print(df.dtypes)

def check_datatype(value):
    if isinstance(value, str):
        return 'string'
    elif isinstance(value, int):
        return 'integer'
    elif isinstance(value, float):
        return 'float'
    else:
        return 'other'
    # apply function to each column of data frame
    for col in df.columns:
        print(col, df[col].apply(check_datatype))
        # check data type of a single value
        value = 'Hello'
        print(type(value))
        print(isinstance(value, str))
        print(issubclass(str, object))