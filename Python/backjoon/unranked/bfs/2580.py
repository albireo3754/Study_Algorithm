import sys

input = sys.stdin.readline
graph=[]
for i in range(9):
    graph.append(list(map(int, input().split())))

def row(x,k):
    if k in graph[x]:
        return False
    return True
def col(y,k):
    for i in range(9):
        if k==graph[i][y]:
            return False
    return True
def check(x,y,k):
    nx=x//3*3
    ny=y//3*3
    #3x3 행렬에 동일한 값이 중복될 경우
    for i in range(3):
        for j in range(3):
            if k==graph[nx+i][ny+j]: return False
    return True
def backtracking(cnt):
    # print(cnt)
    #모든 스도쿠를 다 채웠다면 출력
    if result==cnt:
        for r in graph:
            print(*r)
        return 1
    x,y= arr[cnt]
    # print(x,y)
    for k in range(1,10):
        if row(x,k) and col(y,k) and check(x,y,k):
            graph[x][y]=k
            flag = backtracking(cnt+1)
            if flag:
                return flag
            graph[x][y]=0
    return 0
result=0
arr=[]
for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            result+=1
            arr.append((i,j))

graph=backtracking(0)
