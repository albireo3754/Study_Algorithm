import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split(' '))

matrix = []
matrix.append([2] * (M + 2))
for i in range(N):
    matrix.append(list(map(int, list('2' + input().rstrip() + '2'))))
matrix.append([2] * (M + 2))

time = [[[1, 1] for i in range(M + 1)] for i in range(N + 1)]
direction = [[1 , 0], [-1, 0], [0, 1], [0, -1]]

def bfs():
    q = deque([[1,1,1]])
    while q:
        print(q)
        x, y, drill = q.popleft()
        before_time = time[x][y][drill]
        if x == N and y == M:
            return max(time[x][y])
        for a, b in direction:
            x_, y_= x + a, y + b
            drill_ = drill
            if matrix[x_][y_] == 2:
                continue
            if matrix[x_][y_] == 1: 
                if drill:
                    drill_ -= 1
                else:
                    continue
            if time[x_][y_][drill_] == 1:
                time[x_][y_][drill_] = before_time + 1
                q.append([x_, y_, drill_])
    return -1
answer = bfs()
print(answer)
