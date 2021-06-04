import sys

input = sys.stdin.readline

Inf = 10000000
N, M = map(int, input().split())
edge = [[] for i in range(N + 1)]
cost = [Inf for i in range(N + 1)]
for _ in range(M):
    # A -> B T시간  T <= 0 가능 - 벨만포드 , negative edge계산
    A, B, T = map(int, input().split())
    edge[A].append((B, T))
cost[1] = 0

for _ in range(M - 1):
    for here in range(1, N + 1):
        if cost[here] == Inf:
            continue
        for there, w in edge[here]:
            if cost[there] > cost[here] + w:
                cost[there] = cost[here] + w

def isMinus():
    for here in range(1, N + 1):
        for there, w in edge[here]:
            if cost[there] > cost[here] + w:
                return True
    return False

if isMinus():
    print(-1)
else:
    for i in range(2, N + 1):
        if cost[i] == Inf:
            cost[i] = -1
        print(cost[i])
        
        