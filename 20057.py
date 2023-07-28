import sys
input = sys.stdin.readline

N = int(input())

grid = [list(map(int, input().split())) for i in range(N)]
print_grid = [[0 for _ in range(N)] for _ in range(N)]

center = (N) // 2

def remove_send(x, y, a):
    send = grid[y[0]][y[1]]

    _5 = int(send * 0.05)
    _10 = int(send * 0.1)
    _7 = int(send * 0.07)
    _2 = int(send * 0.02)
    _1 = int(send * 0.01)
    [_5, _10, _7, _2, _1]
    send = grid[a[0]][a[1]]

def remove_send(at, y):
    grid[at[0]][at[1]] -= y



def move():
    point = [center, center]
    move = 0
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    # temp = 1
    while True:
        for dxy in direction:
            dx = dxy[0]
            dy = dxy[1]
            if dx == 0:
                move += 1
            for _ in range(move):
                point[0] += dx 
                point[1] += dy
                if point[0] < 0 or point[1] < 0:
                    # for p in print_grid:
                    #     print(p)
                    return
                # print_grid[point[0]][point[1]] = temp
            
                # temp += 1
            


move()