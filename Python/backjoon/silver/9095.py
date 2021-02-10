import sys

input = sys.stdin.readline

T = int(input())

def dp(n):
    if n == 1 or n == 2:
        return n
    arr = [1 for i in range(n + 1)]
    arr[1] = 1
    arr[2] = 2
    arr[3] = 4
    for i in range(4, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    return arr[n]

for i in range(T):
    print(dp(int(input())))