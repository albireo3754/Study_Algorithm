# score 55 - O(N**2)
# second code is 55 also.
# 3 - 77 score can't calculate O(?)

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import math

def solution(A):
    # write your code in Python 3.6
    aMax = 0
    numCnts = [0 for _ in range(len(A) * 2 + 1)]
    nonDivs = [0 for _ in A]

    for i in A:
        numCnts[i] += 1
    
    for i in range(len(A)):
        div = 0
        j = 1
        while j*j <= A[i]:
            if A[i] % j == 0:
                div += numCnts[j]
                
                if A[i]//j != j:
                    div += numCnts[A[i]//j]
            j+= 1
            
    
        nonDivs[i] = len(A) - div
        
    return nonDivs
