import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

houses = []
chickens = []

N, M = map(int, input().split())
grid = []
chicken_nums = [[-1 for i in range(N)] for i in range(N)]
a, b = 0, 0

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] == 1:
            houses.append((i, j))
            a += 1
        if temp[j] == 2:
            chickens.append((i, j))
            chicken_nums[i][j] = b
            b += 1
    grid.append(temp)
direction = ((1, 0), (-1, 0), (0, -1), (0, 1))
house_chicken = [[0 for i in range(a)] for i in range(b)]

def bfs(idx, house):
    i, j = house
    q = deque()
    q.append((i, j, 0))
    visited = [[False for i in range(N)] for i in range(N)]
    visited[i][j] = True
    while q:
        i, j, t = q.popleft()
        if grid[i][j] == 2:
            house_chicken[chicken_nums[i][j]][idx] = t
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = True
                q.append((ni, nj, t + 1))

for idx, house in enumerate(houses):
    bfs(idx, house)

nums = [i for i in range(b)]
answer = 9999999999


for comb in combinations(nums, M):
    tempanswer = 0
    for i in range(a):
        temp = 99999999999
        for j in comb:
            temp = min(temp, house_chicken[j][i])
        tempanswer += temp
    answer = min(answer, tempanswer)

print(answer)

for i in house_chicken:
    print(i) 