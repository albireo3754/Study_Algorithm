from collections import deque

N, K = map(int, input().split(' '))

q = deque([(N, 0)])
visited = [0] * (1000001)


def bfs(q):
    while True:
        after_q = deque()
        while q:
            position, time = q.popleft()
            if position < 0 or position > 1000000:
                continue
            if visited[position]:
                continue
            visited[position] = 1
            if position == K:
                return time
            q.append((position * 2, time))
            after_q.append((position + 1, time + 1))
            after_q.append((position - 1, time + 1))
        q = after_q


print(bfs(deque([(N, 0)])))
