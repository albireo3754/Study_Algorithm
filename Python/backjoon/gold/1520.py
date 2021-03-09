import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split(' '))
grid = []
for i in range(N):
    grid.append(list(map(int, input().split(' '))))
answer = [[-1 for i in range(M)] for i in range(N)]
direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
def dfs(i, j):
    if i == N - 1 and j == M - 1:
        return 1
    if answer[i][j] == -1:
        answer[i][j] = 0
        for di, dj in direction:
            ni, nj = di + i, dj + j
            if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] < grid[i][j]:
                answer[i][j] += dfs(ni, nj)
    return answer[i][j]

dfs(0,0)
# for i in answer:
#     print(i)
print(answer[0][0])