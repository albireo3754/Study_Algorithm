from sys import stdin
inf = 999999001

input = stdin.readline

n = int(input())
m = int(input())

edge = [[inf for i in range(n)] for i in range(n)]
for i in range(m):
    i, j, w = map(int, input().split(' '))
    edge[i - 1][j - 1] = min(edge[i - 1][j - 1], w)

for i in range(n):
    edge[i][i] = 0

def floyd(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                edge[j][k] = min(edge[j][k], edge[j][i] + edge[i][k])

floyd(n)
for i in range(n):
    for j in range(n):
        if edge[i][j] == inf:
            edge[i][j] = 0
for i in edge:
    print(*i)

