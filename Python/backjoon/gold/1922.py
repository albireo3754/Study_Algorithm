import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
pq = []
cnt = 0
arr = [0 for i in range(N + 1)]
answer = 0
parent = [-1 for i in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(pq, (c, a, b))

def find(a):
    # print(a, parent)
    if parent[a] < 0:
        return a
    return find(parent[a])

def union(x, y):
    # x, y = find(a), find(b)
    # if x < -1 and x == y:
    #     continue
    if x <= y:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
    

while cnt < N and pq:
    c, a, b = heapq.heappop(pq)
    # print(c, a, b)
    x, y = find(a), find(b)
    if x == y:
        continue
    else:
        union(x, y)
        answer += c

print(answer)
