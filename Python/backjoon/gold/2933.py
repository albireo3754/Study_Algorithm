import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())

grid = [list(input().rstrip()) for i in range(R)]

N = int(input())

heights = list(map(int, input().split()))

direction = ((-1, 0), (0, -1), (0, 1), (1, 0))
block = []
def isCluster(i, j):
    q = deque()
    q.append((i, j))
    visited = [[False for i in range(C)] for i in range(R)]
    visited[i][j] = True
    while q:
        i, j = q.popleft()
        block.append([i, j])
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                visited[ni][nj] = True
                if grid[ni][nj] == '.':
                    continue
                if ni == R - 1:
                    return True
                q.append((ni, nj))
    return False

def fall():
    for i, j in block:
        grid[i - 1][j] = '.'

    for i, j in block:
        grid[i][j] = 'x'
    
def isFloat():
    # print(block)
    for idx in range(len(block)):
        i, j = block[idx]
        if grid[i][j] == 'x':
            grid[i][j] = 'o'
        # elif grid[i][j] == '.':
        #     grid[i][j] = ','
    for idx in range(len(block)):
        i, j = block[idx]
        
        if i == R - 1 or grid[i + 1][j] == 'x':
            for idx in range(len(block)):
                i, j = block[idx]
                if grid[i][j] == 'o':
                    grid[i][j] = 'x'
                if grid[i][j] == ',':
                    grid[i][j] = '.'
            return False

    for idx in range(len(block)):
        i, j = block[idx]
        if grid[i][j] == 'o':
            grid[i][j] = 'x'
        if grid[i][j] == ',':
            grid[i][j] = '.'
        block[idx][0] += 1
    return True
        
isleft = True
for height in heights:
    # print(height, '----------------------')   
    # for i in grid:
    #     print(''.join(i))
    height = R - height
    if isleft:
        isleft = False
        for j in range(C):
            if grid[height][j] == 'x':
                grid[height][j] = '.'
                for di, dj in direction:
                    ni, nj = height + di, j + dj
                    block = []
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 'x' and not isCluster(ni, nj):
                        while isFloat():
                            fall()
                        break
                break
    else:
        isleft = True
        for j in range(C - 1, -1, -1):
            if grid[height][j] == 'x':
                grid[height][j] = '.'
                for di, dj in direction:
                    ni, nj = height + di, j + dj
                    block = []
                    if 0 <= ni < R and 0 <= nj < C and grid[ni][nj] == 'x' and not isCluster(ni, nj):
                        while isFloat():
                            fall()
                        break
                break

for i in grid:
    print(''.join(i))

# print(isCluster(2, 5))
# # print(grid[5][5])
# # print(block.append([5, 5]))
# fall()
# for i in grid:
#     print(*i)
