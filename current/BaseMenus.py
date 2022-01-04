from os import system, name

class BaseMenu:
    """Display menu and respond to choice on run()"""
    def __init__(self):
        self.choices = {}
    
    def clearConsole(self): return system('cls') if name == 'nt' else system('clear')
     
    def display_menu(self): pass
    
    def run(self):
        """Display menu and respond to choice"""
        self.clearConsole()
        self.display_menu()
        choice = str(input("Enter an option index: "))
        action = self.choices.get(choice)
        if action:
            self.clearConsole()
            action()
        else:
            print(f"{choice} is not a valid choice")
            return self.run()
    
    def exit_menu(self):
        """BaseMenu: Exit this Menu"""
        self.clearConsole()
        del self

class ProductsMenu(BaseMenu):
    def __init__(self, productslist):
        super().__init__()
        self.choices = {
            "1": productslist.show_dicts,
            "2": productslist.insert_dict,
            "3": productslist.update_dict,
            "4": productslist.delete_dict,
            "0": self.exit_menu
        }
        
    def display_menu(self):
        print(
            """
Products Menu Options:
    1. Show Products List
    2. Insert New Product
    3. Update Product
    4. Delete Product
    0. Exit Products Menu
"""
        )

class CouriersMenu(BaseMenu):
    def __init__(self, courierslist):
        super().__init__()
        self.choices = {
            "1": courierslist.show_dicts,
            "2": courierslist.insert_dict,
            "3": courierslist.update_dict,
            "4": courierslist.delete_dict,
            "0": self.exit_menu
        }
        
    def display_menu(self):
        print(
            """
Couriers Menu Options:
    1. Show Couriers List
    2. Insert New Courier
    3. Update Courier
    4. Delete Courier
    0. Exit App
"""
        )

class OrdersMenu(BaseMenu):
    def __init__(self, orderslist):
        super().__init__()
        self.choices = {
            "1": orderslist.show_dicts,
            "2": orderslist.insert_dict,
            "3": orderslist.update_order_status,
            "4": orderslist.update_dict,
            "5": orderslist.delete_dict,
            "0": self.exit_menu
        }
        
    def display_menu(self):
        print(
            """
Orders Menu Options:
    1. Show Orders List
    2. Insert New Order
    3. Update Order Status
    4. Update Order Details
    5. Delete Order
    0. Exit App
"""
        )