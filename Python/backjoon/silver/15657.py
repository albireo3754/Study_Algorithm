import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))
nums.sort()
temp = []
answer = []
def dfs(idx, l):

    if l == M:
        answer.append(temp[:])
        return

    for i in range(idx, N):
        temp.append(nums[i])
        dfs(i, l + 1)
        temp.pop()

dfs(0, 0)

for a in answer:
    print(*a)


