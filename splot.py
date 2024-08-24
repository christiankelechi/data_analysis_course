import pandas as pd
import matplotlib.pyplot as plt

health = pd.read_csv("Health_and_Lifestyle.csv")

health.plot(kind="line",x='Occupation',y='Quality_of_Sleep',figsize = (10, 6),
    title = "Quality of sleep histogram",)
# print(health["Quality_of_Sleep"].plot(kind="hist"))
plt.savefig('abc.png')
