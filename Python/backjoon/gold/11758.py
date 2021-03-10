import sys
import math
input = sys.stdin.readline

p1 = list(map(int, input().split(' ')))
p2 = list(map(int, input().split(' ')))
p3 = list(map(int, input().split(' ')))


for p in (p2, p3, p1):
    p[0] -= p1[0]
    p[1] -= p1[1]

# print(p1, p2, p3)

if p3[0] * p2[1] == p3[1] * p2[0]:
    print(0)
else:
    r = math.sqrt(p2[0] ** 2 + p2[1] ** 2)

    cos = p2[0] / r
    sin = p2[1] / r
    rot = [[cos, sin], [-sin, cos]]
    rp2 = [r, 0]
    rp3 = [0, 0]

    for i in range(2):
        for j in range(len(rot[i])):
            rp3[i] += rot[i][j] * p3[j]
    # print(rp3)
    if rp3[1] > 0:
        print(1)
    else:
        print(-1)
# 1 1
# 7 3
# 5 5