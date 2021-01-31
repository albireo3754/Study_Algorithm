import heapq


def solution(operations):
    maxq = []
    minq = []
    q = 0
    for i in operations:
        cmd, num_str = i.split(' ')
        num = int(num_str)
        if cmd == 'I':
            q += 1
            heapq.heappush(maxq, -num)
            heapq.heappush(minq, num)
        elif cmd == 'D' and q > 0:
            q -= 1
            if num == 1:
                heapq.heappop(maxq)
            else:
                heapq.heappop(minq)
            if q == 0:
                maxq, minq = [], []
    return [-heapq.heappop(maxq), heapq.heappop(minq)] if q > 0 else [0, 0]
