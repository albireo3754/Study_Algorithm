import math
def solution(a):
    answer = 2
    left = [math.inf for _ in range(len(a))]
    right = [math.inf for _ in range(len(a))]
    left[0] = a[0]
    right[-1] = a[-1]
    #여기부터 다시
    for i in range(1, len(a) - 1):
        if left[i - 1] > a[i]:
            left[i] = a[i]
        else:
            left[i] = left[i - 1]
        if right[- 1 - (i - 1)] > a[- 1 - i]:
            right[- 1 - (i)] = a[- 1 - (i)]
        else:
            right[- 1 - (i)] = right[- 1 - (i - 1)]

    for i in range(1, len(a) - 1):
        if a[i] > left[i - 1] and a[i] > right[i + 1]:
            continue
        answer += 1
    # print(left, right)
    return answer
