import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

T = int(input().rstrip())

answer = []

for i in range(T):
    k = int(input().rstrip())
    max_q = []
    max_q_trash = defaultdict(int)
    min_q = []
    min_q_trash = defaultdict(int)
    size = 0

    for _ in range(k):
        print(max_q, min_q)
        oper, _num = input().split(' ')
        num = int(_num)
        if oper == "I":
            size += 1
            heapq.heappush(max_q, -1 * num)
            heapq.heappush(min_q, num)
        elif oper == "D" and size > 0:
            if num == -1:
                min = heapq.heappop(min_q)
                while max_q_trash[min] > 0:
                    max_q_trash[min] -= 1
                    min = heapq.heappop(min_q)
                min_q_trash[min] += 1
                
            elif num == 1:
                max = -heapq.heappop(max_q)
                while min_q_trash[max] > 0:
                    min_q_trash[max] -= 1
                    max = -heapq.heappop(max_q)
                max_q_trash[max] += 1
                
            size -= 1
            if size == 0:
                max_q = []
                max_q_trash.clear()
                min_q = []
                min_q_trash.clear()
    if size == 0:
        print("EMPTY")
        continue
    min, max = 0, 0
    while True:
        min = heapq.heappop(min_q)
        if max_q_trash[min] == 0:
            break;
        max_q_trash[min] -= 1
    
    while True:
        max = -heapq.heappop(max_q)
        if min_q_trash[max] == 0:
            break;
        min_q_trash[max] -= 1
    print(max, min)