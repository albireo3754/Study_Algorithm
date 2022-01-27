class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remain = 1
        result = []
        for digit in reversed(digits):
            digit += remain
            if digit >= 10:
                digit = 0
                remain = 1
            else:
                remain = 0
            result.append(digit)
        if remain:
            result.append(remain)
        return reversed(result)