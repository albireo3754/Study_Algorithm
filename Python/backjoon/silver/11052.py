import sys

input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    for j in range(N + 1):
        if j < i:
            dp[j] = dp[j]
            continue
        dp[j] = max(dp[j - i] + arr[i], dp[j])

# for i in dp:
#     print(i)
print(dp[N])