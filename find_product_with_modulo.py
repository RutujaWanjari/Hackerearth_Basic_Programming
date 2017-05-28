# This program illustrates how to find the product of all the number in an array Modulo (10^9)+7.

import sys

n = int(sys.stdin.readline())
a = input().split()
a = [int(x) for x in a]
answer = 1

for i in a:
    answer = (answer * i) % ((pow(10, 9)) + 7)

print(answer)
