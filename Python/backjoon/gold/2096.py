import sys
input = sys.stdin.readline

N = int(input().rstrip())
line = [[[0, 0] for i in range(3)] for i in range(2)]
for i, v in enumerate(list(map(int, input().split(' ')))):
    line[0][i][0] = v
    line[0][i][1] = v
for i in range(N - 1):
    temp = list(map(int, input().split(' ')))
    for j in range(3):
        if j == 0:
            line[1][0][0] = min(line[0][0][0], line[0][1][0]) + temp[j]
            line[1][0][1] = max(line[0][0][1], line[0][1][1]) + temp[j]

        if j == 1:
            line[1][1][0] = min(line[0][1][0], line[0][0]
                                [0], line[0][2][0]) + temp[j]
            line[1][1][1] = max(line[0][1][1], line[0][0]
                                [1], line[0][2][1]) + temp[j]

        if j == 2:
            line[1][2][0] = min(line[0][2][0], line[0][1][0]) + temp[j]
            line[1][2][1] = max(line[0][2][1], line[0][1][1]) + temp[j]
    for j in range(3):
        line[0][j] = line[1][j][:]
        line[1][j] = [0, 0]
print(max(map(lambda x: x[1], line[0])), min(map(lambda x: x[0], line[0])))
