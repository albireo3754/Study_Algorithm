import sys
import bisect
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split(' ')))
dp = []
lis = [0 for i in range(N)]


for i in range(N):
    if i == 0 or dp[-1] < A[i]:
        dp.append(A[i])
        lis[i] = len(dp)
    else:
        j = bisect.bisect_left(dp, A[i])
        lis[i] = j + 1
        dp[j] = A[i]

size = len(dp)
print(size)
answer = []
for i in range(N - 1, -1, -1):
    if size == 0:
        break
    if lis[i] == size:
        size -= 1
        answer.append(A[i])

print(*reversed(answer))