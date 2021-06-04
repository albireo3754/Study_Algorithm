import sys

input = sys.stdin.readline

N = int(input())
a, b = map(int, input().split())
M = int(input())
childs = [[] for i in range(N + 1)]
parents = [[] for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for _ in range(M):
    parent, child = map(int, input().split())
    childs[parent].append(child)
    parents[child].append(parent)

def dfs(a):
    stack = []
    stack.append((a, 0))
    visited[a] = True
    while stack:
        i, v = stack.pop()
        if i == b:
            return v
        for j in childs[i]:
            if visited[j]:
                continue
            visited[j] = True
            stack.append((j, v + 1))
        for j in parents[i]:
            if visited[j]:
                continue
            visited[j] = True
            stack.append((j, v + 1))
    return -1
print(dfs(a))