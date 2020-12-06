# 1st. O((N + M) * N) score:  50
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def checkNailed(A,B,C):
    N = len(A)
    M = len(C)
    idxStack = [i for i in range(N)]
    delNode = []
    for nail in C:
        for i in idxStack:
            # print(i)
            if A[i] <= nail and B[i] >= nail:
                delNode.append(i)

        for j in delNode:
            idxStack.remove(j)
        delNode =[]

        if len(idxStack) == 0:
            return True

    return False

# print(checkNailed([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10]))


def solution(A, B, C):
    # write your code in Python 3.6
    N = len(A)
    M = len(C)
    
    startIdx = 0
    endIdx = M
    resultIdx = -1
    
    while startIdx <= endIdx:
        print(startIdx,endIdx)
        midIdx = (startIdx + endIdx) // 2  
        # print(midIdx, startIdx, endIdx)  
        if checkNailed(A,B,C[:midIdx]):
            resultIdx = midIdx
            # print(resultIdx, M,midIdx,"result")
            endIdx = midIdx - 1
        else:
            startIdx = midIdx + 1
               
    return resultIdx

print(solution([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10, 2]))