import sys

input = sys.stdin.readline

# . 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
direction = ((0, 1), (0, -1), (-1, 0), (1, 0))
N, M, x, y, K = map(int, input().split())

grid = [list(map(int, input().split())) for i in range(N)]

cmds = list(map(lambda x: int(x) - 1, input().split()))

class Dice:
    def __init__(self):
        self.top = 0
        self.horizon = [0, 0, 0]
        self.vertical = [0, 0, 0]
    def roll(self, direction):
        if direction < 2:
            self._horizontal_roll(direction)
        else:
            self._vertical_roll(direction)
    def _horizontal_roll(self, direction):
        if direction == 1:
            temp = self.horizon[2]
            self.horizon = [self.top] + self.horizon[:2]
            self._change_top_bottom(temp, self.horizon[1])
        else:
            temp = self.horizon[0]
            self.horizon = self.horizon[1:] + [self.top]
            self._change_top_bottom(temp, self.horizon[1])

    def _vertical_roll(self, direction):
        if direction == 2:
            temp = self.vertical[2]
            self.vertical = [self.top] + self.vertical[:2]
            self._change_top_bottom(temp, self.vertical[1])
        else:
            temp = self.vertical[0]
            self.vertical = self.vertical[1:] + [self.top]
            self._change_top_bottom(temp, self.vertical[1])


    def _change_top_bottom(self, top, bottom):
        self.top = top
        self._change_bottom(bottom)

    def get_bottom(self):
        temp = self.horizon[1]
        return temp
    def set_bottom(self, bottom):
        self._change_bottom(bottom)

    def _change_bottom(self, bottom):
        self.horizon[1] = bottom
        self.vertical[1] = bottom
dice = Dice()
i, j = x, y
for cmd in cmds:
    di, dj = direction[cmd]
    ni, nj = i + di, j + dj
    if 0 <= ni < N and 0 <= nj < M:
        dice.roll(cmd)
        if grid[ni][nj] == 0:
            grid[ni][nj] = dice.get_bottom()
            # print('get?')
            # print(dice.horizon, dice.vertical, dice.top)
        else:
            dice.set_bottom(grid[ni][nj])
            grid[ni][nj] = 0
        i, j = ni, nj
        print(dice.top)