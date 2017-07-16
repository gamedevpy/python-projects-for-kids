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
## Did not follow the recipe in the book chapter- merely
## implemented myself based on the specifications outlined
## in the book chapter.
##
##------------------------------------------------------

# imported libraries go here
import os
import collections
import random
from colorama import Fore, Back, Style

# global variables go here
game_on = None

players_list = []

player_count = 0


def reset_game():


    global players_list
    
    global player_count

    players_list = []
    
    player_count = 0


def add_personal_items(new_player_lookup):

    print("Now add your personal items")

    for j in range(4):
    
        item_num = j + 1
        
        while True:

            item = raw_input('Enter name of item %d : ' % item_num)

            if len(item) > 0:

                if item in new_player_lookup['items_list'].keys():
                    
                    print("You already have that item in your backpack, please try something else.")                    
                else:
                    
                    new_player_lookup['items_list'][item] = 'personal'
                    
                    break
            else:
                print("You need to enter something.  Please try again.")


def add_extra_items(new_player_lookup):
    
    print("Now add some exta items")
    
    for k in range(4):
        
        item_num = k + 1

        while True:
    
            item = raw_input('Enter name of item %d : ' % item_num)

            if len(item) > 0:        
                if item in new_player_lookup['items_list'].keys():
        
                    print("You already have that item in your backpack, please try something else.")                    
        
                else:
        
                    new_player_lookup['items_list'][item] = 'extra'
        
                    break

            else:
                print("You need to enter something.  Please try again.")



def initialize_game():

    global player_count

    global players_list


    players_list  = []

    for i in range(player_count):

        os.system('cls' if os.name == 'nt' else 'clear')

        num = i + 1
        
        player_name = raw_input('Enter name for player %d : ' % num)
        
        new_player_lookup = {}
        
        new_player_lookup['name'] = player_name
        
        new_player_lookup['score'] = 0
        
        new_player_lookup['items_list'] = {}

        add_personal_items(new_player_lookup)

        add_extra_items(new_player_lookup)
           
        printGreen('Backpack is ready for %s' % player_name)

        players_list.append(new_player_lookup)


def begin_challenge():

    os.system('cls' if os.name == 'nt' else 'clear')    
    print("Let the challenge begin!")

    play_on = True

    current_player_num = 0

    other_player_num = 1
    
    while (play_on):

        current_player = players_list[current_player_num]
        current_player_name = current_player['name']

        other_player = players_list[other_player_num]
        other_player_name = other_player['name']

        print("%s, it is your turn to guess what personal items are in %s's backpack " % (current_player_name, other_player_name))
        

        other_player_item_dict = other_player['items_list']
        
        display_backpack_items(other_player_item_dict)
        
        good_guess = False

        guess = raw_input("What's your guess? ")

        if len(guess) > 0:
            
            # if guess in other_player_item_dict.keys():
            for key in other_player_item_dict:
                    
                if key == guess:

                    good_guess = True

                    val = other_player_item_dict[key]

                    if val == 'personal':

                        printGreen("Correct!")

                        current_player['score'] = current_player['score'] + 1
            
                        if current_player['score'] == 4:
            
                            printGreen("%s has one the game!!!" % current_player_name)
                            start_game()
        
                    else:
                        printYellow("That is not one of the personal items")
        

                    del other_player_item_dict[guess]
        
        
                    break
        else:
            print("You need to type something.  Please try again.")            
            next

        if not good_guess:
            printRed("Umm, that is not one of the items in the backpack")

        if current_player_num == 1:
            current_player_num = 0
            other_player_num = 1
        else:
            current_player_num = 1
            other_player_num = 0                        


def display_backpack_items(items_dict):

    printBlue("\nHere are the contents of the backpack:")
    
    od = collections.OrderedDict(sorted(items_dict.items()))
    
    for item in od:
    
        print(item)


# function to start game
def start_game():
    
    global game_on

    global player_count

    game_on = True

    reset_game()

    try:
        printBlue('Welcome. How many players?. (0 to quit) ')
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


    
