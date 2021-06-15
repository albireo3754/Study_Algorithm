import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for i in range(M)]
# parent = [0 for i in range(N + 1)]
edge = [[0 for i in range(N + 1)] for i in range(N + 1)]
for i in arr:
    edge[i[0]][i[1]] = 1
    # edge[i[1]][i[0]] = 1

for i in range(1, N + 1):
    edge[i][i] = 1
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if edge[j][i] == 1 and edge[i][k] == 1:
                edge[j][k] = 1

# print(edge)
for i in range(1, N + 1):
    answer = N
    for j in range(1, N + 1):
        if edge[i][j] == 1 or edge[j][i] == 1:
            answer -= 1
    print(answer)
