import heapq
import sys

input = sys.stdin.readline

N, M, X = map(int, input().split(' '))
edge =[[] for i in range(N + 1)]
for i in range(M):
    a, b, w = list(map(int, input().split(' ')))
    edge[a].append((b, w))

def dijkstra(start):
    q = [(0, start)]
    distance = [9000000 for i in range(N + 1)]
    distance[start] = 0
    while q:
        weight, node = heapq.heappop(q)
        if distance[node] < weight:
            continue
        for end in edge[node]:
            if distance[end[0]] > end[1] + weight:
                distance[end[0]] = end[1] + weight
                heapq.heappush(q, (distance[end[0]], end[0]))
    return distance
back = dijkstra(X)
result = 0
for i in range(1, N + 1):
    if i == X:
        continue
    result = max(result, dijkstra(i)[X] + back[i])
print(result)
