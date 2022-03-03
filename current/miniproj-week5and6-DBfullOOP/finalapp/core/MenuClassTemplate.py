from os import system, name

class BaseMenu: # 56 lines including 6 docstrings lines. total 50 lines
    """Display menu and respond to choice on run()"""
    def __init__(self): # placeholder None-value vars for template
        self.choices, self.menu_options = None, None

    def __del__(self): print("Returning to Main Menu!\n")
    
    def display_menu(self):
        """Prints self.menu_options elements. Returns user_choice prompted string."""
        for opts in self.menu_options: print(opts)
        user_choice = str(input("\nEnter an option index: "))
        return user_choice
    
    def current_menu(self):
        """Display current menu printout variables. Override vars for SubMenus child class. Returns res of display_menu: user_choice"""
        return self.display_menu()

    def run(self):
        """Display menu and respond to choice"""
        while True:
            choice = self.current_menu()
            system('cls') if name == 'nt' else system('clear') #clears console output after nav selection
            action = self.choices.get(choice)
            if choice == "0":
                try: action()
                except TypeError: print(action)
                finally: break
            elif action: action()
            else: print(f"'{choice}' is not a valid choice")

class SubMenu(BaseMenu):
    def __init__(self, obj_here):
        """Sets vars for obj_here respective Menu"""
        self.obj_here = obj_here
        self.menu_options = self.obj_here.menu_options
        self.choices = {
            "1": self.obj_here.get_dicts,
            "2": self.obj_here.insert_dict,
            "3": self.obj_here.update_dict,
            "4": self.obj_here.delete_dict,
            "0": f"Exited {self.obj_here.listname_title} Menu..."}

class OrdersMenu(BaseMenu):
    def __init__(self, orders_obj_here):
        """Sets OrdersMenu obj vars"""
        self.orders_obj_here = orders_obj_here
        self.menu_options = self.orders_obj_here.menu_options
        self.choices = {
            "1": self.orders_obj_here.get_dicts,
            "2": self.orders_obj_here.insert_dict,
            "3": self.orders_obj_here.update_order_status,
            "4": self.orders_obj_here.update_dict,
            "5": self.orders_obj_here.delete_dict,
            "0": "Exited Orders Menu"}