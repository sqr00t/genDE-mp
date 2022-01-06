from os import system, name
from MPFunctions import Products, Couriers, Orders
from MenuClassTemplate import BaseMenu, SubMenu, OrdersMenu

class Main(BaseMenu): # 42 lines including 2 docstrings lines. total 40 lines
    """Initialise app with main menu and load csv to objects."""
    def __init__(self):
        """Display menu and respond to choice on run()"""
        self.productsobj = Products("products.csv")
        self.couriersobj = Couriers("couriers.csv")
        self.ordersobj = Orders("orders.csv", self.productsobj.dictslist, self.couriersobj.dictslist)

    def __del__(self): print("Exiting App...")

    def current_menu(self):
        self.menu_options = ["\nWelcome to Pollen Cafe App!\n","Main Menu Options:","  1:  Products Menu",
                             "  2:  Couriers Menu","  3:  Orders Menu", "  0:  Exit app"]
        self.choices = {
            "1": self.products_menu,
            "2": self.couriers_menu,
            "3": self.orders_menu,
            "0": self.exit_menu}
        return self.display_menu()

    def products_menu(self): SubMenu(self.productsobj).run()

    def couriers_menu(self): SubMenu(self.couriersobj).run()

    def orders_menu(self): OrdersMenu(self.ordersobj).run()

    def exit_menu(self):
        try: #saves files and breaks run() loop
            self.productsobj.save_file()
            self.couriersobj.save_file()
            self.ordersobj.save_file()
            print("Saved lists to files!")
        except: print("Something went wrong trying to save lists to files :(")

if __name__ == "__main__":
    system('cls') if name == 'nt' else system('clear')
    app = Main().run()
    del app