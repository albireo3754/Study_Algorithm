import sys
from collections import defaultdict
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
N, M = map(int, input().split(' '))
edge = defaultdict(list)
pre = [0 for i in range(N + 1)]
hacked = [-1 for i in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split(' '))
    edge[B].append(A)
    pre[A] += 1


def dfs(node):
    if not edge[node]:
        hacked[node] = 0
        return 0
    count = 0
    for i in edge[node]:
        if hacked[i] >= 0:
            count += hacked[i] + 1
        else:
            count += dfs(i) + 1
    hacked[node] = count
    return count


answer = []
for i in range(1, N + 1):
    if pre[i] == 0:
        length = dfs(i)
        answer.append((length, i))
# print(answer)
answer.sort(key=lambda x: -x[0])
print(*[i[1] for i in answer])
