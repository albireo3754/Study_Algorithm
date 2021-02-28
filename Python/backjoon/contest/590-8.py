import sys
import heapq
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
visited = [[[9999999 for i in range(2)] for i in range(M)] for i in range(N)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

answer = []
def bfs(x, y):
    q = []
    for i in range(4):
        heapq.heappush(q, (0, x, y, i))
        visited[x][y][i >> 1] = 0
    while q:
        time, x, y, dr = heapq.heappop(q)
        if grid[x][y] == 'E':
            answer.append(time)
            return
        if visited[x][y][dr >> 1] != time:
            continue
        dx, dy = direction[dr]
        nx, ny = x + dx, y + dy
        time += int(grid[x][y])
        if 0 <= nx < N and 0 <= ny < M:
            if grid[nx][ny] == 'E':
                if visited[nx][ny][dr >> 1] > time:
                    visited[nx][ny][dr >> 1] = time
                    heapq.heappush(q, (time, nx, ny, i))
            elif grid[nx][ny] == 'H':
                continue    
            elif grid[nx][ny] == 'R':
                for i in range(4):
                    if i == dr:
                        continue
                    dx, dy = direction[i]
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if grid[nx][ny] == 'R' or grid[nx][ny] == 'H':
                            continue
                        if visited[nx][ny][i >> 1] > time:
                            visited[nx][ny][i >> 1] = time
                            heapq.heappush(q, (time, nx, ny, i))

            else:
                ## visit check###############
                if visited[nx][ny][dr >> 1] > time:
                    visited[nx][ny][dr >> 1] = time
                    heapq.heappush(q, (time, nx, ny, dr))

bfs(terra[0], terra[1])


print(min(answer) if len(answer) else -1)