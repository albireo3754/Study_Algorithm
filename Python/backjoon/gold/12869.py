grid = [[[-1 for i in range(61)] for i in range(61)] for i in range(61)]

N = int(input())
scvs = list(map(int, input().split()))

while len(scvs) < 3:
    scvs.append(0)

# print(scvs)
# scvs.sort(reverse=True)

def init():
    for i in range(10):
        for j in range(4):
            for k in range(2):
                grid[i][j][k] = 1
        for k in range(4):
            for j in range(2):
                grid[i][j][k] = 1

    for j in range(10):
        for i in range(4):
            for k in range(2):
                grid[i][j][k] = 1
        for k in range(4):
            for j in range(2):
                grid[i][j][k] = 1
    
    for k in range(10):
        for i in range(4):
            for j in range(2):
                grid[i][j][k] = 1
        for j in range(4):
            for i in range(2):
                grid[i][j][k] = 1
    grid[0][0][0] = 0
init()
# init() test
# print(grid[4][9][1])
# print(grid[3][1][9])
perms = ((1, 3, 9), (1, 9, 3), (3, 1, 9), (3, 9, 1), (9, 3, 1), (9, 1, 3))
INF = float('inf')
def health_limit(health):
    if health < 0:
        return 0
    return health
#health test
# print(health_limit(-3))
# print(health_limit(1))
# print(grid[0][0][0])
def go(scvs):
    # print(scvs)
    if grid[scvs[0]][scvs[1]][scvs[2]] != -1:
        return grid[scvs[0]][scvs[1]][scvs[2]]
    
    res = INF
    for di, dj, dk in perms:
        ni, nj, nk = scvs[0] - di, scvs[1] - dj, scvs[2] - dk
        ni = health_limit(ni)
        nj = health_limit(nj)
        nk = health_limit(nk)
        res = min(res, 1 + go([ni, nj, nk]))
    grid[scvs[0]][scvs[1]][scvs[2]] = res
    return res

print(go(scvs))
