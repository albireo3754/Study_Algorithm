import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
Inf = 1e9
edge = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, w = map(int, input().split(' '))
    edge[a].append((b, w))
start, end = map(int, input().split(' ')) 
print(edge)
def dijkstra(start, end):
    distance = [Inf for i in range(N + 1)]
    before = [0 for i in range(N + 1)]
    distance[start] = 0
    before[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, here = heapq.heappop(q)
        if distance[here] < w:
            continue
        for there, w2 in edge[here]:
            if distance[there] > w + w2:
                distance[there] = w + w2
                before[there] = here
                heapq.heappush(q, (distance[there], there))
    return distance, before
distance, before = dijkstra(start, end)
print(distance[end])
parent = end
path = []

cnt = 0
while parent:
    path.append(parent)
    parent = before[parent]
    cnt += 1
print(cnt)
for i in path[::-1]:
    print(i, end=' ')