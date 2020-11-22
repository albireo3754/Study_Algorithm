# 54%

def solution(A):
    # write your code in Python 3.6
    peaks = []

    for i in range(1, len(A)-1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)

    if len(peaks) == 0:
        return 0

    block = len(peaks) + 1

    while block >= 1:
        block -= 1
        blockStart = 0
        blockEnd = 0
        if len(A) % block != 0:
            continue

        for i in range(1, block+1):
            blockStart = blockEnd
            blockEnd = len(peaks) // block - 1
            for peak in peaks:
                if blockStart <= peak:
                    continue
                if blockEnd <= peak:
                    break
        return block
