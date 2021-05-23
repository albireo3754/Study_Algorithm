import sys
import math
input = sys.stdin.readline

N = int(input())

Ai = list(map(int, input().split()))
B, C = map(int, input().split()) 
# print(Ai)

answer = 0

Ai = list(map(lambda x: x - B, Ai))
answer += N
for A in Ai:
    if A <= 0:
        continue
    else:
        answer += math.ceil((A / C))
print(answer)