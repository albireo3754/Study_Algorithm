class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        first = -1000000
        twice = -1000000
        REMOVED = -20000000
        for i, num in enumerate(nums):
            if twice == num:
                nums[i] = REMOVED
            elif first == num:
                twice = num
            else:
                first = num
        for i, num in enumerate(nums):
            if num == REMOVED:
                for j in range(i + 1, len(nums)):
                    if nums[j] != REMOVED:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                else:
                    return i
        