# refference http://chienchikao.blogspot.com/2017/11/codility-lesson-14-binary-search_2.html
# I think Binary Search use only by Index.
# But this approch is wrong. reference use binary Search for get value.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def checkDivisable(mid, K, A):
    numBlockAllowed = K
    currentBlockSum = 0
    N = len(A)
    for i in range(N):
        currentBlockSum = currentBlockSum + A[i]

        if currentBlockSum > mid:
            numBlockAllowed -= 1
            currentBlockSum = A[i]
        
        if numBlockAllowed == 0:
            return False
    
    return True

def solution(K, M, A):
    # write your code in Python 3.6
    
    minSum = 0
    maxSum = 0
    for i in range(len(A)):
        maxSum = maxSum + A[i] # sum of all value
        minSum = max(minSum, A[i]) # one the best min value
    
    possibleResult = maxSum

    while minSum <= maxSum:
        midSum = (minSum + maxSum) // 2

        ok = checkDivisable(midSum, K, A)

        if ok == True:
            possibleResult = midSum
            maxSum = midSum - 1
        else:
            minSum = midSum + 1
    

    return possibleResult
    
    # blockSums = [0] * K
    # blockStarts = [0] * (K + 1)
    # N = len(A)

    # cnt = 0
    # for i in range(K):
    #     blockStarts[i] = cnt
    #     cnt += N//K 
    # blockStarts[K] = N

    # print(blockStarts)
    # for i in range(K):
    #     blockSums[i] = sum(A[blockStarts[i] : blockStarts[i+1]])

    # # K-1 까지해야될수도이슴
    # for i in range(K):
    #     if blockSums[i+1] >= blockSums[i]:

    # print(blockSums)



    # return largeSum
