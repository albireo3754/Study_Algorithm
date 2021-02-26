import sys
import bisect
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split(' ')))

# print(arr)

result = 0
temp_result = result
dp = [0 for i in range(N)]
for i in range(0, N):
    dp[i] = arr[i]
    for j in range(0, i):
        if arr[i] > arr[j] and dp[i] < dp[j] + arr[i]:
            dp[i] = dp[j] + arr[i]

print(max(dp))