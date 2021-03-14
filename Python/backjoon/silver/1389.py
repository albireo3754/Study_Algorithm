import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

Inf = 1000000
edge= [[Inf for i in range(N + 1)] for i in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split(' '))
    
    edge[a][b] = 1
    edge[b][a] = 1
for i in range(N + 1):
    edge[i][0] = 0
    edge[i][i] = 0
# 중간 노드
for i in range(1, N + 1):
    # 시작 노드
    for j in range(1, N + 1):
        # 끝 노드
        for k in range(1, N + 1):
            if edge[j][i] + edge[i][k] < edge[j][k]:
                edge[j][k] = edge[j][i] + edge[i][k]
answer = [0 for i in range(N + 1)]

for i in range(0, N + 1):
    answer[i] = sum(edge[i])

print(answer.index(min(answer)))
# bfs version

# edge = [[] for i in range(N + 1)]


# for i in range(M):
#     a, b = map(int, input().split(' '))
#     edge[a].append(b)

# print(edge)

# for i in range(M):
#     for j in range(N):
#         for k in range(N):



