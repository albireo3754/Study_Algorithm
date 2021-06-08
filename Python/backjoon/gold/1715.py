import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
heapq.heapify(arr)

answer = 0
while len(arr) > 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    heapq.heappush(arr, a + b)
    answer += a + b
print(answer)
