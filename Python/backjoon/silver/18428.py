import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
grid = [input().rstrip().split() for i in range(N)]

Xs = []
Ts = []
direction = ((0, 1), (1, 0), (-1, 0), (0, -1))

def build(comb):
    for i, j in comb:
        grid[i][j] = 'O'

def destroy(comb):
    for i, j in comb:
        grid[i][j] = 'X'

def hide(comb):
    for i, j in Ts:
        for di, dj in direction:
            ni, nj = i + di, j + dj
            while 0 <= ni < N and 0 <= nj < N:
                if grid[ni][nj] == 'O' or grid[ni][nj] == 'T':
                    break
                if grid[ni][nj] == 'S':
                    return False
                ni += di
                nj += dj
    return True

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'X':
            Xs.append((i, j))
        elif grid[i][j] == 'T':
            Ts.append((i, j))



# print(Xs)


for comb in combinations(Xs,3):
    build(comb)
    if hide(comb):
        print('YES')
        break
    destroy(comb)
else:
    print('NO')