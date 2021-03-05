import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

temp = []
answer = []
def dfs(idx, l):

    if l == M:
        answer.append(temp[:])
        return

    for i in range(idx, N + 1):
        temp.append(i)
        dfs(i, l + 1)
        temp.pop()

dfs(1, 0)

for a in answer:
    print(*a)


