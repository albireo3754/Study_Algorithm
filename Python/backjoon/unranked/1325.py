import sys
from collections import deque
# sys.setrecursionlimit(10000000)
input = sys.stdin.readline
N, M = map(int, input().split(' '))
edge = [[] for i in range(N + 1)]
# pre = [0 for i in range(N + 1)]
hacked = [-1 for i in range(N + 1)]
q = deque()
for i in range(M):
    A, B = map(int, input().split(' '))
    edge[B].append(A)
    # pre[A] += 1

# print(edge)


# def dfs(node):
#     if edge[node] == -1:
#         hacked[node] = 0
#         return 0
#     count = 0
#     # for i in edge[node]:
#     while edge[node]:
#         i = edge[node].pop()
#         if hacked[i] >= 0:
#             count += hacked[i] + 1
#         else:
#             count += dfs(i) + 1
#     hacked[node] = count
#     return count
# def dfs(node):
#     stack = [node]
#     unvisited = [1 for i in range(N + 1)]
#     count = 0
#     while stack:
#         top = stack[-1]
#         flag = 1
#         for i in edge[top]:
#             if unvisited[i]:
#                 stack.append(i)
#                 unvisited[i] = 0
#                 flag = 0
#                 count += 1

#         if flag:
#             stack.pop()
#     hacked[node] = count


def bfs(node):
    q.append(node)
    count = 0
    unvisited = [True for i in range(N + 1)]
    while q:
        pos = q.popleft()
        for i in edge[pos]:
            if unvisited[i]:
                q.append(i)
                unvisited[i] = False
                count += 1
    hacked[node] = count


answer = []
for i in range(1, N + 1):
    # if pre[i] == 0:
    if edge[i]:
        bfs(i)
max_hacked = max(hacked)
# print(hacked)

for i, v in enumerate(hacked):
    if v == max_hacked:
        answer.append(i)
print(*sorted(answer))
# answer.sort(key=lambda x: -x[0])
# for i in range(1, N):
#     if answer[i][0] != maxlength:
#         answer = answer[:i]
#         break
# print(answer)
# print(*[i[1] for i in answer])
