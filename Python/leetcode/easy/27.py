class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first_idx = 0
        last_idx = len(nums) - 1
        while first_idx < len(nums) and nums[first_idx] != val:
            first_idx += 1
        while last_idx >= 0 and nums[last_idx] == val:
            last_idx -= 1
        while first_idx < last_idx:
            nums[first_idx], nums[last_idx] = nums[last_idx], nums[first_idx]
            while first_idx < len(nums) and nums[first_idx] != val:
                first_idx += 1
            while last_idx >= 0 and nums[last_idx] == val:
                last_idx -= 1
        return last_idx + 1