n = int(input())

dp = [[0 for i in range(n + 1)] for i in range(10)]

for i in range(1, 10):
    dp[i][1] = 1

if n == 1:
    print(9)
else:
    for j in range(2, n + 1):
        dp[0][j] = dp[1][j - 1]
        dp[9][j] = dp[8][j - 1]
        for i in range(1, 9):
            dp[i][j] = (dp[i - 1][j - 1] + dp[i + 1][j - 1])

    answer = 0
    for i in range(0, 10):
        answer += dp[i][-1] 

    # print(dp)
    print(answer% 1000000000)