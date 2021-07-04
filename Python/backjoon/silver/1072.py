import sys

input = sys.stdin.readline

x, y = map(int, input().split())

def calc(x, y):
    return y * 100 // x

Z = calc(x, y)
answer = 0

def binary_search(x, y, mid):
    return Z != calc(x + mid, y + mid)
        
left = -1
right = 10000000001
while left <= right:
    mid = (left + right) // 2
    if binary_search(x, y, mid):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer if answer > 0 else -1)