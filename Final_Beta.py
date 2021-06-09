import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r'D:\Study Material\Project\Databases\Created\CustomerBetaFinal.csv')







def SetClusterFunc(data):
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
  #print(X)
  kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
  y_kmeans = kmeans.fit_predict(X)
  l = []
  for x in data.values():
    l.append(x)
  x = kmeans.fit_predict([[l[3],l[4],l[5]],[43, 47, 91],[33, 75, 91],[23, 33, 55],[53, 47, 78]])

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














def AddCustomer():
  data = {}
  global dataset
  data["CustomerID"] = max(dataset["CustomerID"]) + 1
  print("\n\nCustomer's ID will be: {}".format(data["CustomerID"]))
  data["Name"] = input("Input Customer Name: ")
  data["Genre"] = input("Input Customer Gender: ")
  data["Age"] = int(input("Input Customer Age: "))
  data["Annual Income (k$)"] = int(input("Input Customer Estimated Salary: "))
  data["Spending Score (1-100)"] = int(input("Input Customer Spending Score: "))
  data["Cluster"] = SetClusterFunc(data)
  print("\nCustomer belongs to the Cluster: ", data["Cluster"])
  dataset = dataset.append(data, ignore_index = True)
  print(dataset.columns)
  dataset.to_csv("CustomerBetaFinal.csv")
  return data








# add basket items to basket optimisation table
def AddBasketData(bas):
  dataset = pd.read_csv(r'D:\Study Material\Project\Databases\ASSOCIATION-Market_Basket_Optimisation.csv',header = None)
  c = dataset.iloc[:,0]
  x = list(range(0,len(c)))
  dataset["Num"] = x

  cols = list(dataset.columns)
  dataset = dataset[[cols[-1]]+cols[1:-1]]


  c = dataset.iloc[:,0]
  
  dataset.at[len(c), 0] = len(c)
  for i in range(len(bas)):
    dataset["Num"] = len(c)
    dataset.at[len(c),i+1] = bas[i] 
  print(dataset)






# Get the data of a new basket's items
def AddBasket():
  item = ""
  basket = []
  while item != " ":
    item = input("Enter the Stock Item(enter single space to finsh): ")
    basket.append(item)
  basket.pop()
  AddBasketData(basket)
  return basket














print("Welcome...\n\nWould you like to:\n1. Input a New Data\n2. Present Data\n")
op = int(input("Enter the Operation: "))
while op not in [1,2]:
  print("Enter a valid Value:")
  op = int(input("Enter the Operation: "))


# Enter new data to tables
if op == 1:
  data = {}
  basket = []
  inp = int(input("\n\nDo you want to Enter Data for:\n1. Customer\n2. Basket Items  "))
  while inp not in [1,2,3]:
      print(r'\nEnter a valid Value')
      inp = int(input("Enter the Operation: "))
# take input for Customer Data
  if inp == 1:
    data = AddCustomer()

# take stock item input 
  elif inp == 2:
    basket = AddBasket()
  print("\n\nHere's the row that will be entered in Database: ")
  print(data)
  print(basket)





# present data
elif op ==2:
  print("1. Show the Items generally bought together\n2. ")
  




