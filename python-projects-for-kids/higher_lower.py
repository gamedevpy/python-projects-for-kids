##------------------------------------------------------
##
## By: Jessica Ingrassellino
## Publisher: Packt Publishing
## Pub. Date: April 14, 2016
## Web ISBN-13: 978-1-78528-585-1
## Print ISBN-13: 978-1-78217-506-3
##
## Python Projects for Kids
## Chapter 5 - Loops and Logic
##
##------------------------------------------------------

# imported libraries go here
import random
from colorama import Fore, Back, Style

# global variables go here
game_on = None
guesses = None
secret = None

min_value = 0
max_value = 10

# function for easy version
def difficulty_level_easy():
    secret = float(random.randrange(min_value, max_value))
    while game_on:

        try:
            printBlue('Guess a number between %d and %d. ' % (min_value, max_value))
            guess = int(raw_input(''))
            
            if guess > secret:
                print('your guess is too high. Try again.')
            elif guess < secret:
                print('your guess is too low. Try again.')
            elif guess == secret:
                printGreen('You win!')
                play_again()
        except:
            printYellow('Encountered some exception.  Will try again.')
            start_game()

            
# function for hard version
def difficulty_level_hard():
    
    global guesses
    guesses = 3
    for i in range(guesses):
        try:

            printBlue('Guess a number between %d and %d. ' % (min_value, max_value))
            guess = float(raw_input(''))

            if i == 2:
                printRed('Game over. Too many guesses.')
                play_again()
            elif guess > secret:
                print('your guess is too high. Try again.')
            elif guess < secret:
                print('your guess is too low. Try again.')
            elif guess == secret:
                printGreen('You win!')
                play_again()
        except:
            printYellow('Encountered some exception.  Will try again.')
            start_game()

            
# function to start game
def start_game():
    global game_on
    game_on = True
    try:
        printBlue('Welcome. Type easy, hard, or quit. ')
        level = raw_input('')

        if level == 'easy':
            difficulty_level_easy()
        elif level == 'hard':
            difficulty_level_hard()
        elif level == 'quit':
            game_on = False
        else:
            game_on = False
    except:
        printYellow('Encountered some exception.  Will try again.')
        start_game()
        
# function to stop game
def stop_game():
    global game_on
    game_one = False
    
# function calls go here
def play_again():
    global game_on
    game_on = True
    try:
        play = raw_input('Play again? Yes or No. ')
        if play == 'Yes':
            start_game()
        else:
            game_On = 'false'
    except:
        printYellow('Encountered some exception.  Will try again.')
        start_game()

def printBlue(msg):
    print(Fore.BLUE + msg)
    print(Fore.RESET)

def printRed(msg):
    print(Fore.RED + msg)
    print(Fore.RESET)

def printGreen(msg):
    print(Fore.GREEN + msg)
    print(Fore.RESET)

def printYellow(msg):
    print(Fore.YELLOW + msg)
    print(Fore.RESET)


start_game()


    
