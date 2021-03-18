import sys

input = sys.stdin.readline

N = int(input())
liq = list(map(int, input().split(' ')))

def bs(i):
    left, right = i + 1, N - 1
    res = 0
    while left <= right:
        mid = (left + right) // 2
        if abs(liq[i] + liq[left]) < abs(liq[i] + liq[right]):
            right = mid - 1
        else:
            left = mid + 1
        res = mid

    return res
#가장 가까운 거리
res = abs(liq[0] + liq[-1])
answer = [liq[0], liq[-1]]
left = 0
right = N - 1

while left < right:
    if abs(liq[left] + liq[right]) < res:
        answer = [liq[left], liq[right]]
        res = abs(liq[left] + liq[right])
    if liq[left] + liq[right] < 0:
        left += 1
    else:
        right -= 1

print(answer)