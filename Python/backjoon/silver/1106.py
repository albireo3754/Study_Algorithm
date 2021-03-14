import sys

input = sys.stdin.readline

C, N = map(int, input().split(' '))

price = []

dp = [[-1 for i in range(C + 1)] for i in range(1100 + 1)]
for i in range(N):
    price.append(list(map(int, input().split(' '))))
    price[0] = 
print(price)


for i in range(1, N + 1):
    p, c = price[i - 1]
    for j in range(p, 1100 + 1):
        if dp[i - 1][j] == 0
        dp[i][j] = max(dp[i - 1][j], dp[i][j - p] + c)

print(dp[N][C])