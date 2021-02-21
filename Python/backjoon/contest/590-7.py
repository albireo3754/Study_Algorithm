import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
N, T = map(int, input().split(' '))
exps = []
for i in range(N):
    ci, ei = map(int, input().split(' '))
    exps.append((ci, ei))
times = []
answer = []
for i in range(N):
    times.append(list(map(int, input().split(' '))))

def dfs(pos, exp, time):
    if time == T:
        answer.append(exp)
        return
    if time > T:
        return
    for i in range(0, len(times[pos])):
        if times[pos][i] == 0:
            dfs(pos, exp + exps[pos][1], time + 1)
        else:
            if exp < exps[i][0]:
                continue
            dfs(i, exp, time + times[pos][i])

for i, v in enumerate(exps):
    if v[0] == 0:
        dfs(i, 0, 0)
print(max(answer))

