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
    if peaks[-1] + 1 <= len(A) // 2:
        return 1
    while block > 1:
        block -= 1
        blockStart = 0
        blockEnd = -1

        if len(A) % block != 0:
            continue

        K = len(A) // block

        k = 0
        t = 1
        for i in range(1, block+1):
            blockStart = blockEnd + 1
            blockEnd = i * K - 1
            for j in range(k, len(peaks)):
                if blockEnd >= peaks[j]:
                    if blockStart <= peaks[j]:
                        k = j + 1
                        break
                else:
                    t = 0
                    break
            if t == 0:
                break

        if t == 0:
            continue
        return block
