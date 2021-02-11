N, M = map(int, input().split(''))

answer = []
before = []

def dfs(start_idx, i):
    for i in range(start_idx, N + 1):
        
