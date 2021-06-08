import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

cristals = [list(map(int, input().split())) for i in range(N)]
bags = [int(input()) for i in range(K)]

cristals.sort()
bags.sort()

pq = []
i = 0
answer = 0
for bag in bags:
    while i < N and cristals[i][0] <= bag:
        heapq.heappush(pq, -cristals[i][1])
        i += 1
    if pq:
        value = -heapq.heappop(pq)
        answer += value
print(answer)