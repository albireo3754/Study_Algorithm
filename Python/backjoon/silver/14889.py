import sys
from itertools import combinations
import math

input = sys.stdin.readline

N = int(input())

grid = [list(map(int, input().split())) for i in range(N)]
# combinations()
combs = list(combinations(range(N), N // 2))
answer = float("inf")

def calc_stat(comb):
    ret = 0
    for i in comb:
        for j in comb:
            if i == j:
                continue
            ret += grid[i][j]
    return ret

lencombs = len(combs)
for i, comb1 in enumerate(combs):
    if lencombs // 2 == i:
        break
    comb2 = combs[- i - 1]
    start = calc_stat(comb1)
    link = calc_stat(comb2)
    answer = min(answer, abs(start - link))
    
print(answer)
