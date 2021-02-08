import heapq
import sys

q = []
for i in range(int(input())):
    oper = int(sys.stdin.readline().rstrip())
    
    if oper == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, oper)