
import DataIn as DI
from InputValidation import InputValidation as InpVal
import DataOut as DO
import StockOut as SO


print("...WELCOME...\n\nWould you like to:\n1. Input a New Data\n2. Present Data ")

op = InpVal(1,2)

if op == 1:
  print("\nDo you want to  Enter data for:\n1. Customer\n2. Basket Items ")
  op = InpVal(1,3)
  data = {}
  bas = []

  if op == 1:
    data = DI.TakeCustomer()

  elif op == 2:
    bas = DI.TakeBasket()
    # if we were to accept reviews...add them to individual items or whole baskets...and up-down the items' rating accordingly










elif op == 2:
  print("What do you want to print:\n1. Customer Data\n2. Stocks Data")
  op = InpVal(1,2)

  if op == 1:
    print("\n1. Show All Customers Data\n2. Show Customers of a particular Cluster\n3. Show Customers according to Spending Score ")
    op = InpVal(1,3)
    # if we were to add Customer ID in the Basket input.....the spending score could be altered likewise so as to train model better

    if op == 1:
      DO.AllCustomers()
      
    elif op == 2:
      print("Enter the Cluster Number for which the Customers are to be Displayed")
      op = InpVal(1,5)
      DO.ClusterCustomers(op-1)

    elif op == 3:
      print("1. Ascending Order of Spending Score\n2. Descending Order of Spending Score")
      op = InpVal(1,2)
      DO.Order(op == 1)








  elif op == 2:
    print("\n1. Show All Stock Items\n2. Items that are bought together\n3. Show Items according to their Rating")
    op = InpVal(1,3)
    if op == 1:
      SO.AllItems()

    elif op == 2:
      SO.Together()
    elif op == 3:
      print("1. Ascending Order of Rating\n2. Descending Order of Rating")
      op = InpVal(1,2)
      SO.Order(op == 1)

    # if we had rating of different items... we could sort by those as well

# make a table of all items with their prices....add a colums of rating for these items 
    #which is altered when a review is given for a basket containing that item
