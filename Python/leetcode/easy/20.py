class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {")":"(","]":"[","}":"{"}
        brackets = s
        for bracket in brackets:
            if bracket in dic:
                if len(stack) == 0:
                    return False
                if stack[-1] == dic[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        return False if stack else True