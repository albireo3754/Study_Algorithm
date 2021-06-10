import sys
import heapq

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
L, P = map(int, input().split())

pq = []
searched = 0
arr.sort()
answer = 0
fuel = P
idx = 0
while True:
    if fuel >= L:
        print(answer)
        break
    while idx < N and fuel >= arr[idx][0]:
        heapq.heappush(pq, -arr[idx][1])
        idx += 1
    if len(pq) == 0:
        print(-1)
        break
    fuel += -heapq.heappop(pq)
    answer += 1
# while pq:
#     a = -heapq.heappop(pq)
#     # print(a, b, c)
#     while searched < N:
#         if arr[searched][0] < fuel:
#             heapq.heappush(-arr[searched][1])
            
#     if b >= L:
#         print(a)
#         break
#     for i in range(c + 1, N):
#         if b < arr[i][0]:
#             break
#         heapq.heappush(pq, (a + 1, b + arr[i][1], i))
# else:
#     print(-1)

# pq = [(P, 0, -1)]

# arr.sort()
# while pq:
#     b, a, c = heapq.heappop(pq)
#     # print(b, a, c)
#     if b >= L:
#         print(a)
#         break
#     for i in range(c + 1, N):
#         if b < arr[i][0]:
#             break
#         heapq.heappush(pq, (b + arr[i][1], a + 1, i))
# else:
#     print(-1)