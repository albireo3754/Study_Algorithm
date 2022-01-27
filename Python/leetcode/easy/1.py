from bisect import bisect_right
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_enum = sorted(list(enumerate(nums)), key=lambda x: x[1])
        nums.sort()
        for i, num in enumerate(nums):
            index = bisect_right(nums, target - num)
            if target - num == nums[index - 1]:
                return [nums_enum[i][0], nums_enum[index - 1][0]]
        