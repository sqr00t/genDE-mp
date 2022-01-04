from os import system, name
from MPFunctions import Products, Couriers, Orders

def clearConsole(): return system('cls') if name == 'nt' else system('clear')

## Init app!
clearConsole()
productsobj = Products("products.csv")
couriersobj = Couriers("couriers.csv")
ordersobj = Orders("orders.csv", productsobj, couriersobj)
print("\nWelcome to Solomon's Mini Project!\n")

while True:
    # init main menu options and prompt choice
    mainopts = ["Main Menu Options:","  1:  Products Menu",
                "  2:  Couriers Menu","  3:  Orders Menu", "  0:  Exit app"]
    for opts in mainopts: print(opts)
    mainmenu = int(input("\nChoose an option by entering it's index: "))
    clearConsole()
            
    # exit main menu while loop and subsequently the app
    if mainmenu == 0:
        clearConsole()
        print("Saving lists and exiting app...")
        productsobj.save_file(), couriersobj.save_file(), ordersobj.save_file()
        del productsobj, couriersobj, ordersobj
        break

    # init product menu options and prompt user
    while mainmenu == 1:
        listName, listNameLower = "Products", "product"
        prodopts = [f"{listName} Menu: Options", f"  1:  List {listName.lower()}",
                       f"  2:  Insert {listNameLower}", f"  3:  Update existing {listNameLower}",
                       f"  4:  Remove {listNameLower}", f"  0:  Return to main menu"]
        for opts in prodopts: print(opts)
        prodmenu = int(input("\nChoose an option by entering it's index: "))
        clearConsole()
        
        # prodopt0: exit products menu while loop to return to main menu
        if prodmenu == 0:
            # exit products menu while loop to return to main menu
            clearConsole()
            print("Returned to main menu!\n")
            break
        
        # prodopt1: list products
        elif prodmenu == 1: productsobj.show_dicts()

        # prodopt2: add to products list    
        elif prodmenu == 2: productsobj.insert_dict()
            
        # prodopt3: list indexes and update an existing product
        elif prodmenu == 3: productsobj.update_dict()

        # prodopt4: list indexes and delete an existing product
        elif prodmenu == 4: productsobj.delete_dict()
    
    # init couriers menu options and prompt user
    while mainmenu == 2:
        listName, listNameLower = "Couriers", "courier"
        courieropts = [f"{listName} Menu: Options", f"  1:  List {listName.lower()}",
                       f"  2:  Insert {listNameLower}", f"  3:  Update existing {listNameLower}",
                       f"  4:  Remove {listNameLower}", f"  0:  Return to main menu"]
        for opts in courieropts: print(opts)
        couriermenu = int(input("\nChoose an option by entering it's index: "))
        clearConsole()
        
        # couropt0: exit couriers menu while loop to return to main menu
        if couriermenu == 0:
            clearConsole()
            print("Returned to main menu!\n")
            break
        
        # couropt1: list couriers
        elif couriermenu == 1: couriersobj.show_dicts()

        # couropt2: add to couriers list
        elif couriermenu == 2: couriersobj.insert_dict()
        
        # couropt3: list indexes and update an existing courier
        elif couriermenu == 3: couriersobj.update_dict()
        
        # couropt4: list indexes and delete an existing courier
        elif couriermenu == 4: couriersobj.delete_dict()
    
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
        elif ordermenu == 1: ordersobj.show_dicts()

        # orderopt2: add to orders list
        elif ordermenu == 2: ordersobj.insert_dict()
        
        # orderopt3: list indexes and update an existing order's STATUS
        elif ordermenu == 3: ordersobj.update_order_status()
            
        # orderopt4: list indexes, update dict at index with user input if not blank/noneType
        elif ordermenu == 4: ordersobj.update_dict()
        
        # orderopt5: list indexes and delete an existing order at index
        elif ordermenu == 5: ordersobj.delete_dict()
# 118 lines, 25 comment lines, total code lines: 93