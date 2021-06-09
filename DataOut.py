import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(r'D:\Study Material\Project\Final Draft\New Customer.csv')


def AllCustomers():
	global dataset
	x = max(dataset["CustomerID"])
	print("\nColumns:\n",list(dataset.columns),"\n")
	for i in range(x):
		print(list(dataset.iloc[i]))
	print (x, "Rows were printed.")



def ClusterCustomers(i):
	global dataset
	x = max(dataset["CustomerID"])
	print("\nColumns:")
	print(list(dataset.columns),"\n")
	a = 0
	for j in range(x):
		if dataset.iloc[j,2] == i:
			print(list(dataset.iloc[j]))
			a = a+1
	print("\n",a, " Rows were printed.")






def Order(i):
	global dataset
	df = dataset.sort_values("Spending Score (1-100)", ascending = bool(i))
	x = max(dataset["CustomerID"])
	print("\nColumns:\n",list(dataset.columns),"\n")
	for i in range(x):
		print(list(df.iloc[i]))
	print (x, "Rows were printed.")



