#!/usr/bin/env python
# HW04_ch08_ex05


# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.

###############################################################################


# Find the ord('a') and ord('z') based on the case of the character c
def limit(c):
    if c.islower():
        a = ord('a')
        z = ord('z')
    else:
        a = ord('A')
        z = ord('Z')
    return (a, z)

def round_off(r):
    if r < 0:
        return ((abs(r) % 26) * -1)
    return (abs(r) % 26)

def rotate_word(word, num):
    new_word = ''
    num = round_off(num) 
    for c in word:
        (a, z) = limit(c)
        nc = ord(c) + num
       
        if nc < a:
            # rotate left
            nc = z - (a - nc) + 1
        elif nc > z:
            # rotate  right          
            nc = a + (nc - z) - 1
        new_word += chr(nc)
    
    return new_word


def main():
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('CHEER', 7))
    print(rotate_word('MELON', -10))
    print(rotate_word('abc', 3))
    print(rotate_word('abc', -29))
    print(rotate_word('ABC', -52))
    print(rotate_word('abc', 2))
    print(rotate_word('abc', -3))
    print(rotate_word('abc', 26))
    print(rotate_word('abc', 52))




if __name__ == '__main__':
    main()
