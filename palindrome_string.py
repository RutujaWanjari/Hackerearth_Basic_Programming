# A program to check whether a string is palindrome or not.

import sys

my_str = sys.stdin.readline()

# remove newline character-"\n" from string.
my_str = my_str.rstrip()

# *************** ONE WAY *****************
# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("It is palindrome")
else:
    print("It is not palindrome")

# ************** ANOTHER WAY ***************
# the [::-1] slice inverts the string
if str(my_str) == str(my_str)[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")
