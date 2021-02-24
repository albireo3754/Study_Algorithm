import sys

input = sys.stdin.readline

K, N = map(int, input().split())

arr = []
for i in range(K):
    arr.append(int(input()))

left = 1
right = max(arr)
answer = 0
while left <= right:
    mid = (left + right) // 2

    count = 0
    for i in arr:
        count += i // mid
    if count >= N:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
