import sys
import heapq

input = sys.stdin.readline

N = int(input())
q = []

for i in range(N):
    num = int(input())
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            print(-heapq.heappop(q))
    elif num > 0:
        heapq.heappush(q, -num)
    