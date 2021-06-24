import math
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += i
    for j in range(math.ceil(left ** 0.5), math.floor(right ** 0.5) + 1):
        answer -= (j ** 2) * 2
    return answer