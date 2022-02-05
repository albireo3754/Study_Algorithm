from functools import cmp_to_key
class Solution:
    def sorting_key(self, x, y):
        x = str(x)
        y = str(y)

        return int(x + y) - int(y + x)
    def largestNumber(self, nums: List[int]) -> str:
        cmp = self.sorting_key
        result = "".join([str(num) for num in sorted(nums, key=cmp_to_key(cmp), reverse=True)])
        if result[0] == "0":
            return "0"
        return result