import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))
grid = []
for i in range(N):
    grid.append(list(map(int, input().split(' '))))

time = 0
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(q):
    visited = [[2 for i in range(M)] for i in range(N)]
    for i,j in q:
        visited[i][j] = 0
    next = deque()
    while q:
        i, j = q.popleft()
        for di, dj in direction:
            ni = di + i
            nj = dj + j
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] > 0:
                if grid[ni][nj] == 0:
                    visited[ni][nj] = 0
                    q.append((ni, nj))
                if grid[ni][nj] == 1:
                    visited[ni][nj] -= 1
                    if visited[ni][nj] == 0:
                        next.append((ni, nj))
                        grid[ni][nj] = 0
    return next
    
next = deque()
next.append((0, 0))
while next:
    next = bfs(next)
    time += 1

print(time - 1)