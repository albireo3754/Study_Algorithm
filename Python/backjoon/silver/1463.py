import sys

X = int(sys.stdin.readline())

dp = [0, 0]

for i in range(2, X + 1):
    a, b, c = sys.maxsize, sys.maxsize, sys.maxsize
    if i % 3 == 0:
        a = dp[i // 3] + 1
    if i % 2 == 0:
        b = dp[i // 2] + 1
    c = dp[i - 1] + 1
    dp.append(min(a, b, c))

print(dp[X])