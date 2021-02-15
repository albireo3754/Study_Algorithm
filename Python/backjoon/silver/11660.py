import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

grid = [[] for _ in range(N)]
for i in range(N):
    grid[i] = list(map(int, input().split(' ')))
grid_sum = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j == 0:
            grid_sum[i][j] = grid[i][j]
        else:
            grid_sum[i][j] = grid_sum[i][j - 1] + grid[i][j]
print(grid_sum)
for i in range(N):
    for j in range(N):
        if i > 0:
            grid_sum[i][j] = grid_sum[i - 1][j] + grid_sum[i][j]
print(grid_sum)
for i in range(M):

    x1, y1, x2, y2 = map(int, input().split(' '))
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    answer = grid_sum[x2][y2]
    if x1 == 0 and y1 == 0:
        pass
    elif x1 == 0:
        answer -= grid_sum[x2][y1 - 1]
    elif y1 == 0:
        answer -= grid_sum[x1 - 1][y2]
    else:
        answer -= grid_sum[x2][y1 - 1]
        answer -= grid_sum[x1 - 1][y2]
        answer += grid_sum[x1 - 1][y1 - 1]
    print("answer", answer)
