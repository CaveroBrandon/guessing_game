#This is a program of number guessing

from random import randrange
import sys
lifes = 3

value = randrange(20)
print('Try guessing the number between 0 - 20')
print('***************************************')

while lifes != 0:
    print('Enter your guessing: ')
    guessing = int(input())
    if guessing == value:
        print('Congratulation you win')
        break
    elif guessing > value:
        lifes -= 1
        print('You have',lifes,'lifes remaining')
        print('The value is lower')
    elif guessing < value:
        lifes -= 1
        print('You have',lifes,'lifes remaining')
        print('The value is higher')

print('The value was: ',value)
sys.exit(0)

