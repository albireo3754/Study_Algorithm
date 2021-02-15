import sys

input = sys.stdin.readline

N, K = map(int, input().split(' '))

bag = [0]
for i in range(N):
    W, V = map(int, input().split(' '))
    bag.append((W, V))
dp = [[0 for i in range(K + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
    for j in range(K + 1):
        if j < bag[i][0]:
            dp[i][j] = dp[i - 1][j]
            continue
        dp[i][j] = max(dp[i - 1][j], dp[i][j - bag[i][0]] + bag[i][1])

print(dp)
print(dp[N][K])
