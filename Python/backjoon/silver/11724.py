import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
N, M = map(int, input().split(' '))
edges = defaultdict(list)
for i in range(M):
    u, v = map(int, input().split(' '))
    edges[u].append(v)
    edges[v].append(u)

visited = set()
def dfs(find):
    if find in visited:
        return
    visited.add(find)
    for i in edges[find]:
        dfs(i)

answer = 0
for key in range(1, N + 1):
    if key in visited:
        continue
    dfs(key)
    answer += 1        
print(answer)