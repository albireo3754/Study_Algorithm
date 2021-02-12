import sys

sys.setrecursionlimit(1000000)
N, M = map(int, input().split(' '))
seq = list(map(int, input().split(' ')))
seq.sort()
answer = []
before = []

def dfs(set):
    if len(before) == M:
        answer.append(before[:])
    for i, j in enumerate(set):
        before.append(j)
        dfs(set[:i] + set[i + 1:])
        before.pop()

dfs(seq)
for i in answer:
    print(*i)