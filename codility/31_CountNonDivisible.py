# score 55 - O(N**2)

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    nonDivs = [0 for _ in A]
    
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            if A[j] % A[i] != 0:
                nonDivs[j] += 1
    
    return nonDivs
