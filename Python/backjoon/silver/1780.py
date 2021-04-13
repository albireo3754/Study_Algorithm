import sys

input = sys.stdin.readline

N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]
answer = [0,0,0,0]
def div(N, i, j):
    if N == 1:
        answer[grid[i][j] + 1] += 1
        return grid[i][j]
    
    n = N // 3
    res = []
    res.append(div(n, i, j))
    res.append(div(n, i, j + n))
    res.append(div(n, i, j + n * 2))
    res.append(div(n, i + n, j))
    res.append(div(n, i + n, j + n))
    res.append(div(n, i + n, j + n * 2))
    res.append(div(n, i + n * 2, j))
    res.append(div(n, i + n * 2, j + n))
    res.append(div(n, i + n * 2, j + n * 2))

    a = res[0]
    for i in range(9):
        if res[i] != a or a > 1:
            break
    else:
        answer[a + 1] += 1
        if N != 1:
            answer[a + 1] -= 9
        return a
    
    return 2
res = div(N, 0, 0)

for i in range(3):
    print(answer[i])