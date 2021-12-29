from os import system, name

def clearConsole():
    return system('cls') if name == 'nt' else system('clear')

while True:
    products = []
    print("Main Menu Options:\n\n",
          "  1:  Products Menu\n",
          "  0:  Exit app\n")
    mainmenu = int(input("Enter 1 or 0:\n"))
    clearConsole()
    
    if mainmenu == 0:
        clearConsole()
        print("Saving lists and exiting app...")
        
        # save products and couriers list to *.txt
        
        break
    
    while mainmenu == 1:
        mainopts = ["List products", "Insert a product",
                    "Update existing product", "Remove a product",
                    "Return to main menu"]
        print(f"Products Menu: Options\n\n",
              f"  1:  {mainopts[0]}\n",
              f"  2:  {mainopts[1]}\n",
              f"  3:  {mainopts[2]}\n",
              f"  4:  {mainopts[3]}\n",
              f"  0:  {mainopts[4]}\n")
        prodmenu = int(input("Enter 1, 2, 3, 4, or 0:\n"))
        # To-do-2: make prodmenu into function/class, default clearConsole(), then overload prodmenu with options #
        clearConsole()
        
        if prodmenu == 0:
            clearConsole()
            print("Returned to main menu!\n")
            break
        elif prodmenu == 1:
            clearConsole()
            print([i for i in products], sep = "\n")
            
            # To-do-1: unify UX with other prodmenu options?
            
        elif prodmenu == 2:
            clearConsole()
            products.append(input("Enter a product name: "))
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Added \"{products[-1]}\" to product list!\n")
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
        elif prodmenu == 4:
            clearConsole()
            for i in range(len(products)):
                print(f"{i}: ", products[i])
            indexdel = int(input("Enter the index of the product you want to remove: "))
            
            # cleanup output and confirm operation completed
            clearConsole()
            print(f"Removed \"{products.pop(indexdel)}\" from product list!\n")