import pandas as pd

myseries = pd.Series([1, 4, 6, 6, 6, 11, 11, 24])

print(f"The mode of my series is {myseries.median()[0]}")