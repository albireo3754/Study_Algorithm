import sys

input = sys.stdin.readline

N = int(input())

grid = []
friends = []
for i in range(N):
    grid.append(list(input().rstrip()))
    friends.append([0 for i in range(N)])

print(grid)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'Y':
                friends[i][j] = 1
            if grid[i][k] == 'N' or grid[k][j] == 'N' or i == j:
                continue
            friends[i][j] = 1

print(max(map(lambda x: sum(x), friends)))