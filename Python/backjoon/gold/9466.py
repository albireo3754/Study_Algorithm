import sys
from collections import deque

input = sys.stdin.readline

for i in range(int(input())):
    N = int(input())
    edge = [0]
    edge.extend(list(map(int, input().split(' '))))
    pre = [0 for i in range(N + 1)]
    for i in range(1, N + 1):
        pre[edge[i]] += 1
    
    q = deque()
    answer = 0
    for i in range(1, N + 1):
        if pre[i] == 0:
            q.append(i)
            answer += 1
    while q:
        here = q.popleft()
        there = edge[here]
        pre[there] -= 1
        if pre[there] == 0:
            q.append(there)
            answer += 1
    print(answer)
            