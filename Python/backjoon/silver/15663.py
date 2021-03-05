import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))
nums = list(map(int, input().split(' ')))

nums.sort()
# print(nums)
answer = set()
def dfs(l, temp, idx):
    # print(l, temp, idx)

    if l == M:
        if temp not in answer:
            print(temp)
            answer.add(temp)
        return

    for i in range(idx, len(nums)):
        if l == 0:
            dfs(l + 1, str(nums[i]), i)
        else:
            dfs(l + 1, temp + ' ' + str(nums[i]), i)

dfs(0, '', 0)

