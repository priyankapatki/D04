#!/usr/bin/env python
# HW04_ch07_ex02

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:

#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes
# the resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

###############################################################################
# Imports


# Body
def eval_loop():
    user_input = ''
    answer = "'none'"      # initializing variable 'answer'
    while user_input != 'done':   # loop will continue till the user enters done  as the input
        user_input = input('Please enter the expression to be evaluated: ')
        try:
            if user_input != 'done':
                answer = eval(str(user_input))
                print('The answer is :' + str(answer))
            else:
                return answer
                break

        except:
            print(" Not a valid expression ")

###############################################################################
def main():
    
    a = eval_loop()
    print('The last answer was ' + str(a))

if __name__ == '__main__':
    main()
