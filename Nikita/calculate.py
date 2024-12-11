#CALCULATION FUNCTIONS FOR SPECIFIC USER INPUTS
import random

def calculate_action(decision, cash, stock_dict):

    #Buy
    if decision==1:
        cash=cash-stock_dict["price"]
        stock_dict["quantity"]=stock_dict["quantity"]+1

    #Sell
    elif decision==2:
        stock_dict["quantity"]=stock_dict["quantity"]-1
        cash+=stock_dict["price"]

    #update stock price
    stock_dict["price"]=stock_dict["price"]*(random.random()+0.5)

    return stock_dict, cash
