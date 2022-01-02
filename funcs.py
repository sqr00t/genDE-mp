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
    finally: # can be redacted and put in showlist(), list showing may not be needed at fileloading
        #print(f"{filename[:-4].capitalize()} list contains:")
        #for dicts in dictslist: print(dicts)
        return dictslist

# writing dictslist to filename.csv
def fileWriter(dictslist, filename):
    with open(fileinsamedir(filename), 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=dictslist[0].keys())
        writer.writeheader()
        writer.writerows(dictslist)

## Sub-menu specific functions
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

## NewDicts
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

def insertListItem(dictslist, listFunction, listName, listNameLower):
    dictslist.append(listFunction)
    return print(f"Added {listNameLower} \"{dictslist[-1]}\" to {listName.lower()} list!")

#TODO using self.newDictFunc to call newDict in class when needed, instead of passing as arg which will call it at func init.
def updateDict(dictslist, listNameLower, newDictFunc):
    showList(dictslist, listNameLower)
    indexToUpdate = int(input(f"\nSelect index of {listNameLower} to update: "))
    # cache oldDict and entries to update
    oldDict = dictslist[indexToUpdate]
    
    # if input is blank/noneType do not update respective dict property, else update
    print(f"Updating {listNameLower}: {oldDict}\n")
    updateOrdersValues = newDictFunc
    
    # update old dict
    dictslist[indexToUpdate].update({k:v for k, v in updateOrdersValues.items() if v and (k != 'status')})
    
    # confirmation of updated order
    print(f"{listNameLower} index {indexToUpdate} updated to:\n {dictslist[indexToUpdate]}")

def deleteListItem(dictslist, listName):
    showList(dictslist, listName)
    indexdel = int(input(f"\nEnter the index of the {listNameLower} you want to remove: "))
    
    # cleanup output and confirm operation completed
    clearConsole()
    return print(f"Removed \"{dictslist.pop(indexdel)}\" from {listName.lower()} list!\n")