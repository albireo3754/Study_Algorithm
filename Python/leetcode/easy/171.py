class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum((ord(char) - ord("A") + 1) * (26 ** i) for i, char in enumerate(reversed(columnTitle)))