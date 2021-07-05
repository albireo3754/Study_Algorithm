import sys

input = sys.stdin.readline


N, M = map(int, input().split())

# 북 동 남 서
# 북 - > 서 -> 남 -> 동
directs = ((-1, 0) ,(0,1), (1, 0), (0, -1))

r, c, d = map(int, input().split())
# r = r - 1
# c = c - 1

grid = [list(map(int, input().split())) for i in range(N)]
visited = [[False for i in range(M)] for i in range(N)]


# def act2a(r, c, d):
    
def rot(r, c, d):
    d -= 1
    if d < 0:
        d = 3
    return r, c, d


def can_back(r, c, d):
    return grid[r - directs[d][0]][c - directs[d][1]] == 0

def back(r, c, d):
    return r - directs[d][0], c - directs[d][1], d

def can_clean(r, c, d):
    return 0 <= r < N and 0 <= c < M and grid[r][c] == 0 and not visited[r][c]

# def can_rot(r, c, d):
#     d -= 1
#     if d < 0:
#         d = 3
#     nr, nc = directs[d][0] + r , directs[d][1] + c
#     return 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0

def clean(r, c, ret):
    if visited[r][c] == False:
        visited[r][c] = True
        return ret + 1
    return ret


def can_go(r, c, d):
    nr, nc = directs[d][0] + r , directs[d][1] + c
    return 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 0

def go(r, c, d):
    nr, nc = directs[d][0] + r , directs[d][1] + c
    return nr, nc, d

def can_rotgo(r, c, d):
    r, c, d = rot(r, c, d)
    if can_go(r, c, d):
        return True
    return False

def rotgo(r, c, d):
    return go(*rot(r, c, d))

# print(can_clean(-1, -1, 1))
ret = 0
while True:
    # act 1
    if can_clean(r, c, d):
        ret = clean(r, c, ret)
    # act 2
    for i in range(4):
        if can_rotgo(r, c, d) and can_clean(*rotgo(r, c, d)):
            r, c, d = rotgo(r, c, d)
            break
        r, c, d = rot(r, c, d)
    else:
        if can_back(r, c, d):
            r, c, d = back(r, c, d)
        else:
            break

print(ret)
# for i in visited:
#     print(i)

print('rot', rot(7, 4, 0), 'is 7, 4, 3')
print('rot', rot(7, 4, 3), 'is 7, 4, 2')
print('can back', can_back(7, 4, 0), can_back(1, 1, 2), 'true, false')
print('back', back(7, 4, 0), 'is 8, 4, 0')
print('go', go(7, 4, 0), 'is 6, 4, 0')
print('rotgo', rotgo(7, 4, 0), 'is 7, 3, 3')
print('rot', rot(7, 4, 2), 'is 7, 4, 1')
print('rotgo', rotgo(7, 4, 2), 'is 7, 5, 1')
