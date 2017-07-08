##------------------------------------------------------
##
## By: Jessica Ingrassellino
## Publisher: Packt Publishing
## Pub. Date: April 14, 2016
## Web ISBN-13: 978-1-78528-585-1
## Print ISBN-13: 978-1-78217-506-3
##
## Python Projects for Kids
## Chapter 7 - What's in your backpack?
##
##------------------------------------------------------

# imported libraries go here
import random
from colorama import Fore, Back, Style

# global variables go here
game_on = None

players_lookup = {}

players_count = 0

def initialize_game():

    global player_count

    for i in range(player_count):
        num = i + 1
        player_name = raw_input('Enter name for player %d : ' % num)
        new_player_lookup = {}
        new_player_lookup['name'] = player_name
        new_player_lookup['score'] = 0
        new_player_lookup['items_list'] = []
        for j in range(4):
            item_num = j + 1
            item = raw_input('Enter name of item %d : ' % item_num)
            new_player_lookup['items_list'].append(item)

        printGreen('Backpack is ready for %s' % player_name)


def begin_challenge():
    pass

# function to start game
def start_game():
    
    global game_on

    global player_count

    game_on = True

    try:
        printBlue('Welcome. How many players?. ')
        player_count = int(raw_input(''))

        if player_count > 1:
            initialize_game()
            begin_challenge()
        else:
            printRed('Need at least 2 players')
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


    
