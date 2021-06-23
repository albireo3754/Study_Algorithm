import sys
import bisect
input = sys.stdin.readline
# sys.setrecursionlimit(1000000)

N = int(input())
arr = list(map(int, input().split()))

def div(arr, i, j):
    if i + 1 == j:
        return arr[i:j], 0
    if i + 2 == j:
        if arr[i] <= arr[i + 1]:
            return arr[i:j], 0
        else:
            return arr[j - 1:i - 1:-1], 1
    
    n = (j - i) // 2
    arr1, cnt1 = div(arr, i, i + n)
    arr2, cnt2 = div(arr, i + n, j)
    cnt = cnt1 + cnt2
    # print(arr1, arr2)
    for elem in arr1:
        idx = bisect.bisect_left(arr2, elem)
        cnt += idx
    arr1.extend(arr2)
    arr1.sort()
    return arr1, cnt
print(div(arr, 0, N)[1])
