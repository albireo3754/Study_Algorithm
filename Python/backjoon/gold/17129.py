import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, list(input().rstrip()))) for i in range(N)]

def find_2():
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                return i, j
i, j = find_2()
direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
def bfs(i, j):
    q = deque()
    visited=[[False for i in range(M)] for i in range(N)]
    q.append((i, j, 0))
    visited[i][j] = True

    while q:
        i, j, v = q.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                if grid[ni][nj] == 1:
                    continue
                if grid[ni][nj] > 1:
                    return v + 1
                visited[ni][nj] = True
                q.append((ni, nj, v + 1))
    return 0
answer = bfs(i, j)
if answer == 0:
    print("NIE")
else:
    print("TAK")
    print(answer)