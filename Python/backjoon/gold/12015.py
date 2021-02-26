import sys
import bisect

input = sys.stdin.readline

N = int(input())

arr = [0] + list(map(int, input().split(' ')))

dp = [0 for i in range(N + 1)]
v = [-1 for i in range(N + 1)]
for i in range(1, N + 1):
    dp[i] = 1
    v[i] = -1
    for j in range(1, i):
        if arr[i] > arr[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            v[i] = j
len_max = 0
idx_max = 0

for i in range(1, N + 1):
    if dp[i] > len_max:
        len_max = dp[i]
        idx_max = i
print(len_max)
result = []
while idx_max >= 0:
    result.append(arr[idx_max])
    idx_max = v[idx_max]

print(*result[::-1])