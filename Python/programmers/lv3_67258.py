def solution(gems):
    kind = set(gems)
    dic = {}
    # gem 종류 N개
    N = len(kind)
    i = 0
    j = 0
    answer = []
    temp_N = 0
    while i < len(gems):
        if gems[i] in dic:
            dic[gems[i]] += 1
        else:
            dic[gems[i]] = 1
            temp_N += 1

        i += 1
        while temp_N == N and j < i:
            answer.append([i - j ,j + 1, i])
            if dic[gems[j]] == 1:
                dic.pop(gems[j])
                temp_N -= 1
            else:
                dic[gems[j]] -= 1
            j += 1   

    # 구간은 1~N이기때문에
    return sorted(answer, key = lambda x: (x[0], x[1]))[0][1:]