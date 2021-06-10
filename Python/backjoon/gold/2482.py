import sys

input = sys.stdin.readline

N = int(input())
K = int(input())

dp = [[0 for i in range(1001)] for i in range(1001)]
dp[1][1] = 1
dp[2][1] = 2
dp[3][1] = 3
dp[3][2] = 1
for i in range(1, 1000):
    dp[i][1] = i
    dp[i][0] = 1


for i in range(4, N + 1):
    for j in range(2, K + 1):
        dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % 1000000003
print((dp[N - 3][K - 1] + dp[N - 1][K])% 1000000003)