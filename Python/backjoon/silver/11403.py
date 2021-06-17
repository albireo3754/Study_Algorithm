import sys

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if grid[j][i] == 1 and grid[i][k] == 1:
                grid[j][k] = 1

for i in grid:
    print(*i)