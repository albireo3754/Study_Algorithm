import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
dp = [0 for i in range(10001)]
for i in range(n):
    coins.append(int(input()))

coins.sort()

# print(coins)

dp[0] = 1

for i, coin in enumerate(coins):
    for j in range(coin, 10000):
        if i == 0 and j == coin:
            dp[j] = 1
        elif j == coin:
            dp[j] += 1
        elif i == 0:
            dp[j] = dp[j - coin]
        else:
            dp[j] = dp[j - coin] + dp[j]

print(dp[k])
# print(dp[:20])