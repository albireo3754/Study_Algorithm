import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    dp = [0 for i in range(N)]
    for i in range(N):
        if i == 0:
            dp[i] = arr[i]
        else:
            dp[i] = max(dp[i - 1] + arr[i], arr[i])
    print(max(dp))