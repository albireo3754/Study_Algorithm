import sys
# sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())


def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    x, y = find(a), find(b)
    if x == y:
        return
    if parent[x] > parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y

for _ in range(T):
    N = int(input())
    parent = [-1 for _ in range(N)]
    arr = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
       for j in range(i + 1 , N): 
           a1, b1, r1 = arr[i] 
           a2, b2, r2 = arr[j]
           if (r1 + r2) ** 2 >= (a1 - a2) ** 2 + (b1 - b2) ** 2:
               union(i, j)
    answer = 0
    # print(parent)
    for p in parent:
        if p < 0:
            answer += 1
    print(answer)