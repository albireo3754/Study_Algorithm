import sys
from collections import defaultdict, deque
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, K = map(int, input().split(' '))
    W = [0]
    W.extend(list(map(int, input().split(' '))))
    edges = defaultdict(list)
    edges_reverse = defaultdict(list)
    pre = [0 for i in range(N + 1)]
    time = [0 for i in range(N + 1)]
    for j in range(K):
        a, b = map(int, input().split(' '))
        edges[a].append(b)
        pre[b] += 1
    destination = int(input())
    q = deque()
    for i in range(1, N + 1):
        if pre[i] == 0:
            q.append(i)
    
    while q:
        node = q.pop()

        for i in edges[node]:
            time[i] = max(time[i], time[node] + W[node])
            pre[i] -= 1
            if pre[i] <= 0:
                q.append(i)
    print(time[destination] + W[destination])