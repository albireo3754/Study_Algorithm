import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for i in range(n + 1)]

for j in range(5, n + 1, 5):
    dp[j] = dp[j - 5] + 1

dp[3] = 1
for j in range(3, n + 1):
    if dp[j - 3] > 0:
        if dp[j] == 0: 
            dp[j] = dp[j - 3] + 1
        else:
            dp[j] = min(dp[j - 3], dp[j])
# print(dp)
if dp[n] == 0:
    print(-1)
else:
    print(dp[n])