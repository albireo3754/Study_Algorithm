import sys

input = sys.stdin.readline
V, E = map(int, input().split(' '))

edges = []

for i in range(E):
    edges.append(list(map(int, input().split(' '))))

parent = [-1] * (V + 1)
edges.sort(key = lambda x: x[2])

def find(x):
    if parent[x] < 0:
        return x
    y = find(parent[x])
    parent[x] = y
    return y

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return;
    
    if parent[x] <= parent[y]:
        parent[x] += parent[y]
        parent[y] = x;
    else:
        parent[y] += parent[x]
        parent[x] = y;
    
answer = 0
for a, b, w in edges:
    if find(a) == find(b):
        continue
    union(a, b)
    answer += w

print(answer)
