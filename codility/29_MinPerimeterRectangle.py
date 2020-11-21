import math


def solution(N):
    # write your code in Python 3.6

    A = 1
    minPeri = 2*(1+N)
    while A <= math.sqrt(N):
        B = N//A

        if A*B == N:
            minPeri = min(minPeri, 2*(A+B))
        A += 1

    return minPeri
