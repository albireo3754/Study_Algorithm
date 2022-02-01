class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -100000
        now_sum = 0
        for num in nums:
            now_sum += num
            if now_sum >= max_sum:
                max_sum = now_sum
            if now_sum < 0:
                now_sum = 0
        return max_sum