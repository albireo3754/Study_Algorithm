class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        n = len(nums)
        
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum > 0:
                    k -= 1
                elif _sum < 0:
                    j += 1
                else:
                    answer.append((nums[i], nums[j], nums[k]))
                    j += 1
                while i + 1 < j < n and nums[j] == nums[j - 1]:
                    j += 1
                while 0 <= k < n - 1 and nums[k] == nums[k + 1]:
                    k -= 1
                
        return answer