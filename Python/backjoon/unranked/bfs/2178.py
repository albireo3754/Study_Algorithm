import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))

grid = ['0' * M]
for i in range(N):
    grid.append(input().rstrip())
grid.append('0' * M)
for i in range(len(grid)):
    grid[i] = '0' + grid[i] + '0'
    grid[i] = list(map(int, list(grid[i])))
direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def bfs():
    q = deque()
    q.append((1, 1, 1))
    while q:
        x, y, t = q.popleft()
        if x == N and y == M:
            print(t)
            return
        t += 1
        for i, j in direction:
            if grid[x + i][y + j] == 1:
                q.append((x + i, y + j, t))
                grid[x + i][y + j] = 0


bfs()
