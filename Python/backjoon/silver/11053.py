import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = [0]
arr.extend(list(map(int, input().split(' '))))
print(arr)
dp = [0]

x = [[0, 0]]

for i in range(1, len(arr)):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    elif dp[-1] > arr[i]:
        lower_bound = bisect.bisect_left(dp, arr[i])
        dp[lower_bound] = arr[i]
print(len(dp) - 1)
