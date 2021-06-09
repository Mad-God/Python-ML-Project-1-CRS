import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv(r'D:\Study Material\Project\Databases\Created\CustomerFinal.csv')

def ClusteringFunc(dataksdjb):
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
	#print(X)
	kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
	y_kmeans = kmeans.fit_predict(X)

	print(y_kmeans)
	print("\n\n\n\n")
	l = []
	for x in dat.values():
		l.append(x)
	x = kmeans.fit_predict([[l[3],l[4],l[5]],[43, 47, 91],[33, 75, 91],[23, 33, 55],[53, 47, 78]])
	print("\n\n\n\n")
	print("jhbdsfjbjhasdf")
	print(x[0])
	return x[0]



	"""
	plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
	plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
	plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
	plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
	plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
	plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
	plt.title('Clusters of customers')
	plt.xlabel('Annual Income (k$)')
	plt.ylabel('Spending Score (1-100)')
	plt.legend()
	plt.show()

	"""
dat = {"n":"Sys", "id":123,"genre": "f", "age":"34", "sal":"50", "score":"49"}
dev = ClusteringFunc(dat)