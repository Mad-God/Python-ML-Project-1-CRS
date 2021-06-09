import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'D:/Study Material/Project/Final Draft/New Customer.csv')





def TakeCustomerGui(data):
  global dataset
  data["CustomerID"] = max(dataset["CustomerID"]) + 1
  if data["Genre"][0].lower() == "m":
    data["Genre"] = 1
  elif data["Genre"][0].lower() == "f":
    data["Genre"] = 0
  else: 
    print("Non-Binary Gender was given...")
    data["Genre"] = 0
  data["Cluster"] = AssignClusterFunc(data)
  print("\nCustomer belongs to the Cluster: ", data["Cluster"])
  dataset = dataset.append(data, ignore_index = True)
  #print(list(dataset["Cluster"]))
  dataset.to_csv(r"D:\Study Material\Project\Final Draft\New Customer.csv", index = False)
  print(data)
  return data








def TakeCustomer():
  data = {}
  global dataset
  data["CustomerID"] = max(dataset["CustomerID"]) + 1
  print("\n\nCustomer's ID will be: {}".format(data["CustomerID"]))
  data["Name"] = input("Input Customer Name: ")
  
  data["Genre"] = input("Input Customer Gender: ")
  if data["Genre"][0].lower() == "m":
    data["Genre"] = 1
  elif data["Genre"][0].lower() == "f":
    data["Genre"] = 0
  else: 
    print("Non-Binary Gender was given...")
    data["Genre"] = 0
  
  data["Age"] = int(input("Input Customer Age: "))
  data["Annual Income (k$)"] = int(input("Input Customer Estimated Salary: "))
  data["Spending Score (1-100)"] = int(input("Input Customer Spending Score: "))
  data["Cluster"] = AssignClusterFunc(data)
  print("\nCustomer belongs to the Cluster: ", data["Cluster"])
  dataset = dataset.append(data, ignore_index = True)
  #print(list(dataset["Cluster"]))
  dataset.to_csv(r"D:\Study Material\Project\Final Draft\New Customer.csv", index = False)
  return data



def AssignClusterFunc(data):
  dataset = pd.read_csv(r'D:\Study Material\Project\Final Draft\New Customer.csv')
  X = dataset.iloc[:, 2:].values  

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
  l = [data["Genre"], data["Age"], data["Annual Income (k$)"], data["Spending Score (1-100)"]]
  print(l,"\n\n\n")
  x = kmeans.fit_predict([l, [23,88,56,32], [23,45,26,32], [23,45,56,67], [23,45,56,32]])


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










# Get the data of a new basket's items
def TakeBasket():
  item = ""
  basket = []
  while item != " ":
    item = input("Enter the Stock Item(enter single space to finsh): ")
    item = item.lower()
    basket.append(item)
  basket.pop()
  SaveBasketData(basket)
  return basket




# add basket items to basket optimisation table
def SaveBasketData(bas):
  dataset = pd.read_csv("D:\Study Material\Project\Final Draft\Market_Basket.csv",header = None)
  c = dataset.iloc[:,0]
  x = list(range(0,len(c)))
  for i in range(len(bas)):
    dataset.at[len(c),i] = bas[i] 
  dataset.to_csv("D:\Study Material\Project\Final Draft\Market_Basket.csv", index = False, header = None)






