import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

edge = [[] for i in range(N + 1)]
re_edge = [[] for i in range(N + 1)]
pre = [0 for i in range(N + 1)]
visited = [-1 for i in range(N + 1)]
time = [0 for i in range(N + 1)]
dp = [0 for i in range(N + 1)]
for i in range(1, N + 1):
    task = list(map(int, input().split(' ')))
    time[i] = task[0]
    pre[i] = task[1]
    for j in task[2:]:
        edge[j].append(i)
        re_edge[i].append(j)
# print(edge)
q = deque()
for i in range(N + 1):
    if pre[i] == 0:
        q.append(i)
        dp[i] = time[i]
# answer = 0
while q:
    here = q.popleft()
    visited[here] = 1
    # answer += time[here]
    for there in edge[here]:
        dp[there] = max(dp[there], dp[here] + time[there])
        if visited[there] > -1:
            continue
        pre[there] -= 1
        if pre[there] == 0:
            
            q.append(there)

# print(time)
print(max(dp))