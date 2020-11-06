def solution(A):
    # write your code in Python 3.6
    
    leftSum = [0 for _ in A]
    rightSum = [0 for _ in A]
    
    for i in range(1, len(A)-2):
        leftSum[i] = max(leftSum[i-1] + A[i], 0)
    
    for i in range(len(A)-2, 1, -1):
        rightSum[i] = max(rightSum[i+1] + A[i], 0)

    maxDoubleSlice = 0
    for i in range(1, len(A)-1):
        maxDoubleSlice = max(maxDoubleSlice, leftSum[i-1] + rightSum[i+1])
        
    return maxDoubleSlice
