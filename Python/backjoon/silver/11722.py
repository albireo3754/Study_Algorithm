import sys
import bisect
input = sys.stdin.readline

N = int(input())
arr = list(reversed(list(map(int, input().split()))))
dp = [1 for i in range(N)]
lis = [arr[0]]

for i in range(1, N):
    if lis[-1] < arr[i]:
        lis.append(arr[i]) 
        dp[i] = len(lis)
    else:
        idx = bisect.bisect_left(lis, arr[i])
        dp[i] = idx + 1
        lis[idx] = arr[i]
# print(dp)
print(len(lis))