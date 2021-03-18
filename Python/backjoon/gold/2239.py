import sys

input = sys.stdin.readline

sdoku = []
zero = 0
arr = []
_hor = [[True for i in range(10)] for i in range(9)]
_ver = [[True for i in range(10)] for i in range(9)]
_squ = [[True for i in range(10)] for i in range(9)]
for i in range(9):
    sdoku.append(list(map(int, list(input().rstrip()))))
    for j in range(9):
        cur = sdoku[i][j]
        if cur == 0:
            zero += 1
            arr.append((i, j))
        else:
            _hor[i][cur] = False
            _ver[j][cur] = False
            _squ[(i//3) * 3 + j // 3][cur] = False

# print(arr, zero)
# def hor(i, j, val):
#     if val in sdoku[i]:
#         return False
#     return True

# def ver(i, j, val):
#     for k in range(9):
#         if val == sdoku[k][j]:
#             return False
#     return True

# def squ(i, j, val):
#     i_ = (i // 3) * 3
#     j_ = (j // 3) * 3
#     for i in range(i_, i_ + 3):
#         for j in range(j_, j_ + 3):
#             if val == sdoku[i][j]:
#                 return False
#     return True



def dfs(idx):
    #다 채움
    # print(idx)
    if zero == idx:
        for i in sdoku:
            for j in i:
                print(j, end='')
            print()
        sys.exit()

    i, j = arr[idx]

    for n in range(1, 10):
        p33 = (i//3) * 3 + j // 3
        if _hor[i][n] and _ver[j][n] and _squ[p33][n]:
            _hor[i][n] = False
            _ver[j][n] = False
            _squ[p33][n] = False
            sdoku[i][j] = n
            if dfs(idx + 1) == 10:
                return 10
            sdoku[i][j] = 0
            _hor[i][n] = True
            _ver[j][n] = True
            _squ[p33][n] = True
    return 0
# i = 0
# j = 3
# n = 2
# p33 = (i//3) * 3 + j // 3
# print(_hor[i][n],_ver[j][n],_squ[p33][n])
dfs(0)
