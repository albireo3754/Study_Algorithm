import sys
from collections import defaultdict

input = sys.stdin.readline

V = int(input())

trees = defaultdict(list)

for i in range(V):
    v_inf = list(map(int, input().split(' ')))
    v_inf.pop()
    v = v_inf[0]
    for j in range(1, len(v_inf), 2):
        trees[v].append((v_inf[j], v_inf[j + 1]))

visited = {}
def dfs(distance, node):
    if node in visited:
        return
    visited[node] = distance

    for i in trees[node]:
        dfs(distance + i[1], i[0])
dfs(0, 1)
max_from_1 = sorted(visited.items(), key = lambda x: -x[1])[0]
visited.clear()
dfs(0, max_from_1[0])
max_from_from_1 = sorted(visited.items(), key = lambda x: -x[1])[0]
print(max_from_from_1[1])