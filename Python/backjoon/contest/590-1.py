import sys

input = sys.stdin.readline

N, M = map(int, input().split(' '))

dic = {}
for i in range(N):
    text = input().rstrip()
    len_t = len(text)
    if len_t < M:
        continue
    if text in dic:
        dic[text][0] += 1
    else:
        dic[text] = [1, len(text)]

sorted_dic = sorted(dic.items(), key = lambda x: (-x[1][0], -x[1][1], x[0]))

for i in sorted_dic:
    print(i[0])
