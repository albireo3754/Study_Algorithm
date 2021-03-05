import sys

input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def diffusion(grid):
    R, C = len(grid), len(grid[0])
    new_grid = [[0 for i in range(C)] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == -1:
                new_grid[i][j] = -1
            if grid[i][j] >= 0: # 4이하는 확산되도 값이안변함
                diffusion_amount = grid[i][j] // 5
                remain_amount = grid[i][j]
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] != -1:
                        new_grid[ni][nj] += diffusion_amount
                        remain_amount -= diffusion_amount
                new_grid[i][j] += remain_amount
    for i in range(R):
        grid[i] = new_grid[i][:]

def circulation(grid, robot):
    R, C = len(grid), len(grid[0])
    ## top
    top = [robot[0], 0]
    temp = 0
    for i in range(1, C):
        grid[top[0]][i], temp = temp, grid[top[0]][i]
    for i in range(top[0] - 1, -1, -1):
        grid[i][-1], temp = temp, grid[i][-1]
    
    for i in range(C - 2, -1, -1):
        grid[0][i], temp = temp, grid[0][i]

    for i in range(1, top[0]):
        grid[i][0], temp = temp, grid[i][0]
    ## bottom
    bot = [robot[1], 0]
    temp = 0
    for i in range(1, C):
        grid[bot[0]][i], temp = temp, grid[bot[0]][i]
    
    for i in range(bot[0] + 1, R):
        grid[i][-1], temp = temp, grid[i][-1]
    
    for i in range(C - 2, -1, -1):
        grid[-1][i], temp = temp, grid[-1][i]

    for i in range(R - 2, bot[0], -1):
        grid[i][0], temp = temp, grid[i][0]

def solution():
    answer = 0

    R, C, T = map(int, input().split(' '))

    grid = []
    machine = [0, 0]
    for i in range(R):
        row = list(map(int, input().split(' ')))
        if row[0] == -1:
            machine[0] = i - 1
            machine[1] = i
        grid.append(row)
    
    for _ in range(T):
        diffusion(grid)
        circulation(grid, machine)
    # print(grid)
    for i in grid:
        print(i)
    print(sum(map(sum, grid)) + 2)

solution()
