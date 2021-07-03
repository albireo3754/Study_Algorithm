import sys
input = sys.stdin.readline

N, a, b = map(int, input().split())

answer = 0
while a != b:
    answer += 1
    a = (a + 1) // 2
    b = (b + 1) // 2

print(answer)