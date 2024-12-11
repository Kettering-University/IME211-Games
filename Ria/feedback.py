#This page gives the user hints

#Comparing the code to the guess
def provide_feedback(code, guess):
    index = 0
    feedback = ["_", "_", "_", "_"]
    for num in guess:
        if num in code:
            feedback[index] = 'x'   #if lowercase x then the number is in the code somewhere
        index += 1

    index = 0
    for num in guess:
        if num == code[index]:
            feedback[index] = 'X'   #if uppercase X then its in correct position
        index += 1

    hint = "".join(feedback) # .join so the hint doesn't print as a list
    print(hint)

    return feedback
