import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
grid=[]
for i in range(N):
    grid.append(list(map(int, input().split(' '))))

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            grid[i][j] += grid[i][j - 1]
        elif j == 0:
            grid[i][j] += grid[i - 1][j]
        else:
            grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
print(grid)
print(grid[-1][-1])