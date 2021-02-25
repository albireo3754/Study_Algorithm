import sys

input = sys.stdin.readline

N = int(input())

grid = []

for i in range(N):
    grid.append(list(map(int, list(input().rstrip()))))

def div(i, j, n):
    if n == 1:
        return str(grid[i][j])
    n = n // 2

    a = div(i, j, n)
    b = div(i, j + n, n)
    c = div(i + n, j, n)
    d = div(i + n, j + n, n)
    if a == b == c == d and a[0] != '(':
        return a
    else:
        return '(' + a + b + c + d + ')'


answer = div(0, 0, N)
print(answer)