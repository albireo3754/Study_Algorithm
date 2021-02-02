import sys
from collections import defaultdict
N = int(input())
sangen = map(int ,sys.stdin.readline().rstrip().split(" "))
M = int(input())
card = map(int, sys.stdin.readline().rstrip().split(" "))

card_cnt = defaultdict(int)
for i in sangen:
    card_cnt[i] += 1

answer = [card_cnt[i] for i in card]
print(*answer)