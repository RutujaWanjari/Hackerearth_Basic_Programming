# A program to toggle a string

import sys

string1 = list(sys.stdin.readline())
string1 = (''.join(c.upper() if c.islower() else c.lower() for c in string1))
print(string1)

