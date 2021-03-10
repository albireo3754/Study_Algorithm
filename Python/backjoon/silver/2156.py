import sys

input = sys.stdin.readline

N = int(input())

grape = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
dp[0] = grape[0]
if N > 1:
    dp[1] = grape[0] + grape[1]
for i in range(2, N):
    dp[i] = max(grape[i] + grape[i - 1] + dp[i - 3], grape[i] + dp[i - 2], dp[i - 1])
print(dp[-1])