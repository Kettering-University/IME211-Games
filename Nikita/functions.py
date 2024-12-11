#GET USER INPUT WHILE REROUTING THEM IF ITS NOT IN RANGE
def get_input(cash, stock_dict):

    func = int(input("Enter the action you would like to take(1.BUY 2.SELL 3.HOLD):"))
    while func not in range(1,4):
        print("Invalid action type...must be 1-3!")
        func = int(input("Enter the action you would like to take(1.BUY 2.SELL 3.HOLD):"))
        # Buy
    while func == 1 and cash < stock_dict["price"]:
        print("Insufficient funds")
        func = int(input("Enter the action you would like to take(1.BUY 2.SELL 3.HOLD):"))

        # Sell
    while func == 2 and stock_dict["quantity"] < 1:
        print("Insufficient stock owned")
        func = int(input("Enter the action you would like to take(1.BUY 2.SELL 3.HOLD):"))
    return func







