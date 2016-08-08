#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
import random

# Body
def random_guess():
    num = random.randint(1, 25)
    count = 0
    while count < 5:
        try:
            user_input = int(input('Please guess a random number between 1 and 25 = '))
            if (user_input == num):
                print('You got it right!')
                count += 1
                break
            elif(user_input < num):
                print('The number was too low.')
                count += 1
                continue
            else:
                print('The number was too high.')
                count += 1
                continue
        except:
            print('Not a number.')
            count += 1
    else:
        print('The random number was ' + str(num))


################################################################################
def main():

    random_guess()

if __name__ == '__main__':
    main()