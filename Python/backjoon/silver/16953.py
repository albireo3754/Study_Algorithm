import sys

input = sys.stdin.readline

A, B = map(int, input().split(' '))

b = B
cnt = 0
while b > A:
    # print(b)
    if b % 2 == 0:
        b = b // 2
    else:
        if b % 10 == 1:
            b = b // 10
        else:
            b = -1
    cnt += 1

print(cnt + 1 if A == b else -1)