class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        squares = [integer ** 2 for integer in range(2, int(n ** 0.5) + 1)]
        for square in squares:
            for i in range(n+ 1 - square):
                dp[i + square] = min(dp[i + square], dp[i] + 1)
        return dp[n]