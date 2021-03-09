import sys

input = sys.stdin.readline

N, B = map(int, input().split(' '))
matrix = []

ans=[[0 for i in range(N)] for i in range(N)]
for i in range(N):
    matrix.append(list(map(int, input().split(' '))))
    ans[i][i] = 1
temp=[[0 for i in range(N)] for i in range(N)]
def mul(a, b):
    for i in range(N):
        for j in range(N):
            temp[i][j] = 0
            for k in range(N):
                temp[i][j] += (a[i][k] * b[k][j])
            temp[i][j] %= 1000
    for i in range(N):
        for j in range(N):
            a[i][j] = temp[i][j]
            
while B > 0:
    if B % 2 == 1:
        mul(ans, matrix)
    mul(matrix, matrix)
    B = B // 2

for i in ans:
    print(*i)