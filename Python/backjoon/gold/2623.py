import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))

pre = [0 for i in range(N + 1)]
edge = [[] for i in range(N + 1)]
vistited = [False for i in range(N + 1)]
for i in range(M):
    order = list(map(int, input().split(' ')))
    a, b = 0, 0
    a = order[1]
    for i in range(2, len(order)):
        b = order[i]
        pre[b] += 1
        edge[a].append(b)
        a = b

q = deque()
# print(edge)
# print(pre)
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

if len(answer) == N:
    for i in answer:
        print(i)
else:
    print(0)