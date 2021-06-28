import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))

start, end = map(int, input().split())

def bfs(limit):
    q = deque()
    q.append(start)
    visited = [False for i in range(N + 1)]
    while q:
        here = q.popleft()
        if here == end:
            return True
        for there, weight in edges[here]:
            if weight >= limit and not visited[there]:
                visited[there] = True
                q.append(there)
    return False

left = 0
right = 1000000000
answer = 0
while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)