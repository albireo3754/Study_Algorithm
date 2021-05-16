import sys

input = sys.stdin.readline

k, n = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

start = int(input())

for a, b in arr:
    if a == start:
        start = b
    elif b == start:
        start = a
print(start)