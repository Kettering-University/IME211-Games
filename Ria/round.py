#This page generates the code and gets the user guess input

from random import randint as ri
from feedback import provide_feedback

#Generates a random 4-digit code
def new_round():
    code =  str(ri(0,9)) + str(ri(0,9)) + str(ri(0,9)) + str(ri(0,9))
    attempts = 8

    while attempts > 0:   # loop for the user to guess the 4-digit
        guess = input("Enter your 4-digit guess: ")   #guess can be 0-9
        if len(guess) != 4:
            print("Please enter EXACTLY 4-digit guess")  #if the user inputs more or less digits it will reprompt
            continue
        if guess == code:
            print("Congratulations!!!You Cracked the Code!!!")
            break
        else:
            provide_feedback(code, guess)
        attempts -= 1
# Failed to guess the code
    if attempts == 0:
        print("You have failed to Crack the Code.....") # statement if user failed to guess code
        print("The correct code was",code,".") #providing user with the correct code


