import random
import sys

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
     
  +---+
  O   |
      |
      |
     ===''', '''
     
  +---+
  O   |
  |   |
      |
     ===''', '''
     
  +---+
  O   |
 ⧸|   |
      |
     ===''', '''
     
  +---+
  O   |
 ⧸|⧹   |
      |
     ===''', '''
     
  +---+
  O   |
 ⧸|⧹   |
 ⧸    |
     ===''', '''
     
  +---+
  O   |
 ⧸|⧹   |
 ⧸ ⧹   |
     ===''']
# stores pictures of hangman for word art to be used in game
words = 'ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar','cow', 'coyote', 'crow', 'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra'
# list of words used in hangman game
def getRandomWord(wordList):
     # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord): # sets up display board
    print(HANGMAN_PICS[len(missedLetters)])

    print('Category: Animals')

    print()

    print('Missed letters:', missedLetters)

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Show the secret word with spaces in between each letter.
        print(letter, end=' ')


def getGuess(alreadyGuessed): # validates guess
    while True:
        print()
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            if guess == secretWord:
                print('Yes! The secret word is', secretWord, '! You have won!')
                sys.exit()
                # determines if user inputs entire correct word and ends game early accordingly
            else:
                print('Please enter a single letter.')

        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsOngoing = True

while gameIsOngoing:
    displayBoard(missedLetters, correctLetters, secretWord)

 # Let the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord and len(guess) == 1 :
        correctLetters = correctLetters + guess

# Check if the player has won.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is', secretWord, '! You have won!')
            gameIsOngoing = False
    else:
        missedLetters = missedLetters + guess

# Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +
                   str(len(missedLetters)) + ' missed guesses and ' +
                   str(len(correctLetters)) + ' correct guesses,'"the word was ", secretWord)
            gameIsOngoing = False