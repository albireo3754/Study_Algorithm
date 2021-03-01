import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

pre_order = []


def post_order(start, end):
    if start > end:
        return
    if start == end:
        print(pre_order[start])
        return
    root = pre_order[start]
    idx = start + 1
    while idx <= end and root > pre_order[idx]:
        idx += 1
    post_order(start + 1, idx - 1)
    post_order(idx, end)
    print(root)


temp = sys.stdin.readline().rstrip()

while temp:
    pre_order.append(int(temp))
    temp = sys.stdin.readline().rstrip()

# print(pre_order)
post_order(0, len(pre_order) - 1)
