import sys

input = sys.stdin.readline

A, B, C = map(int, input().split(' '))

answer = 1
while B:
    if B%2 == 0:
        A = (A * A) % C
        B = B // 2
    else:
        answer = (answer * A) % C
        B = B - 1
print(answer)
        