#importing functions for time delay and random number generator
import random
from time import sleep

#defining winning value page
def winning_values(bets):

#using random to pick the winning number and defining the numbers to their respective color
    winning_number = random.randint(0, 36)
    # sets of numbers in their respective color
    reds = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
    blacks = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
    green = {0}

#if statements to disclose which color and third the winning number is in
    if winning_number in reds:
        winning_color = "red"
    elif winning_number in blacks:
        winning_color = "black"
    else:
        winning_color = "green"

    if winning_number in range(0, 13):
        winning_third = "first"
    elif winning_number in range(13, 25):
        winning_third = "second"
    else:
        winning_third = "third"

#sleep function to delay the winning print to simulate a rolling ball
    sleep_time = 2
    print("Rolling...")
    sleep(sleep_time)
    print("Rolling...")
    sleep(sleep_time)
    print("Rolling...")
    sleep(sleep_time)
    print("")

#winning number prints and users bet print
    print("You bet on",bets)
    print("")
    print("The winning number is", winning_number)
    print("--------------------------------------------------")
    print("The winning color is", winning_color)
    print("--------------------------------------------------")
    print("The winning third is the", winning_third, "third")
    print("--------------------------------------------------")
    print("")
    print("")


    return winning_number, winning_color, winning_third