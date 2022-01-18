class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        n = len(nums)
        nums.sort()
        for a in range(n - 3):
            b = a + 1
            while b < n - 2:
                c, d = b + 1, n - 1
                while c < d:
                    result = nums[a] + nums[b] + nums[c] + nums[d]
                    if target > result:
                        c += 1
                    elif target < result:
                        d -= 1
                    else:
                        answer.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                b += 1
        return answer