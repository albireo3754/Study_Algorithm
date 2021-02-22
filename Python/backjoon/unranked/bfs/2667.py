import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

grid = [[0] * (N + 2)]
for i in range(N):
    grid.append(list(map(int, list('0' + input().rstrip() + '0'))))
grid.append([0] * (N + 2))
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    count = 1
    while q:
        x, y = q.pop()
        for x_, y_ in direction:
            if grid[x + x_][y + y_] == 1:
                q.append((x + x_, y + y_))
                grid[x + x_][y + y_] = 0
                count += 1
    return count


answer = []
for i in range(N + 1):
    for j in range(N + 1):
        if grid[i][j] == 1:
            grid[i][j] = 0
            answer.append(bfs(i, j))
answer.sort()
print(len(answer))
for i in answer:
    print(i)
