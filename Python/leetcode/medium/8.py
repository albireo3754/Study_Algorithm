class Solution:
    def myAtoi(self, s: str) -> int:
        stack = []
        s = s.lstrip()
        start = 0
        plus = 1
        if len(s) == 0:
            return 0
        if s[start] == "-":
            plus = -1
            start += 1
        elif s[start] == "+":
            start += 1
        for i in range(start, len(s)):
            if 0 <= ord(s[i]) - ord("0") <= 9:
                stack.append(ord(s[i]) - ord("0"))
            else:
                break
        print(stack)
        answer = 0
        digit = 1
        while stack:
            answer += stack.pop() * digit
            digit *= 10 
        answer *= plus
        if answer >= 2 ** 31:
            return 2**31 - 1
        elif answer <= -2 ** 31 - 1:
            return -2**31
        return answer