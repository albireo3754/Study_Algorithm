import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))
grid = []
for i in range(N):
    grid.append(list(map(int, input().split(' '))))

time = 0
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(i, j):
    visited = [[2 for i in range(M)] for i in range(N)]
    visited[i][j] = 0

    q = deque()
    q.append((i, j))
    flag = 0
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
                        flag = 1
                        grid[ni][nj] = 0
    return flag
    
while True:
    flag = bfs(0, 0)
    if flag == 0:
        break
    time += 1

print(time)