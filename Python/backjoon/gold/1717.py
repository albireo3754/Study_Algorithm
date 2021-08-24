import sys
sys.setrecursionlimit = 1000000
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [-1 for i in range(N + 1)]

def union(x, y):
    a, b = find(x), find(y)
    # print(a, b)
    if a == b:
        return
    if a > b:
        arr[a] += arr[b]
        arr[b] = a
    else:
        arr[b] += arr[a]
        arr[a] = b

def find(x):
    # print(x)
    if arr[x] < 0:
        return x
    arr[x] = find(arr[x])
    return arr[x]

for i in range(M):
    k, a, b = map(int, input().split())
    # print(arr)
    if k == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")