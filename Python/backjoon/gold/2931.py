import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())

grid = [list(input().rstrip()) for i in range(R)]

direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

goable = [['|', '+', '1', '4', 'Z', 'M'], ['|', '+', '2', '3', 'Z', 'M'], ['-', '+', '1', '2', 'Z', 'M'], ['-', '+', '3', '4', 'Z', 'M']]

def intersection(arr):
    print(arr)
    return set(goable[arr[1]]).intersection(set(goable[arr[0]]))

def get_block(B):
    return grid[B[0]][B[1]]

def swap(i, j):
    return j, i

def minus(i, j):
    return i * -1, j * -1

def sub(A, B):
    return A[0] - B[0], A[1] - B[1]

def go(A, B, block):
    i, j = 0, 0
    if block == '3' or block == '4':
        i, j = sub(B, A)
        i, j = swap(i, j)
    elif block == '1' or block == '2':
        i, j = sub(B, A)
        i, j = swap(i, j)
        i, j = minus(i, j)
    else:
        i, j = sub(B, A)
    
    return B[0] + i, B[1] + j

def find_hacked(A, B):
    visited =  [[False for i in range(C)] for i in range(R)]
    i, j = A
    visited[i][j] == True
    q = deque()
    q.append((A, B))
    while q:
        A, B = q.popleft()
        print(A, B)
        block = get_block(B)
        if block == '+':
            i, j = B
            for di, dj in direction:
                ni, nj = i + di, j + dj
                if visited[ni][nj]:
                    continue
                if grid[ni][nj] == '.':
                    return (B, (ni, nj))
                visited[ni][nj] = True
                q.append((B, (ni, nj)))
        else:
            A, B = B, go(A, B, block)
            if get_block(B) == '.':
                return A, B
            if visited[B[0]][B[1]]:
                continue
            visited[B[0]][B[1]] = True
            q.append((A, B))

def find_block(B):
    i, j = B
    print(B)
    temp = []
    for dd, (di, dj) in enumerate(direction):
        ni, nj = i + di, j + dj
        if grid[ni][nj] in goable[dd]:
            temp.append(dd)
    return temp
A, B = [], []

for i in range(R):
    for j in range(C):
        if grid[i][j] == 'M':
            print(i, j)
            for dd, (di, dj) in enumerate(direction):
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C:
                    print(grid[ni][nj], goable[dd])
                    if grid[ni][nj] in goable[dd]:
                        A, B = find_hacked((i, j), (ni, nj))

inter_set = intersection(find_block(B))
inter_set.remove('+')
if len(inter_set) == 0:
    print(B[0] + 1, B[1] + 1, '+')
else:
    print(B[0] + 1, B[1] + 1, inter_set.pop())

# 5 7
# .......
# ..1-4..
# .M++.Z.
# ..2+3..
# .......