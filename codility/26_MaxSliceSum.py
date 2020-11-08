# 53%
# 2. 100% 1 solution can use 0, there is no idx sum. but this problem
# need one idx value

def solution(A):
    # write your code in Python 3.6

    maxIdx = A[0]
    maxSum = A[0]

    for i in range(1, len(A)):

        maxIdx = max(A[i], A[i]+maxIdx)
        maxSum = max(maxSum, maxIdx)

    return maxSum
