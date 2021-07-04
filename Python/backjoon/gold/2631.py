import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

dp = [arr[0]]

for i in range(1, N):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        j = bisect.bisect_left(dp, arr[i])
        dp[j] = arr[i]

print(N - len(dp))