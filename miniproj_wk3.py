## System functions
import os, sys
from os import system, name

# function to get current script directory
def fileinsamedir(filename):
    return os.path.join(sys.path[0], str(filename))

# function to clear console output irrespective of windows/unix
def clearConsole():
    return system('cls') if name == 'nt' else system('clear')

## Initial file loaders to list
# load products list with .txt contents, make new file if file not found
try:
    with open(fileinsamedir("products.txt"), 'r') as productsfile:
        products = [lines.rstrip() for lines in productsfile]
        print("Loaded product names from products.txt!\n",
              f"  Products list contains: {products}\n")
except FileNotFoundError:
    with open(fileinsamedir("products.txt"), 'w') as productsfile:
        products = []
        print("Made new products file as products.txt")
    
# load couriers list with .txt contents, make new file if file not found
try:
    with open(fileinsamedir("couriers.txt"), 'r') as couriersfile:
        couriers = [lines.rstrip() for lines in couriersfile]
        print("Loaded courier names list from couriers.txt!\n",
              f"  Couriers list contains: {couriers}\n\n")
except FileNotFoundError:
    with open(fileinsamedir("couriers.txt"), 'w') as couriersfile:
        couriers = []
        print("Made new couriers list file as couriers.txt\n\n")

# load initial dictionary, #TODO file loading CSV for orders dictionary
orders = [{
    "customer_name": "John",
    "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
    "customer_phone": "0789887334",
    "courier": 2,
    "status": "preparing"
}]

## Sub-menu specific functions
# ordersmenu function welcome (to be deprecated), refactor later
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

# shows couriers list, prompt user for choice to assign to orders dict<<
def showCouriers():
    for i, item in enumerate(couriers):
        print(f"{i}: {item}")
    
    try:
        choice = input("Enter index of courier to assign to this order: ")
    except ValueError:
        choice = None
        
    return choice

# makes new order dictionary, returns new dictionary
def newOrder():
    clearConsole()
    # make new empty dict, add property input line by line, clearConsole after each line
    newDict = {
        "customer_name": input("Enter customer name: "),
        "customer_address": input("Enter customer address: "),
        "customer_phone": input("Enter customer phone number: "),
        "courier": showCouriers(),
        "status": "PREPARING"
    }
    
    clearConsole()
    return newDict


## Init app!
clearConsole()
print("Welcome to Solomon's Mini Project1: Products and Couriers Manager App\n")

# To-do-2: catch incorrect input errors
while True:
    # init main menu options and prompt choice
    print("Main Menu Options:\n\n",
        "  1:  Products Menu\n",
        "  2:  Couriers Menu\n",
        "  3:  Orders Menu\n",
        "  0:  Exit app\n")
    mainmenu = int(input("Enter 1, 2, 3 or 0:\n"))
    clearConsole()
            
    # exit main menu while loop and subsequently the app
    if mainmenu == 0:
        clearConsole()
        print("Saving lists and exiting app...")
        
        # overwrite products list to products.txt
        with open(fileinsamedir("products.txt"), 'w') as writeprodfile:
            for items in products:
                writeprodfile.write(items + '\n')
        
        # overwrite couriers list to couriers.txt
        with open(fileinsamedir("couriers.txt"), 'w') as writecourfile:
            for items in couriers:
                writecourfile.write(items + '\n')

        break

    # init product menu options and prompt user
    while mainmenu == 1:
        prodopts = ["List products", "Insert a product",
                    "Update existing product", "Remove a product",
                    "Return to main menu"]
        print(f"Products Menu: Options\n\n",
            f"  1:  {prodopts[0]}\n",
            f"  2:  {prodopts[1]}\n",
            f"  3:  {prodopts[2]}\n",
            f"  4:  {prodopts[3]}\n",
            f"  0:  {prodopts[4]}\n")
        prodmenu = int(input("Enter 1, 2, 3, 4, or 0:\n"))
            # To-do-1: make prodmenu into function/class, default clearConsole(), then overload prodmenu with options #
        clearConsole()
        
        # prodopt0: exit products menu while loop to return to main menu
        if prodmenu == 0:
            # exit products menu while loop to return to main menu
            clearConsole()
            print("Returned to main menu!\n")
            break
        
        # prodopt1: list products
        elif prodmenu == 1:
            clearConsole()
            print(f"Products list contains:\n {[i for i in products]} \n")

        # prodopt2: add to products list    
        elif prodmenu == 2:
            clearConsole()
            products.append(input("Enter a product name: "))
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Added \"{products[-1]}\" to product list!\n")
            
        # prodopt3: list indexes and update an existing product
        elif prodmenu == 3:
            clearConsole()
            for i in range(len(products)):
                print(f"{i}: ", products[i])
            indexupd = int(input("Enter the index of the product you want to change: "))
            
            # store value at selected index for later printing, update index value
            indexupdtemp = products[indexupd]
            products[indexupd] = input("Enter a new name for this product: ")
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Updated \"{indexupdtemp}\" with \"{products[indexupd]}\"!\n")
        
        # prodopt4: list indexes and delete an existing product
        elif prodmenu == 4:
            clearConsole()
            for i in range(len(products)):
                print(f"{i}: ", products[i])
            indexdel = int(input("Enter the index of the product you want to remove: "))
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Removed \"{products.pop(indexdel)}\" from product list!\n")
    
    # init couriers menu options and prompt user
    while mainmenu == 2:
        courieropts = ["List courier names", "Insert a courier name",
                    "Update existing courier name", "Remove a courier name",
                    "Return to main menu"]
        print(f"Courier Names Menu: Options\n\n",
            f"  1:  {courieropts[0]}\n",
            f"  2:  {courieropts[1]}\n",
            f"  3:  {courieropts[2]}\n",
            f"  4:  {courieropts[3]}\n",
            f"  0:  {courieropts[4]}\n")
        couriermenu = int(input("Enter 1, 2, 3, 4, or 0:\n"))
            # To-do-1: make couriermenu into function/class, default clearConsole(), then overload couriermenu with options #
        clearConsole()
        
        # couropt0: exit couriers menu while loop to return to main menu
        if couriermenu == 0:
            clearConsole()
            print("Returned to main menu!\n")
            break
        
        # couropt1: list couriers
        elif couriermenu == 1:
            clearConsole()
            print(f"Couriers list contains:\n {[i for i in couriers]} \n")

        # couropt2: add to couriers list
        elif couriermenu == 2:
            clearConsole()
            couriers.append(input("Enter a new courier name: "))
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Added \"{couriers[-1]}\" to couriers list!\n")
        
        # couropt3: list indexes and update an existing courier
        elif couriermenu == 3:
            clearConsole()
            for i in range(len(couriers)):
                print(f"{i}: ", couriers[i])
            indexupd = int(input("Enter the index of the courier name you want to change: "))
            
            # store value at selected index for later printing, update index value
            indexupdtemp = couriers[indexupd]
            couriers[indexupd] = input("Enter courier name to update this with: ")
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Updated \"{indexupdtemp}\" with \"{couriers[indexupd]}\"!\n")
        
        # couropt4: list indexes and delete an existing courier
        elif couriermenu == 4:
            clearConsole()
            for i in range(len(couriers)):
                print(f"{i}: ", couriers[i])
            indexdel = int(input("Enter the index of the courier name you want to remove: "))
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Removed \"{couriers.pop(indexdel)}\" from courier names list!\n")
    
    # init orders menu options and prompt user
    while mainmenu == 3:
        # initiate ordermenu and show options, returns choice
        ordersopts = ["Return to main menu", "Show orders dictionary list", "Add an order",
                "Update existing order status", "Update an existing order", "Remove an order",
                f"Orders Menu: Options\n", "\nChoose an option by entering it's index: "]
        print(f"\n{ordersopts[-2]}")
        for i in range(0, len(ordersopts)-2):
            print(f"  {i}:  {ordersopts[i]}")
        ordermenu = int(input(ordersopts[-1]))
        
        # orderopt0: exit couriers menu while loop to return to main menu
        if ordermenu == 0:
            clearConsole()
            print("Returned to main menu!\n")
            break
        
        # orderopt1: list orders
        elif ordermenu == 1:
            showOrders()

        # orderopt2: add to orders list
        elif ordermenu == 2:
            insertDict = newOrder() # call func to make new order
            
            orders.append(insertDict)
            print(f"Added \"{insertDict}\" to orders list!")
            # cleanup output and confirm operation completed
        
        # orderopt3: list indexes and update an existing order's STATUS
        elif ordermenu == 3:
            clearConsole()
            showOrders()
            indexupd = int(input(f"\nEnter the index of the order status you want to change: "))
            clearConsole()
            
            # store value at selected index for later printing, update index value
            indextempstatus = orders[indexupd]['status']
            orders[indexupd]['status'] = input("Enter new order status: ")
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Updated order index {indexupd} status from \"{indextempstatus}\" to \"{orders[indexupd]['status']}\"!")
            
        # orderopt4: list indexes, update dict at index with user input if not blank/noneType
        elif ordermenu == 4:
            clearConsole()
            showOrders()
            indexToUpdate = int(input("\nSelect index of order to update: "))
            # cache oldDict and entries to update
            oldDict = orders[indexToUpdate]            
            updateTo_oldDict = newOrder()
            
            # if input is blank/noneType do not update respective dict property, else update
            print(f"Updating order: {oldDict}\n")
            
            # update old dict
            orders[indexToUpdate].update({k:v for k, v in updateTo_oldDict.items() if v and (k != 'status')})
            
            # confirmation of updated order
            print(f"Order index {indexToUpdate} updated to:\n {orders[indexToUpdate]}")
                 
        # orderopt5: list indexes and delete an existing order at index
        elif ordermenu == 5:
            showOrders()
            indexdel = int(input("\nEnter the index of the order you want to remove: "))
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Removed \"{orders.pop(indexdel)}\" from orders list!\n")