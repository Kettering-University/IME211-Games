# IMPORT FUNCTION FROM EACH PY
from functions import get_input
from calculate import calculate_action
from display import display_networth
from display import display_initial_info
import random

#PRINTOUTS TO WELCOME THE USER
print("Welcome to a Stock Trading game, where you will become filthy rich or homeless.")
print("Here are the instructions:")

print("You will be given 10 days and 500$ to make as much money as possible.")
print("I will provide you with options to BUY(Number 1 on the keypad), SELL(Number 2 on the keypad), OR HOLD(Number 3 on the keypad)")
print("Be careful because you only get to make one choice a day.")
print("GOOD LUCK!!!\n")

#BASE INFO FOR THE GAME
stock_dict = {"price":100,"quantity":0}
cash = 500
days = 10
decision=["buy","sell","hold"]

# Loop for each day
while days > 0:
    display_initial_info(stock_dict,cash,days)
    func = get_input(cash, stock_dict)
    stock_dict, cash = calculate_action(func, cash, stock_dict)
    days -= 1
display_networth(stock_dict,cash)







