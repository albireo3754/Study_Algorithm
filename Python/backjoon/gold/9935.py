import sys

input = sys.stdin.readline

N = input().rstrip()

M = input().rstrip()

m = len(M)
bomb = []
last = M[-1]
idx = 0
for n in N:
    bomb.append(n)
    if n == M[-1] and ''.join(bomb[-m:]) == M:
        for _ in range(m):
            bomb.pop()

print(''.join(bomb) if len(bomb) > 0 else "FRULA")