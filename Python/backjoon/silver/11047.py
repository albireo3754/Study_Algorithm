import sys

input = sys.stdin.readline

Inf = 1e9

N, K = map(int, input().split())

arr = [int(input()) for i in range(N)]

arr.sort(reverse=True)

answer = 0
for i in arr:
    if K == 0:
        break
    if i > K:
        continue
    else:
        answer += K // i
        K = K % i
print(answer)