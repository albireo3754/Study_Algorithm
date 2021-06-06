import sys

input = sys.stdin.readline
N = int(input())

arr = [0 for i in range(10001)]

for i in range(N):
    n = int(input())
    arr[n] += 1


for i, v in enumerate(arr):
    while v > 0:
        print(i)
        v -= 1
