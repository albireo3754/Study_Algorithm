import sys

input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
stack = []

def do():
    j = 0
    answer = []
    # print(arr)
    for i in range(1, N + 1):
        # print(i, j)
        stack.append(i)
        answer.append("+")
        while stack and arr[j] == stack[-1]:
            stack.pop()
            answer.append("-")
            j += 1
        if j == N:
            return answer
    return ["NO"]

for i in do():
    print(i)