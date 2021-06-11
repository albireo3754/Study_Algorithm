import sys

input = sys.stdin.readline

N = int(input())

arr = [int(input()) for i in range(N)]

answer = 0
arr.sort(reverse=True)
for i, v in enumerate(arr):
    answer = max(answer, (i + 1) * v)
print(answer)

