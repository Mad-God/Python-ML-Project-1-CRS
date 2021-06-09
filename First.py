import pandas as pd
df = pd.read_csv(r'D:\Study Material\Project\Databases\Created\Mall_Customers_3.csv')
names = pd.read_csv(r"D:\Study Material\Project\Databases\Downloaded\NationalNames.csv")

fn = names.loc[(names["Gender"] == "F") & (names["Id"] <= 112)]
mn = names.loc[(names["Gender"] == "M")].head(88)
fn = fn["Name"]
mn = mn["Name"]

n = list(fn) + list(mn)

len(n)

import random
random.shuffle(n)
df["Name"] = n

cols = list(df.columns)
cols
cols[0:-1]	
df = df[[cols[-1]]+ cols[0:-1]]


print(df.head(20))

print(df.describe())

df.to_csv("WithNames.csv", index = False)






