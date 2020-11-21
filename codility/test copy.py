#1 - 62% 

def solution(A):
    # write your code in Python 3.6

    maxIdx = A[0]
    maxSum = A[0]

    for i in range(1, len(A)):
         
        maxIdx = max(A[i], A[i]+maxIdx)
        maxSum = max(maxSum, maxIdx)
    
    return maxSum