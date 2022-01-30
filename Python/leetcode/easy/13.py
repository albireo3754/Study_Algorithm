class Solution:
    def ctoi(self, s):
        return {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}[s]
    def romanToInt(self, s: str) -> int:
        temp = 0
        answer = 0
        for c in s:
            i = self.ctoi(c)
            if temp == 0:
                temp = i
            elif temp >= i:
                answer += temp
                temp = i
            else:
                answer += i - temp
                temp = 0
        return answer + temp