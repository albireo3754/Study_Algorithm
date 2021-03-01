import sys
import bisect
sys.setrecursionlimit(100000)
input = sys.stdin.readlines

def post_order(start, end):
    if start >= end:
        return
    if start + 1 == end:
        print(pre_order[start])
        return
    root = pre_order[start]
    # idx = start + 1
    # while idx <= end and root > pre_order[idx]:
    #     idx += 1
    idx = bisect.bisect_left(pre_order, root, start + 1, end)
    
    post_order(start + 1, idx)
    post_order(idx, end)
    print(root)

pre_order = list(map(int, input()))
# print(pre_order)

post_order(0, len(pre_order))