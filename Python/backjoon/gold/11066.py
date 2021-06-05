import sys

input = sys.stdin.readline

T = int(input())

INF = float("inf")

def td(arr, start, end):
    # print(arr)
    # print(start, end)
    if start == end:
        return 0
    if dp[start][end] != -1:
        return dp[start][end]
    if start + 1 == end:
        dp[start][end] = 0
        return dp[start][end]
    if start + 2 == end:
        dp[start][end] = arr[start] + arr[start + 1]
        return dp[start][end]

    ret = INF
    for i in range(start + 1, end):
        td(arr, start, i)
        td(arr, i, end)
        ret = min(ret, (dp[start][i] + dp[i][end])) 
    dp[start][end] = ret + pre_sum[end] - pre_sum[start]
    return dp[start][end]
# print(td([40,30,30,50], 0, 4))
# print(dp)
for i in range(T):
    dp = [[-1 for i in range(501)] for i in range(501)]
    kruth = [[0 for i in range(501)] for i in range(501)]
    for i in range(1, 501):
        kruth[i - 1][i] = i
    N = int(input())
    arr = list(map(int, input().split()))
    pre_sum = [0 for i in range(502)]
    for i in range(len(arr)):
        pre_sum[i + 1] = pre_sum[i] + arr[i]
    # print(arr)

    print(td(arr, 0, len(arr)))
    # print(dp)