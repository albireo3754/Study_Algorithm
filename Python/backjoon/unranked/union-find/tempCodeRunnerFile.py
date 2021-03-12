import sys

input = sys.stdin.readline

N, L = map(int, input().split(' '))

ladica = [i for i in range(L + 1)]

drink = [0 for i in range(L + 1)]


def find(parent, x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]

def union(parent, x, y, drink):
    x = parent[x]
    y = parent[y]

    if x == y:
        return x
    # print(x, y)
    if drink[x] == 0:
        parent[x] = y
        return x
    elif drink[y] == 0:
        parent[x] = y
        return y
    return y
for i in range(1, N + 1):
    a, b = map(int, input().rstrip().split(' '))

    flag = 1
    if drink[a] == 0:
        drink[a] = i
        union(ladica, a, b, drink)
    else:
        if drink[b] == 0:
            drink[b] = i
            ladica[a] = b
            union(ladica, b, a, drink)
        else:
            temp = union(ladica, a, b, drink)
            if drink[temp]:
                flag = 0
                drink[temp] = i
                print("SMECE")
            else:
                drink[temp] = i
    if flag:
        print("LADICA")