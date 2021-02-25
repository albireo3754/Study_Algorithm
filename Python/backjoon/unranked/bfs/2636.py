import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))
grid = []
visited = []
tempvisited = []
for i in range(N):
    grid.append(list(map(int, input().split(' '))))
    # visited.append([0 for _ in range(M)])
    # tempvisited.append([0 for _ in range(M)])
# print(grid)

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(i, j, visited):
    visited[i][j] = 1
    q = deque()
    q.append((i, j))
    removed_cheese = 0
    while q:
        i, j = q.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj]:
                    continue
                if grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    removed_cheese += 1
                    visited[ni][nj] = 1
                    # print(ni, nj)
                else:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    return removed_cheese

def solution():
    removed_cheese = 0
    remove_count = 0
    while True:
        temp = 0
        visited = [[0 for _ in range(M)] for _ in range(N)]
        temp += bfs(0, 0,visited)
        if temp == 0:
            return [remove_count, removed_cheese]
        remove_count += 1
        removed_cheese = temp
answer = solution()
print(answer[0])
print(answer[1])