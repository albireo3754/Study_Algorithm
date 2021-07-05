import sys
input = sys.stdin.readline

K, N, F = map(int, input().split(' '))

edge = [[False for i in range(N + 1)] for i in range(N + 1)]
go = [True for i in range(N + 1)]
visited = [False for i in range(N + 1)]
for i in range(F):
    a, b = map(int, input().split(' '))
    edge[a][b] = True
    edge[b][a] = True

answer = []
def dfs(i):
    global answer
    # print(i, temp)
    if len(temp) == K:
        answer = temp[:]
        return

    for j in range(i + 1, N + 1):
        flag = True
        for k in temp:
            if not edge[j][k]:
                flag = False
                break
        if flag:
            temp.append(j)
            dfs(j)
            if len(answer) > 0:
                return
            temp.pop()


flag = False
for i in range(1, N + 1):
    temp = [i]
    visited = [False for i in range(N + 1)]
    dfs(i)
    if len(temp) == K:
        for i in temp:
            print(i)
        break
else:
    print(-1)