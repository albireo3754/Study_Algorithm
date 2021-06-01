import sys
from collections import deque
input = sys.stdin.readline

T = int(input())



for i in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1: -1].split(',')

    discard = 1
    q = deque()
    for j in range(n):
        q.append(arr[j])
    for func in p:
        if func == 'R':
            discard *= -1
        elif func == 'D':
            if len(q) == 0:
                print('error')
                break
            if discard == 1:
                q.popleft()
            else:
                q.pop()
    else:
        if discard == 1:
            content = ','.join(q)
            print(f'[{content}]')
        else:
            content = ','.join(reversed(q))
            print(f'[{content}]')
        # print(q)
