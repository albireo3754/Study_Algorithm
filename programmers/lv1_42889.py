from collections import Counter
def solution(N, stages):
    answer = [0] * (N+1)

    user = len(stages)
    counter = Counter(stages)
    for i in range(1, N+1):
        if user == 0:
            break
        answer[i] = counter[i] / user
        user -= counter[i]

    answer = sorted(range(1,N+1), key=lambda x:answer[x], reverse=True)
    return answer