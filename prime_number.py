# A program to print prime numbers till the given number.

n = int(input())
for i in range(2, n):
    if all((i % j) != 0 for j in range(2, i)):
        print(i, end=' ')
