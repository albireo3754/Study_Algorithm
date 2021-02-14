import sys

input = sys.stdin.readline

n, m = map(int, input().split(' '))

result = 1

for i in range(0, m):
    result = result * (100 - i) // (i + 1)

print(result)