# A program to allow a boy named Roy to upload a square picture.
# Inputs given are - l=length of picture, n=total no. of pictures, a=array of height and width per picture.

l = int(input())
n = int(input())

for i in range(1, n+1):
    a = [int(x) for x in input().split()]
    if a[0] < l or a[1] < l:
        print("UPLOAD ANOTHER")
    elif a[0] != a[1]:
        print("CROP IT")
    else:
        print("ACCEPTED")
