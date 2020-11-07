def solution(A):
    # write your code in Python 3.6
    difAdj = []
    for i in range(1,len(A)):
        difAdj.append(A[i] - A[i-1])
    
    maxSum = 0
    maxIdx = 0
    for i in difAdj:
        maxIdx = max(0, maxIdx+i)
        maxSum = max(maxSum, maxIdx)
        
    return maxSum
