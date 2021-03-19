import sys

input = sys.stdin.readline

N, K = map(int, input().split(' '))
coin = [-1]
for i in range(N):
    coin.append(int(input()))
Inf = 100000001
def coinSum():
    dp = [[Inf for i in range(K + 1)] for i in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            if j == coin[i]:
                dp[i][j] = 1
            if j > coin[i]:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - coin[i]] + 1)
            dp[i][j] = min(dp[i - 1][j], dp[i][j])
    # print(dp)
    if dp[N][K] == Inf:
        return -1
    return dp[N][K]
print(coinSum())