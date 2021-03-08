import sys
from collections import deque
input = sys.stdin.readline

grid = []

N = int(input())
for i in range(N):
    grid.append(list(map(int, input().split(' '))))

pipe = [[0, 0], [0, 1]]

move = [(0, 1), (1, 0), (1, 1)]

q = deque()
# print(grid)
cnt = 0
q.append((0, 1, 0))
while q:
    r, c, d = q.popleft()
    # print(r, c, d)
    if r == N - 1 and c == N - 1:
        cnt += 1
    for i, (dr, dc) in enumerate(move):
        nr, nc = r + dr, c + dc
        if d < 2 and (d ^ 1) == i:
            continue
        if 0 <= nr < N and 0 <= nc < N:
            if grid[nr][nc] == 1:
                continue
            if i == 2:
                if grid[nr - 1][nc] == 1 or grid[nr][nc - 1] == 1:
                    continue
            # print(nr, nc, i)
            q.append((nr, nc, i))

print(cnt)
