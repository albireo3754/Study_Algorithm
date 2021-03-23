import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split(' '))
edge = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split(' '))
    edge[a].append(b)
    edge[b].append(a)

for i in range(N + 1):
    edge[i].sort()

visited = [False for i in range(N + 1)]
dfs_answer = [V]
def dfs(node):
    visited[node] = True
    for next in edge[node]:
        if visited[next]:
            continue
        visited[next] = True
        dfs_answer.append(next)    
        dfs(next)
dfs(V)
print(*dfs_answer)
visited = [False for i in range(N + 1)]
bfs_answer = [V]
def bfs(node):
    q = deque()
    visited[node] = True
    q.append(node)
    while q:
        node = q.popleft()
        for next in edge[node]:
            if visited[next]:
                continue
            visited[next] = True
            bfs_answer.append(next)
            q.append(next)
bfs(V)
print(*bfs_answer)
