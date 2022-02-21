class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n > 0:
            answer += (n & 1)
            n = n >> 1
        return answer