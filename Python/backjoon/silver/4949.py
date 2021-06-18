import sys

input = sys.stdin.readline

left = ["(", "["]
right = [")", "]"]
while True:
    stack = []

    string = input().rstrip()
    if string == ".":
        break

    for char in string:
        if char in left:
            stack.append(char)
        if char in right:
            if stack and left[right.index(char)] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
                break
    if len(stack) > 0:
        print("no")
    else:
        print("yes")    