import sys

input = sys.stdin.readline

a = ord('a')


def make_ord(chr):
    return ord(chr) - a


mask = 0
for i in range(26):
    mask |= 1 << i
# print(ords)
# print(bin(mask))
N, M = map(int, input().split(' '))
N_arr = [0 for i in range(N)]
for i in range(N):
    str_ = input().rstrip()
    bit = 0
    for j in str_:
        bit |= 1 << (make_ord(j))
    N_arr[i] = bit

for i in range(M):
    o, x = input().rstrip().split(' ')
    count = 0
    mask ^= 1 << make_ord(x)
    for j in N_arr:
        if j == (j & mask):
            count += 1

    print(count)
#     print(N_arr)
#     print(N_first)
#     answer.append(count)
# print(answer)
# print(N_arr)
# print(N_first)
