def solution(n, money):
    money.sort()
    dp = [0 for i in range(n + 1)]
    for i in range(1, len(money) + 1):
        dp[0] = 1
        for j in range(1, n + 1):
            if j - money[i - 1] >= 0:
                dp[j] = (dp[j - money[i - 1]] + dp[j])%1000000007
        
    return dp.pop()