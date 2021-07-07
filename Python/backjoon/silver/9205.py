import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

for _ in range(T):
    N = int(input())
    arr = []
    
    for i in range(N + 2):
        x, y = map(int, input().split())
        arr.append((x, y, i))
    comp = arr[0][:2]
    # arr.sort(key = lambda x: abs(x[0] - comp[0]) + abs(x[1] - comp[1]))
    # left = 0
    # right = 1
    edge = [[] for i in range(N + 2)]
    for i in range(N + 2):
        for j in range(i + 1, N + 2):
            # print(i, j)
            if dist(arr[i], arr[j]) <= 1000:
                edge[arr[i][2]].append(arr[j][2])
                edge[arr[j][2]].append(arr[i][2])
    visited = [False for i in range(N + 2)]
    visited[0] = True
    # print(edge)
    # def dfs(here):
    #     # print(here)
    #     if here == N + 1:
    #         return True
    #     for there in edge[here]:
    #         if visited[there]:
    #             continue
    #         visited[there] = True
    #         if dfs(there):
    #             return True
    #         visited[there] = False
    #     return False
    def bfs(here):
        q = deque()
        q.append(here)
        while q:
            here = q.popleft()
            if here == N + 1:
                return True
            for there in edge[here]:
                if visited[there]:
                    continue
                visited[there] = True
                q.append(there)
        return False
    print('happy' if bfs(0) else 'sad')
    # while right < N:
        # arr[right] - arr[left]