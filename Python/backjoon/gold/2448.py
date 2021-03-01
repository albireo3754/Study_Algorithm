import sys
import math
input = sys.stdin.readline

N = int(input())

k = int(math.log2(N // 3))

size = 5
for i in range(k):
    size = size * 2 + 1

stars = [' ' * size for i in range(N)]

l = ['*    ', '* *  ', '*****']


def div(i, j, i_size, j_size):
    if i_size == 3:
        return l
    i_size = i_size // 2
    j_size = (j_size - 1) // 2
    a = div(i, j, i_size, j_size)
    # b = 1사분면
    b = [' ' * j_size for i in range(i_size)]
    c = div(i + i_size, j, i_size, j_size)
    d = div(i + i_size, j + j_size, i_size, j_size)
    ab = []
    cd = []
    for a_, b_ in zip(a, b):
        ab.append(a_ + ' ' + b_)

    for c_, d_ in zip(c, d):
        cd.append(c_ + ' ' + d_)

    ab.extend(cd)
    return ab


mid = N - 1
end = 1
for i in (div(0, 0, N, size)):
    print(' ' * mid + i[:size - mid])
    mid -= 1
    end += 2
