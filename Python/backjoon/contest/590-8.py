import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

M, N = map(int, input().split(' '))
grid = []
terra = [0, 0]
for i in range(N):
    grid.append(input().rstrip())
    isterra = grid[i].find('T')
    if isterra >= 0:
        terra[0] = i
        terra[1] = isterra
        grid[i] = grid[i].replace('T', '0')

distance = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[0 for i in range(M)] for i in range(N)]
answer = []
def dfs(x, y, time, dx, dy):
    if grid[x][y] == 'E':
        answer.append(time)
        return
    nx, ny = x + dx, y + dy
    time += int(grid[x][y])
    if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
        if grid[nx][ny].isdigit():
            ## visit check###############
            visited[nx][ny] = 1
            dfs(nx, ny, time, dx, dy)
            visited[nx][ny] = 0
        elif grid[nx][ny] == 'E':
            visited[nx][ny]
            dfs(nx, ny, time, dx, dy)
            visited[nx][ny]
        elif grid[nx][ny] == 'R':
            if dx == 0:
                newdist = distance[:2]
            else:
                newdist = distance[2:]
            for dx, dy in newdist:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if grid[nx][ny] == 'R' or grid[nx][ny] == 'H':
                        continue
                    visited[nx][ny] = 1
                    dfs(nx, ny, time, dx, dy)
                    visited[nx][ny] = 0
for dx, dy in distance:
    dfs(terra[0], terra[1], 0, dx,dy)

print(min(answer) if len(answer) else -1)
        # else:
    # for di, dj in distance:
    #     nx, ny = x + dx, y + dy
    #     if 0 <= nx < N and 0 <= nx < M:
            
    #         pass
    #     else:
    #         return -1
    