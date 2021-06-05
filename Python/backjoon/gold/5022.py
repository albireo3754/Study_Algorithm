import sys
from collections import deque
input = sys.stdin.readline
 
N, M = map(int, input().split())

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
B1 = list(map(int, input().split()))
B2 = list(map(int, input().split()))


grid = [[-1 for i in range(M + 1)] for i in range(N + 1)]
# ngrid = [[-1 for i in range(M + 1)] for i in range(N + 1)]


direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

for i, j in [A1, A2, B1, B2]:
    grid[i][j] = 1

a_track = []
temp = []

def equal(A, B):
    if A[0] == B[0] and A[1] == B[1]:
        return True
    return False
def bfs(B1, B2):
    i, j = B1
    q = deque()
    q.append((i, j, 0))
    visited = [[-1 for i in range(M + 1)] for i in range(N + 1)]
    visited[i][j] = 0
    while q:
        i, j, v = q.popleft()
        for di, dj in direction:
            ni, nj = di + i, dj + j
            if 0 <= ni <= N and 0 <= nj <= M and visited[ni][nj] == -1:
                if equal(B2, [ni, nj]):
                    v += 1
                    visited[ni][nj] = v
                    return v, visited
                if grid[ni][nj] != -1:
                    continue
                visited[ni][nj] = v + 1
                q.append((ni, nj, v + 1))

def track(A2, A1, grid):
    i, j = A2
    n = grid[i][j]
    ret = [(i, j)]
    n -= 1
    while n >= 0:
        if i == B2[0] and j == B2[1]:
            return v
        for di, dj in direction:
            ni, nj = di + i, dj + j
            if 0 <= ni <= N and 0 <= nj <= M and grid[ni][nj] == n:
                i, j = ni, nj
                ret.append((i, j))
                n -= 1
                break
    return ret

try:
    answer = 0
    v, visited = bfs(A1, A2)
    answer += v

    for i, j in track(A2, A1, visited):
        grid[i][j] = 1
    # print(answer)
    answer += bfs(B1, B2)[0]
    print(answer)
except:
    print("IMPOSSIBLE")

# def find(i, j):
#     k = grid[i][j]
#     ngrid[i][j] = 1
#     k -= 1
#     while k >= 0:
#         for di, dj in direction:
#             ni, nj = di + i, dj +j
#             if 0 <= ni <= N and 0 <= nj <= M and grid[ni][nj] == k:
#                 i, j = ni, nj
#                 ngrid[i][j] = 1
#                 k -= 1


# temp = bfs(B1, B2, A1, A2)
# if temp[0] != 0:
#     find(temp[1], temp[2])
#     res = temp[0]
#     grid = [i[:] for i in ngrid]
#     temp2 = bfs(A1, A2, B1, B2)

#     if temp2[0] != 0:
#         res += temp2[0]
#         answer = min(res, answer)

# grid = [[-1 for i in range(M + 1)] for i in range(N + 1)]
# ngrid = [[-1 for i in range(M + 1)] for i in range(N + 1)]

# temp = bfs(A1, A2, B1, B2)
# if temp[0] != 0:
#     find(temp[1], temp[2])
#     res = temp[0]
#     grid = [i[:] for i in ngrid]
#     temp2 = bfs(B1, B2, A1, A2)
#     if temp2[0] != 0:
#         res += temp2[0]
#         answer = min(res, answer)

# if answer == Inf:
#     print(Imp)
# else:
#     print(answer)