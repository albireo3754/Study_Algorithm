import sys

input = sys.stdin.readline

N = int(input())
liq = list(map(int, input().split(' ')))
liq.sort()
#가장 가까운 거리
res = abs(liq[-3] + liq[-1] + liq[-2])
answer = [liq[-3], liq[-2], liq[-1]]

for i in range(N - 3):
    fix = i
    left = fix + 1
    right = N - 1
    while left < right:
        if abs(liq[left] + liq[right] + liq[fix]) < res:
            answer = [liq[fix], liq[left], liq[right]]
            res = abs(liq[fix] + liq[left] + liq[right])
        if liq[fix] + liq[left] + liq[right] < 0:
            left += 1
        elif liq[fix] + liq[left] + liq[right] > 0:
            right -= 1
        else:
            break
    else:
        continue
    break

print(*answer)