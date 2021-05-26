import sys
import heapq
from collections import deque
input = sys.stdin.readline

T, n = map(int, input().split())

# process[0] = a ,b , c
#              id time, priority
process = [list(map(int, input().split())) for i in range(n)]


# print(process)
pq = []


start = 0
temp = []
for i in process:
    heapq.heappush(pq, [-i[2], i[0], i[1]])

for _ in range(T):
    # print(pq)
    c, a, b = heapq.heappop(pq)
    # temp = [[c, a, b]]
    # while pq and pq[0][0] == c:
    #     temp.append(heapq.heappop(pq))
    # # print(temp)
    # temp.sort(key=lambda x: -x[1])
    # c, a, b = temp.pop()
    b -= 1
    if b > 0:
        # temp.append([c + 1, a, b])
        heapq.heappush(pq, [c + 1, a, b])

    # pq.extend(temp)
    # heapq.heapify(pq)
    print(a)
    # print(p[0])
    # for i in pq:
    #     pq[i][0] -= 1
    # if p[0][1] > 1:
    #     p[0][1] -= 1
    # else:
        

# for i in process:
#     heapq.heappush(pq, )