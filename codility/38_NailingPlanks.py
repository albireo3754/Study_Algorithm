# 1st. O((N + M) * N) score:  50
# 2nd. by https://codesays.com/2014/solution-to-nailing-planks-by-codility/ 
# clear this problem fake 100
# print(checkNailed([1, 4, 5, 8], [4, 5, 9, 10], [4, 6, 7, 10]))

def findFirstNail(plankBegin, plankEnd, nails, preResult):
    result = -1
    resultPos = -1
    nailLower = 0
    nailUpper = len(nails) - 1
    nailMid = 0

    while nailLower <= nailUpper:
        nailMid = (nailLower + nailUpper) // 2
        nailPosMid = nails[nailMid][1]

        if nailPosMid < plankBegin:
            nailLower = nailMid + 1
        elif nailPosMid > plankEnd:
            nailUpper = nailMid - 1
        else:
            nailUpper = nailMid - 1
            result = nails[nailMid][0]
            resultPos = nailMid
            print(result,nailMid)
    print("result")
    if result == -1:
        return -1
    
    resultPos += 1

    while resultPos < len(nails):
        if nails[resultPos][1] > plankEnd:
            break
        result = min(result, nails[resultPos][0])
        resultPos += 1
        if preResult >= result:
            return preResult
    return max(result, preResult)

def solution(A, B, C):
    # write your code in Python 3.6
    nails = sorted(enumerate(C), key = lambda x: x[1])
    result = -1
    N = len(A)

    for plankIndex in range(N):
        result = findFirstNail(A[plankIndex], B[plankIndex], nails, result)
        if result == -1:
            return result
    return result + 1
