import sys

input = sys.stdin.readline

N = int(input())

texts = list(input().rstrip())

r = 1 # 1. blue
b = 1 # 1. red

r_cnt = 0 # 2. red on blue
b_cnt = 0 # 2. blue on red
for t in texts:
    
    if t == 'R':
        b += b_cnt
        b_cnt = 0
        r_cnt = 1
    else:
        r += r_cnt
        r_cnt = 0
        b_cnt = 1

print(max(r, b))