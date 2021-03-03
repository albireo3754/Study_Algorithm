import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)
N = int(input())
grid = [[1 for i in range(N + 1)]]
for i in range(N):
    grid.append([1] + list(map(int, input().split(' '))))


# print(grid)
grid_ = [[[999999999999, 9999999999999] for i in range(N + 1)] for i in range(N + 1)]
for i in range(0, N + 1):
    for j in range(0, N + 1):
        if grid[i][j] == 0:
            continue

        a = 1
        while grid[i][j] % (2 ** a) == 0:
            a += 1
        a -= 1

        b = 1
        while grid[i][j] % (5 ** b) == 0:
            b += 1
        b -= 1
        grid_[i][j][0] = a
        grid_[i][j][1] = b

answer = []
# print(grid_)
# def dfs(i, j, a, b):
#     if i == N and j == N:
#         answer.append(min([a + grid_[i][j][0], b + grid_[i][j][1]]))
#         return
#     if grid_[i][j][0] == -1:
#         return
#     if j < N:
#         dfs(i, j + 1, a + grid_[i][j][0], b + grid_[i][j][1])
#     if i < N:
#         dfs(i + 1, j, a + grid_[i][j][0], b + grid_[i][j][1])
# dfs(1, 1, 0, 0)
# print(min(answer))
# print(grid_)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if grid[i][j] == 0:
            continue
        if i == 1 and j == 1:
            continue
        elif j == 1:
            grid_[i][j][0] += grid_[i - 1][j][0]
            grid_[i][j][1] += grid_[i - 1][j][1]
        elif i == 1:
            grid_[i][j][0] += grid_[i][j - 1][0]
            grid_[i][j][1] += grid_[i][j - 1][1]
        else:    
            grid_[i][j][0] += min(grid_[i - 1][j][0], grid_[i][j - 1][0])
            grid_[i][j][1] += min(grid_[i - 1][j][1], grid_[i][j - 1][1])
# print(grid_)
print(min(grid_[N][N]))