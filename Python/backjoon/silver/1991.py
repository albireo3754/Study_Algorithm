import sys

input = sys.stdin.readline

N = int(input())

tree = [[]] * N
for i in range(N):
    parent, left, right = map(lambda x: ord(x) - ord('A')
                ,input().rstrip().split(' '))
    tree[parent] = [left, right]

pre = []
post = []
in_ = []

def order(root):
    pre.append(chr(root + ord('A')))
    if tree[root][0] >= 0:
        order(tree[root][0])
    in_.append(chr(root + ord('A')))
    if tree[root][1] >= 0:
        order(tree[root][1])
    post.append(chr(root + ord('A')))

order(0)

print(''.join(pre))
print(''.join(in_))
print(''.join(post))