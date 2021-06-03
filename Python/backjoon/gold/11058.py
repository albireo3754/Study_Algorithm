import sys

input = sys.stdin.readline

N = int(input())

arr = [i for i in range(101)]
for i in range(7, N + 1):
    ret = max(arr[i - 1] + 1, arr[i - 2] + 2)
    for j in range(3, 7):
        ret = max(ret, arr[i - j] * (j - 1))
    arr[i] = ret
print(arr[N])