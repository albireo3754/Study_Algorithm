import sys
import heapq
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, idx = map(int, input().split())
    arr = list(map(int, input().split()))
    pq = [-arr[i] for i in range(N)]
    q = deque([[i, -arr[i]] for i in range(N)])
    current = q[idx][1]
    answer = 1
    heapq.heapify(pq)
    while pq[0] < current:
        if pq[0] == q[0][1]:
            answer += 1
            heapq.heappop(pq)
            q.popleft()
        else:
            q.append(q.popleft())
    while q and q[0][0] != idx:
        if q[0][1] == current:
            answer += 1
            q.popleft()
        else:
            q.append(q.popleft())
    
    print(answer)
