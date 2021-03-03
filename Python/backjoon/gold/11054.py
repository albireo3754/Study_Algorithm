import sys
import bisect

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split(' ')))
r_arr = list(reversed(arr))
# print(r_arr)
dp = [0 for i in range(N)]
# v = [-1 for i in range(N + 1)]
r_dp = [0 for i in range(N)]
for i in range(0, N):
    for j in range(0, i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] += 1

for i in range(0, N):
    for j in range(0, i):
        if r_arr[i] > r_arr[j] and r_dp[i] < r_dp[j] + 1:
            r_dp[i] += 1

# print(dp)
# print(r_dp)
result = [0 for i in range(N)]
for i, (a, b) in enumerate(zip(dp, reversed(r_dp))):
    # print(a, b)
    result[i] = a + b + 1
print(max(result))