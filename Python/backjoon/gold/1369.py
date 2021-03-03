import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000000)
N = int(input())
grid = [[1 for i in range(N + 1)]]
Inf = 999999999999
grid_ = [[[Inf, Inf] for i in range(N + 1)] for i in range(N + 1)]
for i in range(1, N + 1):
    temp_row = list(map(int, input().split(' ')))
    for j in range(1, N + 1):
        tj = j -1
        if temp_row[tj] == 0:
            continue
        a = 0
        while temp_row[tj] % 2 == 0:
            a += 1
            temp_row[tj] = temp_row[tj] // 2
        b = 0
        while temp_row[tj] % 5 == 0:
            b += 1
            temp_row[tj] = temp_row[tj] // 5


        grid_[i][j][0] = a
        grid_[i][j][1] = b
answer = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 and j == 1:
            continue
        grid_[i][j][0] += min(grid_[i - 1][j][0], grid_[i][j - 1][0])
        grid_[i][j][1] += min(grid_[i - 1][j][1], grid_[i][j - 1][1])
print(min(grid_[N][N]))