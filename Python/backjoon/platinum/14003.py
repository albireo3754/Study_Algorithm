# import sys
# import bisect
# input = sys.stdin.readline

# N = int(input())

# A = list(map(int, input().split(' ')))
# dp = []
# lis = [0 for i in range(N)]


# for i in range(N):
#     if i == 0 or dp[-1] < A[i]:
#         dp.append(A[i])
#         lis[i] = len(dp)
#     else:
#         j = bisect.bisect_left(dp, A[i])
#         lis[i] = j + 1
#         dp[j] = A[i]

# size = len(dp)
# print(size)
# answer = []
# for i in range(N - 1, -1, -1):
#     if size == 0:
#         break
#     if lis[i] == size:
#         size -= 1
#         answer.append(A[i])

# print(*reversed(answer))

import sys
import bisect

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(N)]
lis = [arr[0]]

for i in range(1, N):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
        dp[i] = len(lis)
    else:
        j = bisect.bisect_left(lis, arr[i])
        dp[i] = j + 1
        lis[j] = arr[i]

print(dp)
n = max(dp)
answer = []
i = N - 1
while n > 0:
    if dp[i] == n:
        answer.append(arr[i])
        n -= 1
    i -= 1

print(len(answer))
print(*reversed(answer))