import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())

inorder = list(map(int, input().split(' ')))
postorder = list(map(int, input().split(' ')))
in_pos = [0] * (n + 1)
for i, v in enumerate(inorder):
    in_pos[v] = i

tree = []
def recur(x, y):
    if y[1] - y[0] <= 0:
        return
    root = postorder[y[1] - 1]
    tree.append(root)
    if x[1] - x[0] == 1:
        return
    i = in_pos[root] - x[0]
    recur((x[0], x[0] + i), (y[0], y[0] + i))
    recur((x[0] + i + 1, x[1]), (y[0] + i, y[1] - 1))

recur((0, len(inorder)), (0, len(postorder)))
print(*tree)