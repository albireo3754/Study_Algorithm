import sys
from collections import deque

input = sys.stdin.readline

SUCCESS = 1
FAIL = 0
grid = deque([list(input().rstrip()) for i in range(8)])

def fall():
    grid.pop()
    grid.appendleft(['.' for i in range(8)])

direction = ((1, 0), (1, 1), (1, -1), (0, 1), (0, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1))

def bfs():
    q = deque()
    q.append((7, 0, 0))
    time = 0
    while q:
        i, j, n = q.popleft()
        if n == 8:
            return SUCCESS
        if time < n:
            time += 1
            fall()
        
        if grid[i][j] == '#':
            continue
        
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < 8 and 0 <= nj < 8 and grid[ni][nj] == '.':
                q.append((ni, nj, n + 1))
    return FAIL
print(bfs())
