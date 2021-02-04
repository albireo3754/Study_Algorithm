import sys
sys.setrecursionlimit(100000)

answers = []
for i in range(int(input())):
    m, n, bug = map(int, input().split(' '))
    grid = [[0 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(bug):
        x, y = map(int, input().split(' '))
        grid[x][y] = 1
    
    def dfs(x, y):
        if x == m + 1 or y == n + 1 or x == -1 or y == -1:
            return;
        if grid[x][y] == 1:
            grid[x][y] = 0
            dfs(x + 1, y)
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
    
    answer = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                answer += 1
    answers.append(answer)

for answer in answers:
    print(answer)