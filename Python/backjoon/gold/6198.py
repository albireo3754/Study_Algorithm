import sys
# import bisect
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
# print(arr)
answer = 0
stack = [arr[0]]
for i in range(1, N):
    while stack and stack[-1] <= arr[i]:
        stack.pop()
    answer += len(stack)
    stack.append(arr[i])
print(answer)