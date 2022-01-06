import os.path, sys, csv
# 132 lines with comments and docstrings. 14 docstrings lines, 1 comment line. total: 117 lines
class BaseFunctions: # list BaseFunctions object class. Pass to args: "filenames.csv"
    def __init__(self, filename: str, dictslist=None):
        """Inits obj with BaseFunctions class."""
        self.filepath = os.path.join(os.path.dirname(__file__), '..', 'data/', str(filename))
        self.filename = str(filename)
        self.listname = self.filename[:-4]
        self.listname_title = self.listname.title()
        self.dictslist = dictslist
        self.menu_options = [f"\n{self.listname_title} Menu Options:\n", f"  1:  Show {self.listname} list", f"  2:  Insert {self.listname[:-1]}",
                             f"  3:  Update existing {self.listname[:-1]}", f"  4:  Remove {self.listname[:-1]}", f"  0:  Return to main menu"]
        if self.dictslist is None:
            try:
                with open(self.filepath, 'r') as file:
                    self.dictslist = [dicts for dicts in csv.DictReader(file)]
                    print(f"Loaded {self.filename} into {self.listname} list.")
            except FileNotFoundError:
                with open(self.filepath, 'w') as file:
                    self.dictslist = []
                    print(f"Cannot find {self.filename} in app folder, made new {self.filename}")

    def save_file(self):
        """Save self.dictslist list of dictionaries to .csv file"""
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.dictslist[0].keys())
            writer.writeheader(), writer.writerows(self.dictslist)
    
    def show_dicts(self):
        """Lists dicts in self.dictslist"""
        print(f"{self.listname_title} list contains:\n")
        for i, item in enumerate(self.dictslist): print(f"{self.listname_title[:-1]} Index {i}: {item}")
    
    def delete_dict(self):
        """List dicts in self.dictslist, prompts user for index of choice, remove dict at index"""
        self.show_dicts()
        indexdel = int(input(f"\nEnter the index of the {self.listname[:-1]} you want to remove: "))
        print(f"Removed \"{self.dictslist.pop(indexdel)}\" from {self.listname_title} list!\n")
    
    def new_dict(self): pass # redefine/overload in child classes with corresponding dict template
    
    def insert_dict(self):
        """Append new_dict() returned dictionary to self.dictslist"""
        self.dictslist.append(self.new_dict())
        return f"Added {self.dictslist[-1]} to {self.listname_title} list!"

    def update_dict(self):
        """Calls new_dict(self) to make new dictionary, updates dictionary at prompted index if new_dict not none."""
        self.show_dicts()
        indexToUpdate = int(input(f"\nSelect index of {self.listname[:-1].lower()} to update: "))
        oldDict = self.dictslist[indexToUpdate] # cache oldDict and entries to update
        print(f"Updating {self.listname[:-1]}: {oldDict}\n")
        updateOrdersValues = self.new_dict()
        self.dictslist[indexToUpdate].update({k:v for k, v in updateOrdersValues.items() if v and (k != 'status')})
        print(f"{self.listname_title[:-1]} index {indexToUpdate} updated to:\n {self.dictslist[indexToUpdate]}")

class Products(BaseFunctions): ##Products Class
    def __init__(self, *args, **kwargs):
        super(Products, self).__init__(*args, **kwargs)
        for dicts in self.dictslist: dicts['price'] = float(dicts['price'])

    def new_dict(self):
        """Overrided new_dict() in BaseFunctions. Returns dictionary with products dictionary template"""
        newDict = {
            "name": input("Enter new product name: "),
            "price": input("Enter new product price: ")}
        try: newDict['price'] = float(newDict['price']) # convert price input to float
        except ValueError: newDict['price'] = None
        finally: return newDict

class Couriers(BaseFunctions): ##Couriers Class
    def __init__(self, *args, **kwargs):
        super(Couriers, self).__init__(*args, **kwargs)

    def new_dict(self):
        """Overrided new_dict() in BaseFunctions. Returns dictionary with couriers dictionary template"""
        newDict = {
            "name": input("Enter new courier name: "),
            "phone": input("Enter new courier phone no.: ")}
        return newDict

class Orders(BaseFunctions): ##Orders class
    def __init__(self, filename, productslist, courierslist):
        """Pass ProductsObj.dictslist and CouriersObj.dictslist as args on obj initialisation"""
        super(Orders, self).__init__(filename, dictslist=None)
        self.products, self.products_list_name = productslist, "products"
        self.couriers, self.couriers_list_name = courierslist, "couriers"
        self.menu_options = [f"\n{self.listname_title} Menu Options:\n", f"  1:  Show {self.listname} list", f"  2:  Insert {self.listname[:-1]}",
                             f"  3:  Update existing {self.listname[:-1]} status", f"  4:  Update existing {self.listname[:-1]}",
                             f"  5:  Remove {self.listname[:-1]}", f"  0:  Return to main menu"]
        for dicts in self.dictslist: dicts['courier'], dicts['items'] = int(dicts['courier']), [int(i) for i in dicts['items'].strip("][").split(",")]
        
    def show_other_list(self, other_list, list_name: str):
        """New show other lists for showing any lists with args"""
        print(f"{list_name.title()} list contains:\n")
        for i, item in enumerate(other_list): print(f"{list_name.title()[:-1]} Index {i}: {item}")

    def show_couriers(self):
        """Shows couriers list, returns prompted integer index of assigned courier"""
        self.show_other_list(self.couriers, self.couriers_list_name)
        try: choice = int(input("Enter index of courier to assign to this order: "))
        except ValueError: choice = None
        finally: return choice

    def items_ordered(self):
        """Shows products list, returns prompted list of ordered products indexes"""
        self.show_other_list(self.products, self.products_list_name)
        try: itemsIntList = [int(i) for i in input("Enter comma-separated product index values: ").split(',')]
        except ValueError: itemsIntList = None
        finally: return itemsIntList
    
    def new_dict(self):
        """Overrided new_dict() in BaseFunctions. Returns dictionary with orders dictionary template"""
        newDict = {
            "customer_name": input("Enter customer name: "),
            "customer_address": input("Enter customer address: "),
            "customer_phone": input("Enter customer phone number: "),
            "courier": self.show_couriers(),
            "status": "PREPARING",
            "items": self.items_ordered()}
        return newDict
    
    def update_order_status(self):
        """Updates order status at user chosen dictionary index."""
        self.show_dicts()
        indexupd = int(input(f"\nEnter the order index of the status you want to change: "))
        indextempstatus = self.dictslist[indexupd]['status'] # store value at selected index for later printing
        statuslist = ["PREPARING", "READY FOR DELIVERY", "OUT FOR DELIVERY", "DELIVERED"]
        for i, status in enumerate(statuslist): print(f"  {i}: {status}") #Print statuslist options, update with prompted index value
        self.dictslist[indexupd]['status'] = statuslist[int(input("Enter order status index to update: "))]
        print(f"Updated order index {indexupd} status:\n", f"        from \"{indextempstatus}\"\n",
              f"          to \"{self.dictslist[indexupd]['status']}\"!") #confirm operation completed