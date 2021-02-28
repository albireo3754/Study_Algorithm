import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input())
arr = [0 for i in range(10)]
if M > 0:
    for i in list(map(int, input().split(' '))):
        arr[i] = 1
start = ''

answer = [abs(N - 100)]
size = len(str(N))
def dfs(idx, visited):
    if idx >= size: 
        if len(visited) > 0:
            answer[0] = min(answer[0], abs(N - int(visited)) + len(str(int(visited))))
        return
    for i, v in enumerate(arr):
        if v == 0:
            dfs(idx + 1, visited + str(i))
if M < 10:
    dfs(-1, '')
    dfs(0, '')
    dfs(1, '')
print(answer[0])