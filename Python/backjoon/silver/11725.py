import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

N = int(input())
edge = defaultdict(list)
for i in range(N - 1):
    a, b = map(int, input().split(' '))
    edge[a].append(b)
    edge[b].append(a)

parent = [0] * (N + 1)


def dfs(node, before_node):
    if parent[node]:
        return
    parent[node] = before_node
    for i in edge[node]:
        dfs(i, node)


dfs(1, 0)
for i in range(2, len(parent)):
    print(parent[i])
