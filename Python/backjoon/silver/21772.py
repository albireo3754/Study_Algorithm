import sys

input = sys.stdin.readline

R, C, T = map(int, input().split())

grid = [list(input().rstrip()) for i in range(R)]

direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

S = [[*j] for j in grid]
visited = [[[False for i in range(4)] for i in range(C)] for i in range(C)]
answer = [0]

def dfs(i, j, t, n):
    # DFS → 시간초가 안됬는데 못움직이는 경우 마지막에 answer를 판별하면 값이 안나오게됨
    answer[0] = max(answer[0], n)
    if t == T:
        return

    # print(i, j, t, n)
    for k in range(4):
        di, dj = direction[k]
        ni, nj = i + di, j + dj
        if 0 <= ni < R and 0 <= nj < C and visited[ni][nj][k] == False:
            if grid[ni][nj] == '#':
                continue
            visited[ni][nj][k] = True
            if grid[ni][nj] == 'S':
                grid[ni][nj] = '.'
                dfs(ni, nj, t + 1, n + 1)
                grid[ni][nj] = 'S'
            else:
                dfs(ni, nj, t + 1, n)
            visited[ni][nj][k] = False



for i in range(R):
    for j in range(C):
        if grid[i][j] == 'G':
            # visited[i][j] = True
            dfs(i, j, 0, 0)
            print(answer[0])