import sys

input = sys.stdin.readline

N, L = map(int, input().split(' '))

ladica = [0 for i in range(1, L + 1)]
ab = [0 for i in range(1, L + 1)]
drink = [0 for i in range(1, L + 1)]


def find(parent, x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])


for i in range(N + 1):
    a, b = map(int, input().split(' '))
    b = ladica[a]
    if drink[a] == 0:
        drink[a] = i
    elif
