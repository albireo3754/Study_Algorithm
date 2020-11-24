# score 55 - O(N**2)
# second code is 55 also.
# 3 - 77 score can't calculate O(?)
# 4 - 100

import math

def solution(A):
    # write your code in Python 3.6
    aMax = 0
    numCnts = [0 for _ in range(len(A) * 2 + 1)]
    nonDivs = [0 for _ in A]
    tmps = [-1 for _ in range(len(A) * 2 + 1)]
    
    for i in A:
        numCnts[i] += 1
    
    for i in range(len(A)):
        div = 0
        cur = A[i]
        j = 1
        if tmps[cur] != -1:
            nonDivs[i] = tmps[cur]
        else:
            while j*j <= cur:
                if cur % j == 0:
                    div += numCnts[j]
                    
                    if cur//j != j:
                        div += numCnts[cur//j]
                j+= 1
            nonDivs[i] = len(A) - div
            tmps[cur] = nonDivs[i]

        
    return nonDivs
