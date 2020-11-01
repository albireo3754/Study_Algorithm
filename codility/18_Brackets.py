#1 - 62% 

def solution(S):
    # write your code in Python 3.6
    brackets = []

    for bracket in S:
        if (bracket == "{") or (bracket == "[") or (bracket == "{"):
            brackets.append(bracket)
        else:
            compBra = {"}" : "{", "]" : "[", ")" : "("}[brackets.pop()] 
            if compBra != bracket:
                return 0

    return 1
