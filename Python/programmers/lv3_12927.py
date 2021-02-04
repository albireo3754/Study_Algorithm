import heapq
from functools import reduce
def solution(n, works):
    q = []
    for i in works:
        heapq.heappush(q, -i)

    while n > 0:
        left = heapq.heappop(q)
        if left == 0:
            return 0
        left += 1
        heapq.heappush(q, left)
        n -= 1

    print(q)
    return reduce(lambda acc, cur: acc + cur ** 2, q, 0)
