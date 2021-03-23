import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))

pre = [0 for i in range(N + 1)]
edge = [[] for i in range(N + 1)]
vistited = [False for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split(' '))
    pre[b] += 1
    edge[a].append(b)

q = deque()
# print(edge)
for i in range(1, N + 1):
    if pre[i] == 0:
        q.append(i)

answer = []
while q:
    here = q.popleft()
    answer.append(here)
    for there in edge[here]:
        # print(there)
        if vistited[there]:
            continue
        pre[there] -= 1
        if pre[there] == 0:
            q.append(there)
print(*answer)