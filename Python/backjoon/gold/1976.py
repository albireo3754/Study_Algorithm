import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
grid = []

parent = [-1 for i in range(N + 1)]

def find(x):
    # print(x)
    if parent[x] < 0:
        return x
    
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x > y:
        parent[y] += parent[x]
        parent[x] = y
    else:
        parent[x] += parent[y]
        parent[y] = x


for i in range(N):
    grid.append(list(map(int, input().split(' '))))

plans = list(map(int, input().split(' ')))

for i in range(N):
    for j in range(N):
        if grid[i][j]:
            union(i + 1, j + 1)



p = find(plans[0])
for i in plans:
    if find(i) != p:
        # print(find(i))
        print("NO")
        break
else:
    print("YES")
