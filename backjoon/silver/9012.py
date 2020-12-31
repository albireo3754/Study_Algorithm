import sys

N = int(sys.stdin.readline().rstrip())
def test():
    testset = sys.stdin.readline().rstrip()
    stack = []
    for parenthesis in testset:
        if parenthesis == "(":
            stack.append(parenthesis)
        elif parenthesis == ")":
            if len(stack) == 0 or stack.pop() == ")":
                return "NO"
    return "YES"
for i in range(N):
    print(test())