import sys

input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split(' ')))
stack = []
answer = []
for i in range(N):
    while stack and stack[-1][0] < tower[i]:
        stack.pop()
    if stack:
        answer.append(stack[-1][1] + 1)
        stack.append((tower[i], i))
    else:
        answer.append(0)
        stack.append((tower[i], i))

print(*answer)


