import sys
import math
input = sys.stdin.readline

n = int(input())

edge = [[0 for i in range(n)] for i in range(n)]
before = [-1 for i in range(n)]
for i in range(n - 1):
    a, b, p, q = map(int, input().split(' '))
    if p > q:
        edge[a][b] = p / q
        before[b] = a
    else:
        edge[b][a] = q / p
        before[a] = b

ratio = [0 for i in range(n)]
for i in range(n):
    if before[i] == -1:
        ratio[i] = 1
    else:
        acc = 1
        j = i
        while before[j] >= 0:
            temp = before[j]
            acc *= edge[temp][j]
            j = temp
        ratio[i] = acc
