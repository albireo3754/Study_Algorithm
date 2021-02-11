N, M = map(int, input().split(' '))

answer = []
before = []

def dfs(start_idx):
    if len(before) == M:
        answer.append(before[:])
    for j in range(start_idx + 1, N + 1):
        before.append(j)
        dfs(j)
        before.pop()

dfs(0)
for i in answer:
    print(*i)