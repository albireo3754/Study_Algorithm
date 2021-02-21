import sys
input = sys.stdin.readline
N, T = map(int, input().split(' '))
exps = [(0, 0)]
for i in range(1, N + 1):
    ci, ei = map(int, input().split(' '))
    exps.append((ci, ei))
times = [[0] * (N + 1)]
answer = []
for i in range(1, N + 1):
    times.append([0] + list(map(int, input().split(' '))))
dp = [[0 for i in range(N + 1)] for i in range(T + 1)]

for i in range(N + 1):
    if exps[i][0] > 0:
        dp[0][i] = -9876543212345
for t in range(1, T + 1):
    for n in range(1, N + 1):
        dp[t][n] = dp[t - 1][n] + exps[n][1]
        for i in range(1, N + 1):
            if n != i and t - times[i][n] >= 0 and dp[t - times[i][n]][i] >= exps[n][0]:
                dp[t][n] = max(dp[t - times[i][n]][i], dp[t][n])

print(max(dp[T]))   

# def dfs(pos, exp, time, visited):
#     if time == T:
#         answer.append(exp)
#         return
#     if time > T:
#         return
#     for i in range(0, len(times[pos])):
#         if times[pos][i] == 0:
#             dfs(pos, exp + exps[pos][1], time + 1, visited)
#         else:
#             if exp < exps[i][0] or i in visited:
#                 continue
#             visited.add(i)
#             dfs(i, exp, time + times[pos][i], visited)
#             visited.remove(i)
# for i, v in enumerate(exps):
#     if v[0] == 0:
#         dfs(i, 0, 0, set())
# print(max(answer))

