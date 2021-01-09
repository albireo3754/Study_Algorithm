import sys

N,M = map(int,sys.stdin.readline().rstrip().split(" "))

board = []

for _ in range(N):
    board.append(sys.stdin.readline().rstrip())

# print(board)

white = N * M
black = N * M

for i in range(N - 7):

    for j in range(M - 7):
        min_white = 0
        min_black = 0
        cnt = 1
        for x in range(8):
            for y in range(8):
                # print(i + x, j + y)
                if board[i + x][j + y] == 'W':
                    if cnt == 1:
                        min_black += 1
                    else:
                        min_white += 1
                else:
                    if cnt == 1:
                        min_white += 1
                    else:
                        min_black += 1
                cnt *= -1
            cnt *= -1
        white = min(white,min_white)
        black = min(black,min_black)

print(min(white,black))
                    