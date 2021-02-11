import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

V, E = map(int, input().split(' '))
start = int(input())

edge = defaultdict(list)
for i in range(E):
    u, v, w = map(int, input().split(' '))
    edge[u].append((v, w))

path = [float("inf") for i in range(V + 1)]
path[start] = 0
q = []
for i in range(1, V + 1):
    if i == start:
        heapq.heappush(q, (0, i))
    else:
        heapq.heappush(q, (float("inf"), i))

def dijkstra(q):
    while q:
        _, u = heapq.heappop(q)
        for v, w in edge[u]:
            if path[v] > path[u] + w:
                path[v] = path[u] + w
                heapq.heappush(q, (path[u] + w, v))

dijkstra(q)
for i in range(1, V + 1):
    if path[i] == float("inf"):
        print("INF")
    else:
        print(path[i])