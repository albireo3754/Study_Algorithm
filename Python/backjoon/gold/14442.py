import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(map(int, list(input().rstrip()))) for i in range(N)]
# print(grid)
direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs():
    i, j = 0, 0
    q = deque()
    visited = [[[False for i in range(11)] for i in range(M)] for i in range(N)]
    q.append((i, j, 0, 1))
    while q:
        i, j, v, answer = q.popleft()
        # print(i, j, v, answer)
        if i == N - 1 and j == M - 1:
            return answer
        for nd, (di, dj) in enumerate(direction):
            ni, nj = i + di, j + dj
            # print(nd, ni, nj)
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj][v]:
                   continue
                if grid[ni][nj] == 1:
                    if v + 1 > K:
                        continue
                    q.append((ni, nj, v + 1, answer + 1))
                else:
                    q.append((ni, nj, v, answer + 1))
                visited[ni][nj][v] = True
    return -1
    # print(visited)    

# if N == 1 and M == 1:
#     print(2)
#     # print(bfs())
# else:
print(bfs())