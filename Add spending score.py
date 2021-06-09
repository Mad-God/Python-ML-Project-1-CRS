import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def ClusteringFunc():
	dataset = pd.read_csv(r'D:\Study Material\Project\Databases\Created\CustomerFinal.csv')
	X = dataset.iloc[:, [3, 4,5]].values
	from sklearn.cluster import KMeans
	wcss = []
	for i in range(1, 11):
	    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
	    kmeans.fit(X)
	    wcss.append(kmeans.inertia_)

	"""
	plt.plot(range(1, 11), wcss)
	plt.title('The Elbow Method')
	plt.xlabel('Number of clusters')
	plt.ylabel('WCSS')
	plt.show()
	"""
	print(X)
	kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
	y_kmeans = kmeans.fit_predict(X)

	print(y_kmeans)
	print(len(y_kmeans))
	print(dataset.describe())
	dataset["Cluster"] = y_kmeans
	cols = list(dataset.columns)
	dataset = dataset[[cols[1]]+[cols[0]]+[cols[-1]]+cols[2:-1]]
	print(dataset.head())
	dataset.to_csv("CustomerBetaFinal.csv", index =False)



ClusteringFunc()