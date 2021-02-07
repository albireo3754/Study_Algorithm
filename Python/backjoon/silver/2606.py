from collections import defaultdict

N = int(input())
edge_N = int(input())

edges = defaultdict(list)

for i in range(edge_N):
    x, y = map(int,input().split())
    edges[x].append(y)
    edges[y].append(x)

visited = [0 for i in range(N + 1)]

def dfs(node):
    if visited[node]:
        return
    visited[node] = 1

    for i in edges[node]:
        dfs(i)

dfs(1)

print(sum(visited) - 1)
