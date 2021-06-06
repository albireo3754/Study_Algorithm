import sys
import heapq

input = sys.stdin.readline

N = int(input())
nrr = list(map(int, input().split()))
# print(nrr)
M = int(input())
mrr = list(map(int ,input().split()))

nrr.sort()

def binary_search(a):
    left = 0
    right = N - 1
    while left <= right:
        mid = (left + right) // 2
        if nrr[mid] > a:
            right = mid - 1
        elif nrr[mid] < a:
            left = mid + 1
        else:
            return 1
    return 0

print(*map(binary_search, mrr))