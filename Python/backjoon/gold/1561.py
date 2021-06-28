import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
left = -1
right = 400000000001

def count_child_in_midtime(mid):
    result = M
    for i in arr:
        result += (mid // i)
    return result
result = 0
if N <= M:
    print(N)
else:
    while left <= right:
        mid = (left + right) // 2
        if count_child_in_midtime(mid) < N:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    cnt = 0
    for i in arr:
        cnt += (result // i + 1)

    # print(result)
    # print(cnt)
    # while cnt < N:
    answer = 1
    for i in arr:
        if (result + 1) % i == 0:
            cnt += 1
        if cnt == N:
            break
        answer += 1
    print(answer)
