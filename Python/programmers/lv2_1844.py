import sys

input = sys.stdin.readline

from collections import deque

DIRECTION = ((1, 0), (0, 1), (-1, 0), (0, -1))
def solution(maps):
    answer = 1
    q = deque()
    q.append((0, 0))
    n = len(maps)
    m = len(maps[0])
    visited = [[False for j in range(m)] for i in range(n)]
    while q:
        for i in range(len(q)):
            i, j = q.popleft()
            if i == n - 1 and j == m - 1:
                return answer
            for di, dj in DIRECTION:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and maps[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj))
        answer += 1
    return -1