from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import DataIn as DI
from InputValidation import InputValidation as InpVal
import DataOut as DO
import StockOut as SO




root = Tk()
root.title("Customer Recommendation System")
root.iconbitmap("D:/Study Material/Project/Final Draft/custom.ico")

FrontPage = LabelFrame(root)



def onClick(frame):
    label = Label(frame,text = "Some button was clicked",padx = 30, background = "Black",pady = 30)
    label.grid(row = 30, column = 0, columnspan = 2)
    # simple print() will print the text on the console 
    # instead of the root widget window 


def RemoveFrame(frame, Frame):
	Frame.grid()
	frame.grid_forget()









def InputCustomerFrame():
	FrontPage.grid_forget()


	def SubmitButton():
		if NameInp.get() == " ":
				ErrorLabel = Label(Inpframe, text = "Enter required fields' values.",fg = "red", pady = 20)
				ErrorLabel.grid(row = 5, column = 0, columnspan = 2)
				return
		data = {}
		data["Name"] = NameInp.get()
		data["Age"] = AgeInp.get()
		data["Annual Income (k$)"] = SalaryInp.get()
		data["Genre"] = GenderInp.get()
		data["Spending Score (1-100)"] = ScoreInp.get()
		print( data)	
		data = DI.TakeCustomerGui(data)
		cstr = str(data["Cluster"])
		csnm = str(data["Name"])
		msg = csnm+" belonged to Cluster " + cstr
		print(msg)
		ClusterLabel = Label(Inpframe, text = msg)
		ClusterLabel.grid(row = 8)		
		GenderInp.delete(0,END)
		NameInp.delete(0,END)
		SalaryInp.delete(0,END)
		AgeInp.delete(0,END)
		ScoreInp.delete(0,END)


	# create the frame
	global Inpframe
	Inpframe = LabelFrame(root, text = "Input Customer Data here:", padx = 120, pady = 50, bd = 3, relief = SUNKEN)
	
	ExitButton = Button(Inpframe, text= "Back", padx= 20,pady = 10, fg= "Red", command =lambda: RemoveFrame(Inpframe, FrontPage))
	SubmitButton = Button(Inpframe, text= "Submit", padx= 20,pady = 10, fg= "Red", command =SubmitButton)


	NameLabel = Label(Inpframe, text = "Name:", pady = 20)
	NameInp = Entry(Inpframe, width = 40, borderwidth= 3)
	NameInp.insert(10, " ")

	AgeLabel = Label(Inpframe, text = "Age:", pady = 20)
	AgeInp = Entry(Inpframe, width = 40, borderwidth= 3)
	AgeInp.insert(10, " ")


	SalaryLabel = Label(Inpframe, text = "Salary:", pady = 20)
	SalaryInp = Entry(Inpframe, width = 40, borderwidth= 3)
	SalaryInp.insert(10, " ")


	GenderLabel = Label(Inpframe, text = "Gender:", pady = 20)
	GenderInp = Entry(Inpframe, width = 40, borderwidth= 3)
	GenderInp.insert(10, " ")



	ScoreLabel = Label(Inpframe, text = "Spending Socre(1-100):", pady = 20)
	ScoreInp = Entry(Inpframe, width = 40, borderwidth= 3)
	ScoreInp.insert(10, " ")


	
	# show the InpFrame widgets
	NameLabel.grid(row = 0, column = 0)
	NameInp.grid(row = 0, column = 1)
	AgeLabel.grid(row = 1, column = 0)
	AgeInp.grid(row = 1, column = 1)
	SalaryLabel.grid(row = 2, column = 0)
	SalaryInp.grid(row = 2, column = 1)
	GenderLabel.grid(row = 3, column = 0)
	GenderInp.grid(row = 3, column = 1)
	ScoreLabel.grid(row = 4, column = 0)
	ScoreInp.grid(row = 4, column = 1)
	



	#show the frame
	Inpframe.grid(row = 10, column = 0, columnspan = 2, pady = 40)
	ExitButton.grid(row = 10, column = 1)
	SubmitButton.grid(row = 10, column = 0,padx = 30)

i = 0

def InputBasketFrame():
	FrontPage.grid_forget()
	basket = []

	def AddButtonFun():
		global i
		x = ItemInp.get().lower()
		basket.append(x)
		print(basket)	
		CurrentItemLabel = Label(Inpframe, text = ItemInp.get(), pady = 20)
		CurrentItemLabel.grid(row = 11+i, column = 0)
		i+=1
		ItemInp.delete(0,END)


	def SubmitButtonFun():
		AddButtonFun()
		DI.SaveBasketData(basket)
		global i
		i= 0
		RemoveFrame(Inpframe, FrontPage)
		InputBasketFrame()




	# create the frame
	global Inpframe
	Inpframe = LabelFrame(root, text = "Input Basket Items here:", padx = 120, pady = 50, bd = 3, relief = SUNKEN)
	
	ExitButton = Button(Inpframe, text= "Finish", padx= 20,pady = 10, fg= "Red", command =lambda: RemoveFrame(Inpframe, FrontPage))
	AddButton = Button(Inpframe, text= "Add Item", padx= 20,pady = 10, fg= "Red", command =AddButtonFun)
	SubmitButton = Button(Inpframe, text= "Submit Basket", padx= 20,pady = 10, fg= "Red", command =SubmitButtonFun)


	ItemLabel = Label(Inpframe, text = "Enter Item:", pady = 20)
	ItemInp = Entry(Inpframe, width = 40, borderwidth= 3)
	ItemInp.insert(10, " ")




	# show the InpFrame widgets
	ItemLabel.grid(row = 0, column = 0)
	ItemInp.grid(row = 0, column = 1)
	


	#show the frame
	Inpframe.grid(row = 10, column = 0, columnspan = 2, pady = 40)
	ExitButton.grid(row = 10, column = 2)
	AddButton.grid(row = 10, column = 0,padx = 30)
	SubmitButton.grid(row = 10, column = 1,padx = 30)







def ShowCustomerFrameDisplay():
	FrontPage.grid_forget()
	ShowCustomerFrame = LabelFrame(root)
	ShowLabel = Label(ShowCustomerFrame, text= "Cutomer Data",font = ("Courier 14 bold"), padx= 20,
	                pady = 20, fg= "Red")

	InputLabel = Label(ShowCustomerFrame, text= "How do you want the Data to be Filtered? :", padx= 20,
	                pady = 20, fg= "Blue")


	#Functions
	def ClusterGraph():
		dataset = pd.read_csv('New Customer.csv')
		X = dataset.iloc[:, [2,3,4,5,6]].values

		from sklearn.cluster import KMeans
		wcss = []
		for i in range(1, 11):
		    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
		    kmeans.fit(X)
		    wcss.append(kmeans.inertia_)

		kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
		y_kmeans = kmeans.fit_predict(X)
		print(y_kmeans)

		plt.scatter(X[y_kmeans == 0, 3], X[y_kmeans == 0, 4], s = 100, c = 'red', label = 'Cluster 1')
		plt.scatter(X[y_kmeans == 1, 3], X[y_kmeans == 1, 4], s = 100, c = 'blue', label = 'Cluster 2')
		plt.scatter(X[y_kmeans == 2, 3], X[y_kmeans == 2, 4], s = 100, c = 'green', label = 'Cluster 3')
		plt.scatter(X[y_kmeans == 3, 3], X[y_kmeans == 3, 4], s = 100, c = 'cyan', label = 'Cluster 4')
		plt.scatter(X[y_kmeans == 4, 3], X[y_kmeans == 4, 4], s = 100, c = 'magenta', label = 'Cluster 5')
		plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
		plt.title('Clusters of customers')
		plt.xlabel('Annual Income (k$)')
		plt.ylabel('Spending Score (1-100)')
		plt.legend()
		plt.show()




	def ShowAllData():
		ShowCustomerFrame.grid_forget()
		dataset = pd.read_csv(r'D:\Study Material\Project\Final Draft\New Customer.csv')
		x = max(dataset["CustomerID"])

		OutputFrame = LabelFrame(root, text = "Output Window")
		print(list(dataset.columns))
		ItemFrame = LabelFrame(OutputFrame)

		#scroll = Scrollbar(OutputFrame, orient = 'vertical')
		#scroll.config(command = OutputFrame.xview)
		BackButton = Button(OutputFrame, text = "Back", command = lambda: RemoveFrame(OutputFrame, ShowCustomerFrame))
		BackButton.grid(row = 0, column = 0, padx = 7, pady = 7)


		HeadLable = Label(OutputFrame, text = "Showing ALL CUSTOMERS Data", relief = SUNKEN, border = 2, padx = 0, pady = 3, font = "BOLD 28")
		HeadLable.grid(row = 0, column = 1, padx = 7, pady = 7, columnspan = 20)



		coln = 0
		for i in list(dataset.columns):
			ColLable = Label(ItemFrame, text = str(i), relief = SUNKEN, border = 0, padx = 0, pady = 3, font = "BOLD")
			ColLable.grid(row = 1, column = coln, padx = 7, pady = 7)
			coln = coln + 1
		OutputFrame.grid()

		rown = 1
		count = 0
		for row in range(x):	
			if count < 30:
				count+=1
				for col in range(len(list(dataset.columns))):
					element = dataset.iloc[row,col]
					EleLabel = Label(ItemFrame, text = str(element),  relief = SUNKEN, border = 1, padx = 95)
					EleLabel.grid(row = row+2, column = col)
		ItemFrame.grid(columnspan = 6)
		BackButton = Button(OutputFrame, text = "Back", command = lambda: RemoveFrame(OutputFrame, ShowCustomerFrame))
		BackButton.grid(row = 3, column = 3, padx = 7, pady = 7)

	def GetCluster(): 
		GetClusterFrame = LabelFrame(ShowCustomerFrame, text = "Choose the Cluster")



		def ShowClusterCustomers(cls = 1):
			ShowCustomerFrame.grid_forget()
			dataset = pd.read_csv(r'D:\Study Material\Project\Final Draft\New Customer.csv')
			x = max(dataset["CustomerID"])
			OutputFrame = LabelFrame(root, text = "Output Window")



			BackButton = Button(OutputFrame, text = "Back", command = lambda: RemoveFrame(OutputFrame, ShowCustomerFrame))
			BackButton.grid(row = 0, column = 0, padx = 7, pady = 7)

			HeadLable = Label(OutputFrame, text = "Showing Cluster "+str(cls)+"  CUSTOMERS Data", relief = SUNKEN, border = 2, padx = 0, pady = 3, font = "BOLD 28")
			HeadLable.grid(row = 0, column = 1, padx = 7, pady = 7, columnspan = 20)




			coln = 0
			for i in list(dataset.columns):
				ColLable = Label(OutputFrame, text = str(i), relief = SUNKEN, border = 0, padx = 0, pady = 3, font = "BOLD")
				ColLable.grid(row = 1, column = coln, padx = 7, pady = 7)
				coln = coln + 1
			OutputFrame.grid(row = 0, pady = 30)
			rown = 1
			for col in range(len(list(dataset.columns))):
				for row in range(x):
					if dataset.iloc[row,2] == cls:
						element = dataset.iloc[row,col]
						EleLabel = Label(OutputFrame, text = str(element),  relief = SUNKEN, border = 1, padx = 95)
						EleLabel.grid(row = row+2, column = col)






		cls0 = Button(GetClusterFrame, text = "Cluster 0", command = lambda: ShowClusterCustomers(0))
		cls1 = Button(GetClusterFrame, text = "Cluster 1", command = lambda: ShowClusterCustomers(1))
		cls2 = Button(GetClusterFrame, text = "Cluster 2", command = lambda: ShowClusterCustomers(2))
		cls3 = Button(GetClusterFrame, text = "Cluster 3", command = lambda: ShowClusterCustomers(3))
		cls4 = Button(GetClusterFrame, text = "Cluster 4", command = lambda: ShowClusterCustomers(4))

		Head = Label(GetClusterFrame, text = "Choose which cluster data is to be shown: ")

		Head.grid(row = 0, column = 0, columnspan = 2)
		cls0.grid(row = 1, column = 0)
		cls1.grid(row = 2, column = 0)
		cls2.grid(row = 3, column = 0)
		cls3.grid(row = 1, column = 1)
		cls4.grid(row = 2, column = 1)
		GetClusterFrame.grid(row= 5)



	def GetOrder():
		GetOrderFrame = LabelFrame(ShowCustomerFrame, text = "Choose the type of Ordering: ")



		def ShowOrderedCustomers(cls = 1):
			ShowCustomerFrame.grid_forget()
			dataset = pd.read_csv(r'D:\Study Material\Project\Final Draft\New Customer.csv')
			OutputFrame = LabelFrame(root, text = "Output Window")



			BackButton = Button(OutputFrame, text = "Back", command = lambda: RemoveFrame(OutputFrame, ShowCustomerFrame))
			BackButton.grid(row = 0, column = 0, padx = 7, pady = 7)

			HeadLable = Label(OutputFrame, text = "Showing Customer in Order of Spending Score", relief = SUNKEN, border = 2, padx = 0, pady = 3, font = "BOLD 28")
			HeadLable.grid(row = 0, column = 1, padx = 7, pady = 7, columnspan = 20)




			coln = 0
			for i in list(dataset.columns):
				ColLable = Label(OutputFrame, text = str(i), relief = SUNKEN, border = 0, padx = 0, pady = 3, font = "BOLD")
				ColLable.grid(row = 1, column = coln, padx = 7, pady = 7)
				coln = coln + 1
			OutputFrame.grid(row = 0, pady = 30)
			rown = 1

			df = dataset.sort_values("Spending Score (1-100)", ascending = cls)
			x = max(dataset["CustomerID"])

			for col in range(len(list(df.columns))):
				for row in range(x):
					element = df.iloc[row,col]
					EleLabel = Label(OutputFrame, text = str(element),  relief = SUNKEN, border = 1, padx = 95)
					EleLabel.grid(row = row+2, column = col)





		ord0 = Button(GetOrderFrame, text = "Ascending Order", command = lambda: ShowOrderedCustomers(1))
		ord1 = Button(GetOrderFrame, text = "Descending Order", command = lambda: ShowOrderedCustomers(0))

		Head = Label(GetOrderFrame, text = "Choose in what Oreder Data is to be shown: ")

		Head.grid(row = 0, column = 0, columnspan = 2)
		ord0.grid(row = 1, column = 0)
		ord1.grid(row = 2, column = 0)
		GetOrderFrame.grid(row= 8)









	# Buttons
	AllCustomerButton = Button(ShowCustomerFrame, text = "All Customer Data", padx = 0, pady = 20, command = ShowAllData)
	ClusterCustomerButton = Button(ShowCustomerFrame, text = "Cluster Customer Data", padx = 0, pady = 20, command = GetCluster)
	SortedCustomerButton = Button(ShowCustomerFrame, text = "Sorted Customer Data", padx = 0, pady = 20, command =GetOrder)
	BackButton = Button(ShowCustomerFrame, text = "Go Back", padx = 0, pady = 20, command =lambda: RemoveFrame(ShowCustomerFrame, FrontPage))
	ClusterShowButton = Button(ShowCustomerFrame, text = "Show Graph of All Customers \nAccording to Clusters", command = ClusterGraph, pady = 30)





	# put Customer Display page on the screen
	ShowLabel.grid(row = 0, column = 0)
	InputLabel.grid(row = 1, column = 0)
	AllCustomerButton.grid(row = 2, column = 0, pady = 20)
	ClusterCustomerButton.grid(row = 3, column = 0, pady = 20)
	SortedCustomerButton.grid(row = 7, column = 0, pady = 20)
	
	ClusterShowButton.grid(row = 9, column = 0)
	BackButton.grid(row = 10, column = 0, pady = 20)
	ShowCustomerFrame.grid()
	



def ShowItemFrameDisplay():
	FrontPage.grid_forget()
	ShowItemFrame = LabelFrame(root)
	ShowLabel = Label(ShowItemFrame, text= "Stock Items Data",font = ("Courier 14 bold"), padx= 20,
	                pady = 20, fg= "Red")

	InputLabel = Label(ShowItemFrame, text= "How do you want the Data to be Filtered? :", padx= 20,
	                pady = 20, fg= "Blue")






	def GetOrder():
		GetOrderFrame = LabelFrame(ShowItemFrame, text = "Choose the type of Ordering: ")

		def SortedItems(ord):
			dataset = pd.read_csv("D:\Study Material\Project\Final Draft\Items Table.csv")
			dataset = dataset.sort_values("Rating", ascending = bool(ord))

			print("\nColumns:\n",list(dataset.columns),"\n")

			ShowItemFrame.grid_forget()
			x = dataset["Item"].count()

			OutputFrame = LabelFrame(root, text = "Output Window")
			print(list(dataset.columns))

			#scroll = Scrollbar(OutputFrame, orient = 'vertical')
			#scroll.config(command = OutputFrame.xview)
			BackButton = Button(OutputFrame, text = "Back", command = lambda: RemoveFrame(OutputFrame, ShowItemFrame))
			BackButton.grid(row = 0, column = 0)


			HeadLable = Label(OutputFrame, text = "Showing ALL Stock Items by Rating", relief = SUNKEN, border = 2, padx = 0, pady = 3, font = "BOLD 28")
			HeadLable.grid(row = 0, column = 1, padx = 7, pady = 7, columnspan = 2)



			coln = 0
			for i in list(dataset.columns):
				ColLable = Label(OutputFrame, text = str(i), relief = SUNKEN, border = 0, padx = 0, pady = 3, font = "BOLD")
				ColLable.grid(row = 1, column = coln, padx = 7, pady = 7)
				coln = coln + 1
			OutputFrame.grid()
			rown = 1
			for col in range(len(list(dataset.columns))):
				for row in range(x):
					element = dataset.iloc[row,col]
					EleLabel = Label(OutputFrame, text = str(element),  relief = SUNKEN, border = 1, padx =140)
					EleLabel.grid(row = row+2, column = col)






		ord0 = Button(GetOrderFrame, text = "Ascending Order", command = lambda: SortedItems(1))
		ord1 = Button(GetOrderFrame, text = "Descending Order", command = lambda: SortedItems(0))

		Head = Label(GetOrderFrame, text = "Choose in what Oreder Data is to be shown: ")

		Head.grid(row = 0, column = 0, columnspan = 2)
		ord0.grid(row = 1, column = 0)
		ord1.grid(row = 2, column = 0)
		GetOrderFrame.grid(row= 5)





	def AllItems():
		dataset = pd.read_csv("D:\Study Material\Project\Final Draft\Items Table.csv")
		print("\nColumns:\n",list(dataset.columns),"\n")

		ShowItemFrame.grid_forget()
		x = dataset["Item"].count()

		OutputFrame = LabelFrame(root, text = "Output Window")
		print(list(dataset.columns))

		#scroll = Scrollbar(OutputFrame, orient = 'vertical')
		#scroll.config(command = OutputFrame.xview)
		BackButton = Button(OutputFrame, text = "Back", command = lambda: RemoveFrame(OutputFrame, ShowItemFrame))
		BackButton.grid(row = 0, column = 0)


		HeadLable = Label(OutputFrame, text = "Showing ALL Stock Items", relief = SUNKEN, border = 2, padx = 0, pady = 3, font = "BOLD 28")
		HeadLable.grid(row = 0, column = 1, padx = 7, pady = 7, columnspan = 2)



		coln = 0
		for i in list(dataset.columns):
			ColLable = Label(OutputFrame, text = str(i), relief = SUNKEN, border = 0, padx = 0, pady = 3, font = "BOLD")
			ColLable.grid(row = 1, column = coln, padx = 7, pady = 7)
			coln = coln + 1
		OutputFrame.grid()
		rown = 1
		for col in range(len(list(dataset.columns))):
			for row in range(x):
				element = dataset.iloc[row,col]
				EleLabel = Label(OutputFrame, text = str(element),  relief = SUNKEN, border = 1, padx =140)
				EleLabel.grid(row = row+2, column = col)






	def Together():
		dataset = SO.Together()
		ShowItemFrame.grid_forget()
		print(dataset.columns)
		x = dataset["Support"].count()

		OutputFrame = LabelFrame(root, text = "Output Window")
		print(list(dataset.columns))

		#scroll = Scrollbar(OutputFrame, orient = 'vertical')
		#scroll.config(command = OutputFrame.xview)
		BackButton = Button(OutputFrame, text = "Back", command = lambda: RemoveFrame(OutputFrame, ShowItemFrame))
		BackButton.grid(row = 0, column = 0)


		HeadLable = Label(OutputFrame, text = "Showing ALL Stock Items", relief = SUNKEN, border = 2, padx = 0, pady = 3, font = "BOLD 28")
		HeadLable.grid(row = 0, column = 1, padx = 7, pady = 7, columnspan = 2)



		coln = 0
		for i in list(dataset.columns):
			ColLable = Label(OutputFrame, text = str(i), relief = SUNKEN, border = 0, padx = 0, pady = 3, font = "BOLD")
			ColLable.grid(row = 1, column = coln, padx = 7, pady = 7)
			coln = coln + 1
		OutputFrame.grid()
		rown = 1
		for col in range(len(list(dataset.columns))):
			for row in range(x):
				element = dataset.iloc[row,col]
				EleLabel = Label(OutputFrame, text = str(element),  relief = SUNKEN, border = 1, padx =70)
				EleLabel.grid(row = row+2, column = col)






	# Buttons
	AllItemButton = Button(ShowItemFrame, text = "All Items Data", padx = 0, pady = 20, command = AllItems)
	TogetherButton = Button(ShowItemFrame, text = "Items Bought Together", padx = 0, pady = 20, command =Together)
	SortedItemButton = Button(ShowItemFrame, text = "Rating-wise Sorted Data", padx = 0, pady = 20, command =GetOrder)
	BackButton = Button(ShowItemFrame, text = "Go Back", padx = 0, pady = 20, command =lambda: RemoveFrame(ShowItemFrame, FrontPage))


	# put First page on the screen
	ShowLabel.grid(row = 0, column = 0)
	InputLabel.grid(row = 1, column = 0)
	AllItemButton.grid(row = 2, column = 0, pady = 20)
	TogetherButton.grid(row = 3, column = 0, pady = 20)
	SortedItemButton.grid(row = 4, column = 0, pady = 20)
	BackButton.grid(row = 6, column = 0)
	ShowItemFrame.grid()



def EditCustomerFrame():
	FrontPage.grid_forget()
	EditCustomerFrame = LabelFrame(root)
	EditLabel = Label(EditCustomerFrame, text= "Enter Cutomer Data to search by:",font = ("Courier 14 bold"), padx= 20,
	                pady = 20, fg= "Red")



	NameLabel = Label(EditCustomerFrame, text = "Enter Name:", pady = 20)
	NameInp = Entry(EditCustomerFrame, width = 40, borderwidth= 3)
	NameInp.insert(10, " ")
	NameSearch = Button(EditCustomerFrame, text = "Search", fg = "Red")

	OrLabel = Label(EditCustomerFrame, text = "OR")

	IDLabel = Label(EditCustomerFrame, text = "Enter Name:", pady = 20)
	IDInp = Entry(EditCustomerFrame, width = 40, borderwidth= 3)
	IDInp.insert(10, " ")
	IDSearch = Button(EditCustomerFrame, text = "Search", fg = "Red")

	EditLabel.grid(row = 0, column = 0, columnspan = 2)
	NameLabel.grid(row = 1,column = 0)
	NameInp.grid(row = 1,column = 1)
	NameSearch.grid(row = 1,column = 2)
	OrLabel.grid(row = 2,column = 0, columnspan = 2)
	IDLabel.grid(row = 3,column = 0)
	IDInp.grid(row = 3,column = 1)
	IDSearch.grid(row = 3,column = 2)
	EditCustomerFrame.pack()




def EditBasketFrame():
	FrontPage.grid_forget()
	EditStockFrame = LabelFrame(root)
	EditLabel = Label(EditStockFrame, text= "Enter Item Data to search by:",font = ("Courier 14 bold"), padx= 20,
	                pady = 20, fg= "Red")



	NameLabel = Label(EditStockFrame, text = "Enter Name:", pady = 20)
	NameInp = Entry(EditStockFrame, width = 40, borderwidth= 3)
	NameInp.insert(10, " ")
	NameSearch = Button(EditStockFrame, text = "Search", fg = "Red")

	OrLabel = Label(EditStockFrame, text = "OR")

	IDLabel = Label(EditStockFrame, text = "Enter ID:", pady = 20)
	IDInp = Entry(EditStockFrame, width = 40, borderwidth= 3)
	IDInp.insert(10, " ")
	IDSearch = Button(EditStockFrame, text = "Search", fg = "Red")

	EditLabel.grid(row = 0, column = 0, columnspan = 2)
	NameLabel.grid(row = 1,column = 0)
	NameInp.grid(row = 1,column = 1)
	NameSearch.grid(row = 1,column = 2)
	OrLabel.grid(row = 2,column = 0, columnspan = 2)
	IDLabel.grid(row = 3,column = 0)
	IDInp.grid(row = 3,column = 1)
	IDSearch.grid(row = 3,column = 2)
	EditStockFrame.pack()






def FrontPageFrame():
	# first page widgets
	# the operation buttons
	BasketLabel = Label(FrontPage, text= "Customers",font = ("Courier 14 bold"), padx= 20,
	                pady = 20, fg= "Red")

	CustomerLabel = Label(FrontPage, text= "Stock",font = ("Courier 14 bold"), padx= 20,
	                pady = 20, fg= "Blue")

	# greeting image
	GreetImg= ImageTk.PhotoImage(Image.open("file-delivery.png"))
	GreetImgLabel = Label(FrontPage, image = GreetImg)

	# greeting text
	Greeting = Label(FrontPage,text = "Welcome to Customer Recommendation System", font = "Courier 18 bold",anchor = "s",padx = 10, pady =40)

	# Buttons
	CustomerDataSubmitButton = Button(FrontPage, text = "Enter Customer Data", padx = 0, pady = 20, command = InputCustomerFrame)
	BasketDataSubmitButton = Button(FrontPage, text = "Enter Basket Data", padx = 10, pady = 20,command = InputBasketFrame)


	CustomerDataShowButton = Button(FrontPage, text = "Show Customer Data", padx = 0, pady = 20, command = ShowCustomerFrameDisplay)
	BasketDataShowButton = Button(FrontPage, text = "Show Basket Data", padx = 10, pady = 20, command = ShowItemFrameDisplay)


	CustomerEditButton = Button(FrontPage, text = "Edit Customer Data", padx = 0, pady = 20, command = EditCustomerFrame)
	BasketEditButton = Button(FrontPage, text = "Edit Basket Data", padx = 10, pady = 20, command = EditBasketFrame)



	# put First page on the screen
	CustomerLabel.grid(row = 2, column = 1)
	BasketLabel.grid(row = 2, column = 0)
	Greeting.grid(row = 1, column = 0,columnspan = 2)
	GreetImgLabel.grid(row = 0 , column = 0, columnspan = 2)
	CustomerDataSubmitButton.grid(row = 3, column = 0, pady = 20)
	BasketDataSubmitButton.grid(row = 3, column = 1, pady = 20)
	CustomerDataShowButton.grid(row = 2, column = 0, pady = 20)
	BasketDataShowButton.grid(row = 2, column = 1, pady = 20)
	CustomerEditButton.grid(row = 4, column = 0, pady = 20)
	BasketEditButton.grid(row = 4, column = 1, pady = 20)


FrontPageFrame()


FrontPage.grid()











# something is wrong with the image int the front page frame so it is not showing
GreetImg= ImageTk.PhotoImage(Image.open("file-delivery.png"))
GreetImgLabel = Label(FrontPage, image = GreetImg)
GreetImgLabel.grid(row = 0,column = 0, columnspan = 2)



root.mainloop()
