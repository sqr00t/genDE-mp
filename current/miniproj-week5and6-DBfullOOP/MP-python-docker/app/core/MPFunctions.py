import os, csv, time
from os import system, name
from core.DBfunctions import CRUD
from tabulate import tabulate

class BaseFunctions: # list BaseFunctions object class. Pass to args: "listname"
    def __init__(self, filename: str, dictslist=None):
        """Inits obj with BaseFunctions class."""
        self.filepath = os.path.join(os.path.dirname(__file__), '..', 'data/', str(filename) + ".csv")
        self.listname = str(filename) #used for printouts. SQL match table with this
        self.listname_title = self.listname.title()
        self.dictslist = dictslist
        self.menu_options = [f"\n{self.listname_title} Menu Options:\n", f"  1:  Show {self.listname} list", f"  2:  Insert {self.listname[:-1]}",
                             f"  3:  Update existing {self.listname[:-1]}", f"  4:  Remove {self.listname[:-1]}", f"  0:  Return to main menu"]
        if self.dictslist is None:
            try:
                with open(self.filepath, 'r') as file:
                    self.dictslist = [dicts for dicts in csv.DictReader(file)]
                    print(f"Loaded {self.listname}.csv into {self.listname} list. Local files may be overwritten!")
            except FileNotFoundError:
                self.dictslist = [dicts for dicts in CRUD(self.listname).read()]
                print(f"{self.listname}.csv not in app data, parsed {self.listname} from server.")
            #TODO except on loading db error...:

    def clearConsole(self): system('cls') if name == 'nt' else system('clear')
    
    def wait(self):
        """Waits 3 seconds then clears output"""
        time.sleep(2)
        self.clearConsole()
        
    def skip(self):
        """Leaves and clears display"""
        input(f"Press 'Enter' to return to {self.listname_title} Menu...")
        self.clearConsole()
    
    def export_file(self):
        """Save self.dictslist list of dictionaries to .csv file"""
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.dictslist[0].keys())
            writer.writeheader(), writer.writerows(self.dictslist)
            
    def display_table(self, list_here, listname_here):
        """Displays list_here list of dictionaries in table form using tabulate and tablefmt=fancy_grid"""
        self.wait() # wait 3 seconds, clearConsole
        # format for tabulate and display dictslist with tablefmt format
        header, row = [i.upper() for i in list_here[0].keys()], [row.values() for row in list_here]
        print(f"\n{listname_here} list contains:\n{tabulate(row,header, tablefmt='fancy_grid')}")

    def get_dicts(self):
        """Gets dicts data and lists dicts in self.dictslist"""
        sync_choice = str(input("Get latest server data and overwrite local data? (y/n)"))
        
        #SQL gets data from server into dictslist
        sync_data = [dicts for dicts in CRUD(self.listname).read()]
        if sync_choice == "y" or sync_choice == "Y":
            self.dictslist = sync_data
            self.wait() # wait 3 seconds, clearConsole
            print(f"Local {self.listname} data synced with server data!")
        elif sync_choice == "n" or sync_choice == "N":
            self.dictslist.append(dicts for dicts in sync_data if (dicts not in self.dictslist))
            print(f"Added server data to local {self.listname} list, existing local data not overwritten!")
        else: return print("Incorrect input... No data was overwritten!")

        # print table after delay, press enter to leave displayed table and return to previous menu
        self.display_table(self.dictslist, self.listname_title)

    def selector(self, list_var, listname: str, operation: str):
        """Returns index of dict in dictslist matching prompted id, stores *self.dict_to_change* to match with SQL queries"""
        try:
            self.id_op = int(input(f"\nEnter the id of the {listname[:-1]} you want to {operation}: "))
            for dicts in list_var:
                if dicts['id'] == self.id_op:
                    self.dict_to_change = dicts
                    to_delete_index = list_var.index(dicts)
                    return to_delete_index
        except Exception as e:
            print(f"Please enter a valid id! {e}")
            return self.selector(list_var, listname, operation)

    def delete_dict(self):
        """List dicts in self.dictslist, prompts user for index of choice, remove dict at index"""
        #get dict with id=prompt and index of dict in local list
        self.get_dicts()
        to_delete_index = self.selector(self.dictslist, self.listname, "delete")
        self.wait() # wait 3 seconds, clearConsole
        
        # format deleted dict for table printout
        table_range = self.dictslist.pop(to_delete_index) # delete dict from local list
        header, row = [i.upper() for i in table_range.keys()], [table_range.values()]
        print(f"\nRemoved from {self.listname_title} list:\n{tabulate(row,header, tablefmt='fancy_grid')}\n")
        
        self.skip() # wait 3 seconds, clearConsole
        #SQL delete matching dict in db
        return CRUD(self.listname).delete(self.dict_to_change)

    def new_dict(self): pass # redefine/overload in child classes with corresponding dict template

    def insert_dict(self):
        """Append new_dict() returned dictionary to self.dictslist"""
        data = self.new_dict() # makes new_dict() as data
        self.dictslist.append(data) # adds data dict to self.dictslist
        self.wait() # wait 3 seconds, clearConsole
        
        # format inserted dict for table printout
        header, row = [i.upper() for i in data.keys()], [data.values()]
        print(f"\nAdded to {self.listname_title} list:\n{tabulate(row,header, tablefmt='fancy_grid')}\n")

        self.skip() # wait for continue then clear console
        #SQL insert to db operation
        return CRUD(self.listname).create(data)

    def update_dict(self):
        """Calls new_dict(self) to make new dictionary, updates dictionary at prompted index if new_dict not none."""
        self.get_dicts()
        indexToUpdate = self.selector(self.dictslist, self.listname, "update")
        oldDict = self.dictslist[indexToUpdate] # cache oldDict and entries to update
        print(f"Updating {self.listname[:-1]} id: {oldDict['id']}\n")

        # make new dict to compare and update old dict at dictslist. local list update operation
        updateOrdersValues = self.new_dict()
        self.dictslist[indexToUpdate].update({k:v for k, v in updateOrdersValues.items() if v and (k != 'status')})
        self.wait() # wait 3 seconds, clearConsole

        # format updated dict for printout
        table_range = {k.upper():v for k,v in self.dictslist[indexToUpdate].items() if k != 'id'}
        header, row = table_range.keys(), [table_range.values()]
        print(f"{self.listname_title[:-1]} id {self.id_op} updated to:\n{tabulate(row,header, tablefmt='fancy_grid')}\n")
        
        self.skip() # wait for continue then clear console
        #SQL: select from table vars matching id value of oldDict, update with last updated self.dictslist[indexToUpdate]
        return CRUD(self.listname).update(self.dict_to_change)

class Products(BaseFunctions): ##Products Class
    def __init__(self, filename="products"):
        super(Products, self).__init__(filename)
        for dicts in self.dictslist: dicts['price'] = float(dicts['price'])

    def new_dict(self):
        """Overrided new_dict() in BaseFunctions. Returns dictionary with products dictionary template"""
        newDict = {
            "name": str(input("Enter new product name: ")),
            "price": input("Enter new product price: ")}
        try: newDict['price'] = float(newDict['price']) # convert price input to float
        except ValueError: newDict['price'] = None
        finally: return newDict

class Couriers(BaseFunctions): ##Couriers Class
    def __init__(self, filename="couriers"):
        super(Couriers, self).__init__(filename)

    def new_dict(self):
        """Overrided new_dict() in BaseFunctions. Returns dictionary with couriers dictionary template"""
        newDict = {
            "name": input("Enter new courier name: "),
            "phone": input("Enter new courier phone no.: ")}
        return newDict

class Orders(BaseFunctions): ##Orders class
    def __init__(self, filename="orders"):
        """Pass ProductsObj.dictslist and CouriersObj.dictslist as args on obj initialisation"""
        super(Orders, self).__init__(filename)
        #set names for printouts
        self.products_list_name, self.couriers_list_name = "Products", "Couriers"
        self.menu_options = [f"\n{self.listname_title} Menu Options:\n", f"  1:  Show {self.listname} list", f"  2:  Insert {self.listname[:-1]}",
                             f"  3:  Update existing {self.listname[:-1]} status", f"  4:  Update existing {self.listname[:-1]}",
                             f"  5:  Remove {self.listname[:-1]}", f"  0:  Return to main menu"]
        #formats orders list dicts
        for dicts in self.dictslist:
            dicts['courier'] = int(dicts['courier'])

    def show_couriers(self):
        """Shows couriers list, returns prompted integer index of assigned courier"""
        self.couriers = CRUD("couriers").read()
        print("~~~ASSIGN A COURIER ID TO ORDER~~~\n")
        self.display_table(self.couriers, self.couriers_list_name)
        try: choice = int(input("Enter id of courier to assign to this order: "))
        except ValueError: choice = None
        finally:
            self.wait() # wait 3 seconds, clearConsole
            return choice

    def items_ordered(self):
        """Shows products list, returns prompted list of ordered products indexes"""
        self.products = CRUD("products").read()
        print("~~~ASSIGN ORDERED ITEMS ID TO ORDER~~~\n")
        self.display_table(self.products, self.products_list_name)
        try: itemsIntList = [int(i) for i in input("Enter comma-separated product id values: ").split(',')]
        except ValueError: itemsIntList = None
        finally:
            self.wait() # wait 3 seconds, clearConsole
            return f"{itemsIntList}"

    def new_dict(self):
        """Overrided new_dict() in BaseFunctions. Returns dictionary with orders dictionary template"""
        newDict = {
            "customer_name": str(input("Enter customer name: ")),
            "customer_address": str(input("Enter customer address: ")),
            "customer_phone": str(input("Enter customer phone number: ")),
            "courier": self.show_couriers(),
            "status": 1,
            "items": self.items_ordered()}
        return newDict

    def update_order_status(self):
        """Updates order status at user chosen dictionary index."""
        self.get_dicts()
        #prompt id value
        indexupd = self.selector(self.dictslist, self.listname, "update status of")
        oldDict = self.dictslist[indexupd] # store oldDict for comparison with SQL query
        tempstatus = oldDict['status'] # store value at selected index for later printing
        self.status_list = CRUD("order_status").read()
        #Print status_list options
        print(f"~~~UPDATING STATUS OF ORDER ID: {oldDict['id']}~~~\n")
        self.display_table(self.status_list, "Order status")
        #status_list = [{"id":1, "status":"PREPARING"}, {"id":2, "status":"READY FOR DELIVERY"}, {"id":3, "status":"OUT FOR DELIVERY"}, {"id":4, "status":"DELIVERED"}]
        
        # prompt choice and update status at id of self.dictslist corresponding to id val.
        try: prompt_status_update = int(input("Enter the id of the new status you want to assign to order: "))
        except ValueError as e: return print(f"Error: {e}. Try again!")
        self.dict_to_change['status'] = prompt_status_update
        self.wait() # wait 3 seconds, clearConsole
        
        # confirm local dictslist status update operation completed
        print(f"Updated status of order id {oldDict['id']}:\n", f"        from \"{tempstatus}\"\n",
              f"          to \"{self.dictslist[indexupd]['status']}\"!")
        
        self.skip() # wait for continue then clear console
        #SQL: try from order table update order status with entry matching oldDict field values
        return CRUD(self.listname).update(self.dict_to_change)