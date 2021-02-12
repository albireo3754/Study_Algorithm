import sys
from collections import defaultdict
    

input = sys.stdin.readline

TC = int(input())
inf = 123456789876

for _ in range(TC):
    N, M, W = map(int, input().split(' '))
    edges = defaultdict(list)
    for _ in range(M):
        S, E, T = map(int, input().split(' '))
        edges[S].append((E, T))
        edges[E].append((S, T))
    for _ in range(W):
        S, E, T = map(int, input().split(' '))
        edges[S].append((E, -T))
    distance = [0, 0]
    for i in range(2, N + 1):
        distance.append(inf)
    isNegative = False
    for check in range(1, N + 1):
        for start in range(1, N + 1):
            for end, weight in edges[start]:
                if distance[end] > distance[start] + weight:
                    distance[end] = distance[start] + weight;
                    if check == N:
                        isNegative = True

    if isNegative == True:
        print("YES")
    else:
        print("NO")
