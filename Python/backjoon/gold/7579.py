import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))


memory = list(map(int ,input().split(' ')))
cost = list(map(int, input().split(' ')))

dp = [[0 for i in range(sum(cost) + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    # for j in range(cost[i - 1], len(dp[0])):
    #     dp[i][j] = max(dp[i][j - cost[i - 1]] + memory[i - 1], dp[i - 1][j])
    for j in range(len(dp[0])):
        if j >= cost[i - 1]:
            dp[i][j] = max(dp[i - 1][j - cost[i - 1]] + memory[i - 1], dp[i][j])
        dp[i][j] = max(dp[i][j], dp[i - 1][j])
# for i in dp:
#     print(i)

for j in range(1,len(dp[0])):
    for i in range(N + 1):
        if dp[i][j] >= M:
            print(j)
            # print(dp[i])
            break
    else:
        continue
    break