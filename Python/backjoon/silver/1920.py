import sys

def binary_search(arr, val):
    first = 0
    last = len(arr) - 1
    while first<=last:
        cen = (first + last) // 2
        if arr[cen] == val:
            return True
        elif arr[cen] > val:
            last = cen - 1
        elif arr[cen] < val:
            first = cen + 1
    return False
N = int(input())
A = list(map(int,sys.stdin.readline().rstrip().split(" ")))
M = int(input())
A.sort()
for i in list(map(int,sys.stdin.readline().rstrip().split(" "))):
    if binary_search(A, i) == True:
        print(1)
    else:
        print(0)
    