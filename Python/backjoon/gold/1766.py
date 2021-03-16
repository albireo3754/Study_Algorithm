import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split(' '))
edge = [[] for i in range(N + 1)]
pre = [0 for i in range(N + 1)]
visitied = [False for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split(' '))
    edge[a].append(b)
    pre[b] += 1

q = []

for i in range(1, N + 1):
    if pre[i] == 0:
        heapq.heappush(q, i)
    
answer = []

while q:
    here = heapq.heappop(q)
    answer.append(here)
    visitied[here] = True
    for there in edge[here]:
        if visitied[there]:
            continue
        pre[there] -= 1

        if pre[there] == 0:
            heapq.heappush(q, there)

print(*answer)