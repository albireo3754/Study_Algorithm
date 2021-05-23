import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

left, right = 0, 20000000000

def cut_tree(trees, mid):
    result = 0
    for tree in trees:
        if tree <= mid:
            break
        result += tree - mid
    return result
# cut_tree test
# print(cut_tree(trees, 15))
answer = (left + right) // 2
while left <= right:
    mid = (left + right) // 2
    temp = cut_tree(trees, mid)
    # print(temp)
    if temp >= M:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)
