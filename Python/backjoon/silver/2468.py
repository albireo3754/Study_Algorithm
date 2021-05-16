import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())

grid = []
for i in range(N):
    grid.append(list(map(int, input().split())))

direction = ((1, 0), (0, 1), (-1, 0), (0, -1))

water = 0
def dfs(i, j):
    global N
    global water
    ## 다른 end조건    
    for di, dj in direction:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            # print(visited[ni][nj])
            if visited[ni][nj] == True:
                continue

            if grid[ni][nj] < water:
                visited[ni][nj] = True
                dfs(ni, nj)

def dfs2(i, j):
    global N
    global water
    ## 다른 end조건    
    for di, dj in direction:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N:
            if visited[ni][nj] == True:
                continue
            if grid[ni][nj] >= water:
                visited[ni][nj] = True
                dfs2(ni, nj)


# for i in visited:
#     print(i)

answers = []
visited = []
for w in range(100):
    water = w
    answer = 0
    visited = [[False for i in range(N)] for i in range(N)] 
    for i in range(N):
        for j in range(N):
            if grid[i][j] < water:
                visited[i][j] = True
                dfs(i, j)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                dfs2(i, j)
                answer += 1
    if answer == 0:
        break
    answers.append(answer)
            # for k in visited:
            #     print(k)
            
            # print(i, j)
print(answers)
print(max(answers))