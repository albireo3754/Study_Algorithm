def solution(A):
    # write your code in Python 3.6

    A.sort()
    
    for i in range(2, len(A)):
        if A[i] < A[i-1] + A[i-2]:
            return 1
    
    return 0
