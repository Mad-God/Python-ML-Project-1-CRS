from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import DataIn as DI
import InputValidation as InpVal
import DataOut as DO
import StockOut as SO
import EditingScriptBeta as Edit




root = Tk()
root.geometry("800x600")
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







''' For Customers: Values are being inserted but the data is not yet being inserted
	For Stock: nil'''





def EditCustomerFunc():
	FrontPage.grid_forget()
	EditCustomerFrame = LabelFrame(root, text = "Search Page")
	EditLabel = Label(EditCustomerFrame, text= "Enter Cutomer Data to search by:",font = ("Courier 14 bold"), padx= 20,
	                pady = 20, fg= "Red")













	def ShowCustomerRecord(customer):
		#EditCustomerFrame.grid_forget()
		print(customer)
		#EditCustomerFrame.grid_forget()
		global dataset
		dataset = pd.read_csv(r'D:\Study Material\Project\Final Draft\New Customer.csv')
		OutputFrame = LabelFrame(EditCustomerFrame, text = "Search Result Window")
		print(list(dataset.columns))
		ItemFrame = LabelFrame(OutputFrame)

		#scroll = Scrollbar(OutputFrame, orient = 'vertical')
		#scroll.config(command = OutputFrame.xview)
		BackButton = Button(OutputFrame, text = "Back", command = lambda: RemoveFrame(OutputFrame, EditCustomerFrame))
		BackButton.grid(row = 0, column = 0, padx = 7, pady = 7)

		HeadLable = Label(OutputFrame, text = "The Customer data :", relief = SUNKEN, border = 2, padx = 0, pady = 3, font = "BOLD 15")
		HeadLable.grid(row = 0, column = 1, padx = 7, pady = 7, columnspan = 20)

		coln = 0
		for i in list(dataset.columns):
			ColLable = Label(ItemFrame, text = str(i), relief = SUNKEN, border = 0, padx = 0, pady = 3, font = "BOLD")
			ColLable.grid(row = coln, column = 1, padx = 7, pady = 7)
			coln = coln + 1
		OutputFrame.grid(row = 4, columnspan = 3)
		col = 0
		for x in customer.values():
			element = x
			EleLabel = Label(ItemFrame, text = str(element),  relief = SUNKEN, border = 1, padx = 95)
			EleLabel.grid(row = col, column = 2)
			col +=1
		ItemFrame.grid(columnspan = 6)


		def EditCustomerRecord(customer):
			EditCustomerFrame.grid_forget()
			EditingFrame = LabelFrame(root, text = "Edit Page")


			HeadingLabel = Label(EditingFrame, text = "Edit the Values:",font = ("Courier 14 bold"))
			HeadingLabel.grid(row = 0, column = 0, columnspan = 3)
			col = 0
			for i in list(dataset.columns):
				ColLable = Label(EditingFrame, text = str(i), relief = SUNKEN, border = 0, padx = 0, pady = 3, font = "BOLD")
				ColLable.grid(row = col+1, column = 1, padx = 7, pady = 7)
				col = col + 1
			col = 0
			for x in customer.values():
				element = x
				EleLabel = Label(EditingFrame, text = str(element),  relief = SUNKEN, border = 1, padx = 95)
				EleLabel.grid(row = col+1, column = 2)
				col +=1


			IDLabel = Label(EditingFrame, text = "ID not mutable",  relief = SUNKEN, border = 1)
			IDLabel.grid(row = 1, column = 3)
			NameLabel = Entry(EditingFrame, text = " Enter Upadated Name",  relief = SUNKEN, border = 1)
			NameLabel.grid(row = 2, column = 3)
			NameLabel.insert(20," Enter Upadated")
			ClusterLabel = Label(EditingFrame, text = "Cluster not mutable",  relief = SUNKEN, border = 1)
			ClusterLabel.grid(row = 3, column = 3)
			GenreLabel = Entry(EditingFrame, text = " Enter Upadated Gender",  relief = SUNKEN, border = 1)
			GenreLabel.grid(row = 4, column = 3)
			GenreLabel.insert(20," Enter Upadated")
			AgeLabel = Entry(EditingFrame, text = " Enter Upadated Age",  relief = SUNKEN, border = 1)
			AgeLabel.grid(row = 5, column = 3)
			AgeLabel.insert(20," Enter Upadated")
			SalaryLabel = Entry(EditingFrame, text = " Enter Upadated Salary",  relief = SUNKEN, border = 1)
			SalaryLabel.grid(row = 6, column = 3)
			SalaryLabel.insert(20," Enter Upadated")
			ScoreLabel = Entry(EditingFrame, text = " Enter Upadated Spending Score",  relief = SUNKEN, border = 1)
			ScoreLabel.grid(row = 7, column = 3)
			ScoreLabel.insert(20," Enter Upadated")

			'''
				def SaveEdits():
					print("function inside function. Genre is:")
					print(GenreLabel.get())

			'''
			SaveEditButton = Button(EditingFrame, text = "Save Changes", fg = "Red")
			SaveEditButton.grid(row = 8, column = 2, columns = 3)





			CancleButton = Button(EditingFrame, text = "Cancle", command = lambda : RemoveFrame(EditingFrame, EditCustomerFrame))
			CancleButton.grid(row= 0, column = 0)

			EditingFrame.grid(row = 0, column = 0)



		EditButton = Button(OutputFrame, text = "Edit this Customer", fg = "Blue", command = lambda: EditCustomerRecord(customer))
		EditButton.grid(row = 3, column = 0)




		def DeleteCustomerRecord():
			pass



		DeleteButton = Button(OutputFrame, text = "Delete this Customer", fg = "Blue", command = DeleteCustomerRecord)
		DeleteButton.grid(row = 3, column = 1)
		

		EditCustomerFrame.grid()





	def nameSearch():
		name = NameInp.get()
		name = str(name)
		print(name)
		customer = Edit.NameSearch(name)
		if type(customer) == int:
			print("Customer not found!!!")
		else:
			ShowCustomerRecord(customer)
			NameInp.delete(0,END)

			EditButton = Button()



	def idSearch():
		ID = IDInp.get()
		ID = str(ID)
		print(ID)
		customer = Edit.IDSearch(ID)
		if type(customer) == int:
			print("Customer not found!!!")
		else:
			ShowCustomerRecord(customer)
			IDInp.delete(0,END)





	NameLabel = Label(EditCustomerFrame, text = "Enter Name:", pady = 20)
	NameInp = Entry(EditCustomerFrame, width = 40, borderwidth= 3)
	NameInp.insert(10, "")
	NameSearch = Button(EditCustomerFrame, text = "Search", fg = "Red", command = nameSearch)

	OrLabel = Label(EditCustomerFrame, text = "OR")

	IDLabel = Label(EditCustomerFrame, text = "Enter ID:", pady = 20)
	IDInp = Entry(EditCustomerFrame, width = 40, borderwidth= 3)
	IDInp.insert(10, "")
	IDSearch = Button(EditCustomerFrame, text = "Search", fg = "Red", command = idSearch)
	ExitButton = Button(EditCustomerFrame, text = "Go Back", fg = "Black", command = lambda: RemoveFrame(EditCustomerFrame, FrontPage))


	EditLabel.grid(row = 0, column = 0, columnspan = 2)
	NameLabel.grid(row = 1,column = 0)
	NameInp.grid(row = 1,column = 1)
	NameSearch.grid(row = 1,column = 2)
	OrLabel.grid(row = 2,column = 0, columnspan = 2)
	IDLabel.grid(row = 3,column = 0)
	IDInp.grid(row = 3,column = 1)
	IDSearch.grid(row = 3,column = 2)
	ExitButton.grid(row = 4, column = 0, columnspan = 2)
	EditCustomerFrame.grid()





def EditBasketFunc():
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
	BackButton = Button(EditStockFrame, text = "Go Back", fg = "Black", command = lambda: RemoveFrame(EditStockFrame, FrontPage))


	EditLabel.grid(row = 0, column = 0, columnspan = 2)
	NameLabel.grid(row = 1,column = 0)
	NameInp.grid(row = 1,column = 1)
	NameSearch.grid(row = 1,column = 2)
	OrLabel.grid(row = 2,column = 0, columnspan = 2)
	IDLabel.grid(row = 3,column = 0)
	IDInp.grid(row = 3,column = 1)
	IDSearch.grid(row = 3,column = 2)
	BackButton.grid(row = 4, column = 0, columnspan = 2)
	EditStockFrame.grid()






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


	CustomerEditButton = Button(FrontPage, text = "Edit Customer Data", padx = 0, pady = 20, command = EditCustomerFunc)
	BasketEditButton = Button(FrontPage, text = "Edit Basket Data", padx = 10, pady = 20, command = EditBasketFunc)



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
