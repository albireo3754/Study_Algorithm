import sys
import heapq
input = sys.stdin.readline

INF = 1e8
direction = ((1, 0), (0, 1), (-1, 0), (0, -1))
idx = 1
while True:
    T = int(input())
    if T == 0:
        break
    grid = [list(map(int, input().split())) for i in range(T)]
    
    dp = [[INF for i in range(T)] for i in range(T)]
    dp[0][0] = grid[0][0]
    q = []
    q.append((dp[0][0], 0, 0))
    
    while q:
        v, i, j = heapq.heappop(q)
        if v > dp[i][j]:
            continue

        for di, dj in direction:
            ni, nj = i + di, j + dj
            # print(ni, nj)
            if 0 <= ni < T and 0 <= nj < T:
                if dp[ni][nj] > dp[i][j] + grid[ni][nj]:
                    dp[ni][nj] = dp[i][j] + grid[ni][nj]
                    heapq.heappush(q, (dp[ni][nj], ni, nj))
    # print(dp)
    print(f"Problem {idx}: {dp[T - 1][T - 1]}")
    idx += 1