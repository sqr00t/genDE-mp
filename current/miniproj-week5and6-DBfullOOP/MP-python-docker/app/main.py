from os import system, name
from core.MPFunctions import Products, Couriers, Orders
from core.MenuClassTemplate import BaseMenu, SubMenu, OrdersMenu

class Main(BaseMenu):
    """Initialise app with main menu and load csv to objects."""
    def __init__(self):
        """Display menu and respond to choice on run()"""
        self.productsobj, self.couriersobj, self.ordersobj = Products(), Couriers(), Orders()

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
    # Runs Products Menu using vars SubMenu class, and functions from arg=self.productsobj
    def couriers_menu(self): SubMenu(self.couriersobj).run()
    # Runs Couriers Menu using vars SubMenu class, and functions from arg=self.couriersobj
    def orders_menu(self): OrdersMenu(self.ordersobj).run()
    # Runs Orders Menu using vars from OrdersMenu class, and functions from arg=self.couriersobj
    def exit_menu(self):
        prompt_export = str(input("Do you want to export lists to local .csv? (y/n): "))
        try:
            if prompt_export == "y" or prompt_export == "Y":
                self.productsobj.export_file()
                self.couriersobj.export_file()
                self.ordersobj.export_file()
                print("Saved lists to files!")
            elif prompt_export == "n" or prompt_export == "N":
                print("Cached dictslists data will be purged!")
            else: print("Incorrect option, app will exit without exporting local files.")
        finally: del self.productsobj, self.couriersobj, self.ordersobj

if __name__ == "__main__":
    system('cls') if name == 'nt' else system('clear')
    Main().run()