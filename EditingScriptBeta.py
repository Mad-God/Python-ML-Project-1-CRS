import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'D:\Study Material\Project\Final Draft\New Customer.csv')






def NameSearch(name):
	global dataset
	x = max(dataset["CustomerID"])
	print("\nColumns:\n",list(dataset.columns),"\n")
	f = 0
	for i in range(x):
		f +=1
		n = dataset.iloc[i,1]
		if n.lower() == name.lower():
			print (dataset.iloc[i])
			r = dataset.iloc[i]
			return dict(r)

	if f >= x :
		print("not found")
		return -1


def IDSearch(name):
	global dataset
	x = max(dataset["CustomerID"])
	print("\nColumns:\n",list(dataset.columns),"\n")
	f = 0
	for i in range(x):
		f +=1
		n = dataset.iloc[i,0]
		n = str(n)
		if n.lower() == name.lower():
			print (dataset.iloc[i])
			r = dataset.iloc[i]
			return dict(r)

	if f >= x :
		print("not found")
		return -1



x = NameSearch("lulu")
print(x)
print(type(x))

x = dict(x)

for i in range(4):
	pass
	#print(x[i])
print((x))
