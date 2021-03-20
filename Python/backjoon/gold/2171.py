import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

grid = []
answer = [[0 for i in range(M)] for i in range(N)]
for i in range(N):
    grid.append(input().rstrip())

# print(grid)

max_size = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] == '1':
            answer[i][j] = min(answer[i - 1][j - 1], answer[i - 1][j], answer[i][j - 1]) + 1
            max_size = max(answer[i][j], max_size)
print(max_size ** 2)