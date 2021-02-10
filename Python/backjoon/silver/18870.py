import sys

input = sys.stdin.readline
dict = {}
N = int(input())
coordinate = list(map(int, input().split(' ')))

for i, v in enumerate(sorted(list(set(coordinate)))):
    dict[v] = i

print(*list(map(lambda x: dict[x], coordinate)))