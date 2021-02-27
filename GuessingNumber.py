#This is a program of number guessing

from random import randrange
import sys

#This is the main menu display, with 3 different option, each option leads to minor functions
def menu_display():
    print('**********Menu************')
    print('1: Start game')
    print('2: Choose the difficulty')
    print('3: Close game')
    option = input('Choose an option:')
    #The variable option must be a int value
    try:
        option = int(option)
    except():
        print('Choose a valid option')
        menu_display()
    if option == 1:
        game(3)
    elif option == 2:
        set_difficulty()
    elif option == 3:
        sys.exit()
    elif option > 3 or option < 1:  #In case the option selected is bigger than 3 or smaller than 1
        print('Choose a valid option')
        menu_display()

# In this function we set up the difficulty, if easy = 3 lives, medium = 5 lives, hard = 7 lives
def set_difficulty():
    print('**********Set the difficulty************')
    print('1: Easy')
    print('2: Medium')
    print('3: Hard')
    option = input('Choose an option:')
    try:
        option = int(option)
    except():
        print('Choose a valid option')
        menu_display()
    if option == 1:
        game(7)
    elif option == 2:
        game(5)
    elif option == 3:
        game(3)
    elif option > 3 or option < 1:
        print('Choose a valid option')
        set_difficulty()

#The game structure is meant to compare the input value with the random generated value
#In case the guessing is bigger the program displays the message 'The value is higher'
#In case the guessing is smaller the program displays the message 'The value is lower'
#In case the guessing is equal the program displays the message 'CONGRATULATIONS YOU WIN'
def game(lives):
    value = randrange(20)  # generates a random value between 0 and 20
    while lives != 0:
        guessing = int(input('Enter your guessing:'))
        if guessing == value:
            print('CONGRATULATION YOU WIN')
            break
        elif guessing > value:
            lives -= 1
            print('You have',lives,'lives remaining')
            print('The value is lower')
        elif guessing < value:
            lives -= 1
            print('You have',lives,'lives remaining')
            print('The value is higher')
    print('The value was: ', value)
    menu_display()


print('Try guessing the number between 0 - 20')     #Game introduction first displayed
print('***************************************')
menu_display()
