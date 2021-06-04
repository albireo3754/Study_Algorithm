import sys

input = sys.stdin.readline

N = int(input())

arr = list(input().split())
# print(arr)


answer = ['999999999999', '000000000']

num_set = set([i for i in range(10)])

def dfs(string):
    # print(num_set)
    if len(string) == N + 1:
        answer[0] = min(answer[0], string)
        answer[1] = max(answer[1], string)
        return

    if arr[len(string) - 1] == '<':
        for i in range(int(string[-1]) + 1, 10):
            if i in num_set:
                num_set.remove(i)
                dfs(string + str(i))
                num_set.add(i)
    else:   
        for i in range(int(string[-1]) - 1, -1, -1):
            if i in num_set:
                num_set.remove(i)
                dfs(string + str(i))
                num_set.add(i)
for i in range(10):
    num_set.remove(i)
    dfs(str(i))
    num_set.add(i)

for i in reversed(answer):
    print(i)