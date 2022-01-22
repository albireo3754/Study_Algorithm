class Solution:
    def reverse(self, x: int) -> int:
        prefix = ""
        if x < 0:
            prefix = "-"
            x *= -1
        x = int(prefix + str(x)[::-1])
        if (-2**31 > x) or (2**31 - 1 < x):
            return 0
        return x