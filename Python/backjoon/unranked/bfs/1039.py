import sys
from collections import deque
input = sys.stdin.readline

N, K = input().split(' ')
k = int(K)
N_arr = list(N)
q = deque()
visited = [False for i in range(10000011)]
def bfs(N_arr, k):
    q.append(N_arr)
    n = len(N_arr)
    visited[int(''.join(N_arr))]
    if n == 1:
        return -1
    tempq = deque()
    answer = 0
    while k > 0:
        while q:
            arr = q.pop()
            for i in range(n - 1):
                for j in range(i + 1, n):
                    new_arr = arr[:]
                    new_arr[i], new_arr[j] = new_arr[j], new_arr[i]
                    if new_arr[i] == '0':
                        continue
                    new_int = int(''.join(new_arr))
                    if visited[new_int] == False:
                        tempq.append(new_arr)
                        visited[new_int] = True

        while tempq:
            tq = tempq.pop()
            new_int = int(''.join(tq))
            if k == 1:
                answer = max(answer, new_int)
            visited[new_int] = False
            q.append(tq)
        if not q and not tempq:
            return -1
        k -= 1
    return answer
print(bfs(N_arr, k))
