import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
floor = [-1 for i in range(F + 1)]
direction = [U, -D]
q = deque()
floor[S] = 0
q.append(S)
cnt = 1
while q:
    for i in range(len(q)):
        here = q.popleft()
        for d in direction:
            there = d + here
            if 1 <= there <= F and floor[there] == -1:
                floor[there] = cnt
                q.append(there)
    cnt += 1
print(floor[G] if floor[G] != -1 else 'use the stairs')
