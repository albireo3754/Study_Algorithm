import sys
import bisect

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split(' ')))

dp = [arr[0]]
result = [arr[0]]
temp = [0 for ]
for i in arr:
    if i > dp[-1]:
        dp.append(i)
        result = dp[:]
    elif i == dp[-1]:
        continue
    else:
        idx = bisect.bisect_left(dp, i)
        dp[idx] = i
print(len(result))
print(*result)
