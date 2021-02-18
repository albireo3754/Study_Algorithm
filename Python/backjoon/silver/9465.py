import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for i in range(2)]

    score = [[0 for _ in range(n)] for _ in range(2)]
    reverse = [1, 0]
    for j in range(n):
        for i in range(2):
            
            if j == 0:
                score[i][j] = sticker[i][j]
            else:
                score[i][j] = sticker[i][j] + max(score[reverse[i]][j - 1], score[reverse[i]][j - 2])
    print(max(score[0][n - 1], score[1][n - 1]))