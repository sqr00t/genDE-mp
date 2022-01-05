import sys
from os import system, name
from MPFunctions import Products, Couriers, Orders

class Main:
    """Display menu and respond to choice on run()"""
    def __init__(self):
        self.products = Products("products.csv")
        self.couriers = Couriers("couriers.csv")
        self.orders = Orders("orders.csv", self.products.dictslist, self.couriers.dictslist)
    
    def clearConsole(self): return system('cls') if name == 'nt' else system('clear')
     
    def display_menu(self):
        """Clears console output and prints self.menu_options elements. Returns user_choice prompted string."""
        self.clearConsole()
        for opts in self.menu_options: print(opts)
        user_choice = str(input("\nEnter an option index: "))
        return user_choice if user_choice in self.choices else print(f"{user_choice} is not a valid choice")
    
    def main_menu(self):
        self.menu_options = ["Main Menu Options:","  1:  Products Menu",
                "  2:  Couriers Menu","  3:  Orders Menu", "  0:  Exit app"]
        self.choices = {
            "1": self.products_menu,
            "2": self.couriers_menu,
            "3": self.orders_menu,
            "4": self.exit_menu
        }
        return self.display_menu()
    
    def products_menu(self):
        self.menu_options = self.products.menu_options
        self.choices = {
            "1": self.products.show_dicts,
            "2": self.products.insert_dict,
            "3": self.products.update_dict,
            "4": self.products.delete_dict,
            "0": self.exit_menu #TODO make products_menu class with different exit_menu implementation
            }
        return self.display_menu()
    
    def couriers_menu(self):
        self.menu_options = self.couriers.menu_options
        self.choices = {
            "1": self.orders.show_dicts,
            "2": self.orders.insert_dict,
            "3": self.orders.update_dict,
            "4": self.orders.delete_dict,
            "0": self.exit_menu #TODO make couriers_menu class with different exit_menu implementation
            }
        return self.display_menu()
        
    def orders_menu(self):
        self.menu_options = self.orders.menu_options
        self.choices = {
            "1": self.orders.show_dicts,
            "2": self.orders.insert_dict,
            "3": self.orders.update_order_status,
            "4": self.orders.update_dict,
            "5": self.orders.delete_dict,
            "0": self.exit_menu #TODO make orders_menu class with different exit_menu implementation
            }
        return self.display_menu()
        
    def run(self):
        """Display menu and respond to choice"""
        while True:
            choice = self.main_menu()
            action = self.choices.get(choice)
            if action: action()
            else: print(f"{choice} is not a valid choice")
        
    def exit_menu(self):
        """BaseMenu: Exit this Menu"""
        self.clearConsole()
        self.orders.save_file()
        self.couriers.save_file()
        self.orders.save_file()
        print("Saving lists and exiting app...")
        return sys.exit(0)
    
if __name__ == "__main__":
    Main().run()