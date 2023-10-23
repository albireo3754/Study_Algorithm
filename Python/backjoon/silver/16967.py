import sys

input = sys.stdin.readline

H, W, X, Y = map(int, input().split(" "))

raw_grid = [[i for i in map(int, input().split(" "))] for _ in range(0, H + X)]

result = [[0 for _ in range(0, W)] for _ in range(0, H)]

# print(result) 

for i in range(H):
    for j in range(W):
        result[i][j] = raw_grid[i][j]
        raw_grid[i + X][j + Y] -= result[i][j]

# print(result)
for arr in result:
    print(*arr)