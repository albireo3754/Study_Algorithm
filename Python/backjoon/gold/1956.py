import sys

input = sys.stdin.readline

V, E = map(int, input().split())

Inf = 1e8
edge = [[Inf for i in range(V + 1)] for i in range(V + 1)]
# a -> b / w거리
for i in range(E):
    a, b, w = map(int, input().split())
    edge[a][b] = w

distance = [Inf for i in range(V + 1)]
for i in range(V + 1):
    for j in range(V + 1):
        for k in range(V + 1):
            if edge[j][i] + edge[i][k] < edge[j][k]:
                edge[j][k] = edge[j][i] + edge[i][k]

answer = Inf
for i in range(1, V + 1):
    answer = min(answer, edge[i][i])
if answer == Inf:
    print(-1)
else:
    print(answer)