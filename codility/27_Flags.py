# score 73
import math


def solution(A):
    # write your code in Python 3.6
    peaks = []
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i + 1]:
            peaks.append(i)

    maxFlag2 = int(math.sqrt(len(A)))
    maxFlag = 0
    print(peaks, maxFlag2)

    while maxFlag2 > 0:
        if maxFlag > maxFlag2:
            return maxFlag
        beforePeak = peaks[0]
        flag = 1
        idx = 1
        while maxFlag2 >= flag and idx < len(peaks):
            peak = peaks[idx]
            if peak - beforePeak >= maxFlag2:
                flag += 1
                beforePeak = peak
            idx += 1
        maxFlag = flag
        maxFlag2 -= 1
        print(maxFlag2)

    return flag


solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])
