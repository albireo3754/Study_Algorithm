import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

n = int(input())

tree = defaultdict(list)

for i in range(n - 1):
    parent, child, weight = map(int, input().split(' '))
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

node_len = len(tree.keys())

visited = [0] * (n + 1)
path = set()
def dfs(node):
    path.add(node)

    for i, w in tree[node]:
        if i in path:
            continue
        visited[i] = visited[node] + w
        dfs(i)
        path.remove(i)

dfs(1)
max_idx = visited.index(max(visited))
visited = [0] * (n + 1)
path.clear()
dfs(max_idx)
print(max(visited))