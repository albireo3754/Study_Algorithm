import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split(' '))
edge = [[] for i in range(N + 1)]
hacked = [-1 for i in range(N + 1)]
q = deque()
for i in range(M):
    A, B = map(int, input().split(' '))
    edge[B].append(A)


def bfs(node):
    q.append(node)
    count = 0
    unvisited = [True for i in range(N + 1)]
    unvisited[node] = False
    while q:
        pos = q.popleft()
        for i in edge[pos]:
            if unvisited[i]:
                q.append(i)
                unvisited[i] = False
                count += 1
    hacked[node] = count


answer = []
for i in range(1, N + 1):
    if edge[i]:
        bfs(i)

max_hacked = max(hacked)
for i, v in enumerate(hacked):
    if v == max_hacked:
        answer.append(i)
print(*sorted(answer))
