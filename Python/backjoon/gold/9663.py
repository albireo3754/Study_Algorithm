from collections import deque
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())

answer = [0]
matrix = [0]
import time
a_ = time.time()


def dfs(set_range):
    if len(matrix) == N:
        answer[0] += 1
        return
    pos = len(matrix)
    for i in list(set_range):
        for idx, val in enumerate(matrix):
            # if val == i:
            #     break
            if idx - val == pos - i:
                break
            if idx - pos == i - val:
                break 
        else:
            matrix.append(i)
            new_set = set_range.copy()
            new_set.remove(i)
            dfs(new_set)
            matrix.pop()
for i in range(N):
    matrix = [i]
    set_ = set(list(range(N)))
    set_.discard(i)
    dfs(set_)
print(answer[0])
print(time.time() - a_)

# def dfs():
#     if len(matrix) == N:
#         answer[0] += 1
#         return
#     pos = len(matrix)
#     for i in range(0, N):
#         for idx, val in enumerate(matrix):
#             if i == val:
#                 break
#             if idx - val == pos - i:
#                 break
#             if idx - pos == i - val:
#                 break
#         else:
#             matrix.append(i)
#             dfs()
#             matrix.pop()
# for i in range(N):
#     matrix = [i]
#     dfs()
# print(answer[0])

# bfs
# q = deque()
# for i in range(N):
#     q.append([i])
# while q:
#     x = q.popleft()
#     pos = len(x)
#     if pos == N:
#         answer += 1
#     for i in range(N):
#         for idx, val in enumerate(x):
#             if i == val:
#                 break
#             if idx - val == pos - i:
#                 break
#             if idx - pos == i - val:
#                 break
#         else:
#             q.append(x[:] + [i])
# print(answer)
