import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
def bfs():
    q = deque()
    q.append(1)
    group = 0
    visited = [-1 for i in range(V + 1)]
    q = deque()
    for i in range(1, V + 1):
        if visited[i] >= 0:
            continue
        q.append(i)
        group = 0
        while q:
            # print(visited)
            group = group ^ 1

            for i in range(len(q)):
                here = q.popleft()
                # if visited[here] == group:
                #     return 'NO'
                visited[here] = group
                for there in edge[here]:
                    if visited[there] == group:
                        return 'NO'
                    if visited[there] >= 0:
                        continue
                    q.append(there)
    
    return 'YES'
for _ in range(T):
    V, E = map(int, input().split())
    edge = [[] for i in range(V + 1)]
    for i in range(E):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
    print(bfs())