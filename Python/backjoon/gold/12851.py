import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split(' '))

visited = [0 for i in range(100001)]
def bfs():
    q = deque()
    q.append((0, N))
    visited[N] = 0
    fast = 99999999999
    cnt = 0
    while q:
        # print(q)
        t, here = q.popleft()
        if t > fast:
            continue
        if here == K:
            fast = t
            cnt += 1
            continue
        
        for next in (here + 1, here - 1, here * 2):
            if 0 <= next <= 100000:
                if visited[next] == 0 or visited[next] >= t + 1:
                    q.append((t + 1, next))
                    visited[next] = t + 1

    print(fast)
    print(cnt)
bfs()