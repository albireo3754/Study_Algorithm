import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split(' '))

grid = []
for i in range(N):
    grid.append(list(input().rstrip()))

visited = [[False for _ in range(M)] for _ in range(N)]
direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0] = True
    while q:
        i, j, w = q.popleft()
        if i == N - 1 and j == M - 1:
            return w
        visited[i][j] = True
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj]:
                    continue
                if grid[ni][nj] == '0':
                    q.appendleft((ni, nj, w))
                else:
                    q.append((ni, nj, w + 1))

print(bfs())
