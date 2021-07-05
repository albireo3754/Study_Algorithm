import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
# H * W
grid = [list(input().rstrip()) for i in range(H)]

direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
def bfs(CC):
    c1, c2 = CC
    # print(c1, c2)
    q = deque()
    i, j = c1
    visited = [[[100000000 for i in range(4)] for i in range(W)] for i in range(H)]
    for nd, (di, dj) in enumerate(direction):
        # print(nd, di, dj)
        ni, nj = i + di, j + dj

        if 0 <= ni < H and 0 <= nj < W and grid[ni][nj] != '*':
            ni, nj = i + di, j + dj
            q.append((ni, nj, nd, 0))
            visited[ni][nj][nd] = 0


    while q:
        i, j, d, n = q.popleft()
        # print(i, j, d, n)
        if c2[0] == i and c2[1] == j:
            return n
        for nd, (di, dj) in enumerate(direction):
            ni, nj = i + di, j + dj
            nn = n
            if nd != d:
                nn += 1
            if 0 <= ni < H and 0 <= nj < W and nn < visited[ni][nj][nd] and grid[ni][nj] != '*':
                    visited[ni][nj][nd] = nn
                    if nd == d:
                        q.appendleft((ni, nj, nd, nn))
                    else:
                        q.append((ni, nj, nd, nn))
    return 0    


CC = []
for i in range(H):
    for j in range(W):
       if grid[i][j] == 'C':
           CC.append((i, j))

print(bfs(CC))