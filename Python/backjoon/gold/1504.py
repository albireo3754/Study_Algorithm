import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split(' '))
edge = [{} for i in range(N + 1)]
inf = 9999999999
for i in range(E):
    a, b, c = map(int, input().split(' '))
    if b in edge[a]:
        edge[a][b] = edge[b][a] = min(edge[a][b],c)
    else:
        edge[a][b] = edge[b][a] = c

a, b = map(int, input().split(' '))

def dijkstra(start, end):
    dist = [inf for i in range(N + 1)]
    q = []
    dist[start] = 0
    q.append((0, start))
    while q:
        w, node = heapq.heappop(q)
        if node == end:
            return w
        if dist[node] < w:
            continue
        for next in edge[node].items():
            if dist[next[0]] > next[1] + w:
                dist[next[0]] = next[1] + w
                heapq.heappush(q, (dist[next[0]], next[0]))    
    return inf

answer = min(dijkstra(1, a) + dijkstra (b, N), dijkstra(1, b) + dijkstra (a, N)) + dijkstra(a, b)
print(answer if answer < inf else -1)

