def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    len_1 = len(one)
    len_2 = len(two)
    len_3 = len(three)
    count = 0
    score_1 = 0
    score_2 = 0
    score_3 = 0 
    for i in answers:
        if one[count%len_1] == i:
            score_1 += 1
        if two[count%len_2] == i:
            score_2 += 1
        if three[count%len_3] == i:
            score_3 += 1
        count+= 1 
    pre_answer = sorted([[1,score_1],[2,score_2],[3,score_3]], key=lambda x: x[1], reverse=True)

    maximum = pre_answer[0][1]
    answer.append(pre_answer[0][0])
    for i in range(1, 3):
        if pre_answer[i][1] == maximum:
            answer.append(pre_answer[i][0])


    return answer


# -- don't use counter, but use enumerate