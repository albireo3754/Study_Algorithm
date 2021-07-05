import sys

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for i in range(N)]
dp = [[0 for i in range(N)] for i in range(N)]

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        jump = grid[i][j]
        if jump == 0:
            continue
        if j + jump < N:
            dp[i][j + jump] += dp[i][j]
        if i + jump < N:
            dp[i + jump][j] += dp[i][j]

print(dp[-1][-1])