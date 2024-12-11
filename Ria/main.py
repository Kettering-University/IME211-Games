#Main Page that runs the games

#Importing round to get user guess input
import round

#Instructions for the Game
print("""Welcome to Crack the Code!!!
You will be prompted to guess a 4-digit code. 
Input a 4-digit guess. Each digit can range from 0-9. Numbers can be repeated.
After each guess you will receive feedback (uppercase "X" indicates the number is in the CORRECT POSITION, while a lowercase "x" indicates 
the number is in the code but in WRONG POSITION.)
You will only be given 8 attempts.
Good Luck!!!""")
print("""----------------------------------------------""")

#calls the round page for users guess input
guess = round.new_round()

