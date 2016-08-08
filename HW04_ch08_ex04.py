#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """ This function will return only the value of the first letter
    of the string that has been passed as an argument. This happens because 
    a TRUE or FALSe value is returned no matter what after the first letter
     has been examined, whichcauses the function to end and return the value.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """This function will always return the value as 'True' as
    the if condition has 'c'.islower(), which evaluates the case of the
    character 'c' and not of letters in the string 's'

    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """This function checks each letter in the given string for lower case.
    However, it will return the boolean value based on the last letter of the
    string passed.
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """This function will check every letter for a lower case and
     will return a true value even if there is a single lower case 
    character found. This happens as the value of flag will change to "True"
    due to the OR operator, when the loop encounters a lower case character
    in the string argument.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag



def any_lowercase5(s):
    """This function returns a True value only if all letters in
     the string argument are in lower case.
    """
    for c in s:
        if not c.islower():
            return False
    return True


###############################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")

    print(any_lowercase1('PythoN'))
    print(any_lowercase2('PYTHON'))
    print(any_lowercase3('pythoN'))
    print(any_lowercase5('pytHon'))




if __name__ == '__main__':
    main()
