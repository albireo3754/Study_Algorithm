import sys
from collections import deque
input = sys.stdin.readline

grid = []

N = int(input())
for i in range(N):
    grid.append(list(map(int, input().split(' '))))

pipe = [[0, 0], [0, 1]]

move = [(0, 1), (1, 0), (1, 1)]
dp = [[[0 for i in range(3)] for i in range(N)] for i in range(N)]

for i in range(1, N):
    if grid[0][i] == 1:
        break
    dp[0][i][0] = 1

for i in range(1, N):
    for j in range(2, N):
        if grid[i][j] == 1:
            continue
        if grid[i][j - 1] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        if grid[i - 1][j] == 0:
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
        if grid[i - 1][j - 1] == 0 and grid[i - 1][j] == 0 and grid[i][j - 1] == 0:
            dp[i][j][2] = dp[i - 1][j - 1][0] + \
                dp[i - 1][j - 1][1] + dp[i - 1][j - 1][2]
print(sum(dp[-1][-1]))
# for i in dp:
# print(i)

# q = deque()
# # print(grid)
# cnt = 0
# q.append((0, 1, 0))
# while q:
#     r, c, d = q.popleft()
#     # print(r, c, d)
#     if r == N - 1 and c == N - 1:
#         cnt += 1
#     for i, (dr, dc) in enumerate(move):
#         nr, nc = r + dr, c + dc
#         if d < 2 and (d ^ 1) == i:
#             continue
#         if 0 <= nr < N and 0 <= nc < N:
#             if grid[nr][nc] == 1:
#                 continue
#             if i == 2:
#                 if grid[nr - 1][nc] == 1 or grid[nr][nc - 1] == 1:
#                     continue
#             # print(nr, nc, i)
#             q.append((nr, nc, i))

# print(cnt)
