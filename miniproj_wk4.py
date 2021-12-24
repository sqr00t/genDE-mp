## System functions
import os, sys, csv
from os import system, name

# function to get current script directory
def fileinsamedir(filename):
    return os.path.join(sys.path[0], str(filename))

# function to clear console output irrespective of windows/unix
def clearConsole():
    return system('cls') if name == 'nt' else system('clear')

# Initial file loaders to list
def fileLoader(filename):
    try:
        with open(fileinsamedir(filename), 'r') as file:
            dictslist = [dicts for dicts in csv.DictReader(file)]
            print(f"Loaded {filename} into {filename[:-4]} list.\n")
    except FileNotFoundError:
        with open(fileinsamedir(filename), 'w') as file:
            dictslist = []
            print(f"Cannot find {filename} in app folder, made new {filename}\n")
    finally: # can be redacted and put in showlist()
        print(f"{filename[:-4].capitalize()} list contains:")
        for dicts in dictslist: print(dicts)
        return dictslist

# writing dictslist to filename.csv
def fileWriter(dictslist, filename):
    with open(fileinsamedir(filename), 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dictslist[0].keys())
        writer.writeheader()
        writer.writerows(dictslist)
    
## Sub-menu specific functions
# ordersmenu function welcome (to be deprecated), TODO refactor later
def ordermenu(): 
    ordersopts = ["Return to main menu", "Show orders dictionary list", "Add an order",
                "Update existing order status", "Update an existing order", "Remove an order",
                f"Orders Menu: Options\n", "\nChoose an option by entering it's index: "]
    print(ordersopts[-2])
    for i in range(0, len(ordersopts)-2):
        print(f"  {i}:  {ordersopts[i]}")
    choice = int(input(ordersopts[-1]))
    
    return choice

# shows orders list
def showOrders():
    clearConsole()
    print(f"Orders list contains:\n")
    for i, item in enumerate(orders):
        print(f"Order Index {i}: {item}")
    return "\n"

# refactored show list to be agnostic between submenu types
def showList(dictslist, listName):
    clearConsole()
    print(f"{listName} list contains:\n")
    for i, item in enumerate(dictslist):
        print(f"{listName} Index {i}: {item}")
    return print("\n")

# shows couriers list, prompt user for choice to assign to orders dict<<
def showCouriers(dictslist, listName):
    showList(dictslist, listName)
    # this is effectively an overloaded showList function, if couriers is specified in args
    try:
        choice = int(input("Enter index of courier to assign to this order: "))
    except ValueError:
        choice = None
    finally: #will this break intended flow?
        return choice

def orderItems(dictslist, listName):
    showList(dictslist, listName)
    # this is effectively an overloaded showList function, if products is specified in args
    # necessary to bundle these functionality together
    itemsIntList = [int(i) for i in input("Enter comma-separated product index values: ").split(',')]
    return itemsIntList

# makes new order dictionary, returns new dictionary
def newOrder():
    clearConsole()
    # make new empty dict, add property input line by line, clearConsole after each line
    newDict = {
        "customer_name": input("Enter customer name: "),
        "customer_address": input("Enter customer address: "),
        "customer_phone": input("Enter customer phone number: "),
        "courier": showCouriers(couriers, "Couriers"),
        "status": "PREPARING",
        "items": orderItems(products, "Products")
    }
    
    clearConsole()
    return newDict

def newProduct():
    clearConsole()
    # make new empty dict, add property input line by line, clearConsole after each line
    newDict = {
        "name": input("Enter new product name: "),
        "price": input("Enter new product price: ")
    }
    try:
        # convert price input to float
        newDict['price'] = float(newDict['price'])
    except ValueError:
        newDict['price'] = None
    finally:
        clearConsole()
        return newDict
        
def newCourier():
    clearConsole()
    newDict = {
        "name": input("Enter new courier name: "),
        "phone": input("Enter new courier phone no.: ")
    }
    
    clearConsole()
    return newDict

def deleteListItem(dictslist, listName):
    showList(dictslist, listName)
    indexdel = int(input(f"\nEnter the index of the {listNameLower} you want to remove: "))
    
    # cleanup output and confirm operation completed
    clearConsole()
    return print(f"Removed \"{dictslist.pop(indexdel)}\" from {listName.lower()} list!\n")

## Init app!
# load products list with .csv contents, make new file if file not found
products = fileLoader("products.csv")
# modify to account for 'price' being a float
for dicts in products: dicts['price'] = float(dicts['price'])
    
# load couriers list with .csv contents, make new file if file not found
couriers = fileLoader("couriers.csv")

# load orders list with .csv contents, make new file if file not found
orders = fileLoader("orders.csv")
# modify to account for 'courier' being an int, 'items' being a list of ints
for dicts in orders:
    dicts['courier'] = int(dicts['courier'])
    dicts['items'] = [int(i) for i in dicts['items'].strip("][").split(",")]

clearConsole()
print("Welcome to Solomon's Mini Project1: Products and Couriers Manager App\n")

# To-do-2: catch incorrect input errors
while True:
    # init main menu options and prompt choice
    mainopts = ["Main Menu Options:","  1:  Products Menu",
                "  2:  Couriers Menu","  3:  Orders Menu", "  0:  Exit app"]
    for opts in mainopts: print(opts)
    mainmenu = int(input("Enter 1, 2, 3 or 0:\n"))
    clearConsole()
            
    # exit main menu while loop and subsequently the app
    if mainmenu == 0:
        clearConsole()
        print("Saving lists and exiting app...")
        
        # overwrite products list to products.txt
        fileWriter(products, "products.csv")
        
        # overwrite couriers list to couriers.txt
        fileWriter(couriers, "couriers.csv")
        
        # overwrite orders list to couriers.txt
        fileWriter(orders, "orders.csv")

        break

    # init product menu options and prompt user
    while mainmenu == 1:
        listName, listNameLower = "Products", "product"
        prodopts = [f"{listName} Menu: Options", f"  1:  List {listName.lower()}",
                       f"  2:  Insert {listNameLower}", f"  3:  Update existing {listNameLower}",
                       f"  4:  Remove {listNameLower}", f"  0:  Return to main menu"]
        for opts in prodopts: print(opts)
        prodmenu = int(input("\nChoose an option by entering it's index: "))
            # To-do-1: make prodmenu into function/class, default clearConsole(), then overload prodmenu with options #
        clearConsole()
        
        # prodopt0: exit products menu while loop to return to main menu
        if prodmenu == 0:
            # exit products menu while loop to return to main menu
            clearConsole()
            print("Returned to main menu!\n")
            break
        
        # prodopt1: list products
        elif prodmenu == 1: showList(products, listName)

        # prodopt2: add to products list    
        elif prodmenu == 2:
            # newProduct() gets input for name:price and returns newdict entry
            products.append(newProduct())
            print(f"Added {listNameLower} \"{products[-1]}\" to {listName.lower()} list!\n")
            
        # prodopt3: list indexes and update an existing product
        elif prodmenu == 3: #TODO use action mapping to define respective input arguments
            showList(products, listName)
            indexToUpdate = int(input(f"Enter the index of the {listNameLower} you want to change: "))
            
            # store value at selected index for later printing
            oldDict = products[indexToUpdate]
            
            # get new dict values to update oldDict
            print(f"Updating {listNameLower}: {oldDict}\n")
            updateValues = newProduct()
            
            # if input is blank/noneType do not update respective dict property, else update
            products[indexToUpdate].update({k:v for k, v in updateValues.items() if v})
            
            # confirmation of updated order
            print(f"{listName[:-1]} index {indexToUpdate} updated to: {products[indexToUpdate]}\n")
        
        # prodopt4: list indexes and delete an existing product
        elif prodmenu == 4: deleteListItem(products, listName)
    
    # init couriers menu options and prompt user
    while mainmenu == 2:
        listName, listNameLower = "Couriers", "courier"
        courieropts = [f"{listName} Menu: Options", f"  1:  List {listName.lower()}",
                       f"  2:  Insert {listNameLower}", f"  3:  Update existing {listNameLower}",
                       f"  4:  Remove {listNameLower}", f"  0:  Return to main menu"]
        for opts in courieropts: print(opts)
        couriermenu = int(input("\nChoose an option by entering it's index: "))
            # To-do-1: make couriermenu into function/class, default clearConsole(), then overload couriermenu with options #
        clearConsole()
        
        # couropt0: exit couriers menu while loop to return to main menu
        if couriermenu == 0:
            clearConsole()
            print("Returned to main menu!\n")
            break
        
        # couropt1: list couriers
        elif couriermenu == 1: showList(couriers, listName)

        # couropt2: add to couriers list
        elif couriermenu == 2:
            # newCourier() gets input for name:phone and returns newdict entry
            couriers.append(newCourier())
            print(f"Added {listNameLower} \"{couriers[-1]}\" to {listName.lower()} list!\n")
        
        # couropt3: list indexes and update an existing courier
        elif couriermenu == 3:
            showList(couriers, listName)
            indexToUpdate = int(input(f"Enter the index of the {listNameLower} you want to change: "))
            
            # store value at selected index for later printing
            oldDict = couriers[indexToUpdate]
            
            # get new dict values to update oldDict
            print(f"Updating {listNameLower}: {oldDict}\n")
            updateValues = newCourier()
            
            # if input is blank/noneType do not update respective dict property, else update
            couriers[indexToUpdate].update({k:v for k, v in updateValues.items() if v})
            
            # confirmation of updated order
            print(f"{listName[:-1]} index {indexToUpdate} updated to: {couriers[indexToUpdate]}\n")
        
        # couropt4: list indexes and delete an existing courier
        elif couriermenu == 4: deleteListItem(couriers, listName)
    
    # init orders menu options and prompt user
    while mainmenu == 3:
        listName, listNameLower = "Orders", "order"
        # initiate ordermenu and show options, returns choice
        ordersopts = [f"{listName} Menu: Options", f"  1:  List {listName.lower()}",
                       f"  2:  Insert {listNameLower}", f"  3:  Update {listNameLower} status",
                       f"  4:  Update existing {listNameLower}", f"  5:  Remove {listNameLower}",
                       f"  0:  Return to main menu"]
        for opts in ordersopts: print(opts)
        ordermenu = int(input("\nChoose an option by entering it's index: "))
        clearConsole()
        
        # orderopt0: exit couriers menu while loop to return to main menu
        if ordermenu == 0:
            clearConsole()
            print("Returned to main menu!\n")
            break
        
        # orderopt1: list orders
        elif ordermenu == 1: showList(orders, listName)

        # orderopt2: add to orders list
        elif ordermenu == 2:
            orders.append(newOrder())
            print(f"Added order \"{orders[-1]}\" to orders list!")
            # make newOrder dictionary
            # see updated newOrder func
            
        
        # orderopt3: list indexes and update an existing order's STATUS
        elif ordermenu == 3:
            showList(orders, listName)
            indexupd = int(input(f"\nEnter the index of the order status you want to change: "))
            clearConsole()
            
            # store value at selected index for later printing
            indextempstatus = orders[indexupd]['status']
            # print status list options, update index value
            statuslist = ["PREPARING", "READY FOR DELIVERY", "OUT FOR DELIVERY", "DELIVERED"]
            for i, status in enumerate(statuslist):
                print(f"  {i}: {status}")
            
            orders[indexupd]['status'] = statuslist[int(input("Enter order status index to update: "))]
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Updated order index {indexupd} status from \"{indextempstatus}\" to \"{orders[indexupd]['status']}\"!")
            
        # orderopt4: list indexes, update dict at index with user input if not blank/noneType
        elif ordermenu == 4: #TODO refactor this, k != 'status' remains true for other menus
            showList(orders, listName)
            indexToUpdate = int(input("\nSelect index of order to update: "))
            # cache oldDict and entries to update
            oldDict = orders[indexToUpdate]
            
            # if input is blank/noneType do not update respective dict property, else update
            print(f"Updating order: {oldDict}\n")            
            updateOrdersValues = newOrder()
            
            # update old dict
            orders[indexToUpdate].update({k:v for k, v in updateOrdersValues.items() if v and (k != 'status')})
            
            # confirmation of updated order
            print(f"Order index {indexToUpdate} updated to:\n {orders[indexToUpdate]}")
                 
        # orderopt5: list indexes and delete an existing order at index
        elif ordermenu == 5: deleteListItem(orders, listName)