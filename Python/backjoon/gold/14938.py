import heapq
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split(' '))
Inf = 1e9
item = [0]
item.extend(list(map(int, input().split(' '))))
edge = [[] for _ in range(N + 1)]
for i in range(R):
    a, b, w = map(int, input().split(' '))
    edge[a].append((b, w))
    edge[b].append((a, w))


def dijkstra(start):
    distance = [Inf for i in range(N + 1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, here = heapq.heappop(q)
        if distance[here] < w:
            continue
        for there, w2 in edge[here]:
            if distance[there] > w + w2:
                distance[there] = w + w2
                heapq.heappush(q, (distance[there], there))
    return distance

answer = 0
for i in range(1, N - 1):
    temp_answer = 0
    for i, v in enumerate(dijkstra(i)):
        if v <= M:
            temp_answer += item[i]
    answer = max(answer, temp_answer)

print(answer)