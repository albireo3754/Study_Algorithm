import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

arr.sort()
left = 1
right = arr[-1]
def calc(mid):
    result = 0
    for i in range(len(arr)):
        if arr[i] >= mid:
            result += mid * (len(arr) - i)
            break
        result += arr[i]
    return result

assert calc(127) == 484, 'calc(127) == 484'
answer = 0 
while left <= right:
    mid = (left + right) // 2
    if calc(mid) <= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
    # if calc(mid)