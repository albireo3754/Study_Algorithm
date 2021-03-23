import math
import sys

input = sys.stdin.readline

for i in range(int(input())):
    a, b = map(int, input().split(' '))
    print(math.comb(b, a))
