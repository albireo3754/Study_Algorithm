import sys

input = sys.stdin.readline

sdoku = []
zero = 0
arr = []
for i in range(9):
    sdoku.append(list(map(int, list(input().rstrip()))))
    for j in range(9):
        if sdoku[i][j] == 0:
            zero += 1
            arr.append((i, j))

# print(arr, zero)
def hor(i, j, val):
    if val in sdoku[i]:
        return False
    return True

def ver(i, j, val):
    for k in range(9):
        if val == sdoku[k][j]:
            return False
    return True

def squ(i, j, val):
    i_ = (i // 3) * 3
    j_ = (j // 3) * 3
    for i in range(i_, i_ + 3):
        for j in range(j_, j_ + 3):
            if val == sdoku[i][j]:
                return False
    return True



def dfs(idx):
    #다 채움
    if zero == idx:
        for i in sdoku:
            for j in i:
                print(j, end='')
            print()
        sys.exit()
        return 10
    i, j = arr[idx]
    for n in range(1, 10):
        if hor(i, j, n) and ver(i, j, n) and squ(i, j, n):
            sdoku[i][j] = n
            # print(i, j, n)
            if dfs(idx + 1) == 10:
                return 10
            sdoku[i][j] = 0
    return 0

dfs(0)
