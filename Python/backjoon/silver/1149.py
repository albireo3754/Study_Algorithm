import sys

input = sys.stdin.readline

N = int(input())

rgb = []

for i in range(N):
    rgb.append(list(map(int, input().split(' '))))

for i in range(1, N):
    for j in range(3):
        rgb[i][j] += min((rgb[i - 1][:j] + rgb[i - 1][j + 1:]))

print(min(rgb[N - 1]))