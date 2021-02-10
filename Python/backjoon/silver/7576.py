import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split(' '))

ground = []
for i in range(N):
    ground.append(list(map(int, input().split(' '))))

q = deque([])
for i in range(N):
    for j in range(M):
        if ground[i][j] == 1:
            q.append([i + 1, j, 1])
            q.append([i, j + 1, 1])
            q.append([i - 1, j, 1])
            q.append([i, j - 1, 1])

def bfs():
    max_time = 0
    while q:
        x, y, time = q.popleft()
        if x >= 0 and x < N and y >= 0 and y < M and ground[x][y] == 0:
            ground[x][y] = 1    
            max_time = max(max_time, time)
            if x + 1 < N and ground[x + 1][y] == 0:
                q.append([x + 1, y, time + 1])
            if y + 1 < M and ground[x][y + 1] == 0:
                q.append([x, y + 1, time + 1])
            if x - 1 >= 0 and ground[x - 1][y] == 0:
                q.append([x - 1, y, time + 1])
            if y - 1 >= 0 and ground[x][y - 1] == 0:
                q.append([x, y - 1, time + 1])
    return max_time

def solution():
    max_time = bfs()
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 0:
                return -1
    return max_time

print(solution())

