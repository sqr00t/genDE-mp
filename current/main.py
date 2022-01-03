import sys
from MPFunctions import Products, Couriers, Orders
from MPMenus import BaseMenu, ProductsMenu, CouriersMenu, OrdersMenu

class Main(BaseMenu):
    """Display menu and respond to choice on run()"""
    def __init__(self):
        super(BaseMenu).__init__(self)
        
        self.products = Products("products.csv")
        self.couriers = Couriers("couriers.csv")
        self.orders = Orders("orders.csv", self.products, self.couriers)        
        
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
    
    def products_menu(self): self.products_menu = ProductsMenu(self.products)
        
    def couriers_menu(self): self.couriers_menu = CouriersMenu(self.couriers)
        
    def orders_menu(self): self.orders_menu = OrdersMenu(self.orders)
    
    def exit_menu(self):
        """Exit Main Menu"""
        print("Saving lists and exiting app...")
        sys.exit(0)
        

if __name__ == "__main__":
    Main().run()