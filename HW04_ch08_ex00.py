#!/usr/bin/env python
# HW04_ch08_ex00
# See 8.7

# The following program counts the number of times the letter 'a' appears in a
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print(count)

# Encapsulate this code in a function named "count", and generalize it so that
# it accepts the string and the letter as arguments.

###############################################################################
# Imports

# Body

def count(word, letter_arg):
    letter_count = 0
    for letter in word:
        if letter == letter_arg:
            letter_count = letter_count + 1
    print(letter_count)


###############################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    count('banana', 'a')
    count('python', 'y')
    count('mississippi', 's')
    count('mississippi', 'p')
    count('mississippi', 'x')
    count('mississippi', 'm')
    count('hhhOOO','O')






if __name__ == '__main__':
    main()
