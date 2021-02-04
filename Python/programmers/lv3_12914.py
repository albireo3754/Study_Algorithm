def solution(n):
    answer = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    dp = [[1] * (n + 1), [0 for i in range(n + 1)]]
    dp[1][0] = 1
    dp[1][1] = 1
    dp[1][2] = 2
    for i in range(3, n + 1):
        dp[1][i] = (dp[1][i - 1] + dp[1][i - 2]) % 1234567

    return dp[1][n]