import sys
from collections import deque
input = sys.stdin.readline

N, M, K = list(map(int, input().split()))

grid = [[0 for i in range(M)] for i in range(N)]

for _ in range(K):
    a, b, c, d = list(map(int, input().split()))
    for i in range(a, c):
        for j in range(b, d):
            # print(i, j)
            grid[j][i] = 1

visited = [[False for i in range(M)] for i in range(N)]

direction = ((1, 0), (0, 1), (0, -1), (-1, 0))
def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = True
    answer = 1
    while q:
        i, j = q.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == True or grid[ni][nj] == 1:
                    continue
                visited[ni][nj] = True
                answer += 1
                q.append((ni, nj))
    return answer

areas = []
count = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and visited[i][j] == False:
            print(i, j)
            areas.append(bfs(i, j))
            count += 1

print(count)
print(*sorted(areas))