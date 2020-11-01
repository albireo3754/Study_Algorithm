#1 - 62% 
#why i got 62% score? -> don't check if parenthenis ends at left bracket
#2 - 100%

def solution(S):
    # write your code in Python 3.6
    brackets = []

    for bracket in S:
        if (bracket == "{") or (bracket == "[") or (bracket == "("):
            brackets.append(bracket)
        else:
            if len(brackets) == 0:
                return 0
                
            compBra = {"{" : "}", "[" : "]", "(" : ")"}.get(brackets.pop()) 
            if compBra != bracket:
                return 0

    if len(brackets) == 0:
        return 1
    else:
        return 0