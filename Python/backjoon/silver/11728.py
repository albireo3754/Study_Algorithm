import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A.extend(B)
A.sort()
print(*A)