import sys
import bisect
input = sys.stdin.readline

N, M = map(int, input().split(' '))
points = list(map(int, input().split(' ')))
points.sort()
for _ in range(M):
    a, b = map(int , input().split(' '))
    i = bisect.bisect_left(points, a)
    j = bisect.bisect_right(points, b)
    print(j - i)

