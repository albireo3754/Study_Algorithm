import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split(' '))

grid = []
for i in range(N):
    grid.append(list(input().rstrip()))
INF = 100000
visited = [[INF for _ in range(M)] for _ in range(N)]
direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

def bfs():
    q = deque()
    q.append((0, 0, 0))
    while q:
        i, j, w = q.popleft()
        # print(i, j, w)
        if i == N - 1 and j == M - 1:
            return w
        for d, (di, dj) in enumerate(direction):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if w >= visited[ni][nj]:
                    continue
                visited[ni][nj] = w
                if grid[ni][nj] == '0':
                    q.appendleft((ni, nj, w))
                else:
                    q.append((ni, nj, w + 1))

print(bfs())
