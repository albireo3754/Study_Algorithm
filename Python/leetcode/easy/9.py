class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        remain, _x = 0, x
        y = 0
        while _x > 0:
            remain, _x = _x % 10, _x // 10
            y = y * 10 + remain
        return y == x