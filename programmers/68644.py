#import itertools
#itertools.cominations(numbers, 2) also can 

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    answer = list(set(answer))
    answer = sorted(answer)
    return answer