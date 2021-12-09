def ordersmenu():
    ordersopts = ["Return to main menu", "Show orders dictionary", "Add an order",
                    "Update an existing order", "Remove an order",
                    f"Orders Menu: Options\n", "\nChoose an option by entering it's index: "]
    print(ordersopts[-2])
    for i in range(0, len(ordersopts)-2):
        print(f"  {i}:  {ordersopts[i]}")
    choice = int(input(ordersopts[-1]))
    clearConsole()
        
    return choice