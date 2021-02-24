import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))

grid = []
for i in range(N):
    grid.append(list(map(int, input().split(' '))))

def copy_grid(grid):
    return [i[:] for i in grid]

blanks = []

for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            blanks.append((i, j))
can_make_wall = list(combinations(blanks, 3))
q = deque()
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(i, j, grid):
    q.append((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if (0 <= ni < N) and (0 <= nj < M):
                if grid[ni][nj] == 0:
                    q.append((ni, nj))
                    grid[ni][nj] = 2
    
answer = []
for x, y, z in can_make_wall:
    new_grid = copy_grid(grid)
    new_grid[x[0]][x[1]] = 1
    new_grid[y[0]][y[1]] = 1
    new_grid[z[0]][z[1]] = 1
    for i in range(N):
        for j in range(M):
            if new_grid[i][j] == 2:
                bfs(i, j, new_grid)

    cnt = 0
    for i in new_grid:
        cnt += i.count(0)
    answer.append(cnt)


print(max(answer))