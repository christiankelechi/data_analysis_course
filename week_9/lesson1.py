import pandas as pd

data=pd.read_csv("week_9/Airline_Review.csv")
# before
item_list=[]
# print(data)
for i in data['Rating'][:10]:
    try:
        i=float(i)
    except:
        i=1.9
    item_list.append(i)

data=pd.DataFrame(data={'Rating':item_list})
data.to_csv("ratingcolumn.csv",index=True)
        