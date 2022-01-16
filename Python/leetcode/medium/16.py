class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[-1]
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(target - closest) > abs(temp - target):
                    closest = temp
                if temp < target:
                    j += 1
                else:
                    k -= 1
            if closest == target:
                return closest
        return closest
            