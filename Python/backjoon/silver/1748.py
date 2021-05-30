import sys

input = sys.stdin.readline

N = int(input())

a = 1
cnt = 1
answer = 0
while a * 10 <= N:
    answer += 9 * a * cnt
    a *= 10
    cnt += 1
else:
    answer += (N - a + 1) * cnt
print(answer)