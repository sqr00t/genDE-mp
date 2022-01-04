import sys
from MPFunctions import Products, Couriers, Orders
from MPMenus import BaseMenu

class Main(BaseMenu):
    """Display menu and respond to choice on run()"""
    def __init__(self, productslist, courierslist, orderslist):
        super().__init__()
        
        self.products = productslist
        self.couriers = courierslist
        self.orders = orderslist
        
        self.choices = {
            "1": self.products_menu,
            "2": self.couriers_menu,
            "3": self.orders_menu,
            "0": self.exit_menu
        }
        
    def display_menu(self):
        print(
            """
Welcome to Solomon's MiniProject!

Main Menu Options:
    1. Products Menu
    2. Couriers Menu
    3. Orders Menu
    0. Exit App
"""
        )
        
    def products_menu(self): self.products_menu = ProductsMenu(self.products).run()
        
    def couriers_menu(self): self.couriers_menu = CouriersMenu(self.couriers).run()
        
    def orders_menu(self): self.orders_menu = OrdersMenu(self.orders).run()
    
    def exit_menu(self):
        """Exit Main Menu"""
        print("Saving lists and exiting app...")
        self.products.save_lists()
        self.couriers.save_lists()
        self.orders.save_lists()
        sys.exit(0)
        
    
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
    def exit_menu(self):
        self.clearConsole()
        del self
        Main.run()

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
        
    def exit_menu(self):
        self.clearConsole()
        del self
        Main.run()

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
        
    def exit_menu(self):
        self.clearConsole()
        del self
        Main.run()

if __name__ == "__main__":
    products = Products("products.csv")
    couriers = Couriers("couriers.csv")
    orders = Orders("orders.csv", products, couriers)
    
    Main(products, couriers, orders).run()