import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split(' '))

grid = []

for i in range(H):
    if i % 2 == 0:
        grid.append(list(map(int, input().split(' '))))
    else:
        grid.append(list(map(int, input().split(' '))))
direction_odd = [(1, 0), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, -1)]
direction_even = [(1, 0), (1, 1), (0, 1), (0, -1), (-1, 0), (-1, 1)]
direction = [direction_even, direction_odd]
q = deque()
visited = [[0 for i in range(W)] for i in range(H)] 
def bfs(i, j):
    q.append((i, j))
    visited[i][j] = 1
    count = 0
    while q:
        i, j = q.popleft()
        isodd = i % 2
        for dx, dy in direction[isodd]:
            if i + dx >= 0 and j + dy >= 0 and i + dx < H and j + dy < W\
                and grid[i + dx][j + dy] == 1:
                if visited[i + dx][j + dy] == 0:
                    q.append((i + dx, j + dy))
                    visited[i + dx][j + dy] = 1
            else:
                count += 1
    return count


answer = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 1 and visited[i][j] == 0:
            answer += bfs(i, j)


def isInnerHexagon(i, j):
    visited[i][j] = 2
    q.append((i, j))
    count = 0
    while q:
        i, j = q.popleft()
        isodd = i % 2
        for dx, dy in direction[isodd]:
            if i + dx >= 0 and j + dy >= 0 and i + dx < H and j + dy < W:
                if grid[i + dx][j + dy] == 1:
                    count += 1
                else:
                    if visited[i + dx][j + dy] == 0:
                        q.append((i + dx, j + dy))
                        visited[i + dx][j + dy] = 2
            else:
                count = -9999999999
    if count < 0:
        return 0
    else:
        return count

for i in range(H):
    for j in range(W):
        if grid[i][j] == 0 and visited[i][j] == 0:
            answer -= isInnerHexagon(i, j)

print(answer)