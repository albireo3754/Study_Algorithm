import sys

input = sys.stdin.readline

N = int(input())

step = [int(input()) for _ in range(N)]

dp = [0 for _ in range(N)]
dp[0] = step[0]
if N == 1:
    print(dp[-1])
else:
    dp[1] = step[0] + step[1]

    for i in range(2, N):
        dp[i] = max(dp[i - 2] + step[i], dp[i - 3] + step[i - 1] + step[i])

    print(dp[-1])