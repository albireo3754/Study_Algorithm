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
while i < len(pos):
    max_pi = xi 
    while next_pi < len(pos) and xi >= pos[next_pi]:
        max_pi = max(max_pi, pos[next_pi] + dist[next_pi])
        next_pi += 1
    xi = max_pi
    i = next_pi

    if max_pi >= M:
        flag = 1
        break
    answer += 1

if flag == 0:
    print(-1)
else:
    print(answer)