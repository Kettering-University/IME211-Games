#DISPLAY FOR EACH DAY
def display_initial_info(stock_dict,cash,days):
    print("-------------------")
    print("Days left:",days)
    print(f"You have: ${cash:.2f}")
    print("You own:",stock_dict["quantity"])
    print(f"Stock Price is: ${stock_dict["price"]:.2f}")

#DISPLAY AFTER DAYS ARE OVER
def display_networth(stock_dict,cash):
    networth=(stock_dict["quantity"]*stock_dict["price"])+cash
    print("-------------------")
    print(f"You ended with : ${cash:.2f}")
    print("You own:", stock_dict["quantity"])
    print(f"Stock Price is: ${stock_dict["price"]:.2f}")
    print()
    print(f"Congratulations your networth is: ${networth:.2f}")
