# This program intends to count total number of integers in an array divisible by a particular number.

a = [int(x) for x in input().split()]
count = 0
for i in range(a[0], a[1]+1):
    ans = i % a[2]
    if ans == 0:
        count = count + 1
    else:
        continue
print(count)
