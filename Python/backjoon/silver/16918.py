import sys
from collections import deque
input = sys.stdin.readline

R, C, N = map(int, input().split(' '))
def bomb(R, C, N):
    q = deque()
    grid = []
    for i in range(R):
        grid.append(list(input().rstrip()))
    if N == 1 or N == 0:
        return grid
    
    grid_new = [['O' for i in range(C)] for i in range(R)]
    if N % 2 == 0:
        return grid_new
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    dxs = (1, -1, 0, 0)
    dys = (0, 0, 1, -1)
    def bfs(i, j):
        q.append((i, j))
        grid_new[i][j] = '.'
        grid[i][j] = '.'
        while q:
            x, y = q.pop()
            for dx, dy in direction:
                if x + dx >= 0 and x + dx < R and \
                    y + dy >= 0 and y + dy < C:
                    if grid[x + dx][y + dy] == 'O':
                        q.append((x + dx, y + dy))
                        grid[x + dx][y + dy] = '.'
                    grid_new[x + dx][y + dy] = '.'

    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                bfs(i, j)
    if N % 4 == 3:
        return grid_new

    grid_new_2 = [['O' for i in range(C)] for i in range(R)]
    def bfs(i, j):
        q.append((i, j))
        grid_new_2[i][j] = '.'
        grid_new[i][j] = '.'
        while q:
            x, y = q.pop()
            for dx, dy in direction:
                if x + dx >= 0 and x + dx < R and \
                    y + dy >= 0 and y + dy < C:
                    if grid_new[x + dx][y + dy] == 'O':
                        q.append((x + dx, y + dy))
                        grid_new[x + dx][y + dy] = '.'
                    grid_new_2[x + dx][y + dy] = '.'
    for i in range(R):
        for j in range(C):
            if grid_new[i][j] == 'O':
                bfs(i, j)
    return grid_new_2
        
for i in bomb(R, C, N):
    print(''.join(i))
