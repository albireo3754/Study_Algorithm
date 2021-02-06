from collections import deque
N, K= map(int, input().split(' '))
finded = set()
def solution():
    
    q = deque([[N, 0]])
    while True:
        find, time = q.popleft()
        if find == K:
            return time

        if find + 1 not in finded and find + 1 <= 100000:
            q.append([find + 1, time + 1])
            finded.add(find + 1)
            
        if find * 2 not in finded and find * 2 <= 100000:
            q.append([find * 2, time + 1])
            finded.add(find * 2)

        if find - 1 not in finded and find - 1 >= 0:
            q.append([find - 1, time + 1])
            finded.add(find - 1)

print(solution())
