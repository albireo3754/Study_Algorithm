import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))


pos = list(map(int, input().split(' ')))
dist = list(map(int, input().split(' ')))

answer = 1
i = 0
flag = 0
xi = pos[0] + dist[0]
next_pi = 1
if xi >= M:
    print(0)
else:
    while i < len(pos):
        max_pi = xi 
        while i < len(pos) and xi >= pos[i]:
            max_pi = max(max_pi, pos[i] + dist[i])
            i += 1
        if i < len(pos) and max_pi < pos[i]:
            break
        xi = max_pi

        if max_pi >= M:
            flag = 1
            break
        answer += 1

    if flag == 0:
        print(-1)
    else:
        print(answer)