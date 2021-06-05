import sys
from collections import deque
input = sys.stdin.readline

N, W, L = map(int, input().split())

# N = len(arrs)
arrs = list(map(int, input().split()))
# arrs => 무게리스트
# w -> 길이
# L 다리 최대하중

time = 0
q = deque()
weight = 0
truck = 0
while not(len(arrs) == truck and len(q) == 0):
    # print(q)
    time += 1
    for i in q:
        i[1] += 1
    
    if len(q) > 0 and q[0][1] == W:
        out_truck_weight = q.popleft()[0]
        weight -= out_truck_weight

    if len(arrs) > truck and weight + arrs[truck] <= L:
        q.append([arrs[truck], 0])
        weight += arrs[truck]
        truck += 1
print(time)