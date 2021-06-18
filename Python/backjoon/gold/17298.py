import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
stack = []
stack.append((arr[0], 0))
answer = [-1 for i in range(N)]
for i in range(1, N):
    while stack and stack[-1][0] < arr[i]:
        _, idx = stack.pop()
        answer[idx] = arr[i]
    stack.append((arr[i], i))
    
print(*answer)