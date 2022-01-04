# list BaseFunctions object class
import os.path, sys, csv

class BaseFunctions: #"filenames.csv"
    #obj constructor
    def __init__(self, filename: str, dictslist=None):
        #reusable var init
        self.filepath = os.path.join(sys.path[0], str(filename))
        self.filename = str(filename)
        self.listname = self.filename[:-4]
        self.listname_title = self.listname.title()
        self.dictslist = dictslist
        #fileloading
        if self.dictslist is None:
            try:
                with open(self.filepath, 'r') as file:
                    self.dictslist = [dicts for dicts in csv.DictReader(file)]
                    print(f"Loaded {self.filename} into {self.listname} list.\n")
            except FileNotFoundError:
                with open(self.filepath, 'w') as file:
                    self.dictslist = []
                    print(f"Cannot find {self.filename} in app folder, made new {self.filename}\n")
    
    #write to file on object destructor call        
    def save_file(self):
        with open(self.filepath, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.dictslist[0].keys())
            writer.writeheader()
            writer.writerows(self.dictslist)    
    
    # list dicts in dictslist
    def show_dicts(self):
        print(f"{self.listname_title} list contains:\n")
        for i, item in enumerate(self.dictslist):
            print(f"{self.listname_title[:-1]} Index {i}: {item}")
    
    # list dicts, prompt index of choice, remove dict at index
    def delete_dict(self):
        self.show_dicts()
        indexdel = int(input(f"\nEnter the index of the {self.listname[:-1]} you want to remove: "))
        print(f"Removed \"{self.dictslist.pop(indexdel)}\" from {self.listname_title} list!\n")
    
    # redefine/overload in child classes with corresponding dict template
    def new_dict(self): pass
    
    # append new_dict() to dictslist
    def insert_dict(self):
        self.dictslist.append(self.new_dict())
        return f"Added {self.dictslist[-1]} to {self.listname_title} list!"

    # list dicts, 
    def update_dict(self):
        self.show_dicts()
        indexToUpdate = int(input(f"\nSelect index of {self.listname[:-1].lower()} to update: "))
        # cache oldDict and entries to update
        oldDict = self.dictslist[indexToUpdate]
    
        # if input is blank/noneType do not update respective dict property, else update
        print(f"Updating {self.listname[:-1]}: {oldDict}\n")
        updateOrdersValues = self.new_dict()
        
        # update old dict
        self.dictslist[indexToUpdate].update({k:v for k, v in updateOrdersValues.items() if v and (k != 'status')})
        
        # confirmation of updated order
        print(f"{self.listname_title[:-1]} index {indexToUpdate} updated to:\n {self.dictslist[indexToUpdate]}")

##Products Class
class Products(BaseFunctions):
    def __init__(self, *args, **kwargs):
        super(Products, self).__init__(*args, **kwargs)
        for dicts in self.dictslist: dicts['price'] = float(dicts['price'])

    # override new_dict()
    # make new and return products dictionary
    def new_dict(self):
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
            return newDict

##Couriers Class
class Couriers(BaseFunctions):
    def __init__(self, *args, **kwargs):
        super(Couriers, self).__init__(*args, **kwargs)

    # override new_dict()
    # make new and return couriers dictionary
    def new_dict(self):
        newDict = {
        "name": input("Enter new courier name: "),
        "phone": input("Enter new courier phone no.: ")
        }
        return newDict

##Orders class
class Orders(BaseFunctions):
    # pass ProductsObj.dictslist and CouriersObj.dictslist as args on obj initialisation
    def __init__(self, filename, productslist, courierslist):
        super(Orders, self).__init__(filename, dictslist=None)
        self.products, self.products_list_name = productslist, "products"
        self.couriers, self.couriers_list_name = courierslist, "couriers"
        for dicts in self.dictslist:
            dicts['courier'] = int(dicts['courier'])
            dicts['items'] = [int(i) for i in dicts['items'].strip("][").split(",")]
    
    # new show other lists for showing any lists with args
    def show_other_list(self, other_list, list_name: str):
        print(f"{list_name.title()} list contains:\n")
        for i, item in enumerate(other_list):
            print(f"{list_name.title()[:-1]} Index {i}: {item}")
    
    # shows couriers list, returns prompted integer index of assigned courier
    def show_couriers(self):
        self.show_other_list(self.couriers, self.couriers_list_name)
        try:
            choice = int(input("Enter index of courier to assign to this order: "))
        except ValueError:
            choice = None
        finally: return choice

    # shows products list, returns prompted list of ordered products integer indexes
    def items_ordered(self):
        self.show_other_list(self.products, self.products_list_name)
        itemsIntList = [int(i) for i in input("Enter comma-separated product index values: ").split(',')]
        return itemsIntList
    
    # override new_dict()
    # makes new order dictionary, returns new dictionary
    def new_dict(self):
        newDict = {
            "customer_name": input("Enter customer name: "),
            "customer_address": input("Enter customer address: "),
            "customer_phone": input("Enter customer phone number: "),
            "courier": self.show_couriers(),
            "status": "PREPARING",
            "items": self.items_ordered() #multiple inheritance for obj values?
        }
        return newDict
    
    def update_order_status(self):
        self.show_dicts()
        indexupd = int(input(f"\nEnter the order index of the status you want to change: "))
        # store value at selected index for later printing
        indextempstatus = self.dictslist[indexupd]['status']
        
        # print status list options, update index value
        statuslist = ["PREPARING", "READY FOR DELIVERY", "OUT FOR DELIVERY", "DELIVERED"]
        for i, status in enumerate(statuslist):
            print(f"  {i}: {status}")
        
        self.dictslist[indexupd]['status'] = statuslist[int(input("Enter order status index to update: "))]
        
        # cleanup output and confirm operation completed\
        print(f"Updated order index {indexupd} status:\n",
              f"        from \"{indextempstatus}\"\n",
              f"          to \"{self.dictslist[indexupd]['status']}\"!")
# 165 lines, 36 comment lines, total code lines: 129