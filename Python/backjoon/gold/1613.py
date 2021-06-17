import sys

input = sys.stdin.readline

n, k = map(int, input().split())

edge = [[-1 for i in range(n + 1)] for i in range(n + 1)]
for i in range(k):
    a, b = map(int, input().split())
    edge[a][b] = 1

for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if edge[j][i] == 1 and edge[i][k] == 1:
                edge[j][k] = 1

s = int(input())
for i in range(s):
    a, b = map(int, input().split())
    if edge[a][b] == 1:
        print(-1)
    elif edge[b][a] == 1:
        print(1)
    else:
        print(0)
    