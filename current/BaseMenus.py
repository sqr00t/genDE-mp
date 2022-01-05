from os import system, name

class BaseMenu:
    """Display menu and respond to choice on run()"""
    def __init__(self):
        self.choices = {}
    
    def clearConsole(self): return system('cls') if name == 'nt' else system('clear')
     
    def display_menu(self): pass
    
    def run(self):
        """Display menu and respond to choice"""
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
        pass