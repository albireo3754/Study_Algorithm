import sys

input = sys.stdin.readline

n = int(input())
triangle = [[]]
for i in range(1, n + 1):
    triangle.append(list(map(int, input().split(' '))))

for i in range(2, n + 1):
    for j in range(0, i):
        if j == 0:
            triangle[i][j] += triangle[i - 1][j]
        elif j == i - 1:
            triangle[i][j] += triangle[i - 1][j - 1]
        else:
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])

print(max(triangle[-1]))