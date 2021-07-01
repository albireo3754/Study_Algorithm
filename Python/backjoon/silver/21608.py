import sys

input = sys.stdin.readline

N = int(input())
edge = [[] for i in range(N * N + 1)]
for i in range(N * N):
    a, b, c, d, e = map(int, input().split())
    print(a, b, c, d, e)
    edge[a] = [b, c, d, e]
print(edge)