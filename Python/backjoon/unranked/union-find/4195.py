import sys

input = sys.stdin.readline

T = int(input())


def find(parent, x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]


def union(size, parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return size[x]

    if size[x] > size[y]:
        size[x] += size[y]
        parent[y] = x
        return size[x]
    else:
        size[y] += size[x]
        parent[x] = y
        return size[y]


# answer = []

for _ in range(T):
    N = int(input())
    friends = {}
    parent = [0 for i in range(200001)]
    size = [0 for i in range(200001)]
    for _ in range(N):
        a, b = input().rstrip().split(' ')
        a_, b_ = 0, 0
        if a not in friends:
            a_ = len(friends) + 1
            friends[a] = a_
            size[a_] = 1
            parent[a_] = a_
        else:
            a_ = friends[a]
            a_ = parent[a_]
        if b not in friends:
            b_ = len(friends) + 1
            friends[b] = b_
            size[b_] = 1
            parent[b_] = b_
        else:
            b_ = friends[b]
            b_ = parent[b_]

        print(union(size, parent, a_, b_))
