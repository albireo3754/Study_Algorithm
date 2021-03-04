import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N, M, D = map(int, input().split(' '))

combs = combinations([i for i in range(0, M)], 3)

grid = []

for i in range(N):
    grid.append(list(map(int, input().split(' '))))
grid.reverse()
# print(grid)
direction = []

for i in range(D):
    for j in range(-i, i + 1):
        direction.append((i + 1 - abs(j), j))
# print(direction)
# direction.sort(key = lambda x: x[0])
# print(direction)
# print(direction)
def kill(comb):
    killed = set()  
    q = deque()
    last = 0
    for c in comb:
        q.append((-1, c))
        last = c
    temp_killed = []
    while q:
        i, j = q.popleft()
        for di, dj in direction:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if grid[ni][nj] == 1 and ((ni, nj) not in killed):
                    temp_killed.append((ni, nj))
                    break
            
        if last == j:
            while temp_killed:
                killed.add(temp_killed.pop())
        if i == N - 2:
            continue
        q.append((i + 1, j))
                    #kill and break and next comb
    # print(killed)
    return len(killed)

answer = []
for comb in combs:
    # print(comb)
    answer.append(kill(comb))
# print(answer)
print(max(answer))