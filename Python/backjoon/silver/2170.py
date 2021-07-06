import sys
import bisect

input = sys.stdin.readline

N, C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
sum_arr = sum(arr)

left = 0
right = (arr[-1] - arr[0]) // (C - 1)

def install(mid):
    c = 1
    point = arr[0]
    while c < C:
        idx = bisect.bisect_left(arr, point + mid)
        if idx == len(arr):
            break
        point = arr[idx]
        c += 1
    if c == C:
        return True
    else:
        return False

while left <= right:
    mid = (left + right) // 2
    if install(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
print(answer)
# print(install(3))